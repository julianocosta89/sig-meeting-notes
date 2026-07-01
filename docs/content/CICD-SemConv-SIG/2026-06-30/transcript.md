SIG: CI/CD SemConv SIG
Date: 2026-06-30
Duration: 14 minutes
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 00:17 Hello?
**Adriel Perkins** 00:21 Hey, good day, how are you?
**Christophe Kamphaus** 00:23 Why aren't you?
**Adriel Perkins** 00:25 Okay, thank you.
Just a heads up, I have a hard stop a little bit before the half hour.
I have a meeting I have to get on for work.
**Christophe Kamphaus** 01:05 Sure. No worries.
I don't have any topics from my site this time.
**Adriel Perkins** 01:15 Okay.
I saw that you commented on that PR, I appreciate that.
From last week's updates, I linked that, comment in the original 3767 ticket.
as well.
Hey, Alan.
**Alan Clucas** 01:43 Hello!
Oh, diagnosis.
Yep.
**Adriel Perkins** 01:46 How you been.
**Alan Clucas** 01:47 Yeah, I'm alright, how are you?
**Adriel Perkins** 01:49 Doing okay, thank you.
**Alan Clucas** 01:51 Good.
**Adriel Perkins** 02:40 Alright, well, I don't have anything other than… That, Christoph said he didn't have anything. Alan, did you have anything?
**Alan Clucas** 02:49 No, I don't have anything.
Hi.
I guess I could ask if anyone knows… so the, the carrier stuff that… Crystal Frankfurt, thank you for reviewing.
The stuff last week, I was away. Does it… the… the fact that carriers don't… List the keys that they carry.
Sort of fundamentally makes the environment propagation messy.
**Christophe Kamphaus** 03:31 For the environment variables, The keys method is specified, so you could enumerate some.
It's more… That's… why would you do it?
Because carriers are more… Meant for looking up, and… Injecting.
see, variables.
**Alan Clucas** 03:55 But if the list of known possible keys.
was defined, then… A lot of the worries around just Memory usage and stuff would have gone away.
**Christophe Kamphaus** 04:12 The problem there is… You are not sure which one would be used, because with the propagators, you could specify your own custom propagation key.
**Alan Clucas** 04:28 I wondered whether carriers should take an optional key list, but that then messes things around. No, I don't know. It was just a thought. I was looking at what happened last week, so…
**Christophe Kamphaus** 04:42 error.
**Alan Clucas** 04:42 Alright.
**Christophe Kamphaus** 04:43 I guess… What we are missing is… To specify a key name, maybe.
Which should always be used, unless there's a good reason not to.
**Alan Clucas** 04:59 Yeah, I don't know.
**Christophe Kamphaus** 05:01 Yeah, because you could end up with, Different programs using different key names.
**Alan Clucas** 05:10 Hmm.
**Adriel Perkins** 05:18 I mean, it's meant to carry whatever into a propagator, yeah?
Like, does the prop… like, if you say… if you say, I want to enable B3 propagation, then… you know that you're only gonna support B3 carriers, right? So when your carrier reads from the environments, you're only gonna allow the B3 headers that were set as environment variables.
over, at least the propagator's gonna handle that, concern. Same with W3C face contacts, like, if that's your propagator, then that's only gonna handle carriers that map to the values that would be headers inside of, W3C trace context.
Before you pass to the carriers, you can say, like.
Because, like, right now, I think with, the spec, or no, the Python pull request that just got updated.
for lookup, you're… you're supposed to put os.env in there, or… you could put a map directly, right, into the carrier, and you could just say, like, these are the three keys from os.env that I want to use and pass as a carrier, and if they don't exist, we won't… we won't propagate it.
So I, I…
**Alan Clucas** 06:43 Sorry, an early version of Go took… Took a function, rather than, building in os.emv equivalent.
**Adriel Perkins** 06:53 Yeah, they, they, I think I originally built an OS study in V, and they took it out.
Maybe?
I don't know, I'm misremembering. It's been too long.
Let me go pull up that pull request again, actually.
And then Python can trip, I think it is.
**Christophe Kamphaus** 07:22 Yeah, in the end, also, all the caching stuff was removed.
I had some, quite some discussion still with Robert about it.
But yeah, I think in the end, it's more to guard against some Bono cases, and he said… Yeah, if we already say we should… Cache the result of the lookup.
It doesn't make sense to complicate the implementation further.
**Alan Clucas** 07:56 It's fine. Alright.
**Christophe Kamphaus** 08:01 Yeah, I'm fine with it as well, I just wanted to… See all the upsides and downsides of those options, so we… But do… Kuchu is consciously what we want to go with.
What are we waiting for?
**Adriel Perkins** 08:57 I was looking for that PR, sorry.
**carlosalberto** 09:02 Which Pierre?
**Adriel Perkins** 09:04 Let's see… a Python one.
I sent it in the channel. This is… An update.
Around the snapshot caching.
But in the example, they mentioned getter.get os.environment as an example usage.
So, as the user, you're responsible for Still, you know, calling the carrier.
And pulling from it.
And getting the specific key you're looking for before you use propagation, so… They just pass getter, you know, getter.gitos.environment, and then, like, look up your key, that's been normalized.
So yeah, I guess we didn't have anything else. Carlos, did you have anything you wanted to chat about today?
**carlosalberto** 10:13 No, sorry, I have been, I'm back to work, like, being employed by a company, and that requires some cycles and other stuff, but yeah, I still have the PR for adding the permissions for it to spam processor.
which I need to massage to make it flexible, so Java and Go come different directions, that's the plan for this week.
**Adriel Perkins** 10:36 Okay. Cool.
And I think you've sent me that PR before, yeah.
**carlosalberto** 10:47 Yeah, it's pretty straightforward, I just need to… So, long story short, in that PR, I'm adding 3 new operations, or methods, to spam processor.
To detect when a link was added, an attribute was set, or updated, which is the same, let's say.
And finally, one for, when the name of this bank was changed, you know? Updated.
And, basically, what Java wants is, like, to be… especially because this is an experimental PR, or this could be an experimental section.
death.
Languages are free to implement this as either those three operations, three different methods, or a single unchanged… method.
Where… where you are getting, like, you know.
The values, or information regarding the event.
Which, to me, feeds growing what?
that's the trade-off we are doing for now. I would rather stick to a single approach, one way or another. But let's see, that's… we want to make progress on that. We want people to, you know, prototype that in their languages, and that's part of this.
**Adriel Perkins** 11:57 Okay.
Could you toss that… the link to that PR again? It seems to have lost it, and I can't find it in the chat. Yes.
**carlosalberto** 12:06 Give me, I will paste in the chat and in the docs.
That's wrong.
**Adriel Perkins** 12:17 Oh, is it 5104?
Add-in development, span processor operations, tracking span changes.
**carlosalberto** 12:24 Yeah, correct. That's one.
**Adriel Perkins** 12:25 Oh, okay.
**Christophe Kamphaus** 12:40 Regarding the release candidate of the environment variable carriers.
When do you think it can be merged, said PR?
**carlosalberto** 12:50 The one on the specification?
**Christophe Kamphaus** 12:52 Yeah, I know that Robert is still, going over the… Implementations of it.
But is that blocking to move forward with the PR?
**carlosalberto** 13:04 Hmm… Let me see, it's at, 51.42?
**Christophe Kamphaus** 13:12 Yes.
**carlosalberto** 13:13 Another one. Okay.
I remember he wanted to make… to wait for something, let me see. Actually, he posted a comment last week, all concerns that were raised, having address.
He will double check.
I… he's saying that he would… he would like to wait, that all implementations are compliant.
Yeah, I don't think that's super needed, and actually, we should merge that today. I will raise that in the spec call, because let's say that maybe, I mean, this is not a stability, it's release candidate, which is a good sign, but… yeah, going and checking all the implementations should be a requirement. So I will try to, merge that today, only Robert really, really, really thinks that it's important to hold it.
Yeah.
**Adriel Perkins** 13:59 Okay.
Sounds good. Appreciate it.
**Christophe Kamphaus** 14:03 Sounds good. I also think that all concerns were addressed, so… I mean, it also looks good to merge now.
**Adriel Perkins** 14:16 Awesome.
All right, well, if there is nothing else, we can call it early and give you some time back to your day.
Appreciate y'all joining, and .
**Christophe Kamphaus** 14:31 as well. You too.
**carlosalberto** 14:33 Around.
