SIG: Client Instrumentation SIG
Date: 2026-07-07
Duration: 36 minutes
============================================================

## Zoom Recording Transcript

**Martin Kuba** 07:24 Hello.
**Jason Plumb** 07:39 I'm gonna reach out to Ted and see if he's gonna join.
**Santosh** 08:12 Thanks.
**Jason Plumb** 08:14 I was just on the Android SIG before this, and Hanson was also fired up about talking about Federated SemConf, but without Ted, it might be a little slow to try and bootstrap that discussion.
**Martin Kuba** 08:31 Is Hanson going to join?
**Jason Plumb** 08:33 He said it was, but we'll see.
So, Martin, you're running this meeting for sure But I'm going to share my screen anyway, just to take a couple so we can take a couple of screenshots or whatever. So this was from a week ago in the client side telemetry chat.
On the CNCF Slack.
And… I think there's some interest, right, in, Well, first of all, there's the Flutter thing happening. That's a separate issue. If you're not aware of that, please go check it out.
I think there's a community… PR that's open, or issue that's open, to bootstrap a Flutter group, and I know a lot of people in this group might also be excited about Flutter, or at least have peers that are, or bosses that are, and then there was this discussion about federated semantic invention, so that's kind of, like, where this is coming from. I've asked, and we'll see if Ted can join us, because I think he and Hansen were fired up on this topic. I think… I'm also fired up on this topic I'm doing the thing in Android right now for the bespoke Android semantic conventions and making a federated Repository over there.
I probably don't have cycles to do it for the client's sake, especially if there's a new repository involved, but… I definitely want to help out with that.
**Martin Kuba** 10:15 Ryan, I'm… catching up on this topic. I'm not familiar like with the reasoning and like the the approach recommended here. In the past, like I Remember, there was a guidance to reuse as much as possible from semantic conventions, from the main semantic conventions, I thought.
**Jason Plumb** 10:39 Hey.
**Ted Young** 10:40 Sorry, too many parallel SIG meetings.
**Jason Plumb** 10:43 Well, yeah.
**Ted Young** 10:44 Forgot that this was happening right at this moment.
**Jason Plumb** 10:49 Well, thanks for joining us. I think Hansen said on the Android call that he was gonna join. I know that he's fired up on this topic of… Federating client semantic conventions.
**Ted Young** 11:01 Nice.
**Jason Plumb** 11:06 So, yeah, go ahead.
**Ted Young** 11:10 Oh, you want me to pitch? Sure, I can pitch.
**Jason Plumb** 11:13 I would love to, I mean, I'm…
**Ted Young** 11:16 Yeah.
**Jason Plumb** 11:16 Yeah, so.
**Ted Young** 11:17 I, I guess it, it feels like maybe good timing to, to revitalize this SIG. You know, we.
had this SIG, and then, once Browser kind of got its feet under it, we're like, well, maybe this SIG can go a little dormant and just be kind of like a monthly check-in, or whatever. But now we're seeing there's… especially with, Flutter.
showing up and having some legs. One, a need for, like, that group, like, definitely needs some help to make sure they build the right thing. And we ran into a bit of a wall, which is the people who are supposed to sponsor and do that work are the technical committee. But the technical committee has almost no client side expertise amongst its members. So.
from the spec call we just had, where we were discussing all of this. Some things that came out is one, you know, adding someone to the Tc.
Who has client-side, expertise to help there.
But also trying to find a way to make sure there's just a better feedback loop between what everyone is up to, both on the semantic convention side and on the spec side.
In fact, there was a request, one, for maybe more client maintainers to start coming to that spec meeting.
And actually, something we've been doing in that spec meeting that's been, people have been really liking is just report backs from different SIGs and initiatives. And I think it would be great to have someone from this community kind of do, like, report back On, like, the state of client side, you know, here's what we're doing on browser, iOS, Android, you know, like, just here's where it's at, here's the challenges we're facing.
that kind of a thing. It would be helpful to get those people up to speed.
But one of the things I've been asking is, like, do we need, at this point.
more… some… more coherent structure for our own sake? Is it enough just to have a bunch of SIGs, you know, sister SIGs working in parallel on client stuffs and… and checking in with each other on a regular basis? Or do we want… To have some people saying like, no, I'm, I'm, I'm gonna take on doing the work of.
Trying to, to map out the places where there's overlap between these SIGs and.
And kind of, like, help do that in a more coherent manner.
And there's 2 places where that seems.
There needs… there's a need for that. One is the semantic conventions.
what we're doing on the semantic convention front is this new concept called federated semantic conventions, where rather than all the semantic conventions having to live in one big repo, you know, the SemConv repo.
Having CEMCOM tooling allow that.
that collective thing to pull in from multiple different repos, which is allowing different groups to just kind of take on ownership of their stuff.
But the flip side is like a double-edged sword, right? Like, if we do that, then it also means this SIG is starting to move with a little bit.
less oversight from the general semantic convention people.
So, I think it feels like we need to kind of get our house in order if we're gonna do that, just to make sure we don't… We don't accidentally… You know, ship stuff.
That's regrettable.
The other side is specification work. There's stuff that's… Cross-client, you know specific. There's stuff that maybe the browser specifically needs, but other groups don't need.
And we want to make sure we write those specs down somewhere for the cross client stuff. It should definitely go upstream in the spec doc if the browser is going to kind of go its own way because it's such a weird beast of an environment.
Then they need to write down their specs somewhere else, but… Yep.
There's some need to coordinate all of that, and that's also been, like, a traditional pain point.
I think personified the most by session and session management.
where this needs to shove into our data model somewhere. And the process of trying to figure that out has always been really painful because the the client groups figure out something of what they need. But then it goes through this review process.
entirely by server side people who are not really familiar with the issues.
And… I feel like I've… I've made the problem worse by maybe insisting too hard that we try to find, like, a collective answer versus just packing on some client-specific stuff to the side of our data model. I feel like I'm… I've been beaten down over the years, and am now much more in favor of just, like, anything, just anything that would work. But that's another example of, like.
It would be helpful on the client side if we're going to be managing and presenting that stuff and working with that, that it be some specific people taking on that work rather than just hoping that it kind of shakes out amongst the different client side maintainers.
So… That was a bit rambly, but those were some of the reasons why it just feels like maybe not just rebooting this SIG, but figuring out a bit more structure.
Would be helpful if, if for no other reason than to make sure like there are in fact people with the time and interest to take on some of these cross client projects rather than just kind of like hoping that it's going to work out.
**Jason Plumb** 17:38 Okay.
I know, I wish, I wish, I wish there were two of me every day, Ted.
**Ted Young** 17:43 So do we.
**Jason Plumb** 17:45 I know you do too. I know almost all of us do.
**Ted Young** 17:47 Yes.
**Jason Plumb** 17:50 Yeah, so I wouldn't call it pushback, but the question was raised around the initiative that I've been pushing in Android to have our own semantic conventions federated SimConf over in Android. I guess we're still considered an early adopter, like there's the GenAI stuff, but like not.
many other groups have really started doing Federated SimCom yet, so… I'm definitely doing an Android, and we have stuff in there that should, like, will never have commonality with other platforms, which is… is fine. I think that's why there's room for stuff like Federated in the first place. But the question was, by doing it in Android, does that… limit or make it harder to coalesce between different platforms on one common thing.
And I… I think it doesn't. I think, in fact, it helps, because right now, the current state of things in Android is the shit's just spread everywhere.
Like, you can't tell even where the semantic… like, what the semantic conventions are. Like, some of them are in READMEs that are not template-driven, they're just in the README, they're in the source code, you can't go to one place And this will help that. You can at least then have all of the definitions in one place to compare with all of the definitions from iOS or web or Flutter or whatever. And so I think it's a step toward that direction. As far as like rebooting the SIG and or having a new repo kind of associated with the SIG, I think it's a great idea to have semantic conventions for client side teams or platforms or projects. I think there's room to have like in this same repo side by side, web, iOS, Android, etc. And then common, right? And common then is where stuff can sort of be elevated to once you find that common ground.
**Ted Young** 19:44 I would completely agree with that. I think having… Having the different client SIGs be able to, you know, have agency and control of defining their stuff and a clear place to put it so it gets out of the READMEs is great. But I would worry if we federated so much that it was all literally just embedded in each client, which is possible, right? We could literally embed these in each client repo.
That then it would be hard.
if you're trying to look at, like, across the clients, how do things work? Now it's, like, like, too federated. Yeah.
**Jason Plumb** 20:22 But I mean.
**Ted Young** 20:22 Repo with just enough just maintainer access from all the different maintainers would.
**Jason Plumb** 20:27 Oh yeah, like if I show up next week and this new repo exists with maintainers and there's a spot for Android in there, I'm going to take all of our stuff and just put it over there. Like that's great. And then we'll just, we'll source that with Weaver and we'll do our code generation in the repo and that's fine. But at least then you have the kind of source of truth in one place.
**Ted Young** 20:48 Yeah, that feels, what do other people think about this? Does that feel like a healthy middle ground? Make a new repo for this stuff?
**Cleo Schneider** 20:59 I would love that. As a newbie, it's been really tough to pull from every place and understand. So this would really, really help us out. I also am happy to help do some of that because we are trying to map out where does all this stuff live across these platforms.
Yeah, I'm… I would be a huge fan. Huge fan.
**Stephan Gay (Datadog)** 21:27 I think we would be happy on our side too.
question before this meeting was, ask them what's a session identifier, please. Can you tell… can you tell us what's a session identifier? Android has something, browser is going with something else, we don't even understand it, and we don't know where to look. So… Of course, if we could have a uniquely defined session identifier concept at semantic level, that would be nice, but if we don't have that.
at least having one place where the different session identifiers would be would be amazing.
**Ted Young** 22:02 Yep.
**Stephan Gay (Datadog)** 22:02 Again, for a discoverability reason, I guess, for a Yeah, people who join, or even when we try to onboard a new client, yeah.
Having an idea what we're going to find there.
**Jason Plumb** 22:16 I'm just pulling this up since you brought it up, but this is what we have so far as far as definitions for sessions. And you've probably seen this and it's probably not enough. Yes, I think we're all on the same page there. There probably needs to be genuine spec.
that describes, what a session even is versus, you know, just these kind of a vague, like, there's a vague description and, you know, then some… then some actual detailed SimConf.
Anyway, I'll put a link to this in the SIG doc. Martin.
**Stephan Gay (Datadog)** 22:49 The example value being sorry.
**Jason Plumb** 22:52 Okay.
**Stephan Gay (Datadog)** 22:52 Go on, go on.
**Martin Kuba** 22:54 I was saying at the beginning, Jason, I'm still trying to get up to speed on the reasoning for this, but I'm going to just play a little bit of a devil's advocate here. What's the advantage of having a brand new repository that combine?
semantic conventions, let's say, for different Sdks for different client Sdks help us, maybe like, find common attributes like across different client Sdks. What is that? What is? How is that better than having it in the main semantic conventions, repository, and like just like my, like my, my concern, my little bit of my concern is like in the past. We've had The guidance that I've… That I recall from the TC is that we should reuse.
semantic conventions as much as possible.
So, like, if we, if we now start, start putting everything into a separate repository, like, are we gonna lose that, you know?
lose that kind of overlap with the the main semantic conventions.
Oh.
Or like, what? How would we approach that? How would we.
You know, how would we… Go to, like, finding the right like like, how do we decide like which semantic conventions are only client, only android, or could be actually reused from the main semantic conventions.
**Jason Plumb** 24:28 I think the short answer is if there was a repo that contained all of these, it would be trivial then to say which ones are Android because they're within that namespace.
Like, there's a schema URL that would be specific to Android.
But to answer your question about, does that loosen the guidance around trying to use existing ones or consolidating? I think maybe a little bit, but at least within client, then we are at least more able… probably more able to unify or consolidate.
I mean, there's… this is, like, a great example App versus server, you know, like, we've had that.
Discussion 100 times, and it's like… If we had our own area for semantic conventions, we wouldn't have to have that discussion.
again.
**Martin Kuba** 25:21 And the difference is that we would be publishing our own schema.
**Jason Plumb** 25:26 That's right.
**Martin Kuba** 25:27 Okay.
**Jason Plumb** 25:27 Yes.
**Ted Young** 25:29 It's, in a sense, one of the things. And we could… There is, like, a double-edged sword to this, and I think you've identified it, Martin, which is, like, if we go off on our own, it's now much clearer what are the… client semantic conventions. This is in part about ownership of the semantic conventions. If everything's stuffed into one repo, and you have one giant backlog of pull requests and issues, that just starts to feel unmanageable.
after a certain amount of time, right? Like, if you want to go into that and understand all of the… client-related issues, maybe you can use a tag to search for that, but that's been one of the motivators, is that that has just started to feel like just 10 pounds stuffed into a 5-pound sack, and that's just the nature of any repository.
But the flip side of us taking this work on is, again, we need to make sure we're staying coordinated with the general semantic conventions, right?
app versus service, like… like, do we want to go recreating conventions that already exist? Like, that would be… that would be the… the place where I think things could get lost.
And that's why I'm feeling like if we do this, I think it's not enough just to have iOS, Android, browser, Flutter maintainers. There needs to be some amount of people feeling like they've got the time.
To be stepping back and seeing the whole forest, and being a liaison between what's going on in the client SIGs and the semantic conventions and the spec meeting and like other things.
Or we'll end up just too disconnected from what everyone else is doing.
**Hanson Ho** 27:35 Sorry, folks, I had a thing I couldn't.
get here in time, but, what Ted… well, whatever I did get after dialing in what Ted said is completely agreed. This is… It can't be disconnected. Federated means there is a connection. It's not like, hey, we're off to do our own thing now. Redefinition, even as much as we want to do, sorry, service.name, that's what it's called. That's what it is.
We have to live by that. And I think this is more of a governance issue than a let's do everything differently issue for me. And I believe having strong ties to the main SEMCON group and regular kind of feedback is… essential, which is why I think, you know, set up the project to be easy to actually staff it properly and do that.
I think there has to be very strict duties defined and adhered to.
Which is why I'm scared to put my name forth to do a lot of this stuff as much as I want to.
**Ted Young** 28:37 I think this is the problem. The good thing is the client sinks have grown up, and one of the issues we had in the past was like to to do a lot of this work. You need to both have domain expertise, and you need to have like open telemetry expertise to understand how to design something that's OpenTelemetry flavored for these domains, and we just… that was always, like, traditionally two separate people. You had people who had a deep knowledge of, like, the design philosophy of OpenTelemetry, but they only worked on server-side stuff, and then you had people with deep knowledge of, like, client-side observability, but We're new to OpenTelemetry, maybe new to tracing, some of these other things.
But it feels like the SIGs have kind of grown up a bit over the years. We now have people who have been building and maintaining these SDKs for a while.
you know, have, like, soaked enough in the brine that they understand it. But, shocker, those people are also the people who are, like, really busy and already have a lot of responsibility. So it almost feels like like, having… everyone having to move up a level, right? Like… Being… if people are going to take on some of this higher level, like, coordinating work. It's like… Maybe as part of that, it's like trying to bring more people in as approvers and maintainers at the individual SIG level to free them up.
We can't assume everyone has like infinite time.
So that's… that's just a concern I have, like, we're… it's just growing pains, but… and I… I'll admit, I don't… I don't have the answers, I'm just… just pointing out that's what we need to figure out.
**Hanson Ho** 30:32 So what's the next step?
**Ted Young** 30:35 Well, I think one thing that was proposed is like We want to federate.
where do we put this stuff? And it seems like it would be better to create a repo specifically for this, that we put all of the client things into, and that feels like a good next step. At least then.
It'll be a lot easier for the different client maintainers to keep track of what everyone's trying to do.
Which, if it's all in our own repos, is hard. If it's all in the giant hairball of, like, semantic conventions, that's also hard. So that seems like just a concrete… middle ground. Seems like there's general consensus that would be good. So, just starting with that, and then trying to take everything that we already have and pile it all in there would be, like, a good concrete next step.
Another next step is, there is a general spec meeting that happens right before this one, every week.
**Jason Plumb** 31:38 During the Android meeting.
**Ted Young** 31:39 During the Android meeting, you dirty Android people, But that's that was actually brought up is that actually, that's the place where we do. We coordinate across like the different Sigs and talk about spec issues and stuff. And Client maintainers tend not to show up, to that environment, in part because.
**Jason Plumb** 32:02 They're in another meeting.
**Ted Young** 32:03 We're in another fucking meeting, but… so maybe that's just another practical thing to sort out, is, like, maybe we could… move the Android meeting, and… and as a group, start… not just, like, attending for funsies and being bored through another meeting, but… but start bringing up The stuff we're working on on the client side to that group and to kick it off.
something we've been doing in that meeting that that people have found helpful, and I would love to like get the recordings out. There is just report backs from different Sigs and projects about what they're up to. Everyone has been finding those things like really helpful and enlightening.
**Jason Plumb** 32:47 It's almost like what we used to do with the maintainer meeting.
**Ted Young** 32:50 That's…
**Jason Plumb** 32:50 You know.
**Ted Young** 32:51 Inspect slash maintainer meeting.
**Jason Plumb** 32:53 Yeah.
**Ted Young** 32:54 And… and so we've been getting, like, we combined them because, like, two meetings was just too much.
But, there was a request to, like, have a report back from the, the, the client SIG. So, you know.
kind of, like, here's sort of where browser iOS, Android are today. Here's some of the challenges we're currently facing.
It would be really helpful, for the TC, the other maintainers, everyone to get a presentation about that as like kind of a good next step.
So I would say those two things, very concrete next steps.
If people… if we can… I don't know, I'm just gonna glance hard at Hanson, maybe, and stop glancing hard at Jason to see about, like, just someone who's been around the block for a while to… To maybe collect up some information from.
from the, you know, iOS and browser SIGs and Android S Be able to give a presentation at that meeting would be helpful. That would help us maybe figure out our current state of affairs as an exercise. And then getting this semantic conventions repo cooking.
And then we take it, take it from there.
**Hanson Ho** 34:25 Yeah, ping Jason last week about, hey, what if I just set up a repo and have stuff building? What are the next steps? So, like, you know.
I think doing that first step of, hey, I have a personal repo that's basically building a unlicensed, client and user, semantic convention federated repo, that's a good first step, So I gotta figure out some stuff on my side to… to carve out time, not just, like, pretend to carve out time. She's like, oh yeah, I blocked this day off to do this, and… And then, you know, you don't.
So I think that would be.
tremendously helpful. As for the client, the report, the roundup, well, we can discuss that. I have no idea what's going on in the iOS, like, for instance. So…
**Ted Young** 35:16 The other thing is.
**Jason Plumb** 35:17 That's why it would be good to learn about.
**Ted Young** 35:19 It's also like, like, yeah, it's just maybe just, yes, I went to their meeting for the first time in a while last week, so.
Kind of bringing them back in from the cold.
I think, I think would be good.
**Jason Plumb** 35:36 Time check.
Short meeting. Yeah.
**Ted Young** 35:42 Great.
**Jason Plumb** 35:43 Yep.
**Ted Young** 35:44 Like, concrete next steps. So, to get that repo done, that's just a… that's a request in the community repo, to make a… to make a new repo.
And we can maybe just take this offline. There is, like, the client, what do we call it? Like OTel client side telemetry Slack channel. So if you're not in that channel yet, please join that channel and we'll keep coordinating from there.
**Hanson Ho** 36:12 Excellent.
**Jason Plumb** 36:12 Sounds good.
**Ted Young** 36:13 All right.
**Jason Plumb** 36:14 Thank you, T.
**Ted Young** 36:15 Yo.
**Jason Plumb** 36:16 I…
**Hanson Ho** 36:17 Bye.
