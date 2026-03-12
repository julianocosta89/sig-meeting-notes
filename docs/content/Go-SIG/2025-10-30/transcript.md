SIG: Go SIG
Date: 2025-10-30
Duration: 55 minutes
Zoom Recording URL: https://zoom.us/rec/share/5-ajlqs4ACU1mpzKAmxdzl-520rAyFE6R9DVw_yZaXz9-8R1pYBMvteDmoKJXMIx._eJecUF95UyQjlWh
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:54 Hey, Brian.
**Bryan Boreham** 00:55 Bye.
I agree.
**Tyler Yahn** 00:58 Doing well, how are you?
**Bryan Boreham** 01:01 Yeah, I'm okay.
I'm vibe coding.
**Tyler Yahn** 01:10 So, as good as you can be doing that.
**Damien Mathieu** 01:13 Hey, good afternoon.
**Tyler Yahn** 01:16 Hey.
**Pellared** 01:20 Hello.
Can you hear me?
**Tyler Yahn** 01:22 Hey!
Yeah, I hear ya.
**Pellared** 01:25 Awesome.
Nice t-shirt, Damien.
**Tyler Yahn** 01:34 Yeah, I was just about to say.
**Pellared** 01:36 Damien's from the future.
**Damien Mathieu** 01:38 Thanks.
**Tyler Yahn** 01:41 Although, at this point, I don't know if, it's the future.
**Damien Mathieu** 01:44 I think…
**Tyler Yahn** 01:44 Alright.
**Damien Mathieu** 01:45 Yeah, it's not supposed to be a feature.
**Tyler Yahn** 01:48 Yeah, it's like the present at this point, yeah.
Yeah.
Cool. Alright, it looks like we have, people on the call, so if you haven't yet, please go ahead and add your name to the attendees list. If you have agenda items to talk about, please go ahead… And add them as well, and I'll start sharing my screen here, and we can, jump in.
Okay, cool, so… Oh, excuse me. Start us off.
david, you wanted to talk about monitoring bugs reported by the OSS, fuzz tooling?
**David Ashpole (dashpole)** 02:37 Yeah, yeah, so this came back to us, after we, brought it up to the GC, it seems like It's basically just something that… we're in charge of, or maybe… I think maybe Robert is the only one who has access right now, possibly?
But we should…
**Pellared** 02:56 compass.
**David Ashpole (dashpole)** 02:59 I think it would be awesome to have these filed as bugs in our component, and it sounds like there's an option to do that, so if there are no… objections, I'd love to turn that on, and then we can, you know.
deal with them using our usual processes. Like, they look… potentially useful, potentially related to the OTelconfig stuff.
At least the contrib ones.
But… I'm inclined to turn it on, and then if they turn out to all be useful, we can revisit that. But seems like it would be helpful to have these all as… as, issues on our repo.
**Tyler Yahn** 03:40 Yeah, I would appreciate it if there are issues on the repo. It's really hard to, like.
**Pellared** 03:44 So, is, is the.
**Tyler Yahn** 03:45 behind these.
**Pellared** 03:46 Sure.
is the feature already there, so it can be… so they can create issues in our repo? Because I remember that someone was saying that this has been not implemented yet, or you just want me to copy-paste it.
**David Ashpole (dashpole)** 03:59 Oh, I assumed that Trask… there's a file GitHub issue true thing that was pasted above. I assume that if we did that, it would just work.
But if it doesn't work, then… I guess we should copy our own issues over if we want.
**Pellared** 04:17 Yeah, we can try, but probably I'll need to recreate the issues for the old ones.
**Tyler Yahn** 04:25 Well, is this, like, is it, like… some sort of CIA system that's reporting this, right?
**Pellared** 04:31 Yes.
**David Ashpole (dashpole)** 04:32 Yep.
**Tyler Yahn** 04:33 And then, do you remember the job?
That's doing this, Robert?
**Pellared** 04:42 It's not in our repo, it's in the Google CI.
**Tyler Yahn** 04:46 Well, okay, so where's this thing that Trask is talking about here gonna be set?
**Pellared** 04:53 oils as possible.
**Tyler Yahn** 04:57 Okay.
**David Ashpole (dashpole)** 04:59 OSS funds.
**Pellared** 05:01 I have a question, so, regarding this primary contact, because I think I have access to these kind of details, because I was added there as primary contact, probably.
Or AutoCS, I do not remember which place. Do we want all our maintainer's Google accounts to be copied? Like, to paste their… To put there, or not really?
**Tyler Yahn** 05:27 I'm… Yeah, go ahead, Dan, sorry.
**David Ashpole (dashpole)** 05:31 I was gonna say, if it's filed as a GitHub issue, then I don't care who has access to the, like.
That dashboard, but…
**Pellared** 05:38 Like, the reason is that I'm not sure if… If we want to triage it.
in this… if we want to triage it somehow, I remember to put the comments there, then probably you need to be added there. But I don't think we need to do it now, we can postpone this.
Until we feel that it's necessary. I think we can start just with these GitHub issues first.
**Tyler Yahn** 06:02 I think the GitHub issue sounds good. I also think that the maintainers of the repo should have access to the configurations here, though, so if that means that, like, there's an email list or something like that, that's fine.
I don't know, like, if there's, like, a… like, a group thing we could do? Like, because we have, I think, like, a hotel… like, Go group or something like that in the Google, world. I don't know if, like, that's something we can work on?
Yeah, what I'm saying is, it's like, I'm 100% on board for all of the above, so, yeah.
**Pellared** 06:41 We have some mailing lists on Google.
Hey there?
**Tyler Yahn** 06:45 Well, yeah, I mean, I don't know if there's a Google mailing list for the maintainers specifically. I definitely know there's one for Go, right, because you can sign up for the Go calendar.
And so there's, like, that group.
I don't know if you can, like, use, like, a… yeah, I don't… I don't know.
**Pellared** 07:05 Yeah, I have the same concern, if I can use it for logging in, etc.
**Tyler Yahn** 07:10 Mmm, yeah, maybe not for logging in. I mean, like, there's definitely, like, if we can get something set up for, like, the maintainers, I mean, it'd be really great if you could just use, like, the GitHub team, right?
**Pellared** 07:21 Yep.
**Tyler Yahn** 07:23 I don't know if that works.
But, yeah, I mean, I'm happy to, like, if we wanted to, like, create our… another… email list as well, maybe we can talk to the GC or something like that to do that.
**Bryan Boreham** 07:39 So.
**Pellared** 07:40 Cool.
**Bryan Boreham** 07:41 Sorry.
**Pellared** 07:43 I think that we can also add the OS as fast, if there are any recommendations, how other teams are dealing with this.
**Bryan Boreham** 07:54 I just wanted to mention…
**Pellared** 07:58 Go on, brother.
**Bryan Boreham** 07:59 Is there a raise your hand feature in Zoom? I can't find it.
Anyway, I'll just talk. Coincidentally, we had the exact same conversation a week ago in the Prometheus project, where we went, what is this OSS fuzz thing? Who set it up? Who has access to it? What am I supposed to do about it?
And the upshot of that was that someone said, why don't we just use the built-in fuzzing in Go? Because when the OSS fuzz was set up, there wasn't built-in fuzzing, but there is now, so… I don't want to claim that one is better than the other, but just.
**David Ashpole (dashpole)** 08:37 it seems like it uses the Go fuzz test. Like, I was looking at the Go Getting Started.
**Pellared** 08:46 Which is correct.
**David Ashpole (dashpole)** 08:47 setting up a GoPro… Here. I don't know where.
**Pellared** 08:50 Like, the reason… the reason we are using it is that it's basically run continuously.
So, if you have some fuzzing run, for example, in GitHub, I think there's, you know, you can run it just for a couple of hours, or something like that. And OS fuzz, as far as I understood, works continuously in the background. You have a, you know, continuous job that runs the fuzzing.
**Tyler Yahn** 09:35 Yeah, I mean, I'm not opposed to keeping the Google, Version of it, as long as it can provide the… Access and, notifications appropriately.
I do think, though, like, if there are limitations where, like, it has to be through this one thing and it's only gonna go through you, Robert.
We may want to rethink this, but… Yeah.
**David Ashpole (dashpole)** 09:56 I did also find in the documentation, so you can't have it file GitHub issues, it says it just doesn't do that by default.
Because… Fuzz results are sometimes considered, like, security vulnerabilities.
So… It, like, it's… If we don't want that information public, then we obviously shouldn't turn on public issue filing, but…
**Tyler Yahn** 10:17 Is there a way, like, once it's been verified, to open an issue for it?
**David Ashpole (dashpole)** 10:23 I think there's just a single… Boolean for issue or no issue.
**Tyler Yahn** 10:30 Yeah, alright.
Yeah, I mean, I mean, that's a good point.
I mean… Robert, are you paying attention to these errors at all?
**Pellared** 10:52 Not, but I can start. But I will be… I think it doesn't… I think it's a bus factor, one, it's not good.
**Tyler Yahn** 11:00 Yeah, I'm more just looking for, like, just… just a one-off.
question of, like, the security impact that these are gonna have, like, have you noticed.
**David Ashpole (dashpole)** 11:10 Any sort of, like…
**Tyler Yahn** 11:12 Things that we wouldn't want to be publishing, in the start.
**Pellared** 11:17 So far, as far as I remember, when I was looking, recently I have not looked, there were basically problems with the YAM library itself.
So, basically, it was finding vulnerabilities, but these were, like, panicked because of proper unmatched learning code of the YAML code library.
**Tyler Yahn** 11:37 Hmm.
**Pellared** 11:39 Yeah, I'm gonna be one.
**Tyler Yahn** 11:41 Yeah, that's a tough one.
**Pellared** 11:44 It doesn't mean that in future, it will not find something, you know, harmful for us.
Some unpopular custom unmarshalling and stuff like that.
**Tyler Yahn** 11:54 Okay.
Well, I mean, should we just look into setting up an email list, first, and just start from there?
And maybe just go for a few months of trying to check this out, and like, if… I mean, like, if I'm getting emails, I can, I can do some filtering and try to pay attention to it, but, like, we can also say, like, in 3 months, like, no one's paying attention to it, these things are piling up and they're not actually getting addressed, like, we can maybe then look at the GitHub issue?
**David Ashpole (dashpole)** 12:21 Okay.
**Pellared** 12:22 Just like he was done.
**Tyler Yahn** 12:24 Okay.
So, Robert, are you going to be able to follow up with the GC on getting an email list set up, or is that something you need help on?
**Pellared** 12:31 I can work on it.
Or, David, you want to work on it, or you want me to work on it?
I mean, if you can do it, that would be awesome.
Okay, I can start. If I look at problems, I would just ask for help.
**Tyler Yahn** 12:48 Okay.
Cool.
Let me start sharing again, we go back to the… Agenda… Cool, alright. So, next up…
**David Ashpole (dashpole)** 13:04 There was a…
**Tyler Yahn** 13:05 conversation around stabilization of hotel gRPC, and there's a request from the community about this.
From this user… GitHub's not telling me their name. So Nicholas, I don't know if Nicholas is on the call.
I don't see Nicholas on the call. But yeah, so the idea was that, like, they would like to have this stabilized. I think, yeah, one of the things that… David pointed out that I was thinking as well is, like, you can't really stabilize this without, like, stabilization of the semantic conventions that are underpinning, the metrics or the traces that are being generated here, so… That's definitely a blocker. There's definitely a time consideration that's a blocker as well that I thought of, but I was just wondering what people's ideas and thoughts on maybe prioritizing this in the next year.
Or if they have opposition to this.
I'm interested to hear what you think, David, as well as being one of the, owners of the package.
**David Ashpole (dashpole)** 14:10 Yeah.
**Damien Mathieu** 14:10 I think.
**David Ashpole (dashpole)** 14:12 Go for it. Based on the…
**Damien Mathieu** 14:13 person's request to restore the interceptor.
stabilization is also not something that… where we would restore the interceptor, I think. It's not fair anymore. We really don't have any reason to bring it back. If we had been stabilizing before we removed it, we would keep it, obviously.
But it's not because we stabilized that we should bring it back.
**David Ashpole (dashpole)** 14:39 Oh, I…
**Tyler Yahn** 14:40 I agree. I don't… yeah, I don't think there's any opposition to what you just said.
Yeah, I agree. I don't think at that…
**David Ashpole (dashpole)** 14:49 Needs to come back.
**Tyler Yahn** 14:50 I think it's more about, like, whether, we plan to keep the API stable going forward, is kind of the question.
Which, to be clear, like, I think that there's a few blockers there, one of which is that we need the underlying semantic conventions to stabilize, but two is also, like, an audit of the API itself, because, like, there's probably other cruft here that maybe we want to change, and so, like, I don't think it, like, saying that we would just go with what's there today is the plan.
That's why I think it's gonna take more than just, you know, a week or two to get this done, and I don't think that that prioritized, like, time is gonna happen within this year's timeframe. So, that was my thought on that.
So I do know that, like, the Semantic Convention Group is working to stabilize the RPC Convention, so I do know that that is happening, but I also… you know, understand that, like, there's a SIG dedicated to it, so… Oh, yeah, okay.
**David Ashpole (dashpole)** 15:39 I mean…
**Tyler Yahn** 15:39 I mean, I don't join the SIG, so maybe not, I don't know. I guess we can go look at the, the notes from the SIG, but yeah, like, I know that there is, like, a group dedicated to working on this.
I guess maybe it is an overstatement to say that they're making progress. But yeah, so I don't know there.
I know it's not like… something that has nobody looking at it, I guess, is the difference. So… Yeah, I think there's some… idea of, like, a timeframe there, maybe we can check in there. I think it's also more just a question of, like.
Who would take this on? And do they have enough time to do this in… you know, a time frame. And it could be in a year, it could be in 2 years, I don't know, like, it's up to that person.
**David Ashpole (dashpole)** 16:24 I have no problems taking on the stability of the module. I am not… interest… or I'm not able to drive, like, the SEMCON stability aspect of it.
Right. So that's, like, And… Yeah… GRPC has been… A little bit tricky to work with, because they've kind of just gone and done their own thing, for the most part.
They've engaged in… At some points in the past, and… Then have not.
followed up very well, so I'm… I'm a little bit pessimistic, but that's not to say that it won't happen, but I think once the ball's in our court.
And there are stable conventions.
I 100% will drive.
The stability of the module forward.
But until that point, I'm… I'm not gonna hold my breath.
But… Robert?
**Pellared** 17:23 I think Josh Surrett was considering talking with the gRPC team, but probably… maybe you know already more than I. So, yeah.
Okay, that's all.
**David Ashpole (dashpole)** 17:39 We are in contact with them, but they seem… Mostly driven by their own internal roadmap, and not…
**Pellared** 17:46 Yeah.
**David Ashpole (dashpole)** 17:47 Not, like, focused on… Creating an open standard for their own instrumentation.
**Tyler Yahn** 17:56 Sorry, so do you mean the semantic convention group, or the gRPC team in Google?
**David Ashpole (dashpole)** 18:02 The, the G… well… I mean, the elephant in the room is that like, RPC… is mostly dominated by gRPC, so having an RPC convention that gRPC doesn't participate in Is a little bit moot.
**Tyler Yahn** 18:19 Yeah.
**David Ashpole (dashpole)** 18:20 But… Also, it's kind of on… gRPC… to be engaged as well. And, like… Unless they show up to the table.
You know, it's kind of been up to them, and they haven't… they have participated at some points in the past, but… Not as much as I certainly would have hoped.
And, the pace of their development hasn't been, like… as much based on what OpenTeometry would like of them.
It's mostly been based on when they, have product launches or other things where they need the telemetry, and I've decided to add it.
**Tyler Yahn** 19:00 Hmm. Okay.
I see, Robert, maybe you also added this? Is this also related?
**Pellared** 19:11 Yeah, it's related, and I created it prior, I'm not sure which… I think it was before CapeCon London, and I remember with Damien, we were also talking with the people who were kind of implementing it, and it was, yeah, yeah, we know that we are different, we will talk, we'll return to you, but they never returned. So, yeah.
That's basically what David told me, that they modeled it in the way they found it is good for them internally.
In Google.
**Tyler Yahn** 19:50 Okay, so how does this have anything to do with, like, the hotel gRPC package? Does it use this?
**Pellared** 19:56 No, it's not. But preferably, I would prefer that, you know, the thing that they are doing is following auto-symatic conventions, and we do not even need to have our own auto GRPC.
module package.
**Tyler Yahn** 20:13 Okay, so are we planning to then dedicate resources to, like, working on that in gRPC?
**Pellared** 20:23 they are not willing, so far, to follow the semantic conventions, that's what I've heard so far.
**Tyler Yahn** 20:32 I mean, okay, so… That doesn't sound like something we can count on, then. Like, that strategy of, like, not having something for hotel gRPC like… Yeah, like, getting rid of OTL gRPC and using the OpenTelemetry package that they have in gRPC does not sound like a viable option if they're not going to comply with semantic conventions.
So, I think then the question becomes, like, do we want to provide a telemetry package for gRPC, and do we want to own it, or do we not? Like, I think that's a fair question. Like, in other… you know, instrumentation packages like we've done in the past, like, if we don't want to maintain something, that's fine. The community can come up with their own. Like, that's how we can also do this.
**David Ashpole (dashpole)** 21:19 I mean… from my perspective, I'm perfectly happy to own and maintain the existing one. Like, we have a lot of users, and… Okay. We should try not to break them, but… They're just… yeah.
I agree that you're asking the right question. I feel… yeah, it's like the question that Josh and others Have been asking for a while, and, like, maybe the time has come to, like.
Put more pressure on, and make a decision, and either get them to come to the table, or… to have OTEL have their own conventions, but… Huh.
**Pellared** 21:56 I think the last thing is, I'm not sure if I'm correct, but this co-opensions created by the gRPC team, I think they're experimental, but maybe I'm wrong. I'm not sure if they said anywhere that they are stable. I think they're still, like, in development or something like that, yeah? Am I correct?
**David Ashpole (dashpole)** 22:12 I…
**Pellared** 22:12 is still.
**Tyler Yahn** 22:18 You mean this package here?
**Pellared** 22:20 I mean, not only this package, but I mean, this package is, you know, yeah, it's also… It's also…
**David Ashpole (dashpole)** 22:27 Give me a bug release.
**Tyler Yahn** 22:29 Yeah. Doesn't that? Yeah.
**Pellared** 22:31 Also, the specification of gRPC, I think, is also unstable.
**Tyler Yahn** 22:36 the specification of, like, the RPC, like, itself?
**David Ashpole (dashpole)** 22:41 He has his own proposal process and stuff.
**Pellared** 22:44 Yep.
**Tyler Yahn** 22:44 Yeah, I mean, it's, it's a… it's kind of like a classic example of, like, how to not do versioning, right? Like, it's really problematic for a lot of people in that sense.
So, like, is what your point being that, like, because of that stability guarantee that they… gRPC provides, it's gonna be tough for us to instrument it, is what you're saying?
With the stable package?
**David Ashpole (dashpole)** 23:11 No, that… so, sorry.
There's nothing stopping OpenTelemetry from saying, here are the RPC metric names, they're stable.
Go make stable instrumentation libraries in all languages.
In theory, the OpenTelemetry project has always wanted native instrumentation.
**Tyler Yahn** 23:32 Yeah. And so…
**David Ashpole (dashpole)** 23:33 In theory, we would love if… gRPC and other… Like… similar projects.
Defined semantic conventions, and then followed them in their application code, right?
**Tyler Yahn** 23:50 Yeah, the problem, though, is like you're saying, like.
If there's no movement, and there's no… not even movement, but there's no desire from the gRPC team to even, like, allocate time to this?
then… then that's… that's not a… that's just hope, right? Like, that's not a real strategy, right? And so… I mean, like, yeah, I think that that's great.
then the question becomes, like, do we want to provide something or not, or do we want the community to provide it? And I think, like, that… it sounded like you were, like, on favor of, like, if we… let's just provide it.
I also think that there's nothing stopping us from saying, like, 5 years down the line, until gRPC is stabilized, it's the way to do it, and gRPC gets attacked together, and they're like, oh, wow, like, this is, this is useful, let's… let's add this to the language natively. There's nothing saying you can't deprecate this package and saying just start using you know, hotel gRPC is no longer something that we are gonna, like, maintain, like, and just say, like, migrate to using the native instrumentation from gRPC at that point, right?
**David Ashpole (dashpole)** 24:54 That's fair, yeah. But… Yeah, that's fair.
**Tyler Yahn** 25:02 I mean, isn't that, like, the classic Google strategy anyways? Like… Alright, shots fired. Anyways, okay, so I think with that said, like, really the only thing that's kind of blocking us is… Is more the semantic convention stabilization here, and auditing our implementation.
And then, you know, the decision of whether or not we want to actually, like.
you know, maybe get confirmation from the GRPC team that that's… that their… the inactivity is what their approach is gonna be.
**David Ashpole (dashpole)** 25:36 At one point, they… had tried to donate. I just need to sync back up with what that working group is doing.
Yeah, they've been on and off.
Like, that I had hope at points in the past.
I'm not sure if there's been movement these days.
**Tyler Yahn** 25:58 Yeah.
I mean, I kind of get it from their point, like, if there aren't semantic conventions that are stable for them to follow.
But I also, like.
would wonder if they would actually be happy if they stabilized the semantic conventions for RPC, and then gRPC is like, we don't want to do this? Like, that doesn't seem like a great approach either, so… Is gRPC gonna be at… like, are representatives from that project gonna be at KubeCon, David?
**David Ashpole (dashpole)** 26:30 Good question, I don't know.
**Tyler Yahn** 26:32 Because it might be worthwhile, like, if we could just have conversations in person to talk about that, darn.
**David Ashpole (dashpole)** 26:40 Yeah.
**Tyler Yahn** 26:40 But… Yeah, I don't know, I don't know, like, if you have contacts in that… on that team, or maybe Josh does or something, I don't know, but…
**David Ashpole (dashpole)** 26:52 I'll circle back with Josh.
**Tyler Yahn** 26:57 Okay.
That being said, I think the response to the stabilization question is not gonna happen anytime soon. We have blockers internal to OTEL, we also need some sort of strategy with gRPC, even if that strategy is to just do our own thing.
So yeah, that's, something that we can keep going on. Probably a goal for next year is to kind of finalize that.
Damien, you also want to talk about the stabilization of OTL HTTP.
**Damien Mathieu** 27:22 Yes, I think it's maybe more consensual. There is this issue, which may or may not be a blocker. It's indeed an issue, but maybe it's something that can be fixed afterwards.
Yeah, I… I wonder if it's not time to do an audit of the Autel HTTP API to start thinking about stabilization.
**Tyler Yahn** 27:50 Yeah, I think that sounds great. I think that we should… open an issue with what the current API is in, like.
**Damien Mathieu** 28:01 Movements.
**Tyler Yahn** 28:01 As passed ask for a review of it or something like that, yeah, I think that that seems reasonable, yeah.
You're one of the, owners of the project, or the package, right?
**Damien Mathieu** 28:11 I think I am the only, code owner. So, yeah, I can't open that issue tomorrow.
**Tyler Yahn** 28:18 Yeah, okay, cool. Let's… yeah, let's do that. Sounds great.
**Damien Mathieu** 28:24 Robert, do you know, the… I know you are the most involved in that issue, V… yeah, 7254.
But… I see that you have also opened an issue in semantic conventions, but I've not looked at it. Do you expect that, We should be able to get something soon.
**Pellared** 28:49 I can work on it, basically. Just maybe assign it to me, so… If that's important.
Someone's worth…
**Damien Mathieu** 28:58 Technically, I'm not sure, it's… actually something that prevents stabilization, because it's a bug. We can have bugs, even stable, things. And anyway, it's going to take a bit of time to review the API, so there's no immediate rush, I think.
**Pellared** 29:18 Like, this will be, you know, this is a behavioral change, depending how we'll mark these errors, if they will be just… if we, you know, add these events, or we just add attributes.
And… yep.
That's basically it.
For me, it's tough, because parts of the specification and semantic conventions feel like suggest different approaches, which I… yeah.
as I was reading it, I need to read it a few times more, and probably make it more clear, and maybe, maybe even, you know, just… create some document or whatever, how I understand it, and share it with you.
**Tyler Yahn** 30:08 Okay, cool. Yeah, I've assigned that to you, Robert. So, yeah, we'll look forward to review of that doc.
Mike, up next, you want to talk about the Hotel Explorer Godox?
**Mike Blum** 30:18 So, Jay DeLuca, my old teammate at Toast, is embarking on a project to basically revamp what is understood today as the hotel registry site, where we post about the various integrations that the various SDKs can do.
And one of the things that is getting worked on is the idea of kind of revamping how we document specifically the instrumentations by the various language SDKs for the different modules, be it, you know, AWS or whatever other instrumentation That we're trying to do, and develop a schema around what the exposed spans and metrics are for each of those instrumentations, so that people who are, like, less familiar with the Go S… for example, the Go SDK, or the other ones, the Java SDK, Of acting as a guideline for what… what those signals are, as they relate to, like, semantic conventions and things.
is, in a nutshell, what this is. What I wanted to run by you all is kind of, like, my approach that I'm working on for the Go SDK and Contrib with the YAML schema I've got in there.
mainly around, like, does this approach make sense? Are we schema-ing the… are we surfacing the correct… Telemetry from the various modules, in terms of, like, which spans… we're going after, and I wanted to bring up, like, do we go into, like, EVPF stuff, like the auto… auto instrumentation? Is that ready to get pulled into this, or do we need to kind of, like, downscope what of the Go Hotel ecosystem that we're documenting here?
**Tyler Yahn** 32:01 So, are these field names, are these, like, key names for the map? Are you defined somewhere else?
**Mike Blum** 32:08 they… The schema as it exists right now is quite in flux. The key maps are… I think the end goal here is a Hugo-style thing where we take this YAML and render it off as a Hugo site or something like that.
What this is mainly driving at right now is, like, the static analysis part of the Go code, of pulling out the various… attributes that we want to emit for the… in this case, the instrumentation. So, like, the Go Contrib stuff further… scrolled further down is probably more relevant here. I took a stab at going after, like, the mainline Go SDK, and I don't think that's… Ultimately, what we… Want to be getting into.
But I just wanted to, like, one, raise that this is a thing that I'm chewing on, is this going in the right direction, and… what are some notes, I guess?
Of where we wanted to go.
**Tyler Yahn** 33:08 Yeah, so… This seems weird.
Like, all the library links are not the libraries themselves so far.
I don't know what that is, the description looks like it's a duplication of our GoDocs, I don't know if that's.
**Mike Blum** 33:25 The way it is, it's… I, like, shoved the analyzer through it, and I think it's just, like, copying that into here.
**Tyler Yahn** 33:31 Okay.
The, The repository's not right for this, right? It'd be the contrib repository.
**Mike Blum** 33:41 So, the contrib ones are further down. This one, actually, I had it run, that's why it's a bit confusing. I probably need a rip out, but there are, like, special go-contrib…
**Tyler Yahn** 33:51 Oh.
**Mike Blum** 33:51 Pull up.
**Tyler Yahn** 33:52 I thought that was… sorry, I misunderstood, yeah, yeah, I gotcha.
**Mike Blum** 33:55 Yeah, I was trying to, like, segment it by, like, so the idea being that as this thing goes through the Go SDKs, there's, like, the one for the auto-instrumentation, the one for the VPF, the… There's a third one.
**Tyler Yahn** 34:05 That it would try to scope them for each repo, these are the different telemetries coming out of that.
**Mike Blum** 34:12 SDK, whether it be the contribib one, or the Core one, or the… EVPF1.
**Tyler Yahn** 34:19 Yeah, I gotcha.
I mean, I like this idea of the telemetry, this is just great. Is this gonna be… this telemetry schema, is it the same that's defined in, like, the semantic conventions repo?
**Mike Blum** 34:31 I think that's what's under… I think this is inspired by SemComf?
I don't know if it is, like.
hard, like, you know, bit-for-bit accurate with the convention at the moment, but I think this is…
**Tyler Yahn** 34:45 I would… I would strongly ask that it would be, so that Weaver can be used on these sort of things.
Yeah, without that, I, like.
I can see a lot of utility in this if Weaver's able to use this. Translating it to something that Weaver could use would be very frustrating.
**Mike Blum** 35:05 Right. Right.
**Tyler Yahn** 35:07 Because I think there's a lot of utility here where you can validate things, and you can do translations, and you can transform things as, like, you know, say this evolves.
Say this target version goes, you know, through a schema translation in a V2 or something like that.
Weaver can already do these, like, translations for you, and it can repopulate old spans, it can repopulate old metrics, or something like that. So the utility of using Weaver here would be very important, for… for that kind of thing, and I think it'd be, like, a misstep if we don't have that… that hard requirement that the telematy schema matches with something that Weaver can parse, yeah.
**Mike Blum** 35:42 Yeah, what is… I've never even heard of Weaver.
**Tyler Yahn** 35:44 Oh.
**Mike Blum** 35:45 Or is that something else?
**Tyler Yahn** 35:47 Yeah, yeah, it's a… I don't know if it's Otel Weaver, or…
**Damien Mathieu** 35:51 It's just Weaver.
**Tyler Yahn** 35:53 Yeah. It's a… it's a REST utility, written around the semantic convention, like, repository, where it parses it, and it can then render into a bunch of other, like, processing on it as well. And so, yeah, easily… Interesting. Yeah. So it does a lot of validation, it does, like, real-time, like.
translations for you as well. It does, yeah, it uses a lot of, like, open source tooling, in this, in this pipeline.
**Mike Blum** 36:18 Cool, yeah, that'll definitely help with the valid, because I think one of the tricky parts of it is, like, validating that the system's even pulling in all of the spans and metrics that we're expecting from each of the, Libraries. So this would be good to…
**Tyler Yahn** 36:31 Yeah, I think there's, like, utility here in just generating those, even. It might be helpful, but, I'd have to… I'd have to dig more on that. But yeah, I think that that's definitely something that I would… I would look for.
Yeah, outside of that, like, if… things like library link could be package link, I'd appreciate it, but maybe this is more, like, for more than just Go, so that I could understand, like, that's not the case. So, yeah, like, I guess it's more… It'd be cool, also, if there was, like, a JSON schema here to tell you what format this needs to be in. I don't know… if this is just, like, through, like, ad hoc convention of what these values are, but, like, a JSON schema would be helpful to validate this as well.
**Mike Blum** 37:16 Yeah, one of the thoughts across my mind is, like, this is approaching, like, an open API spec for, like, the OTEL… spans and things like that. It's almost like, could I build an OpenAPI-style JSON spec that would generate this?
**Tyler Yahn** 37:32 Yeah. OpenAPI is based off of JSON schema, so I might just… Or if you're really cool, you can go check out Q, but I can't get many people to join into that.
**Mike Blum** 37:43 I've been to many queue talks, I've stood by a river in Florence talking to one of the queue maintainers, it's… I've never actually had to use Q, though. I do know of it, though.
**Tyler Yahn** 37:51 It's pretty sweet. It does look cool.
**Mike Blum** 37:53 So…
**Tyler Yahn** 37:54 Nobody seems to want to learn it, though. Yeah. But yeah.
Cool, cool. But yeah, otherwise, I mean, I'm like… That's a lot of feedback I have for you. I think this is more needed than my feedback, like, warrants. Like, if you can get a starting point and just, like, merge something like this, I would be more in favor of that than not doing anything.
**Mike Blum** 38:13 the current structure.
**Tyler Yahn** 38:14 Bad.
**Mike Blum** 38:15 Yeah, I just wanted to make sure, like, is this even going in the right direction? And, like, knowing about things like Weaver, and making sure the schema is set up, because I think what's going to end up happening is, as this project goes forward, there's going to be, like, ecosystem-specific implementations, and I want to make sure, like, that this was covering, at least in part, what the Go… SIG wants to, instrument.
**Tyler Yahn** 38:36 Yeah, I mean, I think it sounds great, It would be kind of cool, also, maybe… Yeah, actually, maybe I didn't think of that as well. Like, one of the things that you can do in YAML, it's not… it's kind of horrible, but you… and in JSON itself, is, like, you can link.
So, like, in this telemetry, like, you could have all these, like, details here in the format that, like, is defined by OpenTelemetry, but you could also just say, like, these conform with the, like, hotel HTTP specs, because, like, that's already defined in the semantic convention repo, and you could just say, like, this is… this produces HTTP conventions, and, like, just link to that… that convention.
Yeah, obviously, like, linking causes issues for locality if you don't have, like, connection to the internet sometimes, but, it's also something that, like, maybe helps make this a lot more concise as well, and maybe worth thinking about.
**Mike Blum** 39:26 I'll definitely bring that up. This is, I think.
part of the interesting thing is that this has been driven by from the Java side, like, the Java implementation, this is what drove a lot of what you see here, and I was just kind of following what they're going off on. But I think they're… probably the next conversation is around, like, semconf.
And making sure we're abiding by that. I guess, finally, like, do we care about the auto-instrumentation stuff and the other Go libraries, or do we just mainly care about Go Contrib, as far as this is concerned?
**Tyler Yahn** 39:55 Personally, I care very much about the EPPF world. This SIG, not so much. It's the GoSig, but like… if you wanted to come Tuesday and Wednesday, like, yeah, like, I definitely think that this is something we would be very much into, like, supporting. Like, we already have something like this, I think, in Obi, which is the EDPF instrumentation, talking about, like, our telemetry that we produce. I don't think it's as detailed as this.
But yeah, like, having… supporting… supporting something like this for all… for all of those would be great. We… especially… yeah, we care very much about this. Like, this is definitely something we want to produce, in general. In fact, I think anything that produces telemetry We want… to care about this in OTEL.
**Mike Blum** 40:37 Sorry, by care, I meant, like, I couldn't get a grasp from the README, like, where it was in terms of, like, alpha, beta, prod, like, is it, like, stable enough to, like, shoot this tool at it and get something reasonable back out the other end?
**Tyler Yahn** 40:50 That's gonna be challenging to get… shoot a tool at it. It's all defined in, like.
C code that generates, like, a very unique form of telemetry that then gets processed into, the OpenTelemetry format inside of, like, a different… inside the Go runtime. So, like, tracing that back is a little bit complex, but it does, as best as we can, conform to OpenTelemetry standards there. So, like.
Trying to… trying to… Maybe saying it does. It tries to conform, at least, and so I think that that's something that we could… we can work with you there. Like, I would definitely say joining those SIG meetings is a great idea to get some better understanding there. I don't want to take too much time here, but yeah, we care a lot about that kind of stuff.
**Mike Blum** 41:36 Cool, thanks. I just wanted to, like, get a handle on, like, scope of this thing. But yeah, looks like a…
**Tyler Yahn** 41:39 Yeah, I would say start here. If you have, like, whatever is defined for the Go stuff here is something that we can… there's nothing really that's unique about the OpenTelemetry EVF stuff that would be not able to be represented here.
If that's the case, yeah.
**Mike Blum** 41:56 Oh, sounds like that.
**Tyler Yahn** 41:59 Yeah, thanks for jumping in on this, it looks great, I'm excited.
**Mike Blum** 42:02 Thanks, yeah, I'll keep, I'll take your feedback, and, I'll, let you know what… what happens next with it.
**Tyler Yahn** 42:08 Sounds good.
Okay, last up, Robert, you want to talk about, a sick security issue?
**Pellared** 42:20 So… I was checking this, basically, and also, I was… So, long story short, it uses, lord Jesus.
I have bad memory 6-store.
Yeah, basically, I wanted to just say that, in my opinion, from the things that we already have.
you know, the signing of the car packages, etc, and making the GPG signatures, I think we can keep it, and just enable the signature releases on top of what we have already. I think this is a safe improvement, basically.
**Tyler Yahn** 43:10 So how do we sign our releases, then?
**Pellared** 43:15 right now, we are basically just doing, you know, we are signing the tags, right? You're using, and and we are also…
**Tyler Yahn** 43:24 Oh, I'm sorry, sorry, yeah, signing the tags is in, like, the commit… the commit that's actually being put.
**Pellared** 43:28 That's true.
**Tyler Yahn** 43:29 Yeah, okay, I got you, sorry, yeah.
**Pellared** 43:30 And the additional thing we are doing, we are downloading this, this zip or tar package with the code, and we are signing it and publishing.
Because I remember you wanted to do it because of some compliance for, I do not remember, OSS security or something like that.
**Tyler Yahn** 43:51 Yep.
**Pellared** 43:51 And… Piotr from .NET team created an issue so that if you have immutable releases, so maybe it's not needed, but he just opened it, so I think it's better to keep it for the sake of the scorecard.
even though when I was checking this, this part, you know, this archive that you are downloading, which you are signing.
It's not something that is there and you download it. It's basically created at a download time.
it's described in the GitHub documentation that just, you know, basically downloading the, everything what's currently in Git, and you're downloading that, that's why it's not signed, basically. But if this is this, you know, scorecard recommendation to have it signed, then Yeah, I think that we can just keep it for now.
**Tyler Yahn** 44:46 That sounds like it's more… Important, then, to sign it.
Like, if it's…
**Pellared** 44:53 right.
**Tyler Yahn** 44:54 If it's generating it every time, right? Like, yeah, doesn't that, like… Make it more of a vulnerable target as it could change over time, right?
**Pellared** 45:01 You're right.
when I think of it, yeah, you're right. Something changed in GitHub or whatever, there's some… someone in the middle, you're right.
**Tyler Yahn** 45:08 Right. Yeah.
Yeah, I mean, like, I'm not opposed. I really want to keep signing it, because one, it helps with the trust chain.
It's… That… but it's small, as well, because, like… 99.9% of people do not download the tarball from this project. I'd be surprised if there's one person that does it. They all do GoGit, which also has its own, like, some database, right?
So, I don't think that that's the case, but I do think it's better than nothing. Obviously, it'd be great if we can get out of the compliance. I do think that, like, we can get away from it. I think it's better if we sign it.
So, like, I think the reward there is important, it's just that.
**Pellared** 45:53 Hope to see you.
I just want to add that with this image regular releases.
it will be just double-signed, so it doesn't hurt. Like, there's an additional file, so that's why I just proposed to add it on the top, especially that if someone, I think, from the GC just enables it.
it will just work. The only problem is that we need to be sure that when we publish a release.
We do not make a mistake, and we do not forget about publishing these artifacts, because you can do it only once.
an IP in.
**Tyler Yahn** 46:27 Oh, you can't, like, go back and say, like, regenerate the tarball?
**Pellared** 46:31 Nope.
**Tyler Yahn** 46:33 So how would we sign it, though, I think is my question. Like, so if we do that, how do we upload the signatures after the fact?
**Pellared** 46:44 Give me a sec, I need to remember.
If I remember correctly, but maybe I am wrong.
If you just add a tag, I think you can… still download the… if you go to the releases, can you go to the releases?
**Tyler Yahn** 47:06 Of this repository, or our repository?
**Pellared** 47:08 No, our repository, but whatever, something which has probably some other repository that uses just tags and that does not have releases.
**Tyler Yahn** 47:18 You betcha.
**Pellared** 47:19 one. It's…
**Tyler Yahn** 47:20 Sorry, what repository do you want me to go to?
**Pellared** 47:23 maybe go gRPC Go will be a good one, because I'm not sure if they're making releases, or they're just not making tags.
Go for releases.
and open tags, I think they have more tags. If you go back to releases, because right now, yeah, there are more.
But if you go to tags.
And if we have… and if you open, you see, if you open, you have the zip here, entire zip, that you can download without… so, basically, first, you make, you… you create, basically.
First, you have attack, and then when you have attack, you publish a release based on the tag. So first you make attack, and then you download.
**Tyler Yahn** 48:09 to see if I…
**Pellared** 48:10 years.
**Tyler Yahn** 48:12 Okay, so you would download these, verify them, and then in the release process, you would upload whatever your signatures are there at that point. You can't do it after the fact, is what you're saying, though.
**Pellared** 48:21 Yep.
**Tyler Yahn** 48:23 Okay.
Yeah, definitely puts a little bit more… Yeah.
Okay, I mean, that seems…
**Pellared** 48:34 I have to be more careful.
**Tyler Yahn** 48:36 Yeah.
**Pellared** 48:37 It needs to be documented, for sure.
**Tyler Yahn** 48:40 Okay.
Yeah, but I'm… that sounds like it's solvable, so I think we can do that, yeah.
Yeah, any other questions on that? Or other people have thoughts on that one?
Yeah, if not, Robert, I mean, I think it sounds good. Let's… We got a path forward, just make sure we update the docs on that one.
Okay, cool.
Well, that's the end of the agenda. Let me double check. Yeah, any other topics people wanted to talk about?
Any other things people are working on?
I'm guessing… I don't know, we've talked about KubeCon before, but, like, yeah, looking forward to that. We've got two weeks until that is coming up there. We did get the OpenTelemetry Observatory booth. There's a time the SIG is going to be meeting, I think it's on Tuesday? Robert, do you remember seeing this? Yeah.
**Pellared** 49:44 Correct.
**Tyler Yahn** 49:45 Okay, it's, like, local time, I think it's in the morning, at, like, 10 AM or something like that, but I'd have to double-check. Schedule just got published recently. So yeah, if you're gonna be there, if you are listening to this recording, please stop by.
It definitely is something we want community involvement in, so yeah, it'd be good. I do think that we probably want to cancel the SIG meeting on Zoom during that week, yeah, so, not next week, but the week after. We'll plan on… we'll cancel it, but we'll talk about that again against next week.
But yeah, other than that, yeah.
We could probably end it here.
Thanks, everyone, for joining. Good seeing you all. See you all in a week's time, or maybe 3 weeks' time, or 2 weeks' time, depending on how this all works out. Yeah. But, yeah.
Bye, everyone.
