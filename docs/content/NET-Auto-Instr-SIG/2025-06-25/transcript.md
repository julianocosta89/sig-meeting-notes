SIG: .NET Auto-Instr SIG
Date: 2025-06-25
Duration: 54 minutes
============================================================

## Zoom Recording Transcript

**Paulo Janotti** 01:19 Hello!
**Piotr Kiełkowicz** 01:48 Oh!
**Mateusz Łach** 01:49 Hello!
**Paulo Janotti** 01:54 Hi! Everyone, almost 9 or 3 at the time, for the usual start.
**Piotr Kiełkowicz** 02:07 Pablo, you have mentioned that you have audio issues.
**Paulo Janotti** 02:11 Yeah, I it. It's failing from time to time. Here.
**Piotr Kiełkowicz** 02:18 So. So I fixed my issues.
**Paulo Janotti** 02:26 Overall. Welcome back. Pio. 3.
**Piotr Kiełkowicz** 02:31 Nice to see you all guys.
**Paulo Janotti** 02:56 If you can drive today you'll be great.
**Piotr Kiełkowicz** 03:02 You just a moment.
I will show my screen.
I have too long holidays, so I need to work more. Thank you, Pablo.
So I've added one topic from.
and we've got our internal request.
It is request to release 1 12. 0, version of auto instrumentation with current state.
I'm not sure if we have form to decide. We are ping Greece and Russian slack, and Zack also. Maybe they will be able to say yes or no, and I will. If they agree, I will cut off the release early next week.
**Paulo Janotti** 04:14 A side question. Piotry but related to the SDK Martin has been working on getting the dependencies of the Microsoft extensions tired to the run times. So then we don't have the 8 depending on on the 9 version.
That could resolve a lot of our cases with Microsoft extensions.
Do you think that is something that's gonna be released relatively soon? It's gonna take time there on SDK.
**Piotr Kiełkowicz** 04:59 I doubt that it will be released for.net. 8 ever.
and I suppose we will be in the better shape when.net.
It is retired, and we will have.net 9, 10 working correctly.
**Paulo Janotti** 05:24 I see so, so.
**Piotr Kiełkowicz** 05:27 Yeah.
SDK maintainers considering downgrading package version as a breaking change.
at least, it was considered kind of 2 months ago. I'm not sure what is the current state of.
I'm not aware about the discussions on on last meeting.
**Paulo Janotti** 05:55 Okay, yeah. So so. But anyway, it seems that from that from.net 10 onward a lot of things can happen. But at least the current problem should be minimized if we follow from the pattern for.net 10. And whatever comes after. Yeah.
**Piotr Kiełkowicz** 06:17 Yeah. The question is, if we will need to upgrade diagnostic source and logger extensions. This is kind of too pretty importance.
Packages from the open telemetry perspective. And typically, there are improvements in the newer version. So the question is.
if we should improve and break out the instrumentation and bring new functionalities or no.
I do not have a good answer for this.
**Paulo Janotti** 06:52 No, no, but but the it's a good perspective on this, all right. Thank you.
**Piotr Kiełkowicz** 07:00 So for requests.
Martin. Added some uninstallation instruction to our readme, I think it is ready to merge pretty straightforward code. So.
ghost.
And if Jenny started working on file based configuration, if any would you like to tell more about this.
**Yevhenii Solomchenko** 07:42 I provide 2 new 2 new Avars for start configuring. It's just a second.
Can I share a screen.
**Piotr Kiełkowicz** 07:55 Sure.
**Yevhenii Solomchenko** 08:02 Okay?
So it's a hotel experimental config file. Use a standard config, Yaml and auto experimental with your file enabled.
This one, I take from the specification.
So must be okay hard to find for now.
But it's not from the specification this one.
And we can rename that also, if you and virus which is connected to.net out implementation out of certification, this should.
Yeah, we should create our specification for that. I think.
**Zach Montoya** 09:18 For the.net ones. I know the specification has like for language specific variables as long as it's like hotel underscore language. So yeah, those ones. I don't know if we need us.
**Yevhenii Solomchenko** 09:32 It's actually instrumentation, I think, only for instrumentation, specific.
**Piotr Kiełkowicz** 09:48 What he's trying to say that you can create custom environmental way up, supported only by us by providing prefix auto, underscore.net underscore auto underscore whatever you want.
**Zach Montoya** 10:06 Yeah. So there's yes, even if we don't, it's not in the standard, like as long as we have like hotel underscore language, underscore feature like that's generally acceptable for like language, specific flags.
that's all I wanted to highlight.
**Yevhenii Solomchenko** 10:20 It's for for that is environment. Yeah.
**Zach Montoya** 10:26 This is just this is general environment variables for from like the environment variable part of the spec of open century. So yeah, maybe it also applies here. I would expect it to, since there's a standard way of converting from the environment variable to the config declarative format, but I think.
**Chris Ventura** 10:52 This is more like opting into a feature flag, it seems.
cause I I don't know if that environment variable, something that's going to be used in the long run, or if it's just used in the short term or opting into the file-based configurations. For now.
because it's not something that's been fully rolled out.
So so that's the big unknown to me.
**Yevhenii Solomchenko** 11:32 Okay?
So current status of implementing.
Yes, I start moving features which was on an SDK and move to our configuration site like. Good.
It's a batch exporter.
Configuration, reader. Configuration draws auto exporter, zip endpoint.
and some important thinks it's resources which is on the SDK side for now and I think a few they'll be out of there.
Configuration like.net profiler, but not run times.
Oh, everyone trying!
And that additional settings, for example.
Netflix redirect, enabled because it's also auto specification.
**Chris Ventura** 13:11 So some of these environment variables, we're never going to be able to control via file-based configuration because they need to be present as environment variables before the process starts.
And so the one specifically that you're seeing for the.net clr profiler.
There's we're never going to map that to a file-based configuration.
It's just not possible for us.
but the ones that you see with the hotel.net auto prefix. I think those are all going to be candidates for making available in file-based configuration.
**Yevhenii Solomchenko** 14:00 About 1 1 more time. It's about
**Chris Ventura** 14:05 So the environment variables that you see in the.net Clr profiler section that you have.
those will never be able to be controlled from file-based configuration.
the.net runtime itself requires them to be specified as environment variables before the process starts.
Otherwise our code will never execute but the environment variables.
Oh, and I guess this similar thing will happen for the startup hooks and additional depths and shared store.
because those environment variables are not things under our control.
but the ones that you see with the hotel prefixes.
Those are the ones that are under our control and can be managed through file-based configuration.
**Yevhenii Solomchenko** 15:14 Okay.
I think that's all.
**Chris Ventura** 15:22 1 1 question that I have regarding file based configuration, if I remember right. It's a yaml based format.
But when I previously searched for Yaml parsers in the.net space. I didn't find any that supportednet framework 4, 6, 2, so I don't know if you found something that that would work.
**Yevhenii Solomchenko** 16:01 I think I use that one is a without dependencies.
And for net standards.
**Chris Ventura** 16:14 But it doesn't go back to to net. 4, 6, 2.
**Yevhenii Solomchenko** 16:21 Yes.
So that's something that we're gonna have to consider with our.
**Chris Ventura** 16:31 File-based configuration, support.
**Yevhenii Solomchenko** 16:39 Okay.
**Zach Montoya** 16:44 This one implements net standard, too, so it should support 4, 6, 1 right.
**Chris Ventura** 16:50 I.
**Yevhenii Solomchenko** 16:50 Yeah, that's.
**Chris Ventura** 16:51 Net. Standard 2 isn't fully compatible with netframework. 4, 6, 2. There's some rough edges. Sometimes it works, sometimes it doesn't.
**Zach Montoya** 17:03 Interesting thing.
**Chris Ventura** 17:04 So if you have a so if your host only has 4, 6, 2 installed and you're not, and it's not running like 4, 8 1. But your app is targeting 4, 6, 2, then not all of the necessary libraries to make it 100% net standard 2 compatible are present on the system.
**Zach Montoya** 17:33 Gotcha, so it might be like.
well, net standard, like 1.6 or something like that would probably surface area probably match. But there's some gaps in the 2 point O.
**Chris Ventura** 17:43 Correct, correct.
**Zach Montoya** 17:47 Gotcha. Okay.
**Chris Ventura** 17:49 And so I've I've seen problems when we've relied on a net standard 2 package when trying to instrument a 4, 6, 2 app.
**Piotr Kiełkowicz** 18:03 So what you are saying, Chris, we should test at least manually test it with.net framework 4, 6. To install it without 4, 7, 4, 8, etc, on the kind of ancient machine.
**Chris Ventura** 18:20 Correct.
And even then I've seen some quirks where it also depends on the visual studio version that you're using to build that 4, 6, 2 app, where different versions copied additional assemblies, and and others didn't.
**Piotr Kiełkowicz** 18:44 Other things to consider. I'm not sure if it will be possible, for the framework, for 60 can kind of vendorize how yaml.net version into our code and try to compile directly to 4, 6, 2.
It should be probably the safest option.
**Zach Montoya** 19:05 Yeah, that'd probably be the the better option.
**Yevhenii Solomchenko** 19:23 That's all. From my side.
**Piotr Kiełkowicz** 19:36 Alright!
Give me a second. I need to go back to to correct window and this one short distance.
Sorry, guys. I've seen kind of on holidays.
I as we have kind of quorum for the Maintainers. I would like to back to this topic. I've started at the very beginning. We have internal requests to make a release what we currently have on the main branch and postpone other parts for the next version.
**Chris Ventura** 20:28 I feel like there was one bug or issue brought up last Sig meeting that we felt like we wanted to resolve as soon as possible, but I don't remember what it was mattish. Do do you remember? I feel like it was one that you brought up.
**Mateusz Łach** 20:48 Yes, I think it was this one related to logging the one at the bottom. So yeah, I'll I'll prepare a pr this, basically this week, so that it will be ready or ready to be reviewed by the by by early next week, so that it's not blocking the release.
**Piotr Kiełkowicz** 21:11 But even if it is not fixed, it is not a regression. It is painful for the end, user or costful for the end user. But we are working in this way. Kind of at least couple releases So if you are, if you are fine, I will move all other stuff to 1 13 and cut off release kind of Monday or Tuesday next week.
**Chris Ventura** 21:47 Yeah, I think that can work.
**Piotr Kiełkowicz** 21:51 Thanks.
We come back to to the public requests.
Oh, updating format native images to execute on the latest version. I have sold that. But I will review all continuous integration Pr's next week. But if you have some time, feel free to put your comments here. No, nothing very important.
**Chris Ventura** 22:28 Yeah, one thing that might be worth talking about is as part of that. There's a change in the check names, or are the job names.
and then we have required checks, but our required checks are now managed in another repo and source control.
**Piotr Kiełkowicz** 22:53 Yes.
**Chris Ventura** 22:53 And so.
if we do decide to change the names, we need to figure out how to coordinate these changes.
**Piotr Kiełkowicz** 23:02 So I think the order should be, 1st modify this, admin, repository.
merge it, and then all our, all, all other changes, will be failing on our branch, so we need to merge changes related to the job names.
**Chris Ventura** 23:27 Okay? And then, are we in agreement about the name changes to those jobs.
**Piotr Kiełkowicz** 23:36 I think name changes are fine, in my opinion, because we will not need to change any anymore when we will be changing the windows versions, and we can just easily switch machine on our site without touching admin repository.
And I think it may be good idea to make a follow up Prs for other for other jobs, also to mitigate issues for the future.
**Zach Montoya** 24:13 That would also work pretty well if we're already going to sort of cut a release soon, and not expecting to merge a lot of stuff it should give us some time to rebase as well.
So yeah, I'm in favor of the the name. Change.
**Piotr Kiełkowicz** 24:30 But probably it should be kind of next week. Not not this one, because I don't have time to focus on this testing with windows. Server I'm fine with merging, but there is too much changes, in my opinion, but still, it is not on top my to do list, so I will be happy to review next next week.
Confluent Kafka. I do not even try to understand what's going on here.
**Mateusz Łach** 25:07 Yeah. So I I looked at it last week because, we briefly discussed it. So basically.
there are like 2 modes of operation. And we are using the we are using one of them in our test setup.
And this mode of operation is being dropped in this version. So if you want to update, we should basically change the test setup and use the Kraft mode. There are some we would won't need the zookeeper anymore. We we are, we would need to set up some additional environment variables. So yeah.
**Piotr Kiełkowicz** 25:44 So code simply certification.
**Mateusz Łach** 25:47 Yeah, probably.
Probably. So.
Oh, yeah, I I can work on that after the the the fix that is needed to be before the release.
Also, I was so basically, the when running it locally, the the Kafka container starts and then exits.
And we talked a little bit about the basically the a lot of noise in logs in Ci. So this is not something that I was able to reproduce on my side.
But yeah.
So I only took a like a quick look into that. So and I I don't think this is like related to instrumentation in any way. So yeah.
**Piotr Kiełkowicz** 26:55 Not I was. I'm not sure if you were discussing it last week.
**Mateusz Łach** 26:58 I don't think we were discussing it last week. So basically, Rasmus added a comment, and I also briefly discussed it with Piotr and Piot suggested to create a like a sample setup with a more complete plugin implementation than that is currently here in the test application. So I'll prepare that, and I'll link to a link to it. Or.
yeah, I probably linked to it, because that's probably not not sure. This is something you want to have in this. Pr, it'd be easier if I link from this. Pr, there.
So yeah.
**Piotr Kiełkowicz** 27:45 I'm not sure if you were able to go through the Pr. Since Prs and the issue description guys, it will be very helpful if you can check it in the free time. This kind of new functionality for us.
We would like to share here. We have already implemented it on the Java site.
I'm not sure if it was upstreamed, or it is only in our repository. But we do not have native plugins, so we would like to put it here purely opt in feature, to allow to kind of sample sample stock traces.
For, let's say, loud traces or kind of important traces.
**Chris Ventura** 28:37 Yeah. So there were some questions in this Pr from Rasmus, I believe.
**Mateusz Łach** 28:46 Yeah.
**Chris Ventura** 28:47 And so I I don't know if we need all of the the questions that were brought up there answered before we review this Pr further, or if that'll be covered by the example that we just talked about and things like that, because I think previously, you just wanted this Pr to focus on exposing the minimum building blocks to be able to to support it. So this isn't necessarily the full implementation. But just kinda the 1st round of changes, to to make things ready.
**Mateusz Łach** 29:33 Yeah. So I, this is basically what is needed from the Plugin side in order to implement it. So yeah, so I think we, we discussed both options, or we considered both options either like implementing the whole feature here, and also only exposing, like the the minimum that is helpful to to implement it from to implement it in plugin and and implementing all of it here, would.
as as we, I think, discussed last time I would expect a lot of customization needed from plugins.
So the configuration would be like complex. I think so then I thought about basically implementing the minimum here. So basically exposing the option to start that start and stop something and do the rest in the plugin.
So yeah, so this is what is in. This is what is in this. Pr, I added some to do's that rasmus basically asked about here. So there is some code cleanup that could be done on the native side. The native code side. This is one. The other thing is verification of this of of the case, where both continuous profiler, and this new mode of profiling are enabled. So this is something that I verified for now, manually, but automated tests for it should probably be included here as well. So this I think that's 1 thing that is missing in this pr but at the same time, I think this is like this is ready to be reviewed because one of the things one of the more important things is, I think, how we want to expose it.
The this ability to start and stop something. So for now I'm call, I'm using reflection to call it from the Plugin. But oh, yeah, so I was. I was looking for some suggestions recommendations.
So yeah, I think I think this is in a state that basically, a review would be helpful.
And I think the the the rest of the of the rest of what I want to implement, or what we need to implement is should be fairly easy to implement in plugin.
So yeah.
if you if any of you had a chance to to to give it a closer look, and if it, feedback would be very welcome, so I think we can move on to.
**Piotr Kiełkowicz** 33:23 And that's all.
I did not have chance to to review Chris. Your comments.
I will be back for this in the next week. Sorry.
And what else?
Any issues?
No discussions, no, no open discussions.
And we have kind of some new issues.
2 days, 2 days.
Let's start with this premium.
**Paulo Janotti** 34:17 Yeah. So I did a quick read on this one. It, it seems, that is, describe a real potential issue with loading.
But I I I'm not sure I I didn't think this through about. If it's really something that we wanna fix, or as much as a device, we don't control these things. But My my tendency is to think that at at least at 1st reading I can. I can go back to this. But at 1st reading is kind of okay. It's a possible scenario.
things should not be load on separate threads.
but it's hard to control for that, and it's hard to fix it @firstst That's my 1st reading on a very quick reading, you know.
I think we we should kind of I was gonna reflect. But my my quick 1st reading is that maybe it's not actionable, you know.
**Chris Ventura** 35:46 It would be good if we had an actual reproduction of the problem to to be able to test against.
Otherwise I I don't know how straightforward it will be to set up such a scenario because it has to be anet framework app based on that loader.
If if I'm remembering correctly, and that relies on is is that accurate.
**Paulo Janotti** 36:29 I I think so. I have to to refresh my mind on that, but I think so.
**Chris Ventura** 36:34 Because I don't think we use the loader from the startup hook.
I think that loaders just use for thenet framework case where we inject the startup with the profiler.
Yeah, it just looks for one of the 1st methods to jet, and then calls the loader from there.
And so that's where I think we're going to get a lot of variance in what happens.
**Paulo Janotti** 37:18 Yeah, I I think what you are putting. There is a natural next step, you know.
So far it's kind of it seems a concrete issue. But we we need to have a reply. Understand how they hit this.
**Piotr Kiełkowicz** 37:43 There is information that we are crashing with self.
Hosted application!
It.
**Paulo Janotti** 37:55 It seems the the same problem that we haven't been having with Microsoft extensions, especially on.net. 8.
Oh.
**Chris Ventura** 38:14 I mean, I assume that's the reason for the Nuget package, because we can't automatically load things in all the scenarios.
**Paulo Janotti** 38:22 Yep.
**Piotr Kiełkowicz** 38:23 Exactly.
Oh.
I think we should ask for a minimum reproducive example.
**Paulo Janotti** 39:01 Yeah. At at the minimum logs, like.
**Piotr Kiełkowicz** 39:46 Okay and kind of older stuff.
I'm not sure if you were discussing Kit.
**Paulo Janotti** 39:56 There was was I I think this one we talked about last week. The main thing is that, for we have the the hash for a more version thing, and we think it's valuable to add the key validation for security. But it's not high priority, you know it's a nice to have.
**Chris Ventura** 40:25 Yeah. And I think part of this was just getting some of the processes documented more so that more of us can jump in and do it.
So it came up because while you were out, Pierre.
the hash changed for the installed.net script.
and I wanted to know what the process was for getting the new hash, and realized that there weren't precious.
**Piotr Kiełkowicz** 40:58 Technically, you should download it locally and calculate hashes and put it there.
**Chris Ventura** 41:04 Well, that that's if you wanted to validate the security of it. If we're just using it as a change notification, you can just copy the output from the the job to show the the change.
**Piotr Kiełkowicz** 41:17 But but but the whole purpose of this is to validate the.
**Chris Ventura** 41:22 Yes. So if we want to do security validation, that's where I'm proposing. Following the steps that Microsoft documented using the signatures instead of just using the the hash.
**Piotr Kiełkowicz** 41:39 The only reason we have. It is kind of requirements that all scripts, dependencies, etc, should be pinned to very exact version.
It is pain in the where you know what is the pain and upgrading all these hashes manually, but still I think it is pretty important to us to have it.
**Chris Ventura** 42:05 Yeah. So I'm not saying we're gonna get rid of the the hash piece. It just simplifies the hash where we can just document as it changes, we can just look at the output logs, grab the hash.
But if we wanted to do the signature validation, then, of.
**Paulo Janotti** 42:26 We we we could we could even add this message directly. Instead of documenting somewhere, it could add a message on on the the the workflow itself to just telling this is notification of version of change. Please run this command to validate that the is correct, and the Ci needs to be correct. No, so.
**Chris Ventura** 43:02 Yeah, we could do that. It's in 4 different places. So that's where I thought if we just had it in a markdown file somewhere.
**Paulo Janotti** 43:10 Yeah.
**Chris Ventura** 43:11 To to document. It might be simpler, because it's happening in the docker files that we have.
**Piotr Kiełkowicz** 43:18 And I've tried. I've tried to remove these scripts, and I do not found a better option to install the all legacy.net stuff. And all this the clarifies.
**Paulo Janotti** 43:31 I I think I think it's fine. The the script is, they stand their wait for people doing deals on.net. So I think it's fine. They script. I I just agree with Chris that I agree with Chris that yeah. When you look at that first, st I I think, it's not clear exactly. What are the steps to get? Kind of fix it? Okay, the shots failing, you know. So I need to fix the shop. But it's okay to just copy, do I need to download? And yeah, just that.
**Piotr Kiełkowicz** 44:09 Sure I've put it for the next version, I mean not 1 12, but the next one.
Oh, Nataws!
**Mateusz Łach** 44:26 Yeah. So I think we discuss it on some previous meeting. So basically, there was a issue brought up when open telemetry demo was being updated and the issue was created in Contrip because that's where the instrumentations leaf. I think.
**Piotr Kiełkowicz** 44:50 Yes, and there were kind of one fix this one released today, and there is a chance that it's we'll be fixing stuff.
This is kind of some some magic. It was not working for a SQL. Client. I suppose it will. It can fix also Npga Square, but I'm not sure.
**Paulo Janotti** 45:25 Can. Can you validate that mattels if it if it's fixes and.
**Mateusz Łach** 45:31 Yeah, sure, definitely. So once this is released, then we can.
**Piotr Kiełkowicz** 45:37 This will be no worries.
We, we need to just update the package.
**Mateusz Łach** 45:40 Okay. So once we update it on our site should be rather straightforward to to verify if it helped.
**Piotr Kiełkowicz** 45:54 I will pull the reference of this putting for 1 13 also.
We are waiting for more feedback from right. I think.
**Paulo Janotti** 46:43 Yeah, yeah, it's Mike, yeah.
**Piotr Kiełkowicz** 46:55 What is the last message?
And I think it can wait for Rasmus as he started working on this.
Or if you have any, Chris, you are talking here also. I'm not sure what is the status.
**Chris Ventura** 47:22 Yeah. So for a while the logs for this application couldn't be found. But now the logs were found, and so they're provided. So we just need somebody to dig into those logs. Rasmus suspects that it has something to do with the of binding redirect changes.
That that are happening or not happening.
and that's causing the the method missing method exception.
But we need to dig through the logs to see if that's the case.
**Piotr Kiełkowicz** 48:01 Do you have some time to investigate or not so much.
**Chris Ventura** 48:05 I don't really have much time.
I'm way behind again.
**Piotr Kiełkowicz** 48:10 Okay, we lost.
and this one i i would put it for the next version. We have already discussed the Pr.
not a wush.
**Mateusz Łach** 48:55 Yeah. So we discussed it some time ago as well. I promise to look into that. Sorry I haven't had a chance yet. So basically, there are 2 options, the I I mean, there are 2 things that we want. I think that we wanted to do the like the short term could be adjusting the instrumentation and long term we were discussing about introducing, like additional log level, like more more verbals than debug So for the for the additional log level, I think this can probably wait for the next release, but for the instrumentation.
Yeah, i i i don't want to.
I don't want to keep promising. I'll look into it. But yeah, I'll I'll I I will try. I will try to take a look into it. I have some idea how we could.
because this is for now this is only the the problem is with only this, this one instrumentation which basically creates and discards activity when there are no messages received. So yeah, I'll I'll try to look into that if we can. Like don't do that. That frequently.
**Piotr Kiełkowicz** 50:28 I've just assigned it to you, and.
**Mateusz Łach** 50:30 Yeah, yeah, so definitely.
**Piotr Kiełkowicz** 50:32 Next week to this.
**Mateusz Łach** 50:35 Okay.
yeah. Yeah. So the what Paulo mentioned there, the like, the additional log level. So this is probably something that we can do in the future, and like for short term solution, we could try to adjust the instrumentation for Kafka. So I'll look into that.
**Piotr Kiełkowicz** 50:54 And this one, I think we need to wait for Rasmus for an update. I'm not sure if there were any discussions which are not documented.
**Chris Ventura** 51:04 Yeah. So I think the main thing with that is something that was discussed at the beginning of the meeting today that with the dependency changes. Beginning with.net 10, we're hoping that minimizes the the frequency of these types of issues going forward.
But it'll take a while to get there.
**Paulo Janotti** 51:32 Yeah. And just to make clear, we have to kind of the policy that was just discussed it on the SDK side.
We need to kind of enforce it for I'm thinking very about the future. But net 11, and going forward, you know, because I I perhaps you can create some tests to enforce this at the SDK level about the dependencies.
But right now the the improvement comes from kind of a policy change and not nothing.
that's let's say in the code or enforce it, you know.
**Piotr Kiełkowicz** 52:29 So, yeah, we can create this kind of test and show this. But the policy should be written in the stone. First, st in my opinion.
**Paulo Janotti** 52:37 Yes, yes.
**Piotr Kiełkowicz** 52:43 So I will keep it as it is for one more week.
But still it looks a bit better.
Oh, we'll clean up key issues later and the Project board.
I'm not sure if we have anything to comment here, comment or no.
**Chris Ventura** 53:33 No, the main one. There is the logging one in the in progress where it may get bumped to the the next release.
**Piotr Kiełkowicz** 53:44 Yes, bugs the plum before release. I will try to update testing libraries. I mean all new version of dB clients.
etc, covered by our instrumentation to ensure that we do not have any gaps with the new release.
Do you have any other topics?
Thank you. Have a nice day.
**Mateusz Łach** 54:44 Thank you.
