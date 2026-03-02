SIG: Go Auto-Instrumentation SIG
Date: 2025-06-17
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:33 Hey, Raphael.
**Rafael Roquetto** 00:35 Hey, Tyler, how's it going.
**Tyler Yahn** 00:36 Doing well, how are you.
**Rafael Roquetto** 00:38 Good thanks. How was the break?
**Tyler Yahn** 00:40 It was great. Yeah. Enjoyed taking the time off. I thought I wouldn't disconnect as much as I did, and ended up, just yeah. Just spending the whole 2 weeks doing other things. So yeah, it was great coming back excited to to get back to it. And yeah, that's that's what it breaks for. Yeah.
**Rafael Roquetto** 00:57 Sounds good. Sounds like you've like drained all the garbage collector, and then you're good to go again.
**Tyler Yahn** 01:05 Yeah, I am like, definitely having to like unload things again. I'm like, yeah, what was going on here or what's going on. And there's like tons and tons of notifications. It's always always a big one. Yeah.
**Rafael Roquetto** 01:17 Fair enough.
**Tyler Yahn** 01:19 Yeah, are you? Do you have any summer plans for vacations?
**Rafael Roquetto** 01:23 Not yet, cause my wife is not gonna be able to take any time off during summer. I might just take a few days off, just to like decompress and
but not do anything. I mean, maybe go up them all things now that they are
very close. So yeah, this week. There's a lot of military helicopters and all like drones flying around because of the G. 7 meeting.
**Tyler Yahn** 01:46 Oh, right? Yeah.
**Rafael Roquetto** 01:47 Yeah. So it was pretty interesting to see from watch from the window. But yeah, so probably just
take it easy.
**Tyler Yahn** 01:55 Oh, okay, how far are the mountains for you?
**Rafael Roquetto** 01:58 Half an hour.
**Tyler Yahn** 02:00 Oh, yeah, you gotta. You gotta get out there.
**Rafael Roquetto** 02:02 Yeah, yeah, yeah, it's really close. Yeah.
**Tyler Yahn** 02:05 Yeah. Oh, yeah, that's that's great. Yeah.
How's it going? Mike?
**Mike Dame** 02:10 Hey? Guys, what's up?
Welcome back!
**Tyler Yahn** 02:13 Thanks we're talking about breaks. You have any plans for the for the summer.
**Mike Dame** 02:21 Oh, I just went down to the beach in Rhode Island this weekend with some family, and
yeah, not too much else going on.
**Tyler Yahn** 02:29 Oh, nice is is the water still freezing? There.
**Mike Dame** 02:34 Oh, yeah, water at all.
Actually a pretty crappy, rainy weekend, too, but still still fun.
**Tyler Yahn** 02:43 Yeah. Time. Time to get away. Right? Yeah.
**Mike Dame** 02:46 Especially with the with the little baby. It was his 1st time at I guess it's not really baby anymore, he's almost 2, but his 1st time at the beach, so he had a blast. Grandparents there, and everything.
**Rafael Roquetto** 02:58 If.
**Tyler Yahn** 02:59 Nice. Yeah. Did you actually get on the beach and get to play in the sand and all that.
**Mike Dame** 03:03 Yeah, yeah, we had a little bit of sunshine on Friday.
**Tyler Yahn** 03:06 Oh, nice. Yeah, yeah, that's that's a that's a great time for a kid. Yeah, that's awesome. Yeah. Are your parents down in Rhode Island?
**Mike Dame** 03:17 No, they're from New York.
**Tyler Yahn** 03:19 Oh, okay.
**Mike Dame** 03:19 Upstate New York. So that's where all the New York people go to vacation.
So I've heard a meme. I saw a meme right before we left. That was like, you know, you know, you're in Rhode Island, because you'll see a bunch of New York plates.
**Tyler Yahn** 03:36 Yeah, that was always the joke in Florida as well. It's.
**Mike Dame** 03:39 Yeah, yeah.
**Tyler Yahn** 03:40 Yeah, yeah, yeah. But that's I guess that's more wintering, like snowbirds going down there. But yeah.
**Mike Dame** 03:45 Hmm, yeah.
**Tyler Yahn** 03:46 Vacations at Rhode Island. Yeah.
**Rafael Roquetto** 03:50 Yeah, in December. I'm going to Brazil, for then I'm going for 5 weeks. I'm going to the beach, and I'm looking forward to that. Yeah.
**Tyler Yahn** 03:56 In December. Oh, man, that's the time to go. That sounds great.
**Rafael Roquetto** 04:02 Yeah. Escape the escape the snow for a while. It's gonna be nice.
**Tyler Yahn** 04:05 Oh, yeah, is that? Are you going to Rio de Janeiro?
**Rafael Roquetto** 04:09 No, I'm going to Sao Paulo, where my family is, and my my brother, who lives in New York, is also
flying down. So I think it's gonna be the 1st time in many years we'll be all together as a family. So it's gonna be cool.
**Tyler Yahn** 04:21 Yeah, nice. Yeah.
**Rafael Roquetto** 04:23 Yeah.
**Tyler Yahn** 04:25 Well cool. We can jump in here. I don't have a big agenda for today. So yeah, if you haven't yet, go ahead and add topics you want to talk about, and we can jump on here. See if I can find this.
**Rafael Roquetto** 04:51 Yeah, Nicola is not coming today. By the way.
**Tyler Yahn** 04:53 Oh, cool. Okay, yeah. I guess I was just about to ask that question.
okay, cool. So just to start us off. I wanted to look at the open Prs. I've been going through these for the past 24 h, so just kind of catching up on things that have happened in the past 2 weeks. I'm trying to wade through some of these renovate Prs, which aren't that important. But yeah, I just wanted to kind of like update. Get some updates on this sort of stuff. I did see some comments on these sort of things, so maybe we can just kind of follow up as well.
Mike, I think I saw you comment on this one across platform, perf reader, implementation.
Just asking for some update. I'm guessing.
**Mike Dame** 05:39 Last week we were kind of just going through old Prs and issues and stuff. And just seeing if.
yeah, if this person was interested in still working on it. Give them I don't know. I think a week is probably enough time to see the notification and reply if they're still interested, so we can probably close this. I just figured it was nice to give them a chance.
**Tyler Yahn** 06:03 Yeah. And so the idea is, other fixes in this Pr welcome stubs fixing. So there's like other things we wanted to split off from. This is what the idea is.
**Mike Dame** 06:13 Yeah, that's what it sounded like. We didn't think too much into it. It was just kind of like, oh, the main issue was addressed by this, but it looked like there were some other things that they might have done, too. If they still want to contribute, but we can just close the Pr. And they they're free to reopen it if they want to come back to it. That's probably what I should have done.
**Tyler Yahn** 06:33 Yeah. Well, I'm kind of wondering. Should should somebody else pick it up and and just merge the stub
portions.
**Mike Dame** 06:45 I mean, it looks like it's kind of just that. UN 64. What else did they change.
**Tyler Yahn** 06:53 Yeah, I'm not exactly sure
I'd have to look through a little bit more detail. I know that there was like this like perf package introduced. But I think that, like one of the big things was that like there was actually implementation details for like kernel, other that were not tested. So like, yeah, like this actually was the wrong signature. So if you try to compile it on a system that wasn't like, I guess.
like Amd, 64 or something like that, or probably arm as well.
I don't exactly know what other systems. Maybe this is also just maybe it was just
on an arms. Oh, yeah, I think that's it. So it's like, if you're compiling this on a Mac, which I think the main workflow for, like Ron. And I'm guessing you as well. Mike is just to use Docker right? And so
it like
it works just fine. But I think that, like this person was trying to compile it natively, and it was failing which
it's tough, but I think also like it is failing, because literally like signatures, were incorrect, which should not be the case. So yeah, I think maybe these are the things we need to port over. And so
I mean, that's a pretty simple thing. I can pick it up. I just didn't want to step on people's toes. So it sounds like, based on your comment, we just need to. Yeah, just pull these over.
**Mike Dame** 08:05 Yeah, I think that you know we we get. It's been what like a month since the last update. And give them another week of a ping, so I don't think that they'll be too offended. But gotta move forward.
**Tyler Yahn** 08:17 Yeah, I think that's fine. Sounds good.
Next up is the shift process
management from probe to manager. This is your Pr.
If I remember correctly. There was like some changes you made before I'd left. I don't know where we're at on this.
**Mike Dame** 08:34 Yeah. Well, I added, those in the last comment at the bottom, it was really just 2 things. So kinda I've I've gone over it. Because Niccolo was out, I think, the week before, and then Ron was out. Nicola was back, so I've explained it a bunch of times. I'm getting pretty good at that. The the 2 things that we had were
the manifest question of should the manifest function be part of the interface and then when we were on that call, we you know, we all decided that it is good to have that in the the probe interface. So I added it back.
Cause. I remember it was duplicate, so I tried removing it.
But when I added it back I made these extra kind of slight changes to it.
the right. Now the manifest is different from what the probe stores, because the probe stores actually the full list of U probes and constants, and the manifest only stores struct fields. So it's a subset of the constants. And the we call it symbols, which is just another like format for representing u probes. So what I did in this, and you know, let me know what you think of it. I
made the manifest just store, the raw same consts and new probes that the probe would store.
and then to get those struct fields and symbols is, I added, functions to the manifest type, basically to do that processing. The difference is that in the current approach before my change.
these struct fields being stored on the manifest. Does this like pre processing of sorting them? And you know, parsing them out. So if there's a like an efficiency reason for that. I could totally see wanting to have those stored once. I don't know how often we're actually calling for, you know, all the struct fields and all of the symbols off of a probe. If it's just done at load time, then it might not be that bad to do this.
I I also kind of rearranged this sort function because it was a little crazy.
So that's the change that I made to the manifest
it like I made it the same. I see it kind of confused. I made it the same sort, but it's just not like 5 layers nested
So that's what I did to the manifest. The other change that I made after our feedback was so you had commented on the fact that I'm passing this probe reference into the load functions. Now that the manager holds this object, the probe reference that keeps track of like the closers and the collection. Once the probe has been loaded and activated.
And so you were commenting that, you know, passing that probe reference pointer, and then setting those fields within like the probe load functions, is kind of like implicit and like, I think you said like a programming side effect. And so
what I ended up doing here was to address that I I've made it a lot more explicit that you know, when you call load, it's gonna return like this collection, and then the caller can set the collection on the probe reference, and and kind of like that. The side effect of that is that
currently this load function does a bunch of different things that are all passing these like object references around. And it kind of makes sense, because that's all managed within the probe itself. So it's just acting on itself and setting the collection on itself.
Now that we want to pass that around it kind of required breaking this into a little bit more discrete functionality. So there's now, instead of just one load.
I have like a generate collection. I have a, you know, get closers. I have a I think, inject consts. And so that kind of broke that functionality up a little bit, and I summarized those like I linked to the comments in the bottom of my that message that I posted where I broke down exactly like what I changed a little bit better. I just kind of made that
comment a summary with a link. But those are the 2 big things is putting the manifest back. But the change to you know what the manifest stores and changing. You know, the function
breakdown of loading a probe
and that's pretty much it. So I think what I've been saying is that I think they just take it from a fresh look again. You know, instead of trying. And we've been working on this for a while. So trying to keep track of the context. And it's been some pretty big changes, anyway. So yeah, just take a look at it. Look at my 2 comments that I linked to and feel free to, you know. Let me know what you think. Going forward.
**Tyler Yahn** 13:31 Yeah, okay, I'll I'll definitely do that. Take another look Raphael, have you or Nicola taken a look at this yet?
**Rafael Roquetto** 13:41 I haven't.
Okay. I should. I should.
**Tyler Yahn** 13:46 Yeah, I mean,
yeah, more eyes, the better. One of the things that kind of stands out like this. All those things sound great Mike. So yeah, I just have to like you said, take a look at it with fresh eyes. I do want to think about it in the context of like what we talked about when we initially talked about this and making sure that, like the integration
with the the Epf Instrumentation project, is gonna work like, I think that's kind of like the ultimate goal. And I don't see why that wouldn't be the case. But I just wanted to like. I'm not as familiar as with, like that kind of stuff. So it'd be great if we get somebody from that team more familiar to look at this.
**Mike Dame** 14:23 So I think in that sorry in that context. And it's the same, you know, context for Otigo, too. So we're coming from kind of the same place of it. The 2 goals of this, that this feeds to our one, mainly trying to get dependencies out of the probe definition. These internal dependencies, things like the process, analysis and and management get that out of the probe. And just like there's more things that need to come after this. This is just where I'm starting to chip at it.
So that's the one thing is stripped down. What the probe uses and the other is centralizing that interface for managing probes in the manager, instead of having to keep track of all these probes, so that one is gonna have more of an effect on things like otigos and ob.
for you know how they interact with the probes, because right now, the methodology is kind of like, you know you're calling probe dot load, or you're using these process management functions from the probe. So
that shifts the mentality into like your interface with the instrumentation is through the manager and then the manager manages the probes and the processes for you. So that's if they're trying to keep the big picture in mind, the context, those are the 2 things to strip down these dependencies and re, kind of classify the manager role of what it does.
**Rafael Roquetto** 15:48 Cool, cool. I'll have a look. Probably today's too.
**Mike Dame** 15:51 Cool thanks guys.
**Tyler Yahn** 15:54 Awesome. All right. Yeah. So definitely, more, review on this. Thanks for all the work on this. Mike. Appreciate it.
Appreciate the feedback.
It's a long one.
cool next up the telemetry. Add tests for the trace. Id and span id. I think I saw some. Did you comment on this? Maybe Mike.
**Mike Dame** 16:14 Probably. I think we went back through everything.
And they said that they oh, and they pushed some commits yesterday. Cool.
**Tyler Yahn** 16:24 Okay.
**Mike Dame** 16:24 Looks like. Nicholas approved it.
**Tyler Yahn** 16:28 It's empty, too.
Okay, yeah, it looks like, maybe there's some follow up. But it looks like this is just also ready for some review. So yeah, okay.
cool. Thanks for pinging.
I haven't reviewed that once yet. So that makes sense. This one.
Normally, we don't talk about renovate Prs, which is fair
this does have. There's there was like an update to the Var naming Linter, which caught something that was always kind of bugging me, but didn't really bother me because it was internal. And that's just the package naming for this utils package, which is like kind of
it's not like an official anti-pattern of Go. But it's not really a descriptive name, and a lot of people in many different places think that this is a good example of of a bad name.
so it's also a very small package that does like kind of some like
mundane things, or it's used in certain places. So I was going to look at this later on. Once I get a bunch of Prs wrangled just kind of a heads up that I was looking to rename this package. If people have thoughts on this, or have ideas of how to like split this, or just renames what they think, I'm open to any sort of suggestions on that. But otherwise it's probably just going to be. I mean, yeah, like, it does like kernel level stuff like it does
utils. Obviously is not descriptive of what it does. So hopefully, we can try to split that up. But again, it's all internal. So it wasn't ever really a top priority. So, yeah.
But yeah, if you have ideas, go ahead and comment in this. Pr, otherwise we'll just probably make a really quick change to make the lint pass. So yeah.
cool. Add distro version and name by default to the hotel SDK handler. So this is something that I remember Ron was talking about before I left, where they're not able to get like the in the logs. The the actual distro version
in the Cli I can't remember exactly, but the idea was that, like there was a dependency cycle. So we need a new package to handle this from a centralized place, and this looks pretty straightforward
the thing is is, though, I didn't notice this. This actually isn't what is done in the releasing process. Because Multimod currently just updates this, there's actually tooling already built for this. So I was wondering if we could actually do that here. I don't know
exactly. Actually, I do know exactly, because I think I wrote it, but like we definitely can have it, it'll find this file, and it will look for this version. It's just I think this needs to be a module, or it needs to come from a module is the only thing. And so we could
we could restructure this a little bit is the only ask I have for this, which I don't think should be too hard.
I'm interested. This is interesting, but anyways, I think, since it's internal, it's not really like that critical. But I
provided some feedback, and I was just looking
waiting for for Rhonda. Respond to this. So yes.
I think it. Okay. Yes, I did add comments.
but otherwise this this looks like the still. The same port is Ron on vacation. Mike.
**Mike Dame** 19:47 Yeah, he's gonna be gone, I think. Next week, too.
**Tyler Yahn** 19:52 But then he should be back the week after.
Okay, hmm, alright. I think
maybe we'll talk about that in a little bit. But I think this definitely should be in this milestone given. This is a feature that was removed in the last request. So I'm gonna add to the milestone at least, and we can
discuss about that.
**Mike Dame** 20:14 I mean, I'm sure he wouldn't be offended if you wanted to like pick his commits and start a new branch or
**Tyler Yahn** 20:21 Yeah. I mean, I can also just push to that branch as well as the thing which I mean.
do you think there's a preference there.
**Mike Dame** 20:32 I just prefer not to have people push to my branches personally, but I know that you know either way is probably fine.
**Tyler Yahn** 20:39 Okay.
yeah. I mean, I just then we could keep it in the same. Pr, but I'm happy opening up another Pr as well that I can take that up, too. Yeah.
okay, I will. I'll take a look at that. Then I yeah, especially if he's gonna be out for another week.
I'd love it if you can come back and have things working. So yeah.
that also answers, I think this next question as well. So this is another one that I saw was open while I was
gone. And so there was a build issue that was definitely identified
here, and Ron was able to open up a Pr to try to fix this. So yeah, I wasn't. I was trying to follow this. So excuse my ignorance, but, like. The idea is that in the
docker file, now, we actually have this stanza where we will set the environment variable. And we set the environment variable within this scope. The problem is that we don't actually set it within the same scope as the Go build command because it's actually run in a different scope. So all of these values are only set for this. Go, generate, and then this go. Build doesn't receive any of them, which is where this error is coming from.
So this Pr
is that's looking for. This fix is reverting back to just going with the the docker file, and I think that's a misstep for a few reasons. But, like, you know, one of the things that kind of just points it out like
this actually already has a bunch of failures that come with it, because it's not including all the files it needs to. And they're they're hidden. So if you run this locally, you can. You can see them, but
doesn't actually fail, even though it can't find certain files in the make file.
So I don't think this is the right approach one. It adds more dependencies, it adds churn again, which is one of the reasons we went away from this. When you change the make file, you're actually changing like the invalidating the docker cache.
So I went, and I looked at this. And
I think it like this is.
we can just fix what's actually there, and this is the alternate approach. This is something that Ron had also included in
a comment. Here.
**Mike Dame** 22:57 Yeah, setting the environment variable through the docker file.
**Tyler Yahn** 23:00 Yeah, yeah, yeah.
**Mike Dame** 23:02 Yeah. So yep, that's you know, we had talked about this me and Ron a couple of weeks ago, I think. Well, maybe Nicola was out, too. And I said, Yeah, I mean, I remember that we had all talked about having the make commands in the docker file and preferences for and against that. And so I actually said, like, let's wait for Tyler to come back and see if he can, you know. See what he thinks about this. And maybe while we were brainstorming that we thought of
passing this environment variable through here. So I think if that's fine, then, yeah, like, Ron didn't have a strong preference of specifically wanting to call the make command for it. He just wants it to build on arm. So. If this fixes that, then I think that we should be good. But if you want, I can.
I'll test it. On a Mac. I'm assuming, you know. Have a a Mac to actually make sure that it builds right? So I can check out your branch and test for him while he's while he's gone, and if it works for me, then I'll prove it.
**Tyler Yahn** 24:02 I, yeah, I would appreciate that, like, I definitely tested this by adding in some like echoes, to make sure that like within this command. These things propagated. But I like, that's
only as good as you know it's not. It's not the final solution. So yeah, like, if you could actually like go in and and validate. That'd be great.
I definitely like this. I also realized, you know, when you're doing something like this, one of the benefits that also comes from. This is, if you are using, like the builder image that comes from this, these values persist. So if you ever ran a shell inside this docker image these values would would still exist. You don't have to go back and set them as well. So I think if that's like it actually is way more beneficial like these are just going to be included in every environment that.
**Mike Dame** 24:45 That's cool.
**Tyler Yahn** 24:46 Yeah.
So I think I think this is a great solution as well. So, but yeah, if you can, if you can validate that, I think that'd be great, and I'd be, I'd be excited to go in this direction. So yeah.
**Mike Dame** 24:55 Yeah, I'll give that a test. And I think that Ron will be okay if we go with that approach, too. So.
**Tyler Yahn** 25:01 Cool. All right.
Yeah. And this is kind of the big one. I think that needs to get resolved sooner rather than later. So maybe we talk about it in just a little bit. I wanted to finish this up with, like what we can do for this milestone, but I think this should probably get
prioritized. So if we can get a resolution for this, I'd like to get a release out, I guess, is what I'm saying. So we'll maybe talk about that in a second.
**Mike Dame** 25:23 I'll just leave a comment on the Pr. Right now. So I'm gonna verify this on Mac before we move.
**Tyler Yahn** 25:28 Yeah, perfect.
Thanks.
Okay, cool. So similarly, I think this is another bug that maybe we should try to prioritize getting fixed in this next milestone. I was looking at it just before this meeting. And so one of the things that this is like we've definitely seen a bunch of these things. I thought that we
didn't fail the if if this develop thing existed. But
I don't know. It looks like we still are failing. So I thought, I guess it doesn't really matter what I think it is, what it is. And so this is trying to fix that by fixing this by removing any sort of like version processing. If we detect that the version is this devel thing.
One of the things that I I wanted to
ask, though, is that like it. It does just drop the the module which may not be what we want to do. We may just want to add, like an empty entry.
**Mike Dame** 26:26 Yeah.
So this is another one that we were talking about trying to figure out. The the 1st thing is that we couldn't find a good definitive explanation of When go, adds this devel to it, like exactly when cause, if anything, it would be great if we could log, hey? This module looks like that was built locally, or you're using a local go MoD, replace like some. Those were some of the things that we found that could add it.
So that was one is that we couldn't like. If we can find something I like asking Chat gpt, I was Googling like I couldn't find anything. So that's the main issue with it. And then the second was like, you're saying, do we want to actually drop all of these modules or or not, and part of that reasoning at least for us. And maybe you're thinking of something different
was, if if these develop versions are only happening to like irrelevant packages that aren't being instrumented. And it's just like someone's building something locally with their own project. Or could this develop happen if someone has like a fork of gin or something like, you know, some like probably not doing a fork of like net. Http, but maybe some other packages that they're trying to build with if we could.
you know, do we want to ignore that? At that point my feedback here was not just continue. And that's why we have at a warning log here, as Ron commented, is, you know, if it is one of those relevant modules that we're trying to instrument. Then we would want to have something in the logs that says, Hey, this isn't going to be instrumented because it's a develop package, and it'd be great if we could say it's a develop package because one of these things. But we couldn't do that, I guess.
So yeah, I don't know. What was your thinking about? Keeping just like a nil version here.
**Tyler Yahn** 28:23 Yeah, I
I have to go look a little bit more in the code to find out like how this this map is actually used, I guess. But my idea is that, like, you know, there's this distinction between not having an entry and then having an entry, but it being nil you know, because then you can pass like, exactly like, yeah, you and I are thinking the same thing like, I don't think that he's gonna end up in this case. But similarly, I don't know how these developers are actually showing up. I think it has more to do with vendoring, but I'm not sure where it's coming from.
but yes, so to say, something like gin comes along, and then, like, you know, if we pass this map down the pipeline, and then they can find
some sort of workaround for it. Essentially like there's a difference between saying like, Oh, don't load the probe, because, like that doesn't exist versus like
it does exist. Do you have like a fallback, or like essentially like you handle the error at that point like, that's a way to communicate, saying like, Hey, we don't actually know what version this is like. If you have a way to detect it, go ahead and do that. Otherwise, like.
you know. Let's let's log a warning here and then later on, say, like, maybe there's an error that comes from them. Or maybe there's just like a. They can handle that error, and they don't even have to error like error at that point.
which I think becomes more important as we go through this like separation of like the probe into like that interface right? Because, like, it may be that the probes have a very good way to like handle this. And maybe there's like a way they like. Maybe they don't even need offsets. Essentially right? So like the version doesn't matter. They just know that the modules there, they're like, cool. Well, then, load this probe, and so like having some sort of way to say that it's there rather than say that like.
because, you know, I think it's kind of the best part is like maps have a ternary state, right? You can have like this, like.
you know, not there not detected, but also they could be like there, but empty, or something like that, right.
**Mike Dame** 30:12 No.
**Tyler Yahn** 30:13 So
that was my thought. But like it also could cause nil point dereference panics. Right? So like, that's kind of the other thing is like we have to, I think. Maybe. Look at this a little closer to find out if if this map is just blindly using that version that's returned from this lookup.
and if it is like, then that could be a problem as well. So there's more thought than just.
you know, adding it here without looking. I guess.
**Mike Dame** 30:38 Yeah, I think that's a good point is what is these? I mean, the versions are obviously probably used for the offsets. But besides that.
yeah, could we?
Yeah, I'm not sure what else we would use the if it was nail. Besides, you know, there's we're probably not going to be able to instrument much with something that we don't know the version of, because we're not going to be able to look up the offsets for it.
Unless it has the the build info compiled into it. So there could. This would be totally, basically irrelevant. Then we shouldn't even need to do a version check right if it's
got to build info. So.
**Tyler Yahn** 31:15 Yeah, yeah, I mean, yeah, that's a good point. Like, I
like, I, I guess, like, hmm.
like, yeah, when would there ever be like a U probe where I don't know. Maybe there's like those control U probes as well.
So so that's I guess maybe what I'm thinking about is like.
so you have some like centralized. I don't know https handler for for the you probe to to handle like some sort of. Maybe it wouldn't be a you probe at that point it'd be like a K probe, and you'd only want to load it once. So you just want to know if hey? Does net Http exist in this process? Because then I just want to like, I know that another probe is going to have an action. I actually don't care what version of nethtp it would be, or gin, or whatever it is right like. I just care that if it exists is what I was kind of thinking.
But you know, we don't see that currently, I guess, is is also the other thing, like maybe we could add that when we do see it.
**Mike Dame** 32:13 Yeah. And now well, that sounds kind of like something that we at least we're talking before about not doing so much, since we wanted to scope this to just observability probes.
but I I think that that could be. I feel like I think it'd be cool to load other types of probes, anyway. And you know we have like in the the SDK you have like a a probe that is just setting that flag. Right? So everybody do other things besides just observability probes. But
yeah, I don't know. What. What do you think we should do about this, or maybe see what Ron thinks for that nil option. If we set nil here is definitely gonna be a lot more work than just right now where it's
like a skip or it's just an error right now. But so we could just start with this and maybe make that like a you know, future request to improve and say, Hey, here's why we could maybe do a nil app just to fix this bug for now.
**Tyler Yahn** 33:23 Yeah, I mean.
I'm fine. Like, I mean, we could just iterate like, I mean, we could. We could merge this as is, I could make another Pr. To add the log message as well, and then I can make another Pr. To add the the nil as well like that that seems fine. Like, if we just want to break each one of these suggestions apart like, that, seems fair.
Yeah, yeah, I'm fine with that. That sounds good.
**Mike Dame** 33:49 Yeah, I mean, I think I think that you know. Pr, just for the log message is probably not. We could throw that in here, you know, unless you don't want to wait for Ron, and then we could merge this. You can just add the log message in yours, or whatever. But I think that you know, changing this like the semantics of this to using that no version that could probably be its own change, because that's gonna probably touch a lot of other files to where you'll have to do a mail check, I imagine. So.
**Tyler Yahn** 34:17 Yeah.
So I think, yeah, maybe that's that sounds good. I want to get this in the next release. This is kind of like a bug that's been.
**Mike Dame** 34:36 M.
**Tyler Yahn** 34:36 It's got a lot of issues associated with it, which is weird because I still don't know how this exists.
and yeah, I haven't had one person. Show us how to reproduce it. But that's just because it's all proprietary things. But
but yeah, so I think, like to get this out in the next release, because that okay? So maybe we can talk a little bit about that. I think you said Ron's coming back not next week, but the week after.
**Mike Dame** 34:59 Yeah.
**Tyler Yahn** 35:00 Yeah, I I was hoping to get a release out. Probably before that, I guess, is my goal, just because there's like some bugs that are one is, it doesn't work on Amd. 64 machine architecture like or arm architecture, I guess. So that's that's a that's a pretty big one. I think we should try to prioritize that. And I think this is another one. We can get resolved if we get a log message, or or even just merges as is
But yeah, I think if we split this office to like, maybe something that doesn't have to get resolved before Ron gets back. That seems fair.
**Mike Dame** 35:35 Yeah, I think. Yeah, maybe
I would really like to have a log message here instead of just the continue. You know, since it's like active
something, and so let's we can merge this, and I can open up another Pr, or since this is small, I know I just said, I don't like people pushing the branches, but we could. We could push a log message to his branch, and I'm sure that he's not, gonna you know, complain about that? So yeah, let's just add this log message to this. Pr, we can merge it. And then you're we can change the functionality to that new version. In your Pr.
**Tyler Yahn** 36:13 Yeah. Sounds good. Did you want to take on the task of updating this? And I'm happy to review once you push something to it.
**Mike Dame** 36:20 Yeah, I'll I'll push the the log message to that.
**Tyler Yahn** 36:23 Yeah, okay, sounds good.
Okay.
cool. Almost through this. So set bill guards to environment variables. We already just talked about and then the last one is just a bookkeeping one that I just mean to merge once all the other things get updated. But there was a update to the offsets, and this just adds, change, log and compatibility. Info for it. So
you're welcome to review it. Please do. If
you know more eyes in case I made a mistake. But it's just documentation. So it's not
not code changes here. Okay.
so with that, the only other thing I had on the agenda was to talk about this next release, which we kind of just talked about.
And so I want to just maybe go through this
and see what's going on. So I definitely want to get this develop version in add distro version and and name by default to the
D to the Hotel
SDK handler. I think this is great, and I think we should try to get this in. I can push up another Pr
to try to adjust this, to make this work with multimod as well. So I'm happy. Keeping this in. My goal is to get a release out the end of this week. So I think this is, I think this is achievable is kind of the thing here.
This is, I think, ready to merge. I don't think that's too much of a question. The docker build args to environment variables, I think, also can merge. Once, Mike, you've done some validation on this, I think. Keeping it here is is good.
I think, probably moving this to the next milestone makes sense, because I don't think this is gonna get done in this week.
**Mike Dame** 37:58 Yeah, since we just got those bigger bugs to do. But
yeah, I'd I'd like to wrap that up at some point.
**Tyler Yahn** 38:07 Yeah, agreed.
well, cool. I'll update that
similar here. I don't know if
client gpsy trace id mixup. So these are 2 things that I think Nicola was going to take a look at, and I don't think that these are have active work going on, so I think these might also get bumped to the next release.
I definitely think that, like prioritizing these, I think, is more important than these longstanding issues here.
something from 2023. Still. So yeah, okay, there we go. It works.
I'll move these to the subsequent as well.
But yeah, so I think I think shooting at these as a goal is kind of the idea, and then hopefully, getting a release really set this week would be great. So yeah, any other Prs that are missing or issues that we are trying to maybe get some bug fixes out
don't know why that didn't update. But okay,
what do people think about the 1, 23 being the version, do we want 1, 22.1, and just make this a patch release.
**Mike Dame** 39:29 Yeah, I think that makes sense.
**Tyler Yahn** 39:32 Yeah, let me edit this
cool.
If that's the case, then I will make subsequent v, 23, just v, 0 23.
Okay, cool any other. I guess we didn't look too much through the issues.
yeah, maybe I'll take a look and see if there's any quick bugs as well that we can include here. I don't know about this one.
April 24.th So maybe this is a long standing one.
Yeah. Oh, right, this is.
This is very
oh, God!
alright, yeah, I'm not exactly sure what's going on here, but I don't know if this gonna include okay.
That looks good. So, Raphael, you wanted to talk about a few things the way Microsoft retina deals with binaries.
**Rafael Roquetto** 41:04 Yeah. So Microsoft Retina does
have Ebpf binaries as well. So I hadn't previously looked in the past. How they did it, but you know we it's still an ongoing problem for us, you know, with Bela ob it's a never ending thing
so I I took a fresher look at into it, and just for the record, then it does.
but if I understood correctly, have it has 2 approaches, one, it will kind of build the at a point it will build the C files into object files at Runtime. I don't know if that's actually part of the retainer runtime itself or part of the Ci, but it's in their in their code, like they actually, there is a a plugin compile, that kind of loads. The plugin compiles the plugin, which basically means invoking plank
and compiling it. I don't think that applies to us, and neither do we want to do that. But the other thing they do
is for the whole vendoring thing is that when they viewed
their releases or when they're building, you know their you push a Pr or something in their Ci. They do build the object files in the Ci, but they truncate it to 0. So what gets committed
is a a 0, a 0 size and empty dot, O file. And then when you clone retina and you build it, it obviously overwrites that the explanation they have for that I was going through their prs. Is that so that if you vendor retina.
your your vendor modules will bring the dot all files. But if you want to use that
you, you still have a generate intermediate, generate step that you do go generate that will go and rewrite those object files in their vendor directory. So that means your project. If you're vendoring retina, I take this with a grain of salt. But if you're rendering retina, it means that you you need to vendor like, Go MoD vendor. So you have the vendor directory inside your your tree, your source tree, and then it ends up rewriting the dot all files there. So
my conclusion with all of these going back and forth with all these different approaches, I mean, there's to the proxy approach that I have. We haven't looked into it, I guess, anymore. The workspace. We talked a little bit again. I guess it wasn't the ebpfishment last week that Mike talked a little bit about it as well. But it's if I'm my understanding, you might correct me. It's more like developer, friendly, not really distribution friendly.
So I'm more and more convinced that
there is no, you know, no really good solution. Either you commit the binary files or you are okay. We rewriting and imposing
that into your like downstream. Your object files in in a vendor directory. It gets even worse if you're not using like go MoD vendor. But you're just relying on the package cache, or whatever. I honestly think that
I don't know but it might be. I'm not saying it's impossible. I cannot think of another way around these. I'm kind of going, starting, chasing my own tail at this stage.
**Tyler Yahn** 44:27 So how does how do? Okay, that's interesting. So I like the idea that they have like these 0 link files that they actually include in the get history that that kind of solves like the the git commit explosion that you could, you could see
but so like if I do like, go MoD, get like or not, go, MoD, just go get of like the one of these
modules.
How so? How does that work like I still have to run, go, generate within like whatever's downloaded. So I have to go into my package like Module directory.
**Rafael Roquetto** 45:01 Yes, it. Basically, you need to do, go generate vendor detail.com Microsoft retina whatever, and then it will do its thing and place the output the artifacts in in, you know, override those dot all files. Basically, that's how
it works. So you're you're literally rewriting.
Oh, you're you know your Directory so.
**Tyler Yahn** 45:25 So what happens if you like, if because otherwise, if you just try to like import it and then
run it. It'll like fail at Runtime. It'll just.
**Rafael Roquetto** 45:35 Runtime we had. We had similar problem when we were using tlfs for Beta and
someone tried to build Bayla, but they didn't have detailed installed. So it just pulled the the almost empty file. And what happens is like the the Epf loader will say, invited or something and fails. So that's what happened.
**Tyler Yahn** 45:56 Yeah.
is there a way to like, have it on startup like when it tries to run, give a descriptive message
like because, like you could. You could. You could detect if these files are empty, right? And then you could just, you know, output a message. The question is just like
in the loading chain like, is that possible? Because, like these are embedded? Okay, yeah, because, like, that might.
**Rafael Roquetto** 46:20 Because.
**Tyler Yahn** 46:21 Yeah.
**Rafael Roquetto** 46:22 Sorry go just because, you know, like they get embedded as like bytes, and you just check the whatever the length.
**Tyler Yahn** 46:29 On, the.
**Rafael Roquetto** 46:30 And okay, the embedded fade or something. I think that would be easy to do.
**Tyler Yahn** 46:34 Yeah. And then so then, before you pass that somewhere, right? Or you start to use it, or you try to like, make a call that would use it like you could check that and then say, like, Oh, actually, this isn't there? So you could provide a descriptive message instead of just, you know, like
it really stink if if you don't have these, and then it fails, and it's just like invalid binary length, or something like that, or invalid instruction, because then, like, the user has no idea what's going on. But if you can give a message that's like
this, probe wasn't loaded because, literally like you haven't generated this. Go, run these commands really quick. It would be, I think, be a little bit easier story. You know. Yeah, it wouldn't. It wouldn't be great. It like, obviously it'd be great if it just worked. But
I think this is a better story than than what we currently have. Right.
**Rafael Roquetto** 47:21 Yeah, just.
**Tyler Yahn** 47:22 Doesn't compile like. That's another thing.
**Rafael Roquetto** 47:25 So, yeah, no, I agree. I agree, so speaking as myself, only because this is not a consensus in like inside the Beta team, for instance, with the issue we have with Rafana alloy that vendors Bella and Ob, and all of these like.
I can think of at least 3
3 alternatives, each with their own trade offs. One
was really coming in the object files.
That's the E, the the easiest one. But the trade off is like you, you blow your repo. Yeah. Everything that we know
do is be okay with what retina does, which is pretty much what Beta Gen. File does as well at the end of the rewriting, and I think, I don't.
Audio is the same right Mike, like there's some somewhere else. There's some make file that finds the was it articles or different project? I don't remember.
**Mike Dame** 48:22 Yeah, that's what we do is we have a make file that updates the your local go MoD cache.
**Rafael Roquetto** 48:28 Yeah.
And so there's that. And then, for instance.
then you have to you. You will have this intermediate generate stack in this in this case
and the other thing, which probably doesn't apply at all for open telemetry, but just for the record
flow to the idea of embedded embedding Baylor inside the Loy as a
a a binary blob. So basically it is, you know.
that has the benefit that there's no like conflicting dependencies. No source. But you need to spawn at, you know. Process the good part of that is.
you know.
because all this is a bigger thing and Bailey requires proof like permissions. You could have fine grain permissions for the process and whatnot. But
yeah, it has a lot of downsides, too. So that's out of question. I can't think of anything else at this stage.
Maybe the proxy stuff is still worth pursuing, but.
**Tyler Yahn** 49:28 That's the I think the
so. We'd always kind of wanted to split this up into like a long term and a short term solution.
And I think
I am interested to know, though also like so the git Lfs stuff. I wonder if we could also do this the same way
like you know, like truncating and committing directly into the history is one thing.
If you could have like get Lfs set up where you know, I guess, like that could also work. The key thing is is that like, you need some sort of like way to communicate clearly to the user steps they can take during runtime failures. I guess the key right? So like, like, right now, it just is fails to compile, which
we can't like. There's no way to provide user messages once it compiles like failures. Right? Like, there's just that's that's a problem. I think if we look at like as a short term solution, either using this retina approach or using get Lfs. I don't know if the get Lfs could actually work as well like I don't know if you can say like, Oh, also detect this file or this embedded file exists or not. I don't. I may just fail to start, I think, is the problem.
**Rafael Roquetto** 50:31 I think I think it it can, because, you know, all we need to do is like, and we could even try to do it compile time where, instead of runtime, we can do both where you know, we, we basically need to check if the file is any file, any is Bpf, which is its own like
targets inside the file. I'm pretty sure there are ways to do that at compile time like we, we need to obviously
the
part of the generate step or something. There's gonna be something that we'll look at the files like, find out the old files, and check if they are same.
and then we can figure the compile time. But we could also add, like, I think Runtime is really easy to do like we we basically.
**Tyler Yahn** 51:18 Yeah, I.
**Rafael Roquetto** 51:18 Check the file. Yeah.
**Tyler Yahn** 51:20 I think the runtime is gonna be the way you're gonna have to do it, because, like I, there's not a guarantee that somebody's gonna run a generate step prior to running. Go build, I think, is is the hard part. Right? So like.
yeah.
unless unless you can use like standard go tooling for go build and like, have some sort of like hook there like, I don't know if we can get around that like
So yeah, I think I think if you can do it during the runtime with Git lfs, or you can do it with just this this truncation approach, like, I think if that's a great intermediate step, or even a long term, step right? Like.
I think this gets us off the ground. It gets users some sort of explanation that's like, Yeah, this isn't great. But like this isn't common, that you're importing this. It's also like, here are the steps that you need to do. And you can be very descriptive, too, because you can find out exactly where their go. MoD Path is pointing to. You can say, like, you know, here's literally like, copy this command. It's going to be like a CD go generate. And then, like, you know, it should should run. I guess.
Yeah, they need to download dependencies, but I don't know like, and you could. You could even do it in a docker file like I guess I don't know what I'm saying, I guess, is just like you can provide more useful information other than like
failed to compile. Because this file's missing, you know, like, that's that's a really bad story. Currently.
**Rafael Roquetto** 52:31 Yeah. The only thing with Guitel Fs, I mean to give it another shot eventually. Is that I really couldn't get. Go the go like, go get to to fetch the files, so I don't know it. It would be great if Go get would, but then, I guess, would solve our problem right if go get would just understand. You tell us, and actually pull and
put the files every time I read about it. They hinted that it works, but it never got it to work. I don't know if you guys have any experience with that.
**Tyler Yahn** 53:02 I don't, either. I I've heard other people's experience that you had to configure. Go to use it correctly. It doesn't come out of the box. Using it correctly was what I heard. But I don't know.
I mean, I yeah, like, so what was the user experience? Like, I'm guessing the user experience was a compilation failure, though, with git lfs, though right like you go and you don't have git Lfs. Pull down these object files, and it just tried to compile, and there wasn't a file there. So it failed. The compilation.
**Rafael Roquetto** 53:32 Though it actually works, because the way it works with detail Fs is actually similar to what retina does. It does commit a dot file that is just like it has a hash. It's a text file that has a hash, a reference to the into the actual file upstream. And then. So it's the same case, both faster retina. Our solution would be the same when loading the file.
The that has been embedded we have to check if it's embedded L file or otherwise display a user friendly message.
**Tyler Yahn** 54:02 I mean, honestly like, I think I'd rather use get Lfs because it sounds like retina is just recreating. Get Lfs so like. If if that could work like and we could provide. You know, then that sounds great, right? Because there's like this empty file there, and you can detect it prior to actually failing and saying like, Oh, shoot like, actually, you're missing a step here. Either go configure, go to use, get Lfs. If we could figure that out, or literally, just go to this directory
using Git Lfs run these commands, or something like that, like, I think that's a totally valid story for the short term at least, or maybe even the longer term.
Yeah, because, like, I think, if we yeah, I agree, I think that that we should. We should pursue that, like I would be in favor of of using. Get Lfs and providing descriptive understanding of like when the failure comes.
That makes a lot of sense to me. How does get Lfs handle like instruction sets, though. So like, if I needed to download it for Amd 64 versus arm architectures.
**Rafael Roquetto** 55:01 It doesn't. So the way we work is like as it would work exactly as if you were committing the files directly, so you would have 2
2 files for me to like underscore arms.
**Tyler Yahn** 55:12 Oh, oh, and so, okay.
okay, so you would, just both would be side by side. And you'd download both. Yeah, okay, okay.
yeah. I mean, I'm definitely in favor of that. If we can get it to work, you know, and if there's nuances, then we could try to pivot to the retina approach right like, say, get Lfs like the commands are impossible or something like that.
But I think if that's that's a great, I think that's a great solution, because, like one, it can get ripped out right like it's not like
like, if somebody's doing this, and then in the future we're like, Oh, look!
This proxy thing actually was a great solution. We're finally willing to like, operate this proxy. We're going to work for all these other use cases people can still run the git Lfs commands through some sort of workflow. It wouldn't fail right? It just wouldn't do anything. And then it would just like, you know, it wouldn't be a problem at that point. And then, you know, they could slowly evolve from that. And it could just be easier.
But yeah, like, if if we never move to the proxy, this could also work just in the long term.
**Rafael Roquetto** 56:12 Yeah, okay, okay, I'll give it a go again. No pun intended. Yeah. I.
So a lot of things.
**Tyler Yahn** 56:22 I agree. So I'm excited. I think if that sounds great, I'm happy to. Yeah, we we're gonna have to update workflows. But I think that that's a fair price to pay to resolve this issue.
**Rafael Roquetto** 56:31 Yeah.
**Tyler Yahn** 56:34 Cool. I see you also wanted to talk about C formatting, which kind of reminds me you were talking about. Yep.
**Rafael Roquetto** 56:39 I just happened to see like when you're scrolling in the issues. I saw it there said, Okay, yesterday, you know, today is already. I don't even know today is, Oh, Tuesday, okay. Yesterday I joined the C plus plus
for the 1st time.
and I realize they do. Have they rely a lot of cling, tiding claim format. So I haven't really looked in deep into into their report. Didn't have the time, but I just wanted to point out that maybe maybe maybe it's not doesn't apply to us. But maybe it might be something to look into. And and can something from there, because they might have already, like Pre pre baked config files we could reuse just
Yeah, it was just a thought that I thought I would share.
**Tyler Yahn** 57:25 Yeah, that sounds great.
that's a good point. Yeah. I mean, it definitely be nice to have a consistency across a hotel.
yeah, I mean, I guess if you're a C developer, the whole point is to be inconsistent across a group. So
but yeah, okay, yeah, that I didn't realize they were doing that. That'd be maybe just something we can copy, too. So that'd be great.
Well, cool. We are running up towards the end of the hour here, so I can stop sharing my screen any other last comments before we end the meeting.
Awesome? Well, yeah, it's good seeing you all a lot of stuff going on a lot of stuff to do. So a lot of great work. Yeah, I appreciate everyone for joining thanks, all for coming in and talking, and we can adhere.
I'll see you all in a week's time, or asynchronously.
**Rafael Roquetto** 58:22 Yeah. Welcome. Back.
