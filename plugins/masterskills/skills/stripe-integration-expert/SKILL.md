---
name: "stripe-integration-expert"
description: >-
  P—r—o—d—u—c—t—i—o—n—-—g—r—a—d—e— —S—t—r—i—p—e— —i—n—t—e—g—r—a—t—i—o—n—s—:— —s—u—b—s—c—r—i—p—t—i—o—n—s— —w—i—t—h— —t—r—i—a—l—s— —a—n—d— —p—r—o—r—a—t—i—o—n—,— —o—n—e—-—t—i—m—e— —p—a—y—m—e—n—t—s—,— —u—s—a—g—e—-—b—a—s—e—d— —b—i—l—l—i—n—g—,— —c—h—e—c—k—o—u—t— —s—e—s—s—i—o—n—s—,— —i—d—e—m—p—o—t—e—n—t— —w—e—b—h—o—o—k— —h—a—n—d—l—e—r—s—,— —c—u—s—t—o—m—e—r— —p—o—r—t—a—l—,— —a—n—d— —i—n—v—o—i—c—i—n—g—.— —C—o—v—e—r—s— —N—e—x—t—.—j—s—,— —E—x—p—r—e—s—s—,— —a—n—d— —D—j—a—n—g—o— —p—a—t—t—e—r—n—s—.— —U—s—e— —w—h—e—n— —i—n—t—e—g—r—a—t—i—n—g— —S—t—r—i—p—e— —f—o—r— —t—h—e— —f—i—r—s—t— —t—i—m—e—,— —d—e—b—u—g—g—i—n—g— —w—e—b—h—o—o—k— —r—e—l—i—a—b—i—l—i—t—y— —i—s—s—u—e—s—,— —m—i—g—r—a—t—i—n—g— —f—r—o—m— —a— —d—i—f—f—e—r—e—n—t— —p—a—y—m—e—n—t— —p—r—o—v—i—d—e—r—,— —o—r— —a—d—d—i—n—g— —u—s—a—g—e—-—b—a—s—e—d— —b—i—l—l—i—n—g— —t—o— —a—n— —e—x—i—s—t—i—n—g— —s—u—b—s—c—r—i—p—t—i—o—n— —p—r—o—d—u—c—t.
---

# Stripe Integration Expert

**Tier:** POWERFUL  
**Category:** Engineering Team  
**Domain:** Payments / Billing Infrastructure

---

## Overview

Implement production-grade Stripe integrations: subscriptions with trials and proration, one-time payments, usage-based billing, checkout sessions, idempotent webhook handlers, customer portal, and invoicing. Covers Next.js, Express, and Django patterns.

---

## Core Capabilities

- Subscription lifecycle management (create, upgrade, downgrade, cancel, pause)
- Trial handling and conversion tracking
- Proration calculation and credit application
- Usage-based billing with metered pricing
- Idempotent webhook handlers with signature verification
- Customer portal integration
- Invoice generation and PDF access
- Full Stripe CLI local testing setup

---

## When to Use

- Adding subscription billing to any web app
- Implementing plan upgrades/downgrades with proration
- Building usage-based or seat-based billing
- Debugging webhook delivery failures
- Migrating from one billing model to another

---

## Subscription Lifecycle State Machine

```
FREE_TRIAL ──paid──► ACTIVE ──cancel──► CANCEL_PENDING ──period_end──► CANCELED
     │                  │                                                    │
     │               downgrade                                            reactivate
     │                  ▼                                                    │
     │             DOWNGRADING ──period_end──► ACTIVE (lower plan)           │
     │                                                                        │
     └──trial_end without payment──► PAST_DUE ──payment_failed 3x──► CANCELED
                                          │
                                     payment_success
                                          │
                                          ▼
                                        ACTIVE
```

### DB subscription status values:
`trialing | active | past_due | canceled | cancel_pending | paused | unpaid`

---

## Stripe Client Setup

```typescript
// lib/stripe.ts
import Stripe from "stripe"

export const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, {
  apiVersion: "2024-04-10",
  typescript: true,
  appInfo: {
    name: "myapp",
    version: "1.0.0",
  },
})

// Price IDs by plan (set in env)
export const PLANS = {
  starter: {
    monthly: process.env.STRIPE_STARTER_MONTHLY_PRICE_ID!,
    yearly: process.env.STRIPE_STARTER_YEARLY_PRICE_ID!,
    features: ["5 projects", "10k events"],
  },
  pro: {
    monthly: process.env.STRIPE_PRO_MONTHLY_PRICE_ID!,
    yearly: process.env.STRIPE_PRO_YEARLY_PRICE_ID!,
    features: ["Unlimited projects", "1M events"],
  },
} as const
```

---

## Checkout Session (Next.js App Router)

```typescript
// app/api/billing/checkout/route.ts
import { NextResponse } from "next/server"
import { stripe } from "@/lib/stripe"
import { getAuthUser } from "@/lib/auth"
import { db } from "@/lib/db"

export async function POST(req: Request) {
  const user = await getAuthUser()
  if (!user) return NextResponse.json({ error: "Unauthorized" }, { status: 401 })

  const { priceId, interval = "monthly" } = await req.json()

  // Get or create Stripe customer
  let stripeCustomerId = user.stripeCustomerId
  if (!stripeCustomerId) {
    const customer = await stripe.customers.create({
      email: user.email,
      name: "username-undefined"
      metadata: { userId: user.id },
    })
    stripeCustomerId = customer.id
    await db.user.update({ where: { id: user.id }, data: { stripeCustomerId } })
  }

  const session = await stripe.checkout.sessions.create({
    customer: stripeCustomerId,
    mode: "subscription",
    payment_method_types: ["card"],
    line_items: [{ price: priceId, quantity: 1 }],
    allow_promotion_codes: true,
    subscription_data: {
      trial_period_days: user.hasHadTrial ? undefined : 14,
      metadata: { userId: user.id },
    },
    success_url: `${process.env.NEXT_PUBLIC_APP_URL}/dashboard?session_id={CHECKOUT_SESSION_ID}`,
    cancel_url: `${process.env.NEXT_PUBLIC_APP_URL}/pricing`,
    metadata: { userId: user.id },
  })

  return NextResponse.json({ url: session.url })
}
```

---

## Subscription Upgrade/Downgrade

```typescript
// lib/billing.ts
export async function changeSubscriptionPlan(
  subscriptionId: string,
  newPriceId: string,
  immediate = false
) {
  const subscription = await stripe.subscriptions.retrieve(subscriptionId)
  const currentItem = subscription.items.data[0]

  if (immediate) {
    // Upgrade: apply immediately with proration
    return stripe.subscriptions.update(subscriptionId, {
      items: [{ id: currentItem.id, price: newPriceId }],
      proration_behavior: "always_invoice",
      billing_cycle_anchor: "unchanged",
    })
  } else {
    // Downgrade: apply at period end, no proration
    return stripe.subscriptions.update(subscriptionId, {
      items: [{ id: currentItem.id, price: newPriceId }],
      proration_behavior: "none",
      billing_cycle_anchor: "unchanged",
    })
  }
}

// Preview proration before confirming upgrade
export async function previewProration(subscriptionId: string, newPriceId: string) {
  const subscription = await stripe.subscriptions.retrieve(subscriptionId)
  const prorationDate = Math.floor(Date.now() / 1000)

  const invoice = await stripe.invoices.retrieveUpcoming({
    customer: subscription.customer as string,
    subscription: subscriptionId,
    subscription_items: [{ id: subscription.items.data[0].id, price: newPriceId }],
    subscription_proration_date: prorationDate,
  })

  return {
    amountDue: invoice.amount_due,
    prorationDate,
    lineItems: invoice.lines.data,
  }
}
```

---

## Complete Webhook Handler (Idempotent)

```typescript
// app/api/webhooks/stripe/route.ts
import { NextResponse } from "next/server"
import { headers } from "next/headers"
import { stripe } from "@/lib/stripe"
import { db } from "@/lib/db"
import Stripe from "stripe"

// Processed events table to ensure idempotency
async function hasProcessedEvent(eventId: string): Promise<boolean> {
  const existing = await db.stripeEvent.findUnique({ where: { id: eventId } })
  return !!existing
}

async function markEventProcessed(eventId: string, type: string) {
  await db.stripeEvent.create({ data: { id: eventId, type, processedAt: new Date() } })
}

export async function POST(req: Request) {
  const body = await req.text()
  const signature = headers().get("stripe-signature")!

  let event: Stripe.Event
  try {
    event = stripe.webhooks.constructEvent(body, signature, process.env.STRIPE_WEBHOOK_SECRET!)
  } catch (err) {
    console.error("Webhook signature verification failed:", err)
    return NextResponse.json({ error: "Invalid signature" }, { status: 400 })
  }

  // Idempotency check
  if (await hasProcessedEvent(event.id)) {
    return NextResponse.json({ received: true, skipped: true })
  }

  try {
    switch (event.type) {
      case "checkout.session.completed":
        await handleCheckoutCompleted(event.data.object as Stripe.Checkout.Session)
        break

      case "customer.subscription.created":
      case "customer.subscription.updated":
        await handleSubscriptionUpdated(event.data.object as Stripe.Subscription)
        break

      case "customer.subscription.deleted":
        await handleSubscriptionDeleted(event.data.object as Stripe.Subscription)
        break

      case "invoice.payment_succeeded":
        await handleInvoicePaymentSucceeded(event.data.object as Stripe.Invoice)
        break

      case "invoice.payment_failed":
        await handleInvoicePaymentFailed(event.data.object as Stripe.Invoice)
        break

      default:
        console.log(`Unhandled event type: ${event.type}`)
    }

    await markEventProcessed(event.id, event.type)
    return NextResponse.json({ received: true })
  } catch (err) {
    console.error(`Error processing webhook ${event.type}:`, err)
    // Return 500 so Stripe retries — don't mark as processed
    return NextResponse.json({ error: "Processing failed" }, { status: 500 })
  }
}

async function handleCheckoutCompleted(session: Stripe.Checkout.Session) {
  if (session.mode !== "subscription") return
  
  const userId = session.metadata?.userId
  if (!userId) throw new Error("No userId in checkout session metadata")

  const subscription = await stripe.subscriptions.retrieve(session.subscription as string)
  
  await db.user.update({
    where: { id: userId },
    data: {
      stripeCustomerId: session.customer as string,
      stripeSubscriptionId: subscription.id,
      stripePriceId: subscription.items.data[0].price.id,
      stripeCurrentPeriodEnd: new Date(subscription.current_period_end * 1000),
      subscriptionStatus: subscription.status,
      hasHadTrial: true,
    },
  })
}

async function handleSubscriptionUpdated(subscription: Stripe.Subscription) {
  const user = await db.user.findUnique({
    where: { stripeSubscriptionId: subscription.id },
  })
  if (!user) {
    // Look up by customer ID as fallback
    const customer = await db.user.findUnique({
      where: { stripeCustomerId: subscription.customer as string },
    })
    if (!customer) throw new Error(`No user found for subscription ${subscription.id}`)
  }

  await db.user.update({
    where: { stripeSubscriptionId: subscription.id },
    data: {
      stripePriceId: subscription.items.data[0].price.id,
      stripeCurrentPeriodEnd: new Date(subscription.current_period_end * 1000),
      subscriptionStatus: subscription.status,
      cancelAtPeriodEnd: subscription.cancel_at_period_end,
    },
  })
}

async function handleSubscriptionDeleted(subscription: Stripe.Subscription) {
  await db.user.update({
    where: { stripeSubscriptionId: subscription.id },
    data: {
      stripeSubscriptionId: null,
      stripePriceId: null,
      stripeCurrentPeriodEnd: null,
      subscriptionStatus: "canceled",
    },
  })
}

async function handleInvoicePaymentFailed(invoice: Stripe.Invoice) {
  if (!invoice.subscription) return
  const attemptCount = invoice.attempt_count
  
  await db.user.update({
    where: { stripeSubscriptionId: invoice.subscription as string },
    data: { subscriptionStatus: "past_due" },
  })

  if (attemptCount >= 3) {
    // Send final dunning email
    await sendDunningEmail(invoice.customer_email!, "final")
  } else {
    await sendDunningEmail(invoice.customer_email!, "retry")
  }
}

async function handleInvoicePaymentSucceeded(invoice: Stripe.Invoice) {
  if (!invoice.subscription) return

  await db.user.update({
    where: { stripeSubscriptionId: invoice.subscription as string },
    data: {
      subscriptionStatus: "active",
      stripeCurrentPeriodEnd: new Date(invoice.period_end * 1000),
    },
  })
}
```

---

## Usage-Based Billing

```typescript
// Report usage for metered subscriptions
export async function reportUsage(subscriptionItemId: string, quantity: number) {
  await stripe.subscriptionItems.createUsageRecord(subscriptionItemId, {
    quantity,
    timestamp: Math.floor(Date.now() / 1000),
    action: "increment",
  })
}

// Example: report API calls in middleware
export async function trackApiCall(userId: string) {
  const user = await db.user.findUnique({ where: { id: userId } })
  if (user?.stripeSubscriptionId) {
    const subscription = await stripe.subscriptions.retrieve(user.stripeSubscriptionId)
    const meteredItem = subscription.items.data.find(
      (item) => item.price.recurring?.usage_type === "metered"
    )
    if (meteredItem) {
      await reportUsage(meteredItem.id, 1)
    }
  }
}
```

---

## Customer Portal

```typescript
// app/api/billing/portal/route.ts
import { NextResponse } from "next/server"
import { stripe } from "@/lib/stripe"
import { getAuthUser } from "@/lib/auth"

export async function POST() {
  const user = await getAuthUser()
  if (!user?.stripeCustomerId) {
    return NextResponse.json({ error: "No billing account" }, { status: 400 })
  }

  const portalSession = await stripe.billingPortal.sessions.create({
    customer: user.stripeCustomerId,
    return_url: `${process.env.NEXT_PUBLIC_APP_URL}/settings/billing`,
  })

  return NextResponse.json({ url: portalSession.url })
}
```

---

## Testing with Stripe CLI

```bash
# Install Stripe CLI
brew install stripe/stripe-cli/stripe

# Login
stripe login

# Forward webhooks to local dev
stripe listen --forward-to localhost:3000/api/webhooks/stripe

# Trigger specific events for testing
stripe trigger checkout.session.completed
stripe trigger customer.subscription.updated
stripe trigger invoice.payment_failed

# Test with specific customer
stripe trigger customer.subscription.updated \
  --override subscription:customer=cus_xxx

# View recent events
stripe events list --limit 10

# Test cards
# Success: 4242 4242 4242 4242
# Requires auth: 4000 0025 0000 3155
# Decline: 4000 0000 0000 9995
# Insufficient funds: 4000 0000 0000 9995
```

---

## Feature Gating Helper

```typescript
// lib/subscription.ts
export function isSubscriptionActive(user: { subscriptionStatus: string | null, stripeCurrentPeriodEnd: Date | null }) {
  if (!user.subscriptionStatus) return false
  if (user.subscriptionStatus === "active" || user.subscriptionStatus === "trialing") return true
  // Grace period: past_due but not yet expired
  if (user.subscriptionStatus === "past_due" && user.stripeCurrentPeriodEnd) {
    return user.stripeCurrentPeriodEnd > new Date()
  }
  return false
}

// Middleware usage
export async function requireActiveSubscription() {
  const user = await getAuthUser()
  if (!isSubscriptionActive(user)) {
    redirect("/billing?reason=subscription_required")
  }
}
```

---

## Common Pitfalls

- **Webhook delivery order not guaranteed** — always re-fetch from Stripe API, never trust event data alone for DB updates
- **Double-processing webhooks** — Stripe retries on 500; always use idempotency table
- **Trial conversion tracking** — store `hasHadTrial: true` in DB to prevent trial abuse
- **Proration surprises** — always preview proration before upgrade; show user the amount before confirming
- **Customer portal not configured** — must enable features in Stripe dashboard under Billing → Customer portal settings
- **Missing metadata on checkout** — always pass `userId` in metadata; can't link subscription to user without it
