SIG: Ruby SIG
Date: 2025-09-02
Duration: 31 minutes
============================================================

## Zoom Recording Transcript

**Hannah Ramadan** 00:57 Hey, Wendy. Hey, Kayla.
**Kayla Reopelle** 01:02 Hey, Hannah.
Okay, I think we can… Get started…
Let's see…
Okay, I've, been having some laptop issues, so…
Strange things could happen during this meeting, we'll see what happens. But I was off yesterday for Labor Day and didn't put together any agenda, but I see… thank you, Sean, for putting some things on.
So, yeah, I guess… let's see…
Nice to see you, Rob.
**Robb Kidd (he/him)** 03:08 Hello, buddy.
**Kayla Reopelle** 03:10 Hmm.
**Robb Kidd (he/him)** 03:11 Hoping to be here more often.
**Kayla Reopelle** 03:13 Oh, great.
**Robb Kidd (he/him)** 03:14 We'll see.
I got here today.
**Kayla Reopelle** 03:17 Appreciate that.
Alright, so let's see, SpecSig today was not fully paying attention to it, but I think this was the main…
main thing that I wanted to bring up,
is that the entity SIG is moving along. They're now talking about adding an entity provider for this. This got into a larger discussion about potentially starting a new SIG to deal with
like, SDK initialization and teardown, because it seems like with some of the changes that are happening with the entity provider and, the configuration SIG, that we may need to specify some things.
Or, you know, existing agents might need to change the way that their startup and shutdown works.
We haven't started working on this for Ruby, so this is just more, to be aware, but I'm pretty sure the rest of them… there's a new proto version that's getting released today.
A little more discussion about the attributes value changes that have been going on for a few months.
And… oh yes, this was the other part of the entities, was,
Specifying entity information through an environment variable.
So, these are all still in the OTEP stage, it's, it's pretty early, I think. But…
Good to stay informed.
So, let's take a look at this first one.
Alright, use mapping scale outside rescale logic. You wanna share this one with us?
Sean?
**Xuan Cao** 05:11 Nothing, need, needs, major attention, just,
Because this is a one-line change, and I think I saw you approve it, and just wondering when… when we can have a, like, merge to the…
**Kayla Reopelle** 05:28 I think it can absolutely be merged, and I apologize for approving and not getting it in. I'll update this branch, and then…
Put it in a little merge queue window for today.
Okay. Yes, I can merge that once that's done. Thank you for pointing that out.
Alright, how about the next one?
**Xuan Cao** 05:57 Yeah, so this one, and then the, next to, PR, they're actually, they're,
together, because, I fucked that branch out of this branch. The main point is, one, I didn't test case for those two, tasks, and then…
fundamental more issues. I just point out all the issues, that I think should be fixed.
**Kayla Reopelle** 06:28 Okay.
**Xuan Cao** 06:28 In general, just, the callback.
From the asynchronized interest instruments, if something happened, we haven't have,
like, rescue block to make sure you won't break the entire application, so that's the first thing. And then the second thing is, the timeout, timeout is still… is still there.
**Kayla Reopelle** 06:53 So…
**Xuan Cao** 06:55 Change, change this, right? To timeout.
And then the last point is about the, for multiple view.
While multiple view manipulate the data points, we'll… we'll change the data points.
And then the solution is to have a hash of a view, with its own individual… its own independent data points.
Yeah, I actually had another solution, but last week, I think that's not that good, so I just made another PR.
About using hash, to, store the view.
So… Yeah, there's those two,
Hopefully there can get more attention, for the review.
Yeah.
**Kayla Reopelle** 07:50 And so these are issues that you found, not issues that are fixed in the… in this one, right? Or did you fix them?
**Xuan Cao** 07:57 The offix, yeah.
**Kayla Reopelle** 07:59 Okay, awesome.
**Xuan Cao** 08:01 Yeah.
**Kayla Reopelle** 08:02 Okay, great. Yeah, I can take a look at this one, today, too.
Alright, and then this one was the other one you had linked?
**Xuan Cao** 08:13 Yeah, yeah, yeah.
**Kayla Reopelle** 08:16 Yeah, so this one, yeah, takes care of the views. Awesome.
Awesome, awesome.
Okay, SEMCOM.
**Robb Kidd (he/him)** 08:33 Short of mentioning that it seems to be happening.
Thank you for it.
**Kayla Reopelle** 08:37 Yeah, yeah, I'm, grateful to Wendy for asking a question about it so that we could take a look at it. Yeah, everything seems pretty good. I… I wrote a little README update.
**Robb Kidd (he/him)** 08:51 I saw that, too late to really look into it last week. I intend to, today, or this week. The only thing
I have not looked at the contents. I see that it's failing the checks, in my fork for a markdown… a markdown linter is barking.
**Kayla Reopelle** 09:08 Oh, okay, yep.
**Robb Kidd (he/him)** 09:09 that… We can look at.
Whichever.
**Kayla Reopelle** 09:13 Yeah.
**Robb Kidd (he/him)** 09:14 I don't know if ReviewDog runs easily locally.
**Kayla Reopelle** 09:20 I use it.
**Robb Kidd (he/him)** 09:21 I use ACT.
as a way to run GitHub Actions on my laptop, I don't know.
**Kayla Reopelle** 09:25 offices.
**Robb Kidd (he/him)** 09:26 an action that would happily run in ACT.
**Kayla Reopelle** 09:28 Okay.
I'll have to look into it.
**Robb Kidd (he/him)** 09:31 I give that a… I was gonna give that a try this afternoon.
**Kayla Reopelle** 09:33 Perfect. That would be great, thank you. Sorry for opening a PR with broken links.
**Robb Kidd (he/him)** 09:39 Of course, yeah, yeah.
**Kayla Reopelle** 09:41 Nice, cool, so do you want to wait on that before we merge in the big one?
**Robb Kidd (he/him)** 09:50 Yeah, good point. We had talked about, like, README updates could come after.
**Kayla Reopelle** 09:54 Yeah.
**Robb Kidd (he/him)** 09:56 then we can redirect this PR to…
I guess the big one could merge, and then we could fix READMEs in a follow-up.
**Kayla Reopelle** 10:07 Okay.
Cool.
Then, yeah, I'll merge Schwan's other PR first. I guess if you're gonna look at it this afternoon.
It's already pretty close with timing-wise, so maybe we…
**Robb Kidd (he/him)** 10:24 Well, let's see if we don't get it fixed by this afternoon. We merge the… the bigger PR without it. Perfect. The README fixes can come later.
**Kayla Reopelle** 10:32 I love that.
Yeah. Okay. May I get two sooner than…
Cool.
Let's see if there's anything else… Encore…
Let's see… oh, we have…
New release PR open. This was something I was hoping to get some feedback on last week. I haven't looked, but it doesn't seem like anyone responded. So,
It's just we are… we made a breaking change to the API by removing some unspec'd APIs that we had merged in, so it's going to be a major version bump. But since I said I wouldn't merge until Thursday, I'll wait until Thursday.
for that. And… I might release the logs SDK separately today, since that's ready.
ready to go.
Okay, cool.
Anything else on the PRs?
We have a few other new ones to take a look at.
Anything that anyone here wants to call out?
Okay.
Take a look at issues…
Any issues we want to discuss?
I know there were some things that I think I said I would work on last week, but didn't end up getting to them. Had some support distractions.
All right.
I'll take a look at contrib…
Let's see, looks like we have an Ethon instrumentation release that I think has a bug fix for exception handling.
There's a few other things… This one… I think we were…
I'll be waiting on Eric to take a look at it.
This is a little complicated because, it's calling a method that's only defined in the SDK and not in the API.
So, we're trying to see…
What the best way is to go about this.
**Robb Kidd (he/him)** 13:34 Does the… This is just a random question, I don't know. Does the spec not say that
a tracer provider to shut down such that the API… that APIs in some, like, tracer provider
No op to provide a shutdown function or method.
in the interface.
**Kayla Reopelle** 13:57 I thought it, like, left it out entirely. Oh, is it getting me? I don't want the concepts getting the… the real stuff.
To the API, so if we look at…
Shut down, there isn't anything there.
And then if we go…
**Robb Kidd (he/him)** 14:17 the… So that… the… mmm…
**Wendy Smoak** 14:23 In the SDK.
**Kayla Reopelle** 14:25 Yeah.
**Wendy Smoak** 14:26 how, god.
**Kayla Reopelle** 14:28 Yeah, there are a few methods in the SDK that aren't defined as part of the API, and I guess I don't really understand why that's the case.
**Robb Kidd (he/him)** 14:36 Yeah, that does make it hard to substitute any SDK when the dependency's on an API.
**Kayla Reopelle** 14:43 Yeah.
I guess, yeah, you're only supposed to depend on the API and instrumentation, so…
maybe… There's a sense of, like, what methods they actually want to have be public interfaces versus.
**Wendy Smoak** 14:59 You should do this, but it's…
**Kayla Reopelle** 15:01 Very…
**Wendy Smoak** 15:01 Internal to your… I don't get it.
**Kayla Reopelle** 15:04 Yeah.
**Robb Kidd (he/him)** 15:06 Yeah, it feels like the, with all the other tracing…
With the rest of the interface of tracing it, like on spans and how to create stuff, it seems like there were just no ops defined in the spec.
But the surface area of a tracer provider doesn't seem to have… like, SDK has got more things than the API, which means that
Which means the API doesn't provide an instance of a thing that can stand in for any other thing.
**Kayla Reopelle** 15:33 Yeah, yeah.
And I think…
**Wendy Smoak** 15:36 I almost wonder, is this stop… is this under version control? Surely, somewhere. Like, I almost want to look at the PR for when the shutdown was added to the
SDK to see if there was anything, like, mentioned.
**Robb Kidd (he/him)** 15:50 Yeah.
We're only defining this at the SDK level because… Maybe.
**Wendy Smoak** 15:55 Yeah, it looks like MakeFallow, so I'll have to go back in the blame and see.
**Robb Kidd (he/him)** 16:02 Is it a no-no for us to put a no-op shutdown in the API?
**Kayla Reopelle** 16:07 Well, since we've, we've just, you know, had it…
Revealed to us that we shouldn't do, you know, no ops for attributes and events.
I feel like we would be met with the same… Okay.
For shutdown, but, could be worth an ask.
Yeah. Well, we can, yeah, take a look. I think it would require a little bit of.
**Wendy Smoak** 16:35 little poke around in there, I'm just curious about how this comes to be.
**Kayla Reopelle** 16:38 Thanks, Wendy. Yeah, let us know.
And I think there was… I did ask about this last week in the… specification… Channel… And…
Trask from Java was asking if we could register a shutdown hook with Ruby. In Java, they have…
They have this, they have the ability for you to register shutdown hooks.
But that's also part of the SDK, I don't think that gets away.
with it being in the API,
So that's something we could consider.
**Robb Kidd (he/him)** 17:27 And I.
**Wendy Smoak** 17:28 And it's an SDK extension? Is that, like, the.
**Kayla Reopelle** 17:32 Yeah.
**Wendy Smoak** 17:33 They're calling it. Like, these are not…
**Kayla Reopelle** 17:36 Guess they don't have a README for… SDK extensions.
**Wendy Smoak** 17:44 Almost like they're saying, these are things that weren't not…
**Kayla Reopelle** 17:48 Yeah.
**Wendy Smoak** 17:50 Wow.
**Robb Kidd (he/him)** 17:52 Anyway, it's been a minute since I've spent time in a spec, but, it is… it is…
I guess it's, what do we guard against things blowing up? If…
**Kayla Reopelle** 18:11 Yeah, I mean…
**Robb Kidd (he/him)** 18:12 Some downstream application brings in instrumentation.
which would bring in the API,
And if they did not require an SDK, whether it's the official one or
some other SDK implementation that I'm unaware of.
**Kayla Reopelle** 18:27 Yeah.
**Robb Kidd (he/him)** 18:28 If you didn't have the… concrete implementation of a tracer provider that gives you a shutdown.
Things would blow up.
**Kayla Reopelle** 18:35 So, it could be as simple as adding guards to check to make sure it's defined.
I guess, because it…
**Robb Kidd (he/him)** 18:43 How does the instrumentation use shutdown? Because I wouldn't expect instrumentation to shut down a tracer provider.
**Kayla Reopelle** 18:50 So I think we're just calling it instrumentation. It's not actually instrumentation, it's more of a…
like, a patch for Prima.
**Robb Kidd (he/him)** 18:57 Oh, it's when using Puma, we know that Puma has some, lifecycle hooks, and so we're.
**Kayla Reopelle** 19:03 Next.
**Robb Kidd (he/him)** 19:04 going ahead and hooking into Puma's shutdown to shut down a tracerbury liner.
**Kayla Reopelle** 19:08 Yeah, exactly.
**Robb Kidd (he/him)** 19:09 B.
**Kayla Reopelle** 19:09 So, there isn't any,
telemetry that's emitted by this right now, but this, contributor has expressed interest in adding Puma metric someday.
**Robb Kidd (he/him)** 19:20 It would… well, it would ease the whole, we don't have to tell people where you have to put in tracer provider shutdowns, but maybe we… maybe we just make it… what do you call it? What's the operator? The try.
**Kayla Reopelle** 19:34 Oh!
**Robb Kidd (he/him)** 19:34 If you got a shutdown, try to shut down.
**Kayla Reopelle** 19:37 Yeah, that could work.
**Robb Kidd (he/him)** 19:40 And… and so if you've got a concrete SDK, Loaded.
Giving you that tracer provider, then it'll shut down, and if not, you probably didn't generate any instrumentation, so…
Maybe the try for now.
**Kayla Reopelle** 19:59 Yeah, I like that.
Do you.
**Robb Kidd (he/him)** 20:04 And…
**Kayla Reopelle** 20:05 on here?
**Robb Kidd (he/him)** 20:06 Sure, I can do that. And try is implemented in all the versions of Ruby that we
sport, right?
**Kayla Reopelle** 20:14 I'm pretty sure.
**Robb Kidd (he/him)** 20:15 I can check… I can check that, too.
**Kayla Reopelle** 20:16 3.1 and above, so…
**Robb Kidd (he/him)** 20:18 Yeah, that's probably it. Yep.
**Kayla Reopelle** 20:20 Yeah. And actually, we might even…
need to drop 3.1 soon? I'm not sure what the latest… support window is for Ruby.
**Robb Kidd (he/him)** 20:31 Yeah, I'm out of that loop, too. Well, I can, in making the comment, I can, try to rattle all that stuff off, too.
**Kayla Reopelle** 20:39 Nice, thank you.
Alright, so there's that one. Let's see… oh, my zoom controls are… Right in the way.
Oh, Schwan, I wanted to ask about this one. Do you think that… Robert, I know Robert has…
Commented on a few things in here.
Do you feel like his concerns are resolved? Is it ready for another review?
**Xuan Cao** 21:33 Oh, you.
**Kayla Reopelle** 21:35 Okay.
Alright.
Anything else we want to chat about on here?
This is an exciting new, issue that was opened by Hannah last week. So, we've now shipped, the semantic convention stability opt-in environment variable to all HTTP client and server libraries that we have.
And so, this starts the 6-minute clock, or 6-minute… 6-month clock, to remove that environment variable and migrate fully to stable semantic conventions. So this is just something to keep in mind,
For users, and…
Others alike, that, the environment variable will eventually go away, and will remove the old constants.
I guess not the old constants, we'll remove the references to the old attribute names.
Let's see…
**Robb Kidd (he/him)** 22:47 In chat, I'll say it out loud. Wow!
**Kayla Reopelle** 22:50 Yeah.
Hannah… Hannah killed it. She… Did an awesome job getting it all moved over.
I guess I'll call that out on here, too. Six months.
**Hannah Ramadan** 23:04 And then replacing, we can use the new, semantic conventions stuff in the gem. We should be good.
**Kayla Reopelle** 23:10 Yeah!
**Robb Kidd (he/him)** 23:11 Well, give me a minute, I'll try to convince you not to, but…
Do, it's been a… again, I've been away a while. Have we added, support to… the…
The telemetry that we emit reporting the… oh.
what does the spec call it? The schema version?
**Kayla Reopelle** 23:36 Oh, no, we're not doing schema version stuff yet.
**Robb Kidd (he/him)** 23:39 Okay, because that would be a place… alright, I'll take my minute. That would be a place where if we could say what the schema version is, articulate that in the telemetry that's emitted.
**Kayla Reopelle** 23:49 instruments.
**Robb Kidd (he/him)** 23:49 temptations.
Were I to write an instrumentation, I would probably choose to own the strings of the names, get to know the part of the semantic conventions that I'm targeting.
Declare the version of the semantic conventional targeting, and then just use those
maintain my own constants. I might use the semantic convention library in my test suite.
that, like, as a test dependency, I would bring in a particular version of the semantic conventions, and then I could assert that I am emitting telemetry
That has names that match the constants that are in the semantic conventions library. But then.
It's not a… the semantic conventions Library is not then a runtime dependency of mine.
Which lets them all kind of move independently.
I think that ship has sailed, because there's too many instrumentations using the constants from the semantic convention library.
That's my case, but I think I'm too late.
**Kayla Reopelle** 24:50 Well, I mean, Hannah will get to experiment with those choices at some point, if she can do the HTTP takedown, so… Yep. Something to consider.
**Robb Kidd (he/him)** 25:01 But I think it's predicated on being able to, in… or it would pair nicely with, having the telemetry say what schema version URL it's using, so that.
**Kayla Reopelle** 25:12 Yeah.
**Robb Kidd (he/him)** 25:15 that it's sort of like a… it's sort of a mini-contract of the instrumentation authors saying, asserting, I'm using this version of the semantic conventions, and
I know that, because I went and read them, and I'm using constants, and I have a test that test assertions against that version of the semantic conventions.
**Kayla Reopelle** 25:33 Bye-bye.
**Robb Kidd (he/him)** 25:38 Baby steps.
**Hannah Ramadan** 25:45 Can someone remind me what exactly the schema URL is? I feel like we talked about that a long time ago, but…
**Robb Kidd (he/him)** 25:51 Yeah, there's, I think it is an attribute that gets sent at the…
instrumentation scope level, where an instrumentation scope says that I'm using this version of
you can find what my attribute names mean at this URL. It's very XML-y.
and, like, find the schema for this XML at this URL, but…
You're doing it in ZMP or Jason.
So an instrumentation scope would say, my attribute names mean… are meaningful. You could find out which are valid and what their meanings are at this URL, and the OpenTelemetry project maintains the schema versions.
like, URLs of this… each of the schema versions, that particular URL.
Yeah, that's it. And other tooling could choose to go and retrieve
the schema at that schema URL, and then choose to do transforms against it, it's… it's…
the OTel collector, I think, has a processor in it that would do transforms upwards.
if the…
If the telemetry coming in is annotated with a particular schema version, that…
Again, I've been out of the game a bit, and I don't know if that processor ever came out of beta, but the notion was that it was a transformer that could take older schemas and transform them upwards.
**Kayla Reopelle** 27:29 Cool.
**Robb Kidd (he/him)** 27:30 Yeah, except there are devils in those details, because…
Some names in the scheme… in the semantic conventions change in a way that
that you can't forward compute the new thing. Like, if you break… if you break it up, break up a single value over… that used to be on one attribute, you break it up over multiple attributes in a way that's not computable. Like, a human is expected to go and break this stuff up now.
**Kayla Reopelle** 27:56 Yeah.
**Robb Kidd (he/him)** 27:57 The transforms don't necessarily work.
**Kayla Reopelle** 28:00 I feel like the transforms could be complicated with the Ruby implementations of things, because our semantic conventions are so old, and may not be perfectly… right now.
But.
**Robb Kidd (he/him)** 28:14 It is objectively better to go with the work that Hannah's already done.
**Kayla Reopelle** 28:20 He's there.
**Robb Kidd (he/him)** 28:20 names, and that… that's my… whinging about…
schemas, should not stop that. It's better.
Just bringing you into my ask about schemas.
**Kayla Reopelle** 28:35 No, thank you, thank you for… for… Chairing, and letting.
**Robb Kidd (he/him)** 28:39 Yeah, yeah.
**Kayla Reopelle** 28:40 Yeah.
**Robb Kidd (he/him)** 28:41 be angsty together. But yeah, shouldn't hold up the work that's already in flight.
**Kayla Reopelle** 28:45 Yeah, I feel like SEMCOM is a… is a giant… headache.
**Robb Kidd (he/him)** 28:51 Interesting.
**Kayla Reopelle** 28:51 Just to get everyone to point to the same things. If anyone else is curious about exploring it, I think I've talked about it a little bit before,
Oh, where is it? This one.
This pull request, this user is kind of trying to investigate other ways of…
managing the, kind of, SEMCOM stability opt-in, If the instrumentation like…
category that you're trying to point to isn't stable yet and doesn't have a path to stability. They have a few ideas in this PR.
to kind of have, I guess, different levels, instead of just, I think, like, experimental development and stable, they would also add
Some levels for… I wanna say, migrate and… Remove?
I don't remember where they defined it exactly, but this PR would be the place to get the details, if anyone is curious.
**Robb Kidd (he/him)** 29:58 Okay.
What to do when a field of name is deprecated, it seems like.
**Kayla Reopelle** 30:05 Yep, yeah, because they, they would like to update the race car instrumentation.
Ruby, as well as, I think, some other messaging-related instrumentations.
but right now aren't following the, kind of, three-module process that we've laid out. And they want to keep that on hold until they can see if there's another way to handle it, if there is no path to stability for a certain group's conventions.
So…
**Robb Kidd (he/him)** 30:36 Alright.
**Kayla Reopelle** 30:37 Yeah, because the messaging SIG is totally shut down right now, so I guess they don't really have a date on when.
That'll move forward.
I'll drop that.
**Robb Kidd (he/him)** 30:46 Fantastic.
**Kayla Reopelle** 30:47 Yeah, yeah.
**Robb Kidd (he/him)** 30:56 Thank you for the note.
**Kayla Reopelle** 31:00 Sweet! Okay, I think that covers everything, as we've poked around. Is there anything else that…
We want to take a look at today, or talk about?
Okay, cool. Well, thank you everyone for coming, nice discussions, and I'll see you all next week.
**Hannah Ramadan** 31:25 See you guys.
**Robb Kidd (he/him)** 31:27 Bye!
**Kayla Reopelle** 31:28 Bye!
