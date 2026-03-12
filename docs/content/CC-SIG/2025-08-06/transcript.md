SIG: C/C++ SIG
Date: 2025-08-06
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Doug Barker** 01:02 Hi nico.
**Nikhil Bhatia** 01:04 Hey! Hi!
**Doug Barker** 01:08 How are you doing.
**Nikhil Bhatia** 01:09 I'm doing great. How are you doing.
**Doug Barker** 01:12 Oh, pretty good.
Yeah. It's nice to nice to meet you. Thanks for the the contribution. Have you just started working with open telemetry?
**Nikhil Bhatia** 01:25 Yeah. So I was. So currently, I'm studying in computer science and engineering in a college and my final year. So I was looking for some open source contributions to do so. I looked at opentelemetry, and I found it little amazing. So I want to continue contributing in Ocan telemetry.
**Doug Barker** 01:50 Awesome, sweet.
Look forward to reviewing your contributions.
**Nikhil Bhatia** 01:55 So much.
**Doug Barker** 02:02 So this meeting is usually lightly attended. Sometimes we cancel it early, so we can wait on the call for maybe 5 min, and there's Pranav.
See? It shows up.
**Pranav Sharma** 02:17 Hey, Doug.
**Doug Barker** 02:19 They pronounce.
**Pranav Sharma** 02:23 In the end. The last few segs. There's something important, something interesting. Happen.
**Doug Barker** 02:31 Yep, all kinds of stuff.
Now, I think the last Wednesday meeting we canceled so.
We have a like a little bit of discussion in this meeting. Hopefully on the resource detectors.
**Pranav Sharma** 02:48 Oh, nice. Nice. Yeah, that's something I'm interested in.
**Doug Barker** 02:59 Cool.
Well, we can probably hang on for maybe another 5 5 min or so, and see if or Mark or anybody shows up.
**Pranav Sharma** 03:07 Yep.
**Doug Barker** 05:02 Hey, Raphael.
**Rafael Roquetto** 05:05 Hey? How's it going.
**Doug Barker** 05:06 I'm pretty good.
Are you? Back on hot water?
**Rafael Roquetto** 05:11 Back in hot water. Yeah, thank God.
yeah, I think it was in a different link before. And I think I saw Mark, or am I dreaming? Maybe still not hot enough water? I don't know.
**Doug Barker** 05:32 Can I join this one now?
**Rafael Roquetto** 05:34 Yeah.
**Doug Barker** 05:36 For the meeting. Was there a different meeting link.
**Rafael Roquetto** 05:40 Yeah. But then then I left. He left, I guess, and then maybe it was the same link.
And you guys just joined afterwards, and then just joined again. And here we are.
**Doug Barker** 05:52 Okay.
yeah, we can wait a few minutes to see if Marco shows up. But the thing I added to the agenda was the discussion on the resource detectors. So maybe if you guys want to take some time and review that proposal from in the context is that there are these built in resource detectors for like host process, container and service, and those should be included in the main package.
But we're trying to figure out where they should go in the Repository.
**Rafael Roquetto** 06:29 Cool.
**Pranav Sharma** 07:35 So the other languages also have. these cloud provider specific resource detectors which typically live in contrib.
Are there plans to do that as well.
**Doug Barker** 07:48 Yeah, that's what was proposing. So if you look at the second half of his proposal is put in like Aws, detectors, or anything that's specific to a cloud provider, or that's not the built in one we put in contribut.
**Pranav Sharma** 08:04 Okay. Sounds good.
**Doug Barker** 08:17 All right. Well, there's enough people here. Maybe we just you guys want to talk about this proposal can share it.
See if I can get a chrome tab.
Alright. Can you guys see my screen? It should be a chrome tab.
**Pranav Sharma** 08:49 Yes, it's a.
**Nikhil Bhatia** 08:51 Oh yes!
**Pranav Sharma** 08:52 Can see it.
Yeah, yeah, that's good.
**Doug Barker** 08:59 Okay.
So the origin of this one is that Mark is working on the Yaml declarative feature, and part of that is being able to define that you want these resource detectors that are supposed to be built into the SDK container host process service.
So you define that. And yeah, we'll call them out by name, and then it should load, and Nick Hill took on a task to implement the container detector but then we started discussion in this Pr about where should that actually go? Because we start implementing it in the inside, the SDK folder and inside the resource target or library directly.
So started this discussion, I kind of came up this this proposal. But one we'll review is this one from basically create a new folder for resource detectors and then implement the individual detectors in here and then only create one cmake target. So it'd be.
you know, like open telemetry resource detectors would be the target you link to. If you want to use these.
none of these would be running by default. So when you create a resource with the create method, it would just do what it normally does, and give you a resource with attributes or none depending on what you pass into that method.
and then, to use these resource detectors, you'd have to either use the Yaml configuration feature or instantiate them yourself, and then call merge, you know, detect, and then merge on on the resources.
Does that make sense.
**Nikhil Bhatia** 10:42 Yeah.
**Doug Barker** 10:47 So I think the the only question I have is probably on this container detector. Looking at some of these, it looks like most of them. They don't need any kind of external dependencies. But does anybody have any thoughts on this one? The container detector? Does it need external dependencies to get the container id for the various platforms, because if if we need external dependencies and that may warrant breaking this up into each one is its own target or library. If it brings in a 3rd party, library.
**Nikhil Bhatia** 11:16 Actually to add container detector container Id does not require any external libraries.
**Doug Barker** 11:24 So.
**Nikhil Bhatia** 11:25 But other things like image.id, and other things, require external dependencies. So we need to use a docker, inspect command to get those information.
**Doug Barker** 11:41 Okay.
So if we do that, I don't think any of those are are required right now, are they any of those attributes?
They're all, all like should implement, but not required to implement for the detector.
**Nikhil Bhatia** 12:01 Actually they are recommended for now, but not required.
**Doug Barker** 12:05 Okay.
yeah. So I guess one option is we could.
Since your implementation doesn't have any 3rd party dependencies, we could put them all in 1 1 target and then break it out. When we actually need to add dependencies.
The alternative is to start with this being a Sep, a separate project by itself, and anticipating it, will have a 3rd party dependency.
**Pranav Sharma** 12:34 What if, if I may ask, what what is this 3rd party dependency that is required.
**Nikhil Bhatia** 12:41 So can I answer it?
**Pranav Sharma** 12:44 Sure.
**Nikhil Bhatia** 12:45 So for Docker inspect command, we need to get the docker cli. 3rd party dependence.
**Pranav Sharma** 12:55 Do do. Other sdks also use the same method for container detector.
**Nikhil Bhatia** 13:01 As much as I know the go SDK has implemented only for container id.
so any other SDK doesn't use it.
**Pranav Sharma** 13:13 I see, so should we just follow those other languages, or do we want to do do it by the spec.
**Doug Barker** 13:25 We could probably implement a bare bones, one that just does the container id and A in a lightweight way. And then, if somebody wants a full docker detector, then implement that and contribute with the 3rd party dependency.
**Nikhil Bhatia** 13:42 And I had some few questions.
Actually, so, these Linux based systems have container ids in in that C group file, which is slash, pro slash self and slash C group. But in Darwin based operating system, if it if a container uses Darwin based operating system, then there is no such fiery there. But again, for Darwin based systems, it is present in slash, etc. Slash hostname.
**lalit** 14:18 Yeah, I think Proc, file system is not there in Darwin based at least system. So probably I think it's we may have to do a separate conditional for both.
Oh, 6, and Darwin I mean Lenox and Darwin.
**Nikhil Bhatia** 14:34 Yeah.
**lalit** 14:36 Which it should be okay, right? I mean, I'd be more concerned about the 3rd party dependency which which was mentioned.
Oh.
I mean, unless until there is, I mean, I agree, unless until there is no substantial 3rd party dependency, we can keep it here.
and we can revisit it if we see that there are dependencies coming up, we may want to move it separate.
But yeah, start with the same. And then we can. We can always. It's still experimental, so we can always change it.
**Doug Barker** 15:07 That makes sense.
And.
**Rafael Roquetto** 15:10 Sorry just sorry. I'm not too familiar with this. So I just have a question when you guys talk about container id like running getting the container. Id, is it from within the container itself, or or from the host? Perspective.
**Nikhil Bhatia** 15:26 So container id can be provided by a docker cli which is using docker, inspect command, and also Docker provides its docker container Id. In this Proc. File.
**Rafael Roquetto** 15:40 Because I mean.
you can also get like, what I've done in the past is getting like literally inspecting run, doctor, like container D Directory, and then you get like the Ids. There. There are other ways that we couldn't skip skip dependencies if we if we choose to do so. But this would be like if we're not not inside the container itself, right? If you're inside the container, then maybe you can use the proxelsey group as as you guys have explained, but from outside it's you don't necessarily need to bring in a dependency. You can manually, if if it makes sense. I'm not saying, it is the best course of action, but if you want to avoid independence, it's not too hard to inspect things just by looking at the the run docker container, I guess, but I could be wrong.
Slash, run, slash, dot docker, slash container, G, for instance. Then you get all the running containers there all the Ids, and you can.
you know, get some metadata from there as well.
From the top of my mind. I guess.
**Nikhil Bhatia** 16:47 Actually, I'm not quite sure about that. I mean.
I actually didn't try it anytime. So like outside of the container we can get, but from inside of the container I never tried it.
**Rafael Roquetto** 17:08 Oh, yeah, no, for inside the container it won't be able to. Yeah, that's what I that's what I was asking for inside the container don't have access to that. So only I guess only the proxy of C group. And then you have to do some manual parsing.
Yeah.
**Doug Barker** 17:29 So what do you think if we just keep it simple for now, and just get the container id, and then document what platforms we're supporting and keep it all as one C mate target for now and then, if you know, we decide to implement more attributes later or or more platform support. Then we can figure out if we want to break it out.
See a thumbs up from all that cool.
hey? Let I know you propose.
Oh, go ahead.
**Pranav Sharma** 18:00 Oh, yeah, sorry. I was just saying, Yeah, I like that idea. I think other sdks are also using, doing exactly what you are saying.
I looked at Javascript, and and go.
**Doug Barker** 18:15 Sweet anything else to discuss on this one? Then.
sweet.
alright! I can probably stop sharing my screen. Let! Do you want to drive, go through the issues, or look at anything.
**lalit** 18:40 Yeah, I'm just driving. I just joined for this this discussion of this this point. So I'll be just dropping the hook. Sorry about that.
**Doug Barker** 18:49 Meant, drive the meeting. But you're physically driving this.
**lalit** 18:53 Yeah, that's and I just need to join another meeting. I'll be just dropping now.
just wanted to discuss this point. Yeah, yeah, thanks. Thanks for driving it here.
**Doug Barker** 19:04 Yeah, alright, thanks. I guess we can go through the issues. Then.
Alright.
I think what probably works best is if we go through these offline.
you know, if you have any, you know just any that you see there are need triage, and and you can contribute to just add some comments or ask for clarification. Hopefully, we can. We can transition these.
Are there any Prs that anybody wanted to go over?
So we talked about the resource detectors.
I don't think copilots in the meeting. It's got a few.
Hey, Rafael? I know you're interested in reviewing more Prs. Do you have a chance to talk with Mark, or lit, or anybody.
**Rafael Roquetto** 20:26 No.
no cause I wasn't present on the last meeting, and I want to bring this up like I wanna start getting more involved with the code base. Unfortunately for me, it's been yeah. With the other practice, it's been really busy.
I haven't given up, and I haven't contributed a single line of code. So I don't know if it's okay for me, one to maybe help with reviewing Prs. In spite of that, because that's a way of me for at least, if you do something to help.
why, I cannot really sit down and and like write code. I obviously don't know the code base very well, but I could maybe help with General C, plus plus things. I don't. I don't know if that would be constructive or not, but I thought I would bring this up.
**Doug Barker** 21:18 I'd support it. I think it. I think it's always helpful. And there's other people who aren't like official approvals that are jumping in and making comments when they see you know something. So I I can speak for myself as an approver I definitely appreciate when when people help out. So what do you think.
**Pranav Sharma** 21:35 Yeah, I think that's that's great.
So you need all the help. And I haven't been able to contribute much in the last 2 months.
I'm trying hard, so any help will be appreciated by that. Thanks.
**Rafael Roquetto** 21:51 Alright. Thank you.
**Doug Barker** 21:53 3.
Alright! Well, I think there's probably not a lot else. Is there anything else on the agenda? Anybody? Added.
**Nikhil Bhatia** 22:08 And I would like to add one more thing I found another issue on which I could work on.
so can I work on it too?
**Doug Barker** 22:19 Yeah. Do you want to talk about it? What? Which issue is it.
**Nikhil Bhatia** 22:22 Oh, can you click on the issues.
**Doug Barker** 22:25 Yep.
**Nikhil Bhatia** 22:28 Yeah. Metric filter needs a new attribute processor.
Oh.
**Doug Barker** 22:35 Oh! This one!
**Nikhil Bhatia** 22:36 Yeah, yeah, looks like fair game.
**Doug Barker** 22:41 Yep. Yeah.
**Nikhil Bhatia** 22:42 So this thing already contains an include list. Just we need to add an exclude list.
So it's partially implemented. So I was thinking that I could do it completely by adding, and exclude this.
**Doug Barker** 23:01 Yeah. Sounds like a good one.
I haven't looked at this one yet, but feel free to take it up and just make a comment here that you're working on it. I don't think we can assign the issues to people unless you're in the organization. I think there's something like that. But make a comment to say that you're gonna take it up.
**Nikhil Bhatia** 23:22 Yeah, sure.
**Doug Barker** 23:24 Sweet, all right. Anything else.
**Pranav Sharma** 23:32 Nothing from my side.
**Doug Barker** 23:37 Alright. See, you guys later have a good week.
**Rafael Roquetto** 23:40 Have a good week. Thank you.
**Nikhil Bhatia** 23:43 Thank you. Everyone.
