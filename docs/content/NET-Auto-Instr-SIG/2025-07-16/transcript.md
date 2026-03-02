SIG: .NET Auto-Instr SIG
Date: 2025-07-16
Duration: 16 minutes
Zoom Recording URL: https://zoom.us/rec/share/ERpRZdFw0z3ui5wY7ZpNVzID6kpMBCsIO9cuIgV8T6gDJxohirQwDxxQxuJFEer9.pB2kJhhbsCLL7DiX
============================================================

## Zoom Recording Transcript

**Mateusz Łach** 00:09 Hello!
**Piotr Kiełkowicz** 02:45 Hello guys.
**efshaikh** 02:51 Hello! Everybody!
**Zach Montoya** 02:54 Hello!
I wonder if you guys have all had this experience working on auto instrumentation?
But I just got off a customer call
where they're failing to get traces
because they didn't properly stop and start. Iis.
raise your hand if this has happened to you.
Yep.
Took us a whole hour to get through it, but we did it.
**Piotr Kiełkowicz** 03:35 Yes.
**Chris Ventura** 03:37 At least it was a simple resolution.
**Zach Montoya** 03:40 Yeah, honestly, yeah, it doesn't require more of my time. I'm good.
**Chris Ventura** 03:49 I've had too many recently where
we needed to send memory dumps to Microsoft.
**Zach Montoya** 03:55 Oh.
yeah, we had one. Actually, we just had one. And actually, one just got fixed about a diagnostic listener issue.
Which should be coming up innet 10, and I think we still have to show another memory dump to kind of prove its word to backward. Tonet. 9. But hey, at least our the Runtime Devs are listening.
**Piotr Kiełkowicz** 04:20 No, but.
**Chris Ventura** 04:30 If you give me a moment I can share my screen.
**Piotr Kiełkowicz** 04:34 Great.
**Chris Ventura** 05:07 Okay. So I added this 1st item to the list.
I just want to call out to everyone to
take a look at this comment in particular.
So it's kind of the next step.
For dealing with binding redirects on.net framework, and there are some options thrown out there.
I've kind of shared my opinion upon 1st pass, but it would be good to have others to take a look and share their thoughts on
kind of what they think the next step
Should be for this one.
**Zach Montoya** 05:57 Yeah, sounds good. I'll I'll read that and provide a opinion.
**Chris Ventura** 06:03 Yep.
**Piotr Kiełkowicz** 06:07 Is kind of is on Pto. I'm not sure when he's
how long, but I think kind of 2 weeks
**efshaikh** 06:16 You should be hopefully back by Monday.
**Piotr Kiełkowicz** 06:19 Make Monday. Okay, so next week.
**Chris Ventura** 06:22 That that comment was, provided about a month ago, and I only just caught up to it. So that's why I'm
sharing it more broadly in case others missed it too.
**Piotr Kiełkowicz** 06:36 Cool.
**Chris Ventura** 06:44 Okay, so as far as pull requests, we got a Mongo bump.
and then we got our 2 draft prs, one for the file-based configuration.
Actually, oh, yeah. And the other 4 config
**Piotr Kiełkowicz** 07:03 No progress in on my side, no.
**Chris Ventura** 07:06 Okay.
**Piotr Kiełkowicz** 07:06 Speaking about the file based configuration.
there is a plan to do it into 2 paths
short path to implement it here.
If you agree. Otherwise we need to implement in in our distribution and then
create SDK in the main SDK repository and then utilize it here.
**Chris Ventura** 07:35 So this idea that if we start with our repository we would just consider it a prototype implementation, and then we'll eventually
part it back out.
**Piotr Kiełkowicz** 07:48 Exactly that. That's the plan. But I think we might. We can agree on some shortcuts on our sides.
because we have kind of very limited public Api only to the environmental variable. And
file schema, let's say, and functionalities.
There is no Api for
library developers or end users to to play with this.
So we have kind of smaller scope than SDK needs.
**Rasmus Kuusmann** 08:25 Yeah, I wanted to say. Also, we can skip creating it as a SDK, we can just do it as a file parser.
**Piotr Kiełkowicz** 08:35 Correct.
**Zach Montoya** 08:40 Do you have any concerns like if we prototype it here that we'll have to make just massive changes to it if we want to bring it to SDK, because it seems like that should be the landing place eventually. But yeah, for prototyping.
**Rasmus Kuusmann** 08:55 I think we can.
It is a tiny feature, and it shouldn't be complicated to remove it in the future.
**Zach Montoya** 09:05 I mean, like complications like, if we have an approach here, we poc, and then we contribute to SDK, and then it doesn't like, you know that design doesn't pass like the review, the Maintainers, and we have to change the approach or something.
**Piotr Kiełkowicz** 09:25 Yep, that's the risk to be honest, but
if we correctly market as a fully experimental feature, we should
be fine to to ship it.
especially this kind of feature flag. So you need to
put the file name to some feature flag to enable this file like configuration, and it is done working
only in this. In such cases.
**Rasmus Kuusmann** 09:59 Yeah, we need to make sure that the instrumentation and the exporter keys are
according to the spec, and because we are not going to ship. SDK, then
we don't need to follow that part.
**Chris Ventura** 10:18 Well, at least, if we start it here, it ensures that the dependency tree will be more manageable.
**Rasmus Kuusmann** 10:27 Yes.
**Zach Montoya** 10:28 Yeah.
alright, so as as a plan to just keep keep working on over here.
**Chris Ventura** 10:39 I'm okay with it.
**Zach Montoya** 10:43 Yeah. Sounds good to me.
**Piotr Kiełkowicz** 10:47 Great.
**Chris Ventura** 10:48 Okay.
okay, so this 1st one is a follow up from the more frequent thread. Profiling runs
would probably be useful to copy some of the comments from the previous Pr that call out some of the specific changes.
**Mateusz Łach** 11:24 Okay, I'll do it. Yeah, sure. I created these as sub issues. But.
**Chris Ventura** 11:31 Oh, it's a sub issue.
**Mateusz Łach** 11:32 Yeah. But yeah, it's
okay, either way, I'll I'll I'll fill in the details. Sorry for for missing that.
**Chris Ventura** 11:44 I'll add it to the project.
Let's see, do we have a new milestone?
Okay, same thing for this one.
Okay, so this is a discussion brought up in the last Sig meeting.
And so let's continue discussing this one Async about testing
older library versions that may or may not have security vulnerabilities.
So I shared some of my thoughts, but it would be good to have others share their opinion as well.
Okay.
And then for this issue, we got a response back. It sounds like they are actually running into a deadlock.
And so they've got information from the call stack.
So perhaps this is something we should try to look into
any objections for me, putting it for the next milestone, just so that we look into it.
**Zach Montoya** 13:45 Yeah, let's do that. I can. I can take a look at that.
**Chris Ventura** 13:49 Okay.
I can go ahead and assign you.
Okay.
So let's see, yeah, I think we're still waiting for this person to come back from time off.
And I believe we're still waiting for something here.
Gotta scroll all the way down.
Okay.
okay, well, the last update was a week ago. It may be a while.
We'll just give it a couple more weeks, I think, before we close it.
Okay.
no new discussions.
Okay.
Nothing needs to be added.
hey?
I'm not aware of any changes that need to be made to the Project Board.
I don't think we have any newer things in progress.
So on that note.
Anybody else have topics that they want to bring up.
Okay, I guess we can get back some of our time today.
**Zach Montoya** 16:42 Yeah.
**Piotr Kiełkowicz** 16:43 Thank you. See you. Next week.
**Zach Montoya** 16:45 See you.
**Chris Ventura** 16:45 See.
**Zach Montoya** 16:46 Bye.
**Mateusz Łach** 16:48 Thank you.
