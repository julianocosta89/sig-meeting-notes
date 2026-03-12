SIG: .NET Auto-Instr SIG
Date: 2025-06-18
Duration: 51 minutes
============================================================

## Zoom Recording Transcript

**Mateusz Łach** 01:39 Hello!
**Rasmus Kuusmann** 01:43 Hey!
**Chris Ventura** 01:48 Hello!
So we'll give it another minute or so.
**Paulo Janotti** 02:33 Hi! Everyone.
**Chris Ventura** 02:37 Look.
**Rasmus Kuusmann** 02:39 Hey!
**Paulo Janotti** 02:46 So let's have Chris driving today.
Boom, have some rotation.
**Chris Ventura** 02:58 Yeah, I'm just giving it about another minute or so.
I think we can go ahead and get started.
So we'll start with the pull requests.
So got a dependabot bump.
Let's see. Okay, so infra tests, let's take a look at this.
**Paulo Janotti** 03:48 Yeah, we we did this for the collector. It went smoothly. We should be doing this also. So.
**Chris Ventura** 04:00 Sounds good.
So just migrating from windows 22 to 25.
Okay?
Oh, that was fast.
**Paulo Janotti** 04:20 Yeah.
**Chris Ventura** 04:23 Okay, so yeah. So this is related to an issue, I submitted. I don't think it's linked here.
But yeah, what is this doing, sir, scripts are failing.
Okay, so this is just changing from chef 2, 56 to shop 5, 12, as well as the checksum being compared.
So this is something that Paulo and I were talking offline about is we. Neither of us could really find where these sums were defined or published. So it's kind of on us to review the scripts and determine if the scripts are okay and then update the checksums.
So I've got a proposal and another issue that that can change the way we're doing this.
So we can.
**Paulo Janotti** 05:49 Deck by.
**Chris Ventura** 05:49 That later. But this unblocks all the existing prs.
okay.
let's see.
Okay, this looks like should be a simple what's.
**Paulo Janotti** 06:21 Yeah, I I yeah, I suspect that this is just adding the solution and visual studio now, can build this kind of with the docker.
we I never use. I use always the make file. So I think a local run, and we should be good to kind of validate. If it's work, I I will do that. It's a good long time that I don't open my visual studio.
I've been using just use visual studio code. So after the updates, probably there is a huge update to be make. I, I validate that.
**Chris Ventura** 07:02 Makes sense.
Okay? So we've got another broken. Yeah, URL, Martin's on a roll.
Okay, so looks like, it's a huh? Interesting. Okay, yeah, we're referencing. Maria. dB, but okay, so there's a different URL to use makes sense.
Okay, yeah, this is, yeah. There's another Pr related to this.
This one links to Github.
There's another Pr open that links to the official Docs page.
**Rasmus Kuusmann** 08:09 There were some comments where about the issue.
**Chris Ventura** 08:16 And which one this one.
**Rasmus Kuusmann** 08:20 Yeah, the same one. Yeah. So I was also finding it as a duplicate.
**Chris Ventura** 08:24 Yeah.
**Rasmus Kuusmann** 08:26 Seems this one is what we should use. Actually, according to Martin's comments.
**Chris Ventura** 08:38 So what I found was on the Github Repository. It linked to the old Doc site.
if I remember right.
**Paulo Janotti** 08:51 So if I go to here.
**Chris Ventura** 08:55 Grab this URL, and it still links to the old deprecated website that doesn't work.
So if I go here, can't be reached.
**Rasmus Kuusmann** 09:20 So because he he means that the documents are also hosted in Github.
and the web pages are compiled from there.
**Chris Ventura** 09:32 Okay, yeah. And then this is the newer site. Polydocs.
So you're saying that all the docs are in here and you set the web pages are compiled from here.
**Rasmus Kuusmann** 09:47 Hmm.
**Chris Ventura** 09:53 I don't know which, do you?
Which would you all prefer to go to?
**Rasmus Kuusmann** 10:01 I guess I will follow the Maintainer.
**Paulo Janotti** 10:08 Yeah, it feels like in the end. What we want is kind of I I think this is a bit better we go through Github. But then we have to update the read me on Poly.
**Chris Ventura** 10:23 Yeah. So at the top, I mean, this part needs to go away.
**Paulo Janotti** 10:31 Yeah.
**Chris Ventura** 10:33 With that being said, our link to Poly is for a library that we say we don't support instrumentation, for out of the box.
**Paulo Janotti** 10:43 Yeah.
**Chris Ventura** 10:44 So I I really don't care which one we link to. So if anybody has a preference.
**Paulo Janotti** 10:49 I. I tend to think that the Github is gonna be more stable.
**Chris Ventura** 10:54 Okay.
**Paulo Janotti** 10:56 I prefer to link to Github.
**Chris Ventura** 10:58 That's fine with me, so I will approve this one, and then we can close the one that I opened.
It's fine with me.
Let's see Powershell more prominent.
**Rasmus Kuusmann** 11:33 This one. I wasn't.
Yeah. It's still sure if we wanted.
**Chris Ventura** 11:39 Yes.
**Rasmus Kuusmann** 11:39 Need to test.
**Paulo Janotti** 11:40 So that this makes me think, should we be because we use just we basically use should do windows stuff.
Yeah, no, I think it's fine, because I I kind of I forgot that we have a dependence on Powershell.
We can't use. Bosh.
yeah, yeah, we, if if that's the case. Yeah. And that's the case, right?
Or is more like, we require windows. And this stuff just works. If we use Posh.
**Rasmus Kuusmann** 12:27 I guess it should work also with push. But it must be at least windows, environment.
**Paulo Janotti** 12:35 Yeah. Yeah. So so I wanna be sure that we are requiring the right thing. You know. Because I I suppose that sometime down in the future. Powershell dot X images appear from windows eventually, I don't know.
It's gonna take a long time for that. So yeah. But but just at least for us, you know. You'll be good to know if this is more independence on windows.
then dependence on the the host for the script.
**Chris Ventura** 13:12 Unless this was something that came up with the server. 2025 changes.
**Paulo Janotti** 13:22 Yeah, I I suspect that's more about because we do some stuff for the gag. So we depend on being on windows when we load those dependence.
I suspect I'm not a hundred percent sure.
I can give a quick try on my machine to to see how how it goes. You know.
**Chris Ventura** 13:46 Okay, yeah. Cause this is the 1st time I've seen the need for yeah, this.
**Paulo Janotti** 13:55 Yeah.
**Chris Ventura** 13:57 So I don't know if there's a difference in behavior for server images.
**Paulo Janotti** 14:04 Yeah, I, yeah, I I I'm not sure. I think most of us nowadays have the I. At least I have in all my windows, machines. I have the the portable Powershell. It's the one that I use most.
and once more I would. I would like to understand that I think the dependency is more on windows than on the host itself.
**Chris Ventura** 14:35 Okay.
**Paulo Janotti** 14:40 I'll take a look at that one, too.
**Chris Ventura** 14:43 Okay, and we've got another dependabot. Update this one. I'll just go ahead and close right now.
Okay, this Kafka one I wanted to bring up because the tests that were failing were Kafka related.
And so this may need somebody to take a closer look.
**Rasmus Kuusmann** 15:42 It seems a major up great, so probably we don't instrumentate. I think.
**Chris Ventura** 15:49 Well, we're upgrading the Kafka container.
I don't know that we upgraded the library to talk to Kafka.
**Rasmus Kuusmann** 15:59 Oh, yeah. Correct.
**Chris Ventura** 16:01 And so that's where I don't know if there's some sort of dependency there where the expectation is. You do have to update your Kafka Library or change some sort of setting.
So either way, I think this needs a closer look.
**Mateusz Łach** 16:19 Yeah, definitely, I I took a quick look. Basically, there is a lot of noise in the logs. And this is, it seems like it's failing at the start of the test. When when we try to create the topic.
And and the amount of logs is, it's it's enormous.
**Chris Ventura** 16:41 Yes.
okay. And then we got the Pr for the frequent sampling of threads, which is, we've we've been discussing this off and on for the last few sick meetings. I don't know if there's any updates you want to say on this Pr or call out.
**Mateusz Łach** 17:11 No, maybe just I try to basically document everything here. I'm not sure if it was documented this way after the last meeting. There is some stuff to do, basically some cleanup. I can make it as a part of this Pr or follow up Prs, whatever is like preferable.
yeah. And also, make some decisions that simplified the implementation for me. But try to document most of them here. So and I think feedback would be welcome.
**Chris Ventura** 17:51 Huh?
And yeah, we've got the configuration based instrumentation.
It's on hold. But please continue to review and comment.
Okay, for new issues.
Okay, so this is a request to add new attribute to them some of the Http client metrics.
yeah, I don't know if this is one that should be addressed in opentelemetry.net, or, if it ultimately needs to be in the runtime.
**Rasmus Kuusmann** 19:05 I think.
**Chris Ventura** 19:07 I mean, it might have to be in both. Because I think the yeah, there's an interesting relationship. There.
**Paulo Janotti** 19:19 This this?
Yeah, one way or another, the the SDK side it. It's the best path to get traction to get things synced with the the runtime.
**Chris Ventura** 19:38 Yeah, cause, I think that instrumentation libraries still necessary to handle baggage and the different tracing protocols.
**Paulo Janotti** 19:48 Yeah, that's that's what I'm thinking. They they can't do this on their own. But anyway, they have better attraction together on time to update
**Chris Ventura** 20:00 Okay. I know that Piotr had permissions to migrate issues between the the 2 repos. I don't know if anybody else here has that permission.
**Paulo Janotti** 20:14 I I can give a try, but I I don't know. From the top of my mind.
**Chris Ventura** 20:19 Okay?
So we can.
Yeah, if we need to just create a new issue in that repo or direct them to to create a new issue. We can do that, too.
Okay?
So issue, I submitted after discussion with Paulo yesterday.
Okay, Russ, you had more information on it. So a little background.
Usually, whenever a new version of.net is published somewhere around that same time, this installed.net script seems to change, and we have this Shaw check in place that we saw another Pr for changing it.
So the question is.
do we want to continue to follow that process and have a documented process that we can follow whenever a change is detected, so that we're consistent in in what we do?
Or do. We want to follow the verification step that Microsoft has published.
That uses the the public signing key that they they've made available. Now.
So, Rasmus, I still have to read this.
Okay. So, Rasmus, you believe that the Shah was a way of tracking the version of the script.
**Rasmus Kuusmann** 22:23 Yeah, I can't remember where I saw the instructions for this. So I think we internally were using definitely same version or the same instructions.
and it might be from better.
**Chris Ventura** 22:42 Okay, go ahead.
**Paulo Janotti** 22:44 i i i think I think the the most. Anyway, I I don't know the intention, but the benefit that we get right now is really a notification about the version. Change If you think about kind of the the authenticity aspect, then we have to do a separate thing, because right now is just a shot from the script itself.
So I think we should do this.
But we have to keep what we have in the sense that we have a a notification of the version change, and this one after implemented.
unless for the key change the public key change. It should be kind of never needs update, you know, but to be doing the right thing. What we need to do is store the the key, either directly on the repo or as a a property somewhere, or of the the repo So I think we should do this separately.
**Chris Ventura** 24:07 Okay, I can go ahead and update the proposal in the issue to reflect this discussion after this meeting.
And then this way, we can actually get this change notification piece of it documented as well in our processes.
**Paulo Janotti** 24:26 Yeah. And and then we can be a hundred percent sure also, with the the signature verification happening before we can just pick up whatever spit out and just copy paste and update.
**Chris Ventura** 24:40 Yep, yeah. So that simplifies the process.
**Paulo Janotti** 24:43 Yeah.
**Chris Ventura** 24:45 Sounds good.
Okay.
okay, so this is an issue that was reported in the contrib repo.
Mattesh, is there?
And any thing you want to talk about this other than making us aware.
**Mateusz Łach** 25:19 yeah. So it was I. I think it was noticed when open telemetry demo was being updated. I actually looked at it some time ago didn't look very, very closely, I mean, it seems to be connected to the fact when 2 instrumentations are enabled at the same time. So there is a workaround of deabling one of them. But I didn't get to the root cause of the issue.
Just something created to have something on our side, because oh.
**Paulo Janotti** 25:52 So just just to to confirm the work is gonna be done out on the contribute side, or we need to do some updates after
**Mateusz Łach** 26:04 Yeah. So I'm not sure. That's why I okay, no worries. Okay as as well. Yeah. I haven't had a chance to look at it very, very closely, yet.
**Paulo Janotti** 26:14 Yeah. So just add, edit, the description to say that this issue is here to in case we need follow up work, no.
**Mateusz Łach** 26:28 Sure.
**Paulo Janotti** 26:31 Yeah. Thanks. Screen.
**Chris Ventura** 26:43 Okay.
**Mateusz Łach** 26:46 And also, Chris, if you could refresh because I created one new issue today and assigned it a milestone. So it was not showing up. Sorry for that. So I removed the milestone. Yeah. So basically, when working on this.
on on some unrelated issue, I realized that every log call is followed by a flash attached to this. Basically. So we are.
This is this is something that is not needed. And this can incur this basic. This definitely incurs an overhead. So how much of an overhead that depends on the setup?
Yeah. So this, yeah. So this this is something that I I've I, I think we should. And I can, I can work on. So we should. Basically, basically, probably address it as soon as possible. That's why I added the milestone for the next release. But didn't realize that will not show up in here. So.
**Paulo Janotti** 27:50 Yeah, I I suspect that most users are sending the data to some back end. So that's why we did a note before this is just effect, file sync, right?
**Mateusz Łach** 28:05 Yes, so this is for the internal logs, our internal logs. So I I think that with the so it depends how how fast is the disk right for me locally, for example, in a default configuration, the all of the flash calls take approximately 30 ms right? But this might take a lot of a lot of a lot, a lot of more time elsewhere. Right? So yeah, if you could.
**Paulo Janotti** 28:34 Dude.
**Mateusz Łach** 28:35 Yeah, we. I think we should.
**Paulo Janotti** 28:38 Okay? So this mainly explains, like the full degradation that we see when we put detailed debugging verbals, logs.
**Mateusz Łach** 28:51 Yeah, definitely in the in the debug logs. This will be like the most like visible right? Because.
**Paulo Janotti** 29:01 Can tell that I notes that the performance I I whenever I ask it anyone to enable that I say, Hey, don't run. If this log is because their performance is gonna really suffer.
And if this can improve a little bit even a little bit that you'll be, you'll be great.
**Chris Ventura** 29:21 Yup. Good. Catch.
Okay.
Yeah. Yeah.
**Paulo Janotti** 29:39 My Mike didn't respond. But I I think as Rasmus is saying in there in the comment, I think it's a kind of well known case. If my memory serves correctly.
**Chris Ventura** 29:53 It should be, but we can give it another week.
**Paulo Janotti** 29:58 Yeah, I think.
**Chris Ventura** 30:12 Similarly, this is an issue.
Let's see, did we get more information.
**Paulo Janotti** 30:25 Okay.
**Chris Ventura** 30:27 Yeah.
okay, so it looks like we need to follow up on this issue and take a look at the logs and warnings.
Oh, no logs.
Okay.
yeah. So we need somebody to follow up on this. We may need a repro app.
Okay? And we've talked about the frequent thread sampling already.
Let's see.
**Mateusz Łach** 31:40 Yeah, this this we discussed already as well.
Oh.
**Paulo Janotti** 31:48 If if you didn't have time. It's fine.
**Mateusz Łach** 31:52 Yeah, sorry I was, basically, I started start wanted to work on that and then realize there is problem with logs like the the issue that I created that got.
Yeah, I I think there's maybe there is there. There's like our approach to logging. We could like re refine some of it so probably as a part of this one, and also the part of the addressing the other issue. But the the other issue seems like more pressing right now, so.
**Chris Ventura** 32:31 Yeah, that makes sense.
Okay?
And yeah, we've been talking about this issue off and on
**Paulo Janotti** 32:49 I I think I think we should really track the.net one that Bras was linked there.
That the one on top right on top. Yeah, I think, is this one?
Yeah. Because, if the SDK acts on the way that they are describing right now, I think it will reduce our problems very, very, in a very noticeable manner. So
**Chris Ventura** 33:23 I think so.
but I also don't know how much traction this is going to get.
It's a.
**Paulo Janotti** 33:38 Is still on on the Sig working with them. We perhaps we can bug Allen, or or and or period when Piota come back, so.
**Chris Ventura** 33:50 I think.
**Rasmus Kuusmann** 33:51 To already.
I think they already made decision.
If you scroll to the last moment.
**Chris Ventura** 34:00 Just didn't scroll enough.
**Paulo Janotti** 34:03 Yeah.
**Rasmus Kuusmann** 34:04 I just got updated. Somebody sent me the link that they decided.
Wondering if it was this issue, or it was decided in another.
**Chris Ventura** 34:20 Okay, this is so 2 commits that reference. This issue.
So yeah, maybe Martin is taking some of this on what's starting to reduce it. So yeah, maybe there is some traction.
**Paulo Janotti** 34:51 Yeah, we can. We can. We can go review and also vote for the change. So.
**Rasmus Kuusmann** 35:01 I have direct link.
**Chris Ventura** 35:07 Okay.
let's see.
So okay, so we've marked this as answered.
Oh, no, okay. So this is answered. So I'm gonna close it.
**Paulo Janotti** 35:45 Yeah.
**Chris Ventura** 35:52 Okay.
And this one is, okay.
I'm also going to close it tracing your business.
Okay? At this point, I'm going to close it.
Okay?
And yeah, just close this one, too.
And we don't have anything open.
**Paulo Janotti** 36:56 Look, beautiful.
**Chris Ventura** 37:04 Okay, nothing else to add there.
and as far as the project board goes, Matthias.
are are you actively working on this log flushing.
or should I leave it in the backlog?
**Mateusz Łach** 37:33 Yes, I I'm working on it. Please assign it to me, and I'll prepare a Pr.
**Chris Ventura** 37:39 Okay.
yep.
okay. So you should hopefully be assigned. Now.
okay, I think that's the only ticket that needs update any other topics. You all want to bring up.
**Paulo Janotti** 38:23 I. I have a very random question just because people doing.net sometimes. We have the overlap with windows.
I was getting that a bunch of windows, docker image reply, report a bunch of vulnerability on scams but even the things that are later published, and I can't find any reference on the Internet. And I was curious. If anyone had the same kind of. And okay, it's in the base image what what I can do. I I they don't give a easy way to update those things like sense client their windows defender service.
anyone has met that same issue.
**Chris Ventura** 39:18 I've honestly tried to avoid using windows containers because of all sorts of friction points.
**Paulo Janotti** 39:29 Just because of the size is a good idea, you know. Avoid.
**Chris Ventura** 39:33 I mean size, but also the kernel version problems.
That's usually the thing that trips me up the most.
**Paulo Janotti** 39:47 Yeah, yeah.
I was just curious. I have all these reports. And okay, I, I can't fix, they don't know how to update those dependents, and they are shipping on the box.
So.
**Chris Ventura** 40:02 Yeah, and it. And if you force a pull of a fresh image, it still fails. The scan.
**Paulo Janotti** 40:08 The files are there. I can pick up the image. I load the image I check. Yeah, it's the old version. It's there, and it the interesting part. It's 3rd party components like the sales service ships, some Dll from 7 Zip.
and that Dll from 7 Zip is out date and has a bit. So the risk is not high because you are not gonna be using that. Depend on the customer using that. But it's kind of, hey? The fix is out, I think. Year months, I don't know, and the things keep reporting. This kind of keeps reporting. I have to add a bunch of Oh, okay, I know about this one. This one is good. Oh, I know. But but yeah, I was just curious. If someone perhaps had the same issue, so.
**Chris Ventura** 41:08 And that's primarily with the windows. Server images as opposed to the windows. Nano.
**Paulo Janotti** 41:14 Server core. I.
**Chris Ventura** 41:16 Okay.
**Paulo Janotti** 41:17 I didn't check Nano, but I checked several, or you know that is one of the trim down images. So it's still there.
**Chris Ventura** 41:31 On that note. You know. It's been a long time since I've even looked at Windows Nano Server, and I honestly don't know if auto instrumentation works on windows. Nano.
**Paulo Janotti** 41:46 Windows. Nano is so 1st we will not have a way to install, I think, by default. I think we don't have the Powershell enabled by default.
So yeah. But but I think, adding, the Powershell is not that hard?
But then I I don't know what will happen to be fair. I don't have customers on Nano, so.
**Chris Ventura** 42:20 Try.
**Paulo Janotti** 42:21 Most most customers that use windows, darker image that I have contact with. They use those asp, not framework.
That's the most common one. You know much more even than server, core.
**Igor Kiselev** 42:41 Pretty logical, because for Nana there is no.net framework, so there is no.net framework. It means there is no dependency on windows at all. So customers probably just use Linux docker in that case. So yeah, I'm not surprised. Is it.
**Paulo Janotti** 42:56 Yeah.
**Chris Ventura** 43:04 Yeah, I I mean, I've seen requests for doing windows images in Kubernetes. But so far, yeah, they've all been either a spin at core or a windows. Server, image.
**Paulo Janotti** 43:19 Yeah, we we do support the collector on deployments with kubernetes, with windows. So, and, as you said, is asp framework most of the time.
**Chris Ventura** 43:36 Does the open telemetry operator support windows?
Images at this point in time.
**Paulo Janotti** 43:45 I actually don't know the dependencies. I can tell you that our distribution support but I I we use we built on top of the operator. But then, on the top of my mind, I don't know. If it comes from the open telemetry operator, or it's something that we added on top.
**Chris Ventura** 44:07 Yeah, what I was thinking of is, if open telemetry does, then that might give more people to ask the the question to about dealing with.
of those base images.
**Paulo Janotti** 44:22 Yes, yes.
yeah. It. It was a long shot asking here. But I searched it yesterday for quite some time. Nothing useful. I found I didn't find anything useful about it, so.
**Igor Kiselev** 44:43 Nice.
I have a short topic to this to update. Actually. So I return back to single grants that issue previous, my fix was to always use single domain, a load optimization, single domain for second job domain. I'd like to give an alternative solution with, correctly redirecting all assemblies to proper versions. It would be done through through up config update on up domain creation to set proper binding redirects.
Was it proper binding redirects. I have interest on issues that there is innet, a list of assemblies that are you that are subject to unification. So it means thatnet framework itself have some hard-coded list of Assemblies version for which it would resolve an assembler version that comes from thisnet, instead of what application asked for.
And in fact, it's pretty. Yeah, there is no documentation with at least what it would be. I believe it's a list of assemblies that comes with.net framework, so that include in redistribution list framework would be always a subset of symbols can be in that unification list. So, and if the the problem with the unification list. If applications creates, redirect creates, bind and redirect.
In that case.net framework would not use unification list. But think that okay, is that application explicitly ask for that version, and I would use a version that forced by bind and redirect.
So it means that we could not create bent rhetorics for all of our dependent assembly, as some of that assemblies are subject for that unification of that unification, and we would break application on different version. So the only way that I see to.
So there are multiple ways to fix it. I covered it in issue different options. But from my point of view, the best way would be to switch to multi targeting and actually build us different version for.net framework for 62464747148, and so on it would greatly increase the number of files. So that's why I plan to after I build it. Do as a post, build, step, remove all duplicate files files, and instead of real files, create some link for us. So let's say, Dell, dot, link or something like that, so that our assembly loader would know that it needs to look into different folder.
and with it, when we install and register assembly. Syng, we would register assembly syng, only required for current framework, and would not to use for all the frameworks it would solve. Help solving.
The problem is correct, create and bind and Redix, as we would not anymore have any assemblers that are subject to unification, it would at the same time would helps with other problems like, you. Remember, there is a issue with Octa. Octa fails after we installed assembly in Garg and some other things, it happens exactly because we install in gag assembles version that should never be placed in gag because they are already comes with.net framework itself.
Right now we correctly handle it only from the some way handle it only from that standard assembly. We don't try to install net standard assembly through our installation, but at the same time. As soon as we skip net standard assembly we break compatibility withnet framework 4, 6, 2, apparently, because in 4, 6, 2.net standard is not part of net framework, and that it should be installed and got is that multi-targeting? We may solve all of that bunch of problem. But installation and assembly loading would be a little bit harder. So scripts, I mean installing installation scripts would be harder. So if nobody see any think why I should not try it. I would try it, and they'll see how successful it would be.
**Chris Ventura** 49:03 I.
**Paulo Janotti** 49:05 Go ahead, Chris!
**Chris Ventura** 49:06 Oh, I was just thinking with the post install step to minimize which things you have on on disk.
if they eventually update their version of.net framework. They would have to uninstall and reinstall auto instrumentation to make it work. So so we would need to make that clear.
**Igor Kiselev** 49:32 Yes, if customer would update version of.net, they should uninstall and install it. Because in visit we would remove assemblies that we put in. Otherwise.
after it we may introduce the same problems that we introduce right now. Yup, hey, oops!
**Paulo Janotti** 49:56 Yeah. Igor, just thinking, I I I don't think by your description that this should affect the new get package because it it's gonna be at the time that the assembling load is happening. And that happens via the profile. So in principle, I don't think affects that but but it's good to to run the test and see if there is any side effect to the new. Get package.
**Igor Kiselev** 50:30 Yes, I definitely would do.
I believe that.
Most of look at package would be used in.net. I would check how it is used in.net framework, and well, see, I'm not sure if it is fully supported at all.
**Paulo Janotti** 50:55 Sounds good.
**Chris Ventura** 51:09 I think that's it.
See you all later.
**Paulo Janotti** 51:15 Alright, bye.
**Mateusz Łach** 51:19 Bye-bye.
