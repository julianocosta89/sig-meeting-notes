SIG: JavaScript SIG
Date: 2026-06-03
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Jamie Danielson 00:00:40 Hello!
Marylia Gutierrez 00:00:42 Oh.
Raphaël Thériault 00:00:47 Hello.
Marc Pichler (Dynatrace) 00:00:55 Hello.
Jamie Danielson 00:01:00 I feel like it's been so long.
Since I've been on one of these.
Trent Mick 00:01:04 Yeah, welcome back.
Jamie Danielson 00:01:05 Thanks!
Trent Mick 00:01:10 And it's one of those I-want-to-believe meetings.
Marc Pichler (Dynatrace) 00:01:17 Yeah, sometimes, there's… nobody in the office here, so I take the car from here, otherwise I… Go to a separate room.
Alright.
I guess we can get started. The first topic here is… trend with SDK Trace package.
Trent Mick 00:01:54 Can you make your screen wider?
Marc Pichler (Dynatrace) 00:01:59 That's fine for me.
Trent Mick 00:01:59 People with bigger managers.
Marc Pichler (Dynatrace) 00:02:03 do this.
Trent Mick 00:02:04 Thank you.
Right, so… We had these changes that we wanted to make to the… ticket environment variable reading out of SDK trace base, and also related the SDK Trace Node and SDK trace web we've been doing talk of and various work for.
getting rid of the need for them. They're kind of separate issues, but… So David had had a PR that he was working on, and I'd been reviewing. I guess I don't know if David's coming, but… Let me open Slack today. Where he had been… adding a tracer provider class in SDK Trace Base, that… alongside Basic Tracer Provider that we have right now, and the main thing we did was remove environment variables. So… I… started an alternative, which is to create an SDK trace package alongside the other one so it can exist in parallel for a while. This PR moves SDK Trace Base to be basically just a light shim that only does the environment variable handling, and otherwise is deferring everything to SDK Trace.
And then the future that we want when we're allowed breaking changes, so when we do actual 3.0 maybe, depending on timing, unless it comes too quickly, then it's kind of too short of a deprecation period, arguably. We can debate that. But the eventual plan would be then we can drop SDK trace base.
We can move everything over.
So… I guess so I had some… that's the basic setup. Reviews are welcome on that. I think David reviewed it yesterday.
What were the questions that I had there?
Sorry, I added these agenda items a day or two ago.
Okay, I think, Mark, you've been most involved, because you set up that… that… issue a while ago describing, like, lands and things that we want to do for Dignit, so… A quick review from you would be welcome.
The PR looks… big, but it's a lot smaller than it could otherwise be. Almost every file is a move, and the diffs in there are relatively small for the files under source, so the runtime files, and there are a lot of cosmetic changes to the tests, because everywhere a basic tracer Provider was used was changed to be Tracer Provider.
And everywhere, so an internal change, for example, is that the internal tracer class, which is not public.
Shouldn't be created directly, though the tests were doing that everywhere, so there were some cosmetic changes there to go through a tracer provided to create it, so… Anyway.
Marc Pichler (Dynatrace) 00:04:54 Yeah, I'll assign this to myself, and I will have a look. I already started having a look at that earlier today, but didn't get very far.
Okay.
Trent Mick 00:05:06 Cool.
Marc Pichler (Dynatrace) 00:05:08 dope.
Trent Mick 00:05:08 And then, so I took the opportunity to clean up.
A little bit in there, so the internal tracer was carrying a generic limits object, which had no point other than on input, like, you want to merge the generic… the environment variables for generic limits in with the spam limits, if someone's specifically done the spam things, but after that, there's no point in having those separate objects, so… I'd had a question that I didn't bother following up on. We could use this as a chance to change the… Instructor option to trace a provider from span processors to just processors.
So when you create a logger… log… when you create a logger provider, for example, you just pass in processors, not log record processors, for example. We can change that.
And declarative config for both logging and tracing uses processors instead of spin processors, so… If we wanted to, but I don't know if there's a lot of value one way or the other. It's just one constructor option.
Yeah.
Jamie Danielson 00:06:13 I tried updating one of the links, I feel like the links might not be… pointing to the right things, or I might just be getting confused.
there you go.
Trent Mick 00:06:24 URLs in the… in the agenda doc, you mean?
Jamie Danielson 00:06:28 Yeah, so this was, like, 6765… And then the third link was also 6765, so I changed it to 6775, but I might have them backwards.
Trent Mick 00:06:42 Oh, I probably just pasted wrong.
Jamie Danielson 00:06:45 So I just… I don't… I just changed it, and I don't know if I changed it right, so I figured I'd… ask.
Trent Mick 00:06:54 Oh, they're backwards. Okay.
Okay, so the… PR to review is… Should be that one, 7-5.
Jamie Danielson 00:07:06 Okay.
Trent Mick 00:07:07 And… I guess this one's 6'5".
is… that's the one that I'm blocked on for… Oh, wait a second.
Jamie Danielson 00:07:19 Sure, that should be…
Trent Mick 00:07:19 I totally screwed it up now.
Sorry The things are… Can we not be fancy? Just give me text and auto URL.
Jamie Danielson 00:07:27 Right?
Trent Mick 00:07:30 Okay.
I'm deleting everything.
Forget it didn't happen, don't need any reviews, it's all good.
I'm learning.
push for it.
Sorry, the thing I'm blocked on is work on declarative config for… setting up tracing from declarative config, I want… the code path there needs to not use environment variables.
And so, to do that, I need the trace package to have a way to create trace providers that doesn't use the environment variables, so… that's the thing that was blocked on there.
Marc Pichler (Dynatrace) 00:08:20 Yeah, thanks for working on this, I will have a look at that, I think it's, The way you did it with the moving the files is, good way to go about it. Otherwise, the diff would have been huge, but this looks… looks good.
Trent Mick 00:08:40 That's actually secondary. The most important thing to me was that the Git history is still there, so if.
Marc Pichler (Dynatrace) 00:08:44 going on in both.
Trent Mick 00:08:45 back and see when did this change, and possibly why did it change, we can… the… the good histories here. So, yeah.
Marc Pichler (Dynatrace) 00:08:52 We don't have any deprecated things in SDK trace space right now, right, that we would be able to remove.
Trent Mick 00:09:01 I didn't go looking hard, but I didn't see anything that was… Yeah, maybe I'll take a look to see if there's something that we take a chance to drop, you mean, yeah?
Marc Pichler (Dynatrace) 00:09:17 Cop.
Alright, then I'll have a look later to… unblock the config bug, and get this in, and then, should be… You should be good to go.
Trent Mick 00:09:31 Cool, thanks.
Marc Pichler (Dynatrace) 00:09:37 Alright, and this is the config PR image, right?
Trent Mick 00:09:41 David, you had your hand up.
Don't prefer.
David Luna Bistuer 00:09:43 About duplicating and dropping, what's the, strategy here, so if… I guess my idea, or what I understood, was to have this change here, and then for SDK 3.0.
Just have to remove SDK Trace Web.
Node and base, and now they have… SDK trace, period.
Marc Pichler (Dynatrace) 00:10:10 Yeah, so there's two ways we can go about it. We could just drop it in 3.0, and then it's just gone, or we can still publish a 3.0 of the old packages that are continuing to exist.
But we tell people not to use it.
And don't add any new features to that, so… everybody who wants to use new options and stuff like that has to, start using SDK Trace, and then we drop it with Fortido, or we can also drop it out of bed, I think. We can just… after a year, retire package. I think we've done that before with something else, I don't exactly recall what it was, but there was a stable package before that we just stopped publishing somewhere along the 1.x range.
So we're flexible in that sense.
We don't have to do it with read at all, necessarily.
Trent Mick 00:11:16 Thanks for bringing it up, David. There was… if you can go back to the agenda, Doc, I'd had a question there.
So… one of the things I think that was in your… initial issue right up, Mark, was… or one of the issues, or a whole bunch of issues.
Cure NPRs. Was whether we provide utilities for people that are using the environment variable.
Marc Pichler (Dynatrace) 00:11:40 income.
Trent Mick 00:11:40 an SK Trace Base, and aren't using SDK Node, for example, which does all the variable handling, whether we'd want to expose Methods to reproduce that same behavior.
If someone has a strong opinion on that, let me know, otherwise I'll settle on some opinion and decide.
I'm not sure about bothering to provide one.
I don't know. Or where that would live, for example. I don't want it in SDK trace, because it shouldn't just… it's nice if it's just not reading environment variables at all. And if it's an SDK node, then why aren't they using SDK node?
To build up the SDK.
Marc Pichler (Dynatrace) 00:12:19 Yeah.
if we can get away without doing it, I think that's the preferred option.
Pranav Sharma 00:12:26 Burn.
Marc Pichler (Dynatrace) 00:12:27 we could add it to SDK node. I think I suggested that on one comment at some point.
since SDK node will stick around, and it's also kind of difficult to remove stuff from it.
Maybe we also try to avoid that.
That leaves one more option, which would be a SDK trace node.
Which is deprecated anyway, and is going away, in… some… Some point in the future.
So we could put it there if we need it, but if we can avoid adding it.
That's also fine.
Trent Mick 00:13:11 Okay.
I feel like maybe I'm arguing both sides of the debate. I might actually… argue for SDK node having… exporting a bunch of functions for… here's how to create SDK components from config, whether that's environment variable or the file config stuff, just so that SDK node, or maybe some not-node-specific SDK lib package gets around, so that distros that have SDKs or that export an SDK can use SDK node as, like, an SDK builder type thing, which I think is… Maybe an intended thing, but anyway, that's down there, don't worry about that. Okay.
All good.
David Luna Bistuer 00:13:55 I have another question before it's available.
Maybe it's off-topic, but, looking at the… well, making my… the PRs from the CK note and looking at the UPR trend.
I'm wondering if… We would like to do some ran… some runtime checks for config… from configuration.
Because what I saw is, like, we are kind of relying on types.
just to, for example, I expect a number, and then it's, okay, the configuration option is set, otherwise I fall back to the default value.
But I'm… we are not doing… When we are… actually, when we are, getting from the EMBA and the environment, yeah, we are… we're doing the type checklings.
Because the functions that get, strings, booleans, lists from.
From the environment variables there, they do the type check at runtime.
But if we get an object with a lot of properties, then we just, you know, we do, we just check that the property exists, or not, we just.
Trent Mick 00:14:58 Do you mean a configuration object?
David Luna Bistuer 00:15:02 Yeah.
Trent Mick 00:15:02 So, like, if someone is using file-based config, but they just build up the config object from the types, is that what you mean?
David Luna Bistuer 00:15:10 Exactly, so I'm just installing SDKnode, I'm just gonna want to create a tracer, and I'm passing a tracer options object, And, okay, max buffer size, I put a string instead of a number.
were an object.
Trent Mick 00:15:27 So, maybe? I don't know, I'm undecided on that one. Like, I don't know how much we're gonna promote Breeding your own config object, rather than going through… Fair.
David Luna Bistuer 00:15:39 Right.
Trent Mick 00:15:40 Yeah, I mean, it doesn't have… sorry, I was gonna say configuration file, but we could change it so it's configuration content, that it doesn't have to come from.
David Luna Bistuer 00:15:46 files.
Trent Mick 00:15:46 someone could load it from Remote Config or something like that, but it goes through a schema validation there, so, like, that's… The intended first line of defense, at least, whether we have second line and have… anywhere that config comes in, be defensive, I guess we can decide. I don't know.
Yeah, currently. Currently, we're just trusting the first line of defense, basically.
Marc Pichler (Dynatrace) 00:16:09 Yeah, this is one of the things I ran into when playing around with the component provider, stuff.
is… I kind of created the type for the component provider, and then I was like, it would be kind of nice to have it typed instead of getting unknown and then having to look at all the different options and doing the same validation again that happened in the config package already.
So, I kind of worked around it by, having it, just tricking the types into, like, not having me make… validate everything. But that only works for internal stuff right now, so anything that we already have defined.
For… other… component providers that users might write in the future, they would still have to do that validation manually, so there might be some opportunity to align things there.
If we decide to move the… where the validation happens around, I don't have a good suggestion how to do that, though.
Seems like a big change.
Trent Mick 00:17:37 And something I think we can discuss separately, independently, decide. Like, I wouldn't want us to marry to a particular package like Zod that provides… you know, runtime schema checking kind of thing, necessarily, or at least not right now. Have that be an independent decision if we go there.
Marc Pichler (Dynatrace) 00:17:55 Thank you.
I agree.
David Luna Bistuer 00:18:03 Thanks.
Trent Mick 00:18:06 So, yeah, my idea, if we have an SK Trace package that lives beside the other ones for a while, if… if it looks like we're potentially pushing a 3.0 SK release out till September, then maybe if we get this in soon enough, that's enough of a deprecation period that… we can drop the other SDK pack.
SDK trace-star packages for 3.0, and I think that'd be kind of a nice cleanup, and then we have SD logs, SDK metrics, SDK trace.
That makes the usage a little bit cleaner.
Okay, so this next one is just a request for reviews.
It looks like, oh, since I put this up.
Marilla at least started asking questions.
So we've done…
Marylia Gutierrez 00:18:56 They may…
Trent Mick 00:18:57 First pass?
Marylia Gutierrez 00:18:58 Yeah, just a few nits on, like, specific use case, but yeah. Otherwise, yeah, it's fine. Just a little question.
Trent Mick 00:19:08 Cool, I'll respond to those, and then… ask for another review on that, thank you.
Marylia Gutierrez 00:19:15 Oh, so you already opened the one that I put it there? So yeah, just Robert reached out to me, because they… apparently they're trying to… mark this back as stable, so they went to a few, like, different SDKs just to implement it, have it basically showing that it's working, kind of thing. So he wanted to make sure that somebody is… reviewing this, so I did, like, a… just a quick pass, but if anyone else can also do, like, a review, to help them out as well.
Trent Mick 00:19:47 These… I think I looked at the spec, like, a week ago, the spec issue, not… not his implementation here for us, because we're, like, one of the only languages that doesn't have this, so that I think is why he went and implemented it.
What is this for?
Is this for being able to carry, I guess, across sub-processes or something like that, but does a user have to… I should just read it.
Marc Pichler (Dynatrace) 00:20:17 I think it does.
Trent Mick 00:20:18 He does have a usage example. That was a simple… that was the thing I was missing. Does a user have to use this directly with Inject, or do they… can they set it as a propagator?
His use case is using propagator.injectandExtract directly.
Okay.
Marc Pichler (Dynatrace) 00:20:44 I also have to take a look at this.
The main use case for this is… CICD stuff, right?
Marylia Gutierrez 00:20:57 Yeah.
Marc Pichler (Dynatrace) 00:21:03 I think it could be very helpful for, gitHub Actions and stuff.
I'll have a look at this one, too. I'll assign myself… Sure.
Thanks for bringing that up.
How many, prototypes are there already, we would be the third one, right? Or is it already… does it already exist as well?
Marylia Gutierrez 00:21:40 I can actually check, that's a good question. Yeah, he just told me, like, the plan is that in a few months, they want to mark it stable.
So, it's kind of like just a rough timeline for now.
Marc Pichler (Dynatrace) 00:21:53 Alright, sounds good.
I'm… And I guess we can move on to the next one.
This is feedback on the…
Pranav Sharma 00:22:11 Yeah, 8.
Okay, so me, when I posted that comment, I did not notice that there was some additional feedback.
So, just wanted to understand. So, the idea right now is that if there's an ongoing export going.
We just skip it, but basically, is the desired behavior that on force flush, we wait for the ongoing export promise to complete, and then manually trigger the run once again?
Marc Pichler (Dynatrace) 00:22:42 Yeah, I think… that is how it has worked before, and I think the metric spec is the only spec that doesn't state this outright, but there is an issue somewhere where this basically agreed that this is the behavior that is desired for a force flush in In the metrics SDK.
Pranav Sharma 00:23:07 Hmm.
Okay, so just to be clear, like, this will be just, like, a wait till the ongoing export promise is continued, like, is finished, and then just start again with the.
Marc Pichler (Dynatrace) 00:23:21 Yeah, that's my understanding how that feature would play into, how that feature would play into the spec for it. As I mentioned earlier, I'm not sure if it is actually in the spec document, or if that is missing. I seem to remember there was some, discussion at some point, you might have to go look for… for issues.
Jamie Danielson 00:23:48 posted it in the chat, the issue mark you opened November of 2022.
Marc Pichler (Dynatrace) 00:23:54 Yeah, that's a vintage one.
Pranav Sharma 00:24:00 I did not take a look at this issue. I mean, this wasn't part of the spec, but I can… I can read this issue.
And.
Trent Mick 00:24:09 He didn't read all issues back to 2022.
Pranav Sharma 00:24:17 Oh, man, yeah.
Marc Pichler (Dynatrace) 00:24:19 I think this is just… Wait, I think this is something different, Red.
Jamie Danielson 00:24:26 Is it?
Marc Pichler (Dynatrace) 00:24:28 Is if metric reader should have forced flush at all.
Jamie Danielson 00:24:43 Oh, that might be what it is.
Marc Pichler (Dynatrace) 00:24:46 Not sure if that is… Maybe that's already fixed.
I have to double check.
Let's meet the provider.
metric reader…
Jamie Danielson 00:25:07 Oh, there's another one.
Marc Pichler (Dynatrace) 00:25:09 There's shut down.
And the periodic exporting metric reader has forest flush.
Jamie Danielson 00:25:18 There's another issue from Aaron.
It says, when I do shut down, I want to do a final collection of metrics.
Marc Pichler (Dynatrace) 00:25:32 Yeah, I think there's some place where that link is missing, too.
Jamie Danielson 00:25:45 Oh, yeah, so then you have…
Marc Pichler (Dynatrace) 00:26:08 It doesn't say specifically here in the spec, but…
Jamie Danielson 00:26:18 like, in 2024, you had commented, like, looking at implementations at the time that Java and Python don't collect Before shutdown, but Java and Python… no.
The for- the shutdown does not force flush.
Oh, that they do about fear.
Trent Mick 00:26:38 My provider doesn't, but periodically.
Jamie Danielson 00:26:40 Yeah, the periodic metric.
thing.
Trent Mick 00:26:44 Reader.
Jamie Danielson 00:26:44 Ugh, yeah.
Marc Pichler (Dynatrace) 00:26:51 So, the… Or it doesn't answer the question yet. I… we'll go have a look and see if I can come up with a good, Good issues somewhere that, says that… we should… Forest Flush, but also we should collect on forest flush, but since it's actually now doing that, in that way, I think if we were to change it.
people would be a bit confused. I know that it's used for lambda and stuff like that, to flush data, at the end, so… People might be broken by changing the behavior there.
So I think we just want to make sure that we don't break the existing behavior if people Haven't set the new patching option. Could be one way.
So I would also like to avoid having two different behaviors for, like, whether an unrelated option is set or not.
Pranav Sharma 00:28:02 Yeah, that would be, better. Like, batching seems unrelated to how force flush should behave, so… I agree with that. I also just implemented this in Java, and… but I can't remember exactly… it's been a while since this was open, so I can't remember exactly what I did, there. Like, does it trigger a new collect plus export cycle, if an ongoing one is already there?
How do you, propose that I address this comment here right now? Should I just… .
Marc Pichler (Dynatrace) 00:28:43 Yeah, I guess if we just… Await whatever is in progress, and then, collect again, and, implement forest flush that way. That wouldn't necessarily change Anything for people that are using it without the option, and people that are using it with the option.
Pranav Sharma 00:29:06 Okay, and…
Marc Pichler (Dynatrace) 00:29:07 Yeah.
Pranav Sharma 00:29:08 One slightly unrelated thing was that you mentioned the use of, like, this in Lambda and other serverless environments. So, does this behavior, alleviate the concerns for people running in serverless? Because I just had an issue where A user reached out and they said that they were having trouble with this in Java, because… They were trying to force flush, manually, and because of the ongoing export cycle, it was… it just kept getting, skipped. So… Have there ever been concerns about AWS Lambda or other serverless environments before?
Marc Pichler (Dynatrace) 00:29:51 Yeah, so, I think, so, we previously never ran into a… Problem where we had an ongoing operation that Oh wait, let me think about that again.
maybe that is a bug that exists currently, in the current implementation, but I'm not exactly sure.
So, I think what you… what you said is, like, there's an ongoing export, then forest flush comes around, and… it just skips the ongoing one, right? Right.
I think that…
Trent Mick 00:30:43 The ongoing one, or it doesn't reschedule a new one?
Pranav Sharma 00:30:45 It doesn't schedule it, because there's already an ongoing thing, ongoing export cycle going on, so just… it doesn't initiate a new collect cycle for them.
Yeah.
Marc Pichler (Dynatrace) 00:31:00 I think we always had, like, the… or not always, but at some point, we added this, behavior that forest flash would do one more collect cycle, and then, that would alleviate that issue. What I think would still be a… would still be possible, that could happen is I… I think Pending export that might be in progress when forced flush is called is not awaited right now.
Before we schedule the new one.
But I'm… I'm not entirely sure.
I'll have to double-check that.
Pranav Sharma 00:31:42 So what I'm hearing is that whatever I do with this PR, it should not deviate from the existing behavior, whatever is the behavior on the main branch right now.
Yeah.
Marc Pichler (Dynatrace) 00:31:53 If possible, it should not deviate from that behavior, because one of the problems that we were solving by having that forced flush behavior is addressing concerns for Lambda users.
And… Aye.
would have to go back through the issues, but I think there were at least 3 issues opened over the course of a few years, where people wanted to use Forest Flush for exactly that.
or wanted to use Shutdown, which includes a forest flush, and they weren't able to get the collection to trigger.
So… Some people might be broken if we… if we change the behavior there.
Pranav Sharma 00:32:39 Okay, so what I'm gonna do is, like, I'm gonna read the code again from the main branch and see what the existing behavior is. I'm gonna post my understanding of the existing behavior, and I'll let you comment there, and then, address the comment that you just made.
Marc Pichler (Dynatrace) 00:32:55 Sounds good. Thank you.
Trent Mick 00:33:00 This might not be helpful, but I was just going back through… Mark, I remember reviewing one of your Pierre, there's a thing I just opened, er, LinkedIn chat.
Was that a similar discussion?
This is for logging, not for metrics, but… There's an in bold in the description saying we need to make sure we do not await the export.
Before calling. Maybe that's not related. I didn't… I vaguely recall.
Marc Pichler (Dynatrace) 00:33:36 own… Yeah.
Trent Mick 00:33:38 Test cases of multiple exports happening at the same time.
Marc Pichler (Dynatrace) 00:33:43 There's, so this was also another… another issue with, force flush in the SDKs is, Currently, we don't have a functional force flush for exporters, mainly because it's not really specified.
Or… not.
There's no real spec for what an exporter should do when it's being first flushed, just says it should speed up the export, but that's kind of a bit vague, because it's going as fast as it can already.
So, the problem here was that, We were awaiting the export before calling for a flush on the exporter.
So it never had the chance to do this.
Speed up the… Export, whatever it would do.
And in our case, what we would do with the experts is we would cancel the retries.
Or a pending export.
Because what is happening right now is, since… Force flush effects are included in shutdown, when there's an export that's going on and the collector is not reachable.
the… Export timeout.
Will, just be completely used up.
And that's, I think, by default, 10 seconds or so. So people that are in running containers somewhere and they are crashing on startup, they, might wait 10 seconds until they can restart again, because they are still trying to Flush, but there's no way to flush, to a collector that doesn't exist.
So it blocks shutdown.
This is a somewhat related but different issue, I would say.
I don't think it's in scope for the… PR that's, up right now for the metric reader to… implement.
That change as well there.
Trent Mick 00:36:05 Thanks.
Yep.
I'm not helping.
Pranav Sharma 00:36:10 Just to be clear on one thing, like, we absolutely want to avoid, like, simultaneous exports, right? At one point, only a single export cycle should be going on, right?
Marc Pichler (Dynatrace) 00:36:27 I think the answer is yes.
I think all the… all the different processes avoid that right now, to scale your micro ones at the same time. I think there's also, card in the exporters that… Avoids that multiple exports are in progress at the same time.
Or in some exporters, at least. And I think there's also some specification for it.
Trent Mick 00:37:04 You said you're working on the job site, Pranav, do you know if that's… Similar there, or not?
Pranav Sharma 00:37:09 Yeah, I did implement this in JavaSite, and I think we all… we waited there. Like, if there was an ongoing export, we just skipped that cycle. But it's been a while since I did that.
Yeah, I can't really remember if we, on 4Slush, we trigger a new, collect cycle, if there's already one. I think.
I think we just leave it there. Like, we don't… we don't trigger a new cycle.
If one is already going on, so…
Trent Mick 00:37:42 You can always put up your hands and say, it's forced flush, it's just… we're doing our best here, so… Too bad.
Nothing. Yeah. Okay.
Marc Pichler (Dynatrace) 00:37:54 Sorry that you, had to stumble into this, somewhat mess.
Trent Mick 00:38:01 You're only allowed to say that on startup and shutdown, Jamie, not… Regular thing you have to keep doing your best, but…
Pranav Sharma 00:38:15 Alright, thank you.
Marc Pichler (Dynatrace) 00:38:18 Thank you. Thank you.
Alright.
Moving on to Jenny Isemitic conventions, Jamie.
Jamie Danielson 00:38:32 So, just general state of the world, for folks who aren't aware, the GenAI semantic conventions are split off into a new repo instead of staying in the core semantic conventions repo. And, There's going to be… There's not a release yet for the GenAI SimConv, but there's gonna be a release of Core soon. So, like, two things. One.
Whenever we update… our semantic conventions, if there isn't a GenAI release yet, all the GenAI semantic conventions will show as deprecated.
Because they're deprecated in the main core repo.
So that's kind of an FYI. I feel like we might get questions about that. But I put a link there, too, to Lyudmila's announcement in CNCF Slack.
But then the other thing in general is that we will have to… have a new package for GenAI semantic conventions, separate from regular semantic conventions, because it's gonna have a different release cadence and version.
So this is just kind of a link to an issue, that… Wolfgang had opened, links back to the issue that I had created in Gen AI SimComConv for, like.
tracking, you know, the updates in the various repos.
Yeah.
Trent Mick 00:40:06 Was there gonna be a… a… Sorry, I lost my tab here. And OpenTelemetry-js-genai, because there's one for Python.
So…
Jamie Danielson 00:40:17 So…
Trent Mick 00:40:25 So there's no JS-specific thing there, so I'm not sure what the intent is.
Jamie Danielson 00:40:29 We don't… have to have a new repo. I'm trying to remember… Oh, they created a new one because they didn't want to have to deal with new versioning, like, I think, maybe?
Or maybe they're testing something?
But… like, the… basically, we would just have another package. Like, right now, we have OpenTelemetry.
slash semantic conventions. We'll add a new package for OpenTelemetry slash Semantic Conventions GenAI.
Trent Mick 00:41:08 Okay, so the SEMCOM… will… Update more quickly there.
Jamie Danielson 00:41:18 Yeah, and Python also has a separate repo created for Gen AI instrumentations, to try to get things moving faster and get more eyes from more places.
Trent Mick 00:41:33 Sorry, maybe I was misunderstanding. When you're talking a new JS package, are you talking about needing a… another semantic conventions package for.
Jamie Danielson 00:41:42 Yes.
Trent Mick 00:41:43 I see, okay.
Jamie Danielson 00:41:44 Yeah, and so, like, the issue that's linked should, like, kind of explains it. There's a lot of wordiness in there, but basically, in bold in the middle, the recommended approach is generate into a new, separate semantic conventions GenAI package. So basically, the way that we currently have semantic conventions.
kind of do the same exact thing for semantic conventions GenAI. So we have, main entry point and incubating entry point for experimental.
So, we should have a cemented conventions GenAI package that also has a main entry point for any stable GenAI attributes, and an incubating entry point for experimental Gen AI attributes.
Trent Mick 00:42:31 Okay, so… I think that sounds fine.
Jamie Danielson 00:42:35 Hmm.
Trent Mick 00:42:35 I can… I don't know if you have more bandwidth to drive that, but I can certainly help with those scripts and things.
Would… do you think that… Package will live in core repo, or separate repo, or…
Jamie Danielson 00:42:51 I guess that's a good question. I was thinking it would live kind of alongside the… where semantic conventions are now, which is in Core.
Trent Mick 00:42:58 I think… I think that's fine. We can update the release process to have a… SEMConf Gen AI release step, so it can be released independently.
Jamie Danielson 00:43:08 Yeah, because we already do that, which makes it not as bad. Like, some different languages do different things. Like, Java has a whole nother repo for semantic conventions.
Sure.
I think they're gonna create a whole other repo again, too, for Gen AI, because they don't want to have different releases in their… Like.
Trent Mick 00:43:26 Yep.
Jamie Danielson 00:43:26 Whatever, we already do that.
Trent Mick 00:43:28 It'll be straightforward.
Jamie Danielson 00:43:29 Yeah, so I think it's a pretty light list.
Trent Mick 00:43:33 Yep, it should be.
Jamie Danielson 00:43:35 I think Wolfgang might even work on it, or I might work on it with him, unless someone wants it specifically.
But otherwise… We can probably do that.
The weirdest part right now is just that we don't have a release of the new thing yet, so it's like… Preparing for it, but we don't yet have it.
Trent Mick 00:43:58 Okay, sure. Yeah, like, whoever's driving, I can definitely help with reviews, or, like, have a chat to… get a first PR.
Whipped up.
Just hit me up.
Jamie Danielson 00:44:12 Cool.
Thanks.
Marc Pichler (Dynatrace) 00:44:17 New package, or… generally, the semantic conventions packages approach is something we still want to do, right? We don't want to go code generation only.
Or anything new?
I'm probably opening can of worms.
Jamie Danielson 00:44:37 It is the can of worms, like, the way that, Python… Does it?
Marc Pichler (Dynatrace) 00:44:42 I think we had talked about it at some point, that, Since we have to copy experimental.
attributes anyway, code generation might be the easier way to go, because there you just say, hey, I'm using semconf, this version, and generate the code for it.
The reason I'm asking is I was playing around with… Weaver.
some time ago. And… I was looking into if there's a way to have an NPM package that redistributes Weaver and just points towards a specific semantic conventions version, and you just say.
Auto… Generate stuff. Edit.
Jamie Danielson 00:45:30 Hmm.
Marc Pichler (Dynatrace) 00:45:30 like, writes that to a TypeScript file, or a JS file, or whatever you want.
In a specified format that's already redistributed with the package, so you don't have to, like, set that up yourself.
Jamie Danielson 00:45:46 That is… an option?
Probably. There's another issue that I was gonna open in general related to, like, adding Weaver Live Check to our CI to see if instrumentations are omitting valid attributes.
But I think that would be separate from what you're describing, because this would be more like a testing CI. Yours is more of, like.
Instead of us… Tell me if I'm understanding right. Instead of us having, like, that semconv.ts file that we're copy-pasting into… Well, don't we have a script? Didn't Trent write a script for…
Trent Mick 00:46:23 There is a script called Jen SemConf TS.
Living.
Marc Pichler (Dynatrace) 00:46:27 Yeah, it's very similar. In a place that people…
Trent Mick 00:46:29 Most people probably don't know about it, but it's not advertised, really, anywhere.
But I'm not exactly sure what the CodeGen thing is.
That we're talking about here, so… You're saying, like, a creator of an instrumentation, whether that's in the contribib package or a third.
Marc Pichler (Dynatrace) 00:46:46 Oh, yeah.
Trent Mick 00:46:47 would generate their own SEMConf TS from Weaver and a package version? Or, sorry.
Marc Pichler (Dynatrace) 00:46:56 Yeah.
Trent Mick 00:46:56 CENCOM version.
Marc Pichler (Dynatrace) 00:46:59 Yeah, exactly, so you would have a semconconf version, maybe you would have some config file that's, like, utter semconconf.
JSON or whatever, and it says, like, this is my SEMCOM version, maybe also this is a repo, since probably GenAI is not gonna be the only SAMCOM that's gonna be federated in the future, there's probably gonna be multiple ones. They're just pointed towards the repo from which you want to generate your SEMConf stuff.
And then you select what you want to have, it also writes that to that config file, so now you have a step that you can run via, like, an NPM script or whatever. You can do npx, generate some config, and then… You get the stuff based on your config file.
And then you have this Otter-Weber redistribution be a def dependency of whatever project you have.
And you can just execute that instead.
I actually do have… I haven't touched it in a while, but I can show how it would work if you're interested.
Jamie Danielson 00:48:14 I'm intrigued.
Trent Mick 00:48:15 Yeah, sometime. Sounds interesting.
Marc Pichler (Dynatrace) 00:48:19 I can actually share it right now if… Oh, y'all.
Trent Mick 00:48:27 Is there arguably potentially less sharing going on there, then?
because everyone, for even, like, for stable SEMCOMF things, then… You could have… Like, this is… my girl.
Optimization, so maybe it doesn't matter, but you could have 5… Yeah. Instrumentations that are all using the same define, and so you get 5 constants.
Marc Pichler (Dynatrace) 00:48:50 instead of…
Trent Mick 00:48:51 What could have been won in some cases.
Marc Pichler (Dynatrace) 00:48:53 Yeah.
Trent Mick 00:48:54 Maybe it's not a big concern.
Marc Pichler (Dynatrace) 00:48:56 Yeah, I was mainly going off of the size.
of the current SemConf package, which is fairly large.
And comparing it to that, duplicating it.
is probably fine. I think nowadays we also include the ASP.net SAMconf in the sameconf package.
Which just adds a bunch of stuff that we also probably wouldn't need. So, I guess there's a crossover point at some… place where the SAMConf package, or the duplicated SAMConf is larger than the current SAMConf package.
Trent Mick 00:49:39 Well, yeah, the duplicated thing, I think this size on… well, okay. I think the only time… so there's the… the package gets so big that just npm install uses all of my bandwidth for the month that kind of big, like, ridiculous, which is what cement conventions is getting to, because we're carrying all of the… the backwards compatibility stuff. But then the… usually the… the discussion on sizes, For bundling, and what… you know, how many extra defensive things are in there for that, so that was the one I was talking about, but yeah.
Anyway, that would be interesting.
what you have at some point.
Marc Pichler (Dynatrace) 00:50:16 This is, this is essentially what I… Back-coded.
So you do… Something like, this here, and then you generate this config, and I have it sit somewhere here.
just says, like, this is just one, SEMConf.
Repo right now, but, you know, one could easily say It's using different, A different place, or a different repo, and then it generates it from that, and then you say, like, what sort of stability you want to have, and what you want to include.
So here I have, like, Node.js and HTTP, and then it uses… the templates and stuff that, Trent, you created in the… In the core repo to just generate this.
And one of the benefits of that is you only have the ones that you need.
You don't have more than that, and also you have it versioned, so you just… have this here, and with JSON 5, you could probably also put, like, a comment here to have a renovate bot updated.
Which… probably is also helpful for instrumentation authors. You will get, like, essentially a SemConf update that will then generate your PR, and then you can use that PR as a starting point to change things.
Or not, depending on… Yeah.
Trent Mick 00:52:00 Okay.
This is a separate, bigger discussion. I don't want to get…
Marc Pichler (Dynatrace) 00:52:04 And, yeah.
I think… I'm not sure if there's any other topics on the agenda still.
Trent Mick 00:52:10 I added two.
Marc Pichler (Dynatrace) 00:52:12 Oh, also…
Trent Mick 00:52:14 Also, I have a package named Flynn.
Jamie.
You can get, like, 70… almost 80 characters width, I think, in that one.
Jamie Danielson 00:52:23 Excellent.
Trent Mick 00:52:25 Were you gonna do a release this week, Mark? I'm moving on.
Marc Pichler (Dynatrace) 00:52:29 I was going to, yeah, but I'm not sure if I would be able to make it.
Trent Mick 00:52:35 Okay, that's cool.
I'll be away next week.
In case you need… or… I mean, you can ping me for the clicking.
The… accept the release review thing, if you want.
Marc Pichler (Dynatrace) 00:52:50 Yeah, I will just, see if I have… anybody available at that time. I keep annoying David to approve my releases, so I might do that again.
So now I can find…
Trent Mick 00:53:09 Maria, we can do those.
Marc Pichler (Dynatrace) 00:53:10 Firefox window.
Trent Mick 00:53:11 pre-release tags.
Marylia Gutierrez 00:53:13 Nice.
Trent Mick 00:53:14 Yeah.
Marylia Gutierrez 00:53:15 Final, final, final. This is the final. For real, yeah.
Trent Mick 00:53:24 I'd had enough time thing. I started trying to do, another PR on the attributes widening, but using unknown, as standard.
thrown out as a potential thing we discussed a few SIG meetings ago, if you remember.
Boy, that runs into some interesting things.
like… But I spent more time on TypeScript yesterday than I enjoy spending on TypeScript. So anyway, there's not really much to show there.
I admit to… getting a bit scared and wanting to go back to having a separate attributes type for doing this kind of thing, but if we did… so a thing I discovered is SQ Metrics does not really do any guarding on the attributes coming in, so… for example, the Prometheus serializer, there's… I think this is coming from spec, so, like, when serializing attributes for Prometheus.
Oh… Tags or strings, right? So let's go to Stringify.
everything, and that's… that's easy for primitive types, but I think the rule in the spec is that an attribute that's a more complex thing should just be JSON.stringified.
And so we use JSON.stringify, but as soon as you allow attributes to be type unknown, if there's a big int in there, then JSON.stringify crashes, or throws. So now, Prometheus Serializer.
And throw if people are throwing weird stuff into attributes, and do we want to get to a place where… and this is kind of what the spec is implying, is that attributes should allow all of these complex types.
Not bigInt, but it doesn't say anything about guarding against a circular reference, which is another thing that'll crash JSON.stringify, so… Should we… is the spec… Here's a question, this is rhetorical, maybe. Should… is the spec saying that an implementation of SDK metrics should be guarding every call that's passing in attributes and checking that there aren't circular references in there. Or we change to… from JSOND Stringify to… a JSON stringify library, and there are myriad ones out there that, for example, all the loggers are using to guard against circular references, things like that, which is maybe where we end up going on this.
Anyway.
Marc Pichler (Dynatrace) 00:55:45 I think there was some exception for… SDK metrics, that it doesn't have to accept everything.
Trent Mick 00:55:55 store.
I couldn't… I couldn't find that. There is an exemption in the attributes spec page for metrics and resources not having to implement attribute limits.
But not about… A subset of the attribute value types.
Which I thought was interesting, because I misremembered that and went back to the spec. If you do happen across that metrics being allowed to But, I mean, what does it mean for… say… say that did exist, and metrics… like, we can always say in our implementation, like, by the way, using anything but primitive types for attributes on metrics is, like, a bad practice, don't do it. And that's… that's… the language for the spec is in there. Like, if you're doing weird stuff with attributes, expect things to be slower.
But there isn't really a mechanism for… us to have an SDK metrics where users we tell users to use it as an adult, and so that we don't have to double-check every attribute that's coming in. It would be nice to have that, because that's a faster path, right? We can just serialize your attributes and move on. We don't have to guard against you doing stupid things like circular references, or really complex types, and there are really deep things. But I'm not sure that there's a mechanism for that, so… Anyway… Yeah, that PR's not… not writing anytime soon. I don't know if we end up… Kicking the can down the road on the logs.
SDK stabilization for this.
Anyway, I'll still… I'll still push at this and try.
Marc Pichler (Dynatrace) 00:57:32 Yeah, I think there's no efficient way to do this for metrics, or… no way that's more efficient than what we have now.
And people are already, kind of, unhappy with the performance of the metrics SDK, especially when it comes to recording measurements.
So I think… that, and doing the validation might… Even make the problem a bit worse.
Trent Mick 00:58:13 Well, I mean, if we're checking the attributes are safe every time, it undoubtedly will make things worse there, yeah. I don't know if the answer… I don't know the SDK Metrics implementation that well, but, like, are we… are we ultimately screwed? If we're just receiving an attributes object, instead of… I guess in some other languages, they might create, like, a… an immutable… attributes… Thing that you can just rely on identity of that thing for doing the groupings, right?
Marc Pichler (Dynatrace) 00:58:42 me.
Yeah.
Trent Mick 00:58:44 We don't… we don't necessarily have that, so… Jamie, I'm not sure if that helps. I can't remember.
Jamie Danielson 00:59:00 Like, you can reject it if it has semantic errors, I don't know if that's considered a semantic error, though.
Marc Pichler (Dynatrace) 00:59:24 This is the consumer recommendations.
Jamie Danielson 00:59:28 Yeah, like, producer is right above consumer.
But…
Marc Pichler (Dynatrace) 00:59:41 There it is.
Trent Mick 00:59:44 It still means checking, though, instead of relying on the user to be… Using the foot gun properly.
Marc Pichler (Dynatrace) 01:00:01 Looks like we are out of time for today.
Trent Mick 01:00:05 I've already triaged again.
Marc Pichler (Dynatrace) 01:00:15 Thanks, everybody, for joining.
Sorry to cut the… Discussion about the attribute stuff, short.
Trent Mick 01:00:23 That's all good. It's all good. Thanks for driving.
Marc Pichler (Dynatrace) 01:00:27 Yep, have a nice week, and a nice vacation trend, or you're out of office.
Trent Mick 01:00:33 Oh, no, it's working.
There's a work meetup next.
Jamie Danielson 01:00:35 True.
Trent Mick 01:00:36 Where?
Marc Pichler (Dynatrace) 01:00:37 Have a nice morning.
Trent Mick 01:00:38 It's fine, it's in Madrid, it's good. Oh, it's good. Well, where it's, like, 35 degrees, but we'll see. So, yeah, sorry, that's higher for you Fahrenheit people, but yeah.
Okay, anyway.
Anyway. Yeah.
Jamie Danielson 01:00:52 Bye.
