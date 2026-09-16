SIG: Client SIG
Date: 2026-09-15
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Martin Kuba** 00:37 Heather, how are you?
**Cleo** 00:41 Doing alright. How are you doing, Martin?
**Martin Kuba** 00:44 I'm doing fine.
Back from a couple weeks away, so… Getting back into this mealtime, okay.
**Cleo** 00:51 Yeah.
Yeah. Did you have a good vacation?
**Martin Kuba** 00:56 Yeah, it was, it was nice.
**Michael Bushe (Dartastic.io)** 00:57 Fair enough.
**Martin Kuba** 00:58 How about you?
**Cleo** 01:00 Yeah, it was great.
It was great.
**Ted Young (Raintank, Inc. – Grafana Labs)** 01:09 Hey, what's happening, y'all?
**Martin Kuba** 01:12 Alright, Dad.
**Ted Young (Raintank, Inc. – Grafana Labs)** 01:13 I feel like it's been a while.
**Michael Bushe (Dartastic.io)** 01:20 No religious music anymore. Well, yoga chanting.
How's everyone doing?
**Ted Young (Raintank, Inc. – Grafana Labs)** 01:30 I'm good.
**Cleo** 01:34 Yeah, trying to… trying to remember what I do here, that's… It was a good vacation.
**Jason Plumb** 01:47 Still joining the old meeting.
**Ted Young (Raintank, Inc. – Grafana Labs)** 01:53 Yeah.
I'm slowly flushing all the old meetings out of my personal calendar, but some of them still remain.
**Martin Kuba** 02:08 We have one topic, from Hanson that we want to talk about, so I'm just waiting for him to join.
**Jason Plumb** 02:36 I guess while we're waiting, I'll just say that a couple of weeks ago, I think I suggested that maybe more than a few times, I've suggested that I would, take point on bootstrapping a session SIG, finally. And then, extenuating circumstances happened, and I certainly don't have time for that right now, so… I hope to be able to revisit that topic again in the near future, I'm sorry.
There's only one of me.
**Ted Young (Raintank, Inc. – Grafana Labs)** 03:07 Is that something you could participate in, Jason, if other people were doing the heavy lifting of driving it?
**Jason Plumb** 03:13 Yes, I think I could.
Guest.
**Hanson Ho** 03:17 Talk about sessions?
**Ted Young (Raintank, Inc. – Grafana Labs)** 03:19 Yeah.
Jason's too busy to lead it.
If someone else has time to organize us.
**Jason Plumb** 03:30 In the short term, at least, like, I, you know… Can't see the future, but maybe, maybe in a month or two.
**Hanson Ho** 03:40 I will also participate if someone were leading.
**Ted Young (Raintank, Inc. – Grafana Labs)** 03:45 Okay.
**Martin Kuba** 03:49 I think I can probably take the lead on this, Yeah, I can give it a try.
**Jason Plumb** 03:56 Read…
**Ted Young (Raintank, Inc. – Grafana Labs)** 03:57 Awesome.
**Hanson Ho** 03:58 Hear it.
**Martin Kuba** 04:01 Alright, so…
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:02 I can help. I would normally be like, yeah, fine, but I feel like my schedule has been so spotty with so much work-related travel that… I'm nervous about… about saying yes to that, but I will definitely help Martin, make this happen, because it's important.
It kind of feels like the last boss of, like, client-side stuff after… after the SEMCOM repo, which we're about to talk about.
**Hanson Ho** 04:31 It's the last boss of Season 1, season 2.
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:35 Season 2 is the client-side protocol, maybe.
- maybe that's Season 3.
**Hanson Ho** 04:47 Who's driving this? Martin, do you want me to do it?
**Martin Kuba** 04:51 Yeah, so, I mean, you're… you have the only… you have no topic on the agenda, maybe.
**Hanson Ho** 04:55 Sure.
**Martin Kuba** 04:56 Talk about it.
**Hanson Ho** 04:57 I will share my screen.
There we go… Everybody can see it.
Yeah. All right, I mean, if somebody has additional agenda items, feel free to co-add it.
But the Client Side Semcom repo has been created, Trask created 3 weeks ago, and we've been busy since. Not busy doing this stuff, I wish we were busy doing this stuff, with other stuff. So now that Martin's back, I have a bit more time, we can look forward to, basic progress here. So right now, the repo exists, I've cloned it, I've… start putting stuff in there, but I haven't put a PR in yet, because, it needs to do validation and making sure everything kind of works. But, right now, it is empty, and, we went to the SEMConv SIG yesterday and kind of talked about how we bootstrap this, what kind of process we need, and we were basically given… I wouldn't say carte blanche, but we were given a lot of latitude to basically say what goes in, what, what… how you prove it, and things like that. They do want, obviously, us to stay, tethered to the main boat, especially if we're doing things that are, a bit outside of expectations, not as a means to hold us back, but more like, hey, are there… Understandings we need to have or improve in order for us to promulgate, you know, these sets and use cases.
So, we haven't thought about how to do that in a formal way. Like, do we just go to… like, does one of the maintainers go to the SEMCOM meeting every week, and we rotate and just make sure that, you know, nothing gets out of sync? And if there are big things that we talk to them, post in the groups and things like that.
et cetera, et cetera. So all that needs to be kind of formalized and finalized. But right now, the repo is there.
list of to-dos that we have to get things going to, like, a V1. I just quickly jotted stuff down, which is, like, the initial setup with the CI and everything, the validation so things don't drift.
We, are supposed to decide which namespaces we want to own, new ones and old ones as well. So, I think… app is effectively mostly stuff that we do, so that's one of the ones that we may think of taking, as well as, mobile client, like, whatever things that make sense, especially if they already have, semantic conventions, defined within it.
So… the process of taking, it might just be deprecating and declaring. I don't know what the details are, but that's something we should figure out.
And then, obviously, after that, it's the migration. How do we deprecate you know, app.jank or whatever we have, and then put it up in the new repo. And have… and more importantly, have, anything that Generates these, platform-specific constants, take in the new repo, and basically, have it included.
That's something that we could do, in terms of modifications to existing repo, or we simply let the consumer say, hey, where is this? Because I'm using it.
Some of them make more sense than others, like Java and, you know, and Kotlin. We probably need to pull that in sooner, because Android will be using it, and iOS, if they're using that, I don't know what the browser situation is like, and JS, so… but luckily, we have folks, you know, in this call who can, you know, do that kind of sort of stuff.
If those were the only projects that consume it, but unlikely. So we have to kind of figure out how the rest of it goes.
And then what I think is probably the trickiest, is figuring out a review process. Like, the core semantic conventions where you go on a very formalized process. You have a YAML file that you take, and you take the ticket, and you put it there, and you do… We could do that if we want. Do we want to do that? So that's kind of up for discussion. Not something we have to decide today, because we're not going to be approving anything today, but probably something going forward that we want to, figure out sooner rather than later.
And, yeah, leave some time for open questions that we should, like, you know, talk about. But one thing that I think Martin and I talked about yesterday was, increasing the cadence of this, to every week.
At least in the short term, specifically to talk about the semantic convention stuff.
Anybody have a… think we should have a new time, or we can just use this one… this time, because… Feels convenient.
**Jason Plumb** 10:09 That's a lot works for me.
**Ted Young (Raintank, Inc. – Grafana Labs)** 10:11 Yeah.
Let's just keep using this one.
**Hanson Ho** 10:18 Cool.
**Martin Kuba** 10:19 Should we, should we just update, like, the community, page to just make… to make it obvious that, this meeting is used for semantic conventions?
**Hanson Ho** 10:28 Yes, I can do that.
Oh, should put action items. Yeah, I need something else now.
**Jason Plumb** 10:38 Do we have maintainers identified for this repo?
**Hanson Ho** 10:42 Yeah, right now it's, Martin, Jared, and me. Great.
**Jason Plumb** 10:48 Great, first up.
**Hanson Ho** 10:49 Yeah.
We are updating…
**Jason Plumb** 11:06 So if we get the README updated, then I won't have to ask that question ever again.
**Hanson Ho** 11:11 Yeah, you know what? Maybe I just do that first, because I have an initial setup, like, working in my repo. I was porting that to make sure everything's good, but maybe it's just update the initial README, so we don't have to… wait till a big PR gets approved, so…
**Jason Plumb** 11:27 Yeah, and is there, like, branch… is there branch protection and all that kind of repo stuff already in there? Like, this was stood up with Terraform, presumably.
**Hanson Ho** 11:35 whatever trash did to set this up, that's what happened. Okay, good. It's got all the basic stuff, yeah, so, I have to validate what, what is there.
Otherwise I'll just push it and say, oh, it got through, that's bad. But also good, because it's there.
**Jason Plumb** 11:57 Yeah, it's in Terraform.
**Hanson Ho** 11:59 Cool.
Alright.
Any other opening questions about this? How we… Move forward, or do we just say, let's socialize this, and then come next week, and plan for the real?
Because I know, Martin, you know, you and Jarrett, you, you guys want some of the browser stuff to be in. So, maybe we can, if we… if there are no other open questions, we can take the one that I have.
But, you know, it'd be great if there are other open questions.
**Cleo** 12:48 I had one about iOS.
And… Who or how we want to sort of reconcile that because, the maintainer doesn't attend this meeting, and doesn't seem like at least as far as I know, they are not interested in attending this meeting.
Do you have any thoughts on… on how we want to handle that?
**Hanson Ho** 13:18 I think first things first, I probably want to reach out to, like, at least the group to see if anybody else who's not a maintainer might want to kind of be involved. It would be really, not great if we moved forward without them. I would say there's two platforms, so at least we could development on the iOS-specific side will be, non-existent, and they won't get a say in it. But, if we reach out, do our best, and they, don't respond, or whatever, because, you know, everybody's busy, We kind of have to move on.
I think.
**Ted Young (Raintank, Inc. – Grafana Labs)** 13:59 My impression with iOS is they're… they're interested. The problem is more of, like, a people power problem over there. They have a set of maintainers who are very part-time, But I know certainly here, you know, speaking for… with my Grafana Labs hat on, we're very interested in iOS and Swift, so we're putting some people on there. Those people are not maintainers yet, obviously, but… there are now more people showing up, and I've been trying to poke Olita to have Apple show up, and Apple does show up, albeit, like, somewhat inconsistently, but semantic conventions might be an area where they might be more interested in showing up consistently.
So… so if we kick this thing off, I think I can… it'll be easier to, like, get them to show up. So I don't think we should wait for them, I think we should just get it rolling, and I will help make sure that people from over there stay involved.
**Hanson Ho** 15:03 I've, put an action item on you, Ted, to reach out to iOS folks.
**Ted Young (Raintank, Inc. – Grafana Labs)** 15:06 Yeah, that's fine.
**Hanson Ho** 15:14 Any other… Open questions.
**Jason Plumb** 15:17 Yeah, Hanson, do you anticipate we'll just move all of the Android conventions over there?
**Hanson Ho** 15:22 So this is what I kind of want to talk about, with this open question.
**Jason Plumb** 15:26 football, I just, I legit.
**Hanson Ho** 15:28 Completed that we got to…
**Jason Plumb** 15:29 estimated…
**Hanson Ho** 15:30 No, I would say the… so, I would say… the Android repo right now.
We have a lot of hard-coded constants in instrumentation.
We have a lot of, poorly designed conventions without respecting namespaces.
Those should never be moved beyond the Android repo. Those are… those are… I think it should be pulled out into, like, you know, a file that looks like a semantic invention, but that should never be shared as if it were a semantic invention.
**Jason Plumb** 16:04 It's much better than it was, like, a few months ago. I think you might be overstating it. Like, the number of constants, like, the string literals, is almost, almost zero.
**Hanson Ho** 16:12 Okay, perfect.
**Jason Plumb** 16:12 It might even be zero. And then the namespace problems, I've fixed, like, a couple of the glaring ones, but there might be a couple more.
**Hanson Ho** 16:22 And do you… does it have a flag to basically say, don't give me the new one, give me the old one?
**Jason Plumb** 16:30 It does.
**Hanson Ho** 16:32 And the old one is still, sorry, the new one is still not, approved as semantic convention, right? So there could be a new, new one.
**Jason Plumb** 16:41 I mean, stability's all over the… like, we don't declare anything as stable yet, so…
**Hanson Ho** 16:46 Right.
**Jason Plumb** 16:46 Yeah.
**Hanson Ho** 16:48 So, like, my initial thought is because… and just looking at the Android situation, is we have a bunch of things that we are not sure that, is… is completely appropriate, so… once we determine that, hey, this is the shape that we want, getting that into the share repo is a good idea. Whether it needs its own namespace, because it's so Android-specific, that may be something we want to talk about.
But, my intention was, was… Ideally, if we could turn whatever we have in Android into a form that is acceptable as a shared semantic convention, I would like that. But whether all of them have that level of, of, of kind of, I don't know, reusability, I don't know.
**Jason Plumb** 17:40 So maybe some pros in the README would also help here, too, that kind of explains the vision of that repo. So, I think when we talked months ago, it was like, this repo is going to contain all of the agreed-upon semantic conventions that work across client-side, right? So stuff that's interoperable between Android, iOS, you know, Swift, whatever, web, and then also in that same repo would be platform-specific client-side semantic conventions, and this repo would produce all of those. Is that… if that's still aligned with the vision, then let's… let's get that written down.
**Hanson Ho** 18:14 Yeah, so that's what the open question is discussed, like, do we… do we want that? Because another alternative is have a browser-specific repo, have an Android-specific repo.
**Jason Plumb** 18:23 No, I think this is… I think this is what that's supposed to be, is the spot for all this client stuff.
**Hanson Ho** 18:28 I agree too, especially since it, it, having a shared place would be nice.
**Jason Plumb** 18:36 But with that, then if there's… if there's a… the comments… I'm just gonna say common. I know common is often, like, a dumping grounds, but if it's, like, we have the Client Common that's… works across all platforms that we've agreed upon, and then we've also got one for Android. Why not bring all the Android stuff over?
And I think what I heard… I think what I heard you say earlier is because we only want to bring the good stuff over, and that's fair. Yeah. Like, if there's stuff that's, like, way off base, then don't bother. I get it. Okay, so I think that's the reason.
**Hanson Ho** 19:05 So the repo is mainly a collection of namespaces, right? So, by Android-specific, are we saying that we should have an Android-specific top-level namespace, or have app.android?
however we want. That's not what I'm saying.
**Jason Plumb** 19:21 I mean, someone might say that, I'm not saying that.
**Hanson Ho** 19:23 What do you… do you have a specific idea, then, that, like.
**Jason Plumb** 19:26 Yeah, like, all… just all of the existing semantic conventions, before they have become commonized, that we are using in Android today.
**Hanson Ho** 19:35 Okay, with, with…
**Jason Plumb** 19:37 That those are candidates to be brought over.
**Hanson Ho** 19:40 So, normalize… normalizing to proper namespaces?
**Jason Plumb** 19:45 I might have to have you elaborate on what you mean by that, but right now, everything is not within an Android namespace, no. We have some stuff that's in apps, some that's in Client. We might have Android, but we certainly have… App and client.
**Hanson Ho** 20:00 So, so maybe that's what we should discuss then, because if it goes into app.
it becomes common probably by… by convention. So, should we have platform-specific events or… or a semantic convention, that is not… Called out by namespace.
I don't know.
This is, this is, this is, like, more…
**Jason Plumb** 20:24 You don't want it. It sounds like you want it to be clear from the namespace. That was never a goal of mine.
**Hanson Ho** 20:32 Okay.
**Jason Plumb** 20:34 I'm not pushing back on that, I'm just calling it out as, like, I'm trying to reiterate what I'm… I think I'm hearing.
**Hanson Ho** 20:39 I… I… at 60-40 for me, I could be easily convinced. I want to hear, kind of, because I… I know, I know the browser folks have a lot more, thinking about this, so, Martin and Ted, maybe, or… or others, do you agree that that stuff should live in this repo? Like, if there were browser-specific inventions living in this repo.
Does that sound fine? That's question one.
And the question two is, ought it be in a namespace, a sub-namespace, or it should just be, documented as such in the, in the descriptions?
**Martin Kuba** 21:25 So, I don't know if I have a strong opinion on this myself, like, we started we started adding some of the conventions for browser to the browser SDK repo, just because, that's what Android has done. And also, like, we thought we could move it later if we made that decision, but it's in the process, so, like, right now, like.
This decision, like, directly affects us.
how we can… how we would proceed. I think somewhere in the semantic conventions.
repo, also in the documentation, it says that Like, the domain-specific conventions are encouraged to live along with the… with the SDK, I can't find it right now, but I think it's captured somewhere, so I would look for someone, maybe, like, that's something we can bring back to the semantic conventions group and ask them directly, but…
**Hanson Ho** 22:20 That feels like it might, might be… Was that part of the Federate, like, the whatever OTEP, that proposed about the convention?
**Martin Kuba** 22:30 I'm not sure, I'm… I don't… may not have been part of that, may have been, like, part of… Previous documentation.
But I also… but I also remember that… that I thought your kind of vision for this was to have everything combined in one… in this one repo, is that correct? Or do you have opinion on this, Todd?
**Ted Young (Raintank, Inc. – Grafana Labs)** 23:01 You're not…
**Hanson Ho** 23:06 I think it's convenient to have everything in this repo, and… I also want to kind of… differentiate between the official, like, you know, platform-specific project with the semantic conventions, because one could consume the semantic conventions without the project, and conflating those two seems, you know.
not great. So if we're gonna have to, like, put it… go… because there's not that many of them, and put it along with something else, we could put it in this repo, and because of the way Federated demands conventionally defined, we could move it to a new repo, you know, through the same migration path, deprecate, and basically start a new one. We can even, like, you know, match the versions if we want to.
**Ted Young (Raintank, Inc. – Grafana Labs)** 23:51 Yeah, I should clarify, I think regardless of where they live, we should try to use the federated semantic convention tooling. And yeah, we shouldn't… we should not be just, like, burying, quote, if it's just something buried in our implementation, that's not a semantic invention.
Right.
For the reasons you just mentioned.
**Hanson Ho** 24:13 I think the Android repo uses the semantic convention tooling, and does the generation, specifies the manifest and all that stuff, it's just… I don't think it's published individually as a version, it's just kind of like whatever Android version it is, and I don't even think we publish a, a, snapshotted versions of our semantic conventions, right?
I think it just… We build whatever's in the repo, during the build and consume it.
**Jason Plumb** 24:43 I think we published.
**Ted Young (Raintank, Inc. – Grafana Labs)** 24:44 Yeah.
**Jason Plumb** 24:44 Yeah.
**Hanson Ho** 24:45 We publish it with a version.
**Jason Plumb** 24:47 Yeah, whatever the current version of Android is, yeah. It's versioned alongside the main…
**Hanson Ho** 24:51 Okay, okay, okay, okay.
**Ted Young (Raintank, Inc. – Grafana Labs)** 24:54 But it's not just us public… I think part of the point of the federated approach is that, like, we can… the main semantic convention repo should be, like, pulling these things in in some way.
Or maybe not, right? Like, there should be some… these things should be generally discoverable outside of, like, our implementation.
repo.
And I would say that even if the main one doesn't pull them in, then this client repo should pull them in. And whether that's because they're all getting published directly there, and, like, that's where you make your PRs to change them, or whether the platform-specific ones live somewhere else, like, having one spot where they're all getting pulled in automatically.
would be helpful. The only reason why I guess I don't have opinions is I don't know, like, is it an… you have to do, like, releases of these things, right? And I don't know what's more annoying, everyone… Having to depend on each other to make a release, or everyone being able to do their releases independently?
They're both probably annoying.
Because it's, like, bidirectional dependencies.
**Hanson Ho** 26:07 releases are cheap, at least.
At least to begin with. If it's about cadence, then I don't think it's a problem. If it's about, like.
compat and other things, that may be a bigger problem, but I would almost want to solve this problem when we get there. Like, have all the client-side, platform-specific, non-platform-specific in one repo.
We declare, if we choose to have specific namespaces, we declare all those namespaces. And if, at some point, we feel that, things should be moved over, to a new one, then we could do that.
So I think I'm developing a stronger opinion as we go through this. The appropriate Android semantic convention should be moved over. Namespaces permitting, and things like that.
**Ted Young (Raintank, Inc. – Grafana Labs)** 26:54 Yeah.
My feeling, for what it's worth, is that's the better way to do it. I think we would all be happier with just one repo, with all the client stuff in it, including all the platform-specific stuff. That's probably less crazy-making for everybody to have it all there.
**Hanson Ho** 27:11 And…
**Ted Young (Raintank, Inc. – Grafana Labs)** 27:11 Probably build it first, you know, and, you know, see how it goes.
**Hanson Ho** 27:17 And it's actually pretty straightforward, like, the tooling… so Android builds the binaries, from the manifest.
it could choose a subset of namespaces, or even select specific events and semantic conventions to include in the binary. So even if the repo itself has, like, like… summation of all the semantic conventions. If JavaScript only wants the JavaScript ones, and they could, you know.
easy way to filter that out. That's… that's possible. So, OpenTele Entry JS… there's a specific JS semantic conventions repo, right, that generates the JavaScript binaries?
**Martin Kuba** 27:58 Correct.
**Hanson Ho** 27:59 Right, so that one will be modified to basically take in this one, you know, and then… it will generate the binaries, based on… on that, and it itself is not a, manifest declaring repo. So that is just a means to an end. And I think for Android, we have that in our own, we take whatever repos that we want, generate constants, use them. We don't export those constants. Well, we probably do, just by the nature of modules, but the real definition is in the manifest and is in the repo, so we'll have one version going forward.
Until we have more, if we wish.
**Martin Kuba** 28:42 Really quick, before we need to end this call, also one implication is the schema.
We would, instead of having, like, separate schemas, we would share the same schema.
Right, so… That's, maybe part of the decision, too.
**Hanson Ho** 28:59 Well, the scheme… the schema is just basically the URL so version, and, like, if it's dev, you know, we would tag it, alpha, things like that. So… I'm okay with that, although maybe I just don't know the details of it.
I would say one thing that we learned yesterday was that no other federated semantic invention repo currently publishes.
So there are… there is no version of, like, Gen AI or mainframe. People are defining, but they have not cut a version to consume. So, We will probably be the first ones, because we have, like, use cases clamoring for it. So we may be running into things where we're the first ones doing it, so we make a mistake.
Simply because no one else has tried it. But I think it's okay with that, because, you know, by our very nature, clients are a bit more flexible, so hopefully, through deprecation and other automated means, we could fix our… sins. We can start with the dev, and then go from there. Declare its instability, and kind of move on.
**Ted Young (Raintank, Inc. – Grafana Labs)** 30:10 So we're at time.
**Jason Plumb** 30:15 My stuff can wait, we can talk about it another time. I think I answered the first question on my own.
There's a… there's two groups, the names of which are very confusing, but let's do it next time. Yep.
**Hanson Ho** 30:26 Okay. Alright, bye.
