SIG: .NET Auto-Instr SIG
Date: 2025-07-30
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Mateusz Łach** 00:39 Hello!
**Zach Montoya** 00:47 Hello!
**Piotr Kiełkowicz** 02:43 Hello, guys, sorry I I cannot drive today.
**Zach Montoya** 02:50 Hello, yeah, no worries. I can. I can drive today.
**Piotr Kiełkowicz** 02:54 Great thanks.
**Zach Montoya** 02:57 And yeah, let's get started. Couple nights after the hour.
All right.
Alright. So here's our meeting notes looks like we have one item on the agenda.
about naming our nuget package for the out of process collection.
I actually was not aware that this issue was opened up. So The gist of this is that the that separate branch of work that Raj is working on regarding an out of process collector wants to revise the name so more accurately reflects what it's doing. And so that is, it has a mini SDK that's able to collect signals outside the process without monitor, and then export them.
Support only the processor exported portions of SDK.
Use as little open temperature as possible just handle so much data. That done it, monitors providing it, and then yes, port out of process. So much collection without by code.
So he opened up this issue and initial proposal of naming it of a forwarder or forwarder configuration for that additional configuration package and some alternative options include out of process, forward or external forwarder egress? So I'm sure this is something we can iterate on But it seems like this is going down the right path as we're not really trying to have like an SDK, it's definitely misleading for its intended purpose.
And ideas, or any conversation you guys wanna have right now.
**Piotr Kiełkowicz** 04:55 It. To be honest, it would be great to have separate namespace, not related out to instrumentation, to, to not confuse, end users.
So open telemetry out of process, or whatever. Just the second. The second part of the main speech should should be this different than outer instrumentation, in my opinion.
**Zach Montoya** 05:23 Yeah, I think that's I think that's really good feedback.
Maybe something like opensometry. Yeah, out of process collection, or even.net monitor collection.
yeah. So yeah, I don't think we need to decide this right now. But I think it would be great to have some feedback on this maybe for the next meeting, because it seems like Raj is gonna be is back from his vacation, and we can talk about it. So if you have any ideas, please add them to this this issue. Yeah. Well, I'm a fan of like.
like, for example, like of insometry, I think you said out of process, or something like that.
**Piotr Kiełkowicz** 06:50 Yep.
**Zach Montoya** 06:51 Alright awesome!
Alright! Let's add that for now, and welcome to add further comments on this issue.
Going back to our regularly scheduled agenda. Let's check the open pull request.
Okay? So we have a couple of different ones going on in that that branch. So there's adding testing for the different signals.
I won't go into that. I think that sounds pretty explanatory.
Let's see.
So those are all. After that, a process collection we still have. Oh, this is a draft that I started having.
**Piotr Kiełkowicz** 07:31 This out of process. Rush Pink asked on the slack to to review this. So if you have time today, it would be great.
**Zach Montoya** 07:40 Okay, yeah,
**Piotr Kiełkowicz** 07:43 I will take a look tomorrow, probably.
**Zach Montoya** 07:46 Okay.
yeah. I'm not sure I'm gonna have time today. May have time at the end of the week.
but I won't be able to get to that today.
so for this particular one, this came from an issue that was reported about a potential deadlock. I started a solution here. And yeah, got some feedback to to update it. So I'll continue working on this. But I don't yet have a repro.
So that's the next thing that I'm that's why I kind of kept it in draft, because I don't have a good regression test at the moment.
So nothing yet to review.
Hopefully, the fix is as small as it is, which only it does, refactoring to avoid some of the locking that happens at Runtime.
So hopefully, we don't have to do too much. Besides, just refactor a little bit.
But I'll I'll post updates on that as I get them.
Let's see file based config and configuration based config. Are there any any updates that we should discuss on these.
**Yevhenii Solomchenko** 08:58 I think one part we should discuss is about trial fast.
Navarro.
We're keeping that file 1st from the environment, even in the file, or adding some additional field.
Early.
**Zach Montoya** 09:22 So what's the configuration we have for controlling this right now? Just what's.
**Piotr Kiełkowicz** 09:34 We are. We are crashing the application, as I as I remember.
**Zach Montoya** 09:57 so yeah, do we? Are we? Still, the default behavior is still to just we fail fast. We just exit, or are we we're choosing to basically crash.
**Piotr Kiełkowicz** 10:11 When file 1st is set to true, we are crashing process. Normally, we are silently trying to silently continue without auto instrumentation.
**Zach Montoya** 10:21 Got it?
Okay? So you have any. What was the the question then, that you're trying to.
**Yevhenii Solomchenko** 10:29 About adding a field to do the environment because it's out of specification.
**Piotr Kiełkowicz** 10:38 You can.
**Yevhenii Solomchenko** 10:39 Okay.
**Piotr Kiełkowicz** 10:40 You can document that it is not supported in the 1st version, if needed, we can extended behavior and adds possibility to read it from the file.
**Yevhenii Solomchenko** 10:56 But save functionality from there and bar, because file based overrides all others.
not all but a lot of configuration.
**Piotr Kiełkowicz** 11:10 So if if it is easier for you to add our custom entry to support in this file configuration, that's fine. If it is easier to just the comment that it is not supported by file and envar will be used instead the file configuration from the file. It is also fine for the initial solution.
**Yevhenii Solomchenko** 11:37 Okay. So you're okay to add something. But it's not in there specification.
**Piotr Kiełkowicz** 11:43 I I think it should be fine.
**Yevhenii Solomchenko** 11:46 Okay.
**Piotr Kiełkowicz** 11:48 It is purely our auto instrumentation feature. It will probably never go to specification.
**Zach Montoya** 12:06 Okay, yeah, that sounds sounds good any other discussions on this. Pr, for now.
alright and then the remaining one is configuration based mutition anything that we need to discuss on this one.
**Piotr Kiełkowicz** 12:26 Chris, you were not last week. It is ready to re-review.
I've added coverage both for generic methods Async methods, etcetera, and it seems to be working fine.
Still, we do not have configuration for this, because lack of file based configuration.
Hmm.
so it is blocked. But from the technical, from from the proof of concept perspective, it is ready to to check.
**Zach Montoya** 13:04 Sounds good.
Alright, alright, so that covers our our pull requests.
Let's see, it does not depend about once new issues.
Okay, looks like we have a couple weight handle profiler. Is this a feature request?
Okay?
Alright. So this looks like a feature request.
**Piotr Kiełkowicz** 13:38 Oh, I've seen this name before. Okay.
**Zach Montoya** 13:52 looks like they actually added a wait feature request over there as well. Okay, so for this one.
How should we handle this just putting this because we don't have a I mean, unless someone's itching to to do this right now, I don't think we're immediately shifting our gonna shift, our attention to this.
**Piotr Kiełkowicz** 14:13 I think we can ask for the contribution otherwise put in the future.
**Zach Montoya** 14:19 Yeah. Okay.
**Piotr Kiełkowicz** 14:23 Be next.
**Zach Montoya** 14:24 Be next. Okay.
Alright, I'll go back and respond on that.
okay, this looks like a potential bug with some apples are getting their data, some other. Some aren't okay. This one. We need some more information here.
I asked. Terrific hard to get some applications or refresh for So I guess we can start 1st with some some logs What else might we get from this?
see, do we have?
Do we have log collection steps here?
I shouldn't hear you.
I'll just provide with this, for now we can kind of go from there.
Let's see what else we have. So another feature request, oh, from Steve Gordon. Let's see.
Okay, yeah, that looks good.
Nothing to follow up on right now.
**Piotr Kiełkowicz** 17:39 I will support this especially. Db, statements.
Possibility to enable dB, statement or a square query text. dB, query, text attributes.
We have also internal request for this.
**Zach Montoya** 17:54 Okay, is this, is this new instrumentation that we don't have? Or is this aligning like the attributes with the spec? Or I guess.
**Piotr Kiełkowicz** 18:03 Square instrumentation. SQL client package have it.
But with all semantic conventions the content is exactly the same. So it's about the renaming. But it is not working for legacy, square clients.
it is working only for the modern one. So here we have request to extend the coverage for the older library version of the library.
**Chris Ventura** 18:32 But it's just for the.net framework version of that library. Correct.
**Piotr Kiełkowicz** 18:40 Exactly.
**Chris Ventura** 18:41 The the.net version of that library. It's able to to capture things.
So there it really is. Legacy applications on the Legacy library that can't capture the SQL. Statements.
**Piotr Kiełkowicz** 19:01 But we have internally exactly the same request. So yeah.
if Steve has idea to to contribute, it will be great, in my opinion.
**Zach Montoya** 19:18 Yeah, that makes sense.
**Chris Ventura** 19:20 Yeah. The one thing I'm curious about is it all.net framework versions that fall into this problem, or just the framework? 4, 6, 2 target that falls into this problem.
**Piotr Kiełkowicz** 19:37 I think all.net were sprints using the bundled version of the of the library. As I remember, there is the issue linked in Steve Post.
I think you can found there more information.
**Chris Ventura** 20:03 Yeah, I just wasn't sure if the dot, the net standard build target had the same problem.
But maybe there isn't even a net standard build target.
**Zach Montoya** 20:18 And if it's not standard, it might even just map to the to the one provided by the Gac.
Maybe.
Okay.
alright, yeah. Let's let's see if if Steve is able to share any poc.
and then we can go from there.
See?
What else do we have?
The let's see. Ci approach. Okay? And I think these ones are you covered before?
See I, this one seems like a similar issue to the one above. I don't know if we got any. Oh, I think we're waiting for response.
Still waiting on a response. Since June. Okay, guess we'll just keep yeah on vacation. Okay.
can check back on it next week, I suppose.
And then this one, this one's also stale. Okay.
shall we close this one? If it's been stale for a while.
**Piotr Kiełkowicz** 21:38 I think so.
**Zach Montoya** 21:45 Okay, do. Okay.
Alright.
Covers all our issues. Discussions. Looks like there is one which is, we can answer this Async. But, interestingly, this person looks like they might just be trying to use the SDK so not entirely sure what they're doing if they're using code based configuration might just put on the SDK and see what they are.
The docs suggest on add source. But I think I'm pretty sure start works for for all sources.
**Chris Ventura** 22:52 I don't know if they're intending to use the SDK to do the initialization here.
I think they just want similar behavior to it.
**Zach Montoya** 23:02 Oh, I see!
**Chris Ventura** 23:05 And so, if that's the case, we should have an environment variable that does the same thing.
**Zach Montoya** 23:14 Would it be called.
**Chris Ventura** 23:16 I I think it is.
**Piotr Kiełkowicz** 23:17 Additional sources, or something like this.
**Zach Montoya** 23:23 See code docs.
okay, is there a better link? We have?
**Chris Ventura** 23:35 If you go to the config, Doc.
**Zach Montoya** 23:40 Oh, here we go perfect.
Let's just go to Main.
Alright.
So let's in.
What's this one? This one is auto traces additional sources.
I can. I can just finish typing this offline. I don't need to hold you guys here.
so that's that's all our discussions. So issues that should be assigned. We have nothing. Is this up to date?
Yeah, okay, alright.
And then last, we have Project board.
Let's see, think I see any activity deadlock.
This will be this one's in progress.
No, I don't see any other updates. Are there any other changes that we should update?
Looks like, no, alright so that does wrap up our agenda.
Are there any other items you guys wanted to chat about while we're here?
Alright, looks like we're all good. I'll finish responding to that discussion, and I'll stay offline but yeah.
looks like a call a day and see you guys next week.
**Piotr Kiełkowicz** 26:06 Sure, bye.
**Mateusz Łach** 26:08 Thank you. Bye-bye.
