SIG: Zig SIG
Date: 2026-07-01
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Francesco Gualazzi** 01:16 What do you want me?
**Giovanni Panice** 01:17 I mean?
I don't hear you.
**Francesco Gualazzi** 01:20 I don't dance for the street.
**Giovanni Panice** 01:22 Okay.
And you shouldn't see me.
Okay.
Nice.
**Francesco Gualazzi** 01:36 I'm good.
**Giovanni Panice** 01:38 Oh, rude.
**Francesco Gualazzi** 01:40 Nice.
**Giovanni Panice** 01:43 I don't know if, but this is the week, Where Antonio…
**Francesco Gualazzi** 01:49 Antoine is not going to join this week, unfortunately.
**Giovanni Panice** 01:52 Okay, I think that we'll do this, work together.
**Francesco Gualazzi** 01:59 We can start triaging some of the… some of the issues in the board. Let's see if someone else is joining, and then…
**Giovanni Panice** 02:07 Okay, let's wait, let's… yeah, let's do a couple of minutes, and then…
**Francesco Gualazzi** 02:11 That's why I can tell you, I archived the old repo.
**Giovanni Panice** 02:16 Okay, cool.
**Francesco Gualazzi** 02:17 And if you take a look right now in the home page… So in the main README, I created a… banner on top that says, this project is not mandated anymore, we're proud to have moved it under OpenTelemetry at OpenTelemetry 3. So, there's a link to the new repo, and…
**Giovanni Panice** 02:39 Perfect.
**Francesco Gualazzi** 02:40 So it's read-only, which means that, yeah.
It's… it's there. Also, I had already ported all the issues in the board, so… I hope new things come… In the bottom?
Soon, but we can start to look in at those, the open ones right now. I know… Jacob asked the… in the Zlap.
If the declarative configuration is, is, available, and I said, no, there is a cardboard for that.
The problem there is the YAML parsing, because, again, there is no out-of-the-box standard library support in… in Zeek, and what we've been using so far, is a library that I wrote myself, so yaml.zig, it's a library that sits in my…
**Giovanni Panice** 03:34 You have written the parser for YAML, Spend time.
**Francesco Gualazzi** 03:40 to… I had to, and it's… it's not… it's not complete, it's probably passing… finger and recording is 75 to… 65-70% of the sweet test.
But, but it's, let's say it's good enough.
And I don't know if we want to use that as a dependency, because again, it's, It's not the best. Just like what Antoine did with GFPC. I get it, it's a… it's a blind spot in the Zeek ecosystem, but we cannot just take personal projects and ship them into… Production code of our community repo, and… and… go easy with that, no? So, I figure that's where probably someone with higher seniority than us in the community can give us some guidelines, maybe? But yeah, maybe I should write them in Slack about it, I don't know. But yeah.
So that's my only concern, you know, so… because anyone can develop something new, and say, oh, this solves this specific problem that nobody else solves, take it as a dependency, and then, you know.
That's a bit dangerous, no?
**Giovanni Panice** 04:59 Yeah, exactly.
Correct.
**Francesco Gualazzi** 05:02 Okay, so, 5 minutes in, let's just go in and see and triage these, these things.
I don't know, how do I know what we should do it? Can I share? Let me see if I can share… Maybe I can do this.
Ben, do you see my screen?
Good boy.
Thank you, Pat.
**Giovanni Panice** 05:24 Yes, I can see it.
**Francesco Gualazzi** 05:26 Alright, let me go.
So… Alright, this one, I don't know what's happening with this one, honestly. I… I think Renovate wants to do something with our, With our, need of actions, but every time I check this box, nothing happens in the repo, so… I don't know, maybe I should just close.
**Giovanni Panice** 05:51 Hmm.
**Francesco Gualazzi** 05:52 But okay, leave it there. This one, I think, is very important, and we should do it, someone should assign it to themselves and do it immediately.
The evening needs to be reviewed and improved, and we need the contributing attendee.
And I think your suggestion to be inspired by what the Java repo has done is greatly… is on point. So, yeah, not sure…
**Giovanni Panice** 06:20 If you want, you can assign to me, if, don't worry, if you don't have cycle, don't worry, I can get it, so…
**Francesco Gualazzi** 06:26 Alright, that, that would be amazing, thanks.
around that.
**Giovanni Panice** 06:31 Okay…
**Francesco Gualazzi** 06:33 And now, into the backlog, right? Because this is the juicy part.
**Giovanni Panice** 06:38 Yeah.
**Francesco Gualazzi** 06:40 Alright, let's go with the… what I think is the most… Priority one, right?
**Giovanni Panice** 06:47 Okay…
**Francesco Gualazzi** 06:48 I believe… The most priority one… is not even gRPC.
is, putting the proto also in, in this repo.
Because…
**Giovanni Panice** 07:04 Okay.
**Francesco Gualazzi** 07:05 Because, I'll tell you why, To do this, we need to figure out How we structure the repo.
With one built.zig file that can build multiple modules, and how we can export these individual modules so they can be consumed.
by… by other, you know, other projects, other Zeek projects, right? So… I think this is… this is needed.
And, to do that, actually, I believe… We have to check, huh?
Ding Here… I believe we have to check… Oh, yeah, I upgraded already this one to 016, nice.
I didn't even remember doing that, but okay.
Which means that… Also, this one could use… an upgrade of… no, it's already using Protoba 5, which is the latest, and we'll check that later.
And, yeah, so… yeah. I will assign this to myself, because I have an idea of what to do.
Anyway, before doing that.
Honestly, I would like to form some consensus here, but I see nobody yet picked up my suggestion to…
**Giovanni Panice** 08:34 My… Only about that. If you don't have cycle to work on this issue, at least, I mean, write your idea, okay?
Okay, write your idea in the comment, and don't assign it to you until you think that you can work on it, okay? This is only, I mean, a suggestion, okay? I don't know, so… Because, yeah, so… so if you have some cycle, write your idea on what you want to achieve it, or we can keep the discussion about that.
But, if you don't have… you are not sure to have a cycle on that, you can assign it to you when you are ready to do it, okay?
**Francesco Gualazzi** 09:28 Makes much sense.
**Giovanni Panice** 09:29 So, because we are maintain… are maintainers, we are maintainers, so we don't need to ask for a sign to ourselves, so, you know, well, so-and-so, so, but again, yeah.
**Francesco Gualazzi** 09:43 What I would like to… to see, if… with, some noise on social media, like, X… LinkedIn and such, we can… we can start gathering more people in the project, and so I will do that this week, possibly. No. And we'll try to… We had to figure out how… on the whole thing about… Well…
**Giovanni Panice** 10:12 What we can do for sure, for example, and something that, I mean, I was, I mean… it's not the topic now, right now, to talk about that, but one thing that we can do is also to propose the project as, in the Linux Foundation for, you know, mentoring, things like that, so we can have someone that can contribute, you know, to the project.
This is an idea, like, you know, the Minux Mentoring Program, so… for the Cloud Foundation, to have someone to contribute. This is an idea, but it's not, I mean, the topic right now. It's something that we can discuss with the other But, to having more contributors, I mean…
**Francesco Gualazzi** 10:57 Okay.
**Giovanni Panice** 10:58 And I think that Zeek… and I think Zeek is, I mean, a really interesting project to having, you know, contributors, so… I'm, positivo.
Yeah.
**Francesco Gualazzi** 11:10 Nope.
Anyway, I have no clue how that would happen, but I can ask, as well in the Slack channel about it, if you want… Hope you'll see that.
**Giovanni Panice** 11:23 Hmm?
**Francesco Gualazzi** 11:24 Nope.
I wouldn't that?
**Giovanni Panice** 11:30 Okay. Okay, okay, don't worry. Okay.
**Francesco Gualazzi** 11:35 Then, let's see… Then, if Antoine would be here, I would say that this is the next.
big thing, so…
**Giovanni Panice** 11:46 Hmm.
**Francesco Gualazzi** 11:47 We need this. We need this.
As soon as the repo is well formed, and the PR.
**Giovanni Panice** 11:55 Hmm.
**Francesco Gualazzi** 11:55 Diamond.
And we are able to show how to use it.
**Giovanni Panice** 12:00 -
**Francesco Gualazzi** 12:01 we should definitely support gRPC, because right now, HTTP Proto is fine, but gRPC is what most people will use.
So some way, one way or the other, we would have to… we would have to support, right?
**Giovanni Panice** 12:19 Yes.
And, I mean, I don't know, do you want to assign it to one-to-one, or, I don't know, we want to wait in, so… No, okay, okay, it's not.
**Francesco Gualazzi** 12:31 to hear from…
**Giovanni Panice** 12:33 Sadly.
**Francesco Gualazzi** 12:33 He had created the PR in the old repo. In fact, the PR is still there.
**Giovanni Panice** 12:42 For that issue?
**Francesco Gualazzi** 12:45 Yes?
I think it… Well, is it even March, so maybe I don't know, No, no, no, no… No, no, no, no, probably not, maybe I'm mistaken. But, Oh, yeah. Oh, we closed it? I don't remember what happened here, let me see…
**Giovanni Panice** 13:18 I think he decided to… to split it, I don't know.
**Francesco Gualazzi** 13:26 Because now, yeah, we upgraded to 016, and, yeah, probably he was a bit, thrown off by… by this thing, okay.
And there's another PR from Antoine that we… I probably want to bring over, so I think this, Easy option, but of course, this one This is, let's say, an iteration…
**Giovanni Panice** 13:57 Yes.
**Francesco Gualazzi** 13:57 DJ episode.
**Giovanni Panice** 13:58 Yeah, yes, yes.
**Francesco Gualazzi** 13:59 other driver, so yeah. Okay. Yeah, let's wait for him to come back online, or I will ping him in the channel, see if he wants to… To assume this stuff by himself.
Or no, and then we can self-assign.
the, the continuum.
Cause that, that one would be the next one, also.
**Giovanni Panice** 14:25 Hmm?
**Francesco Gualazzi** 14:26 conv module.
And it would… semantic conventions?
**Giovanni Panice** 14:31 Hmm?
**Francesco Gualazzi** 14:32 And that's… that should be relatively straightforward to do. I would assign to Hendrik if it would be… More provocative, but again, no worries if he's not able to… To follow us in these meetings, it's completely fine.
Let's see… let's see.
**Giovanni Panice** 14:52 Well, we can… I mean, is it… I mean, if it's, I get priority, on the exemplar, you can assign to me, and I can, work on it, so…
**Francesco Gualazzi** 15:04 No.
I mean, this one needs to land first, because it defines…
**Giovanni Panice** 15:10 What?
**Francesco Gualazzi** 15:10 Everything else, you know?
**Giovanni Panice** 15:12 Yeah, yeah, I know, but this is… one is virtually assigned to you, okay, so… Okay, so…
**Francesco Gualazzi** 15:18 It's not… it's not, assigning to me, but I will…
**Giovanni Panice** 15:21 Sure.
**Francesco Gualazzi** 15:21 Juanita.
**Giovanni Panice** 15:22 Okay, so… so, I mean, if you want, you can assign me to me to the Open Generally semantic convention, it's, it's feasible for me, so… And move the priority on the exemplar, because I think that exemplar are,
**Francesco Gualazzi** 15:42 And samples are interesting stuff, and we should definitely… we have a lot of to-dos.
**Giovanni Panice** 15:50 It's not assigned to me. Can you assign to me? No, it's assigned to you.
**Francesco Gualazzi** 15:55 the…
**Giovanni Panice** 15:56 In the previous, in the previous, okay. I don't know, but, I mean, the exemplars were assigned to the previous, to the… the other reposito, yeah. But, yes. But, okay, so leave it, for now in the.
**Francesco Gualazzi** 16:12 Yeah, in the bed.
**Giovanni Panice** 16:12 one another.
Yeah, okay, so… assign to me… I don't know if you want to give priority, as I said, to the exemplar or to the semantic convention, so… because the read means, like, one minute to finger, but…
**Francesco Gualazzi** 16:25 No, I think it's better to keep this on top. Okay. Well, if I should order by priority, this should be it, so… The SDK configuration…
**Giovanni Panice** 16:40 Okay, okay.
**Francesco Gualazzi** 16:42 And, this, this for J-Compo?
Yep.
**Giovanni Panice** 16:48 Okay…
**Francesco Gualazzi** 16:49 And, this one… Not this one.
Don't.
**Giovanni Panice** 16:56 Okay.
**Francesco Gualazzi** 16:57 down… Profiles need to go up.
So, documentation goes, here.
Yeah.
**Giovanni Panice** 17:08 Okay.
**Francesco Gualazzi** 17:10 That's probably the order in which I would do things, honestly, because the RPC, top of mind.
And then the various modules that we want to move, in this new repo, and figuring out the build structure.
The declarative configuration, which is something that, is getting a lot of attention and traction, because People want to variety YAML all the time.
**Giovanni Panice** 17:36 Hell, yeah.
**Francesco Gualazzi** 17:37 This is… this is a… this is a goal that we have only done for logs and traces, we don't have it for the metrics.
So yeah.
This needs to be done.
And also this one, and yeah, the benchmarks actually go all the way down.
Because we have… Very good benchmarks already.
And, yeah, I think that would be… Profiles… I guess profiles is already in the portal, let me check.
So, supporting that in the SDK, it only means, basically, to provide Accessory?
Antels, something like that.
Let me check here.
Yeah. So, in the proto, we already have it as a development.
Probably they upgraded that to stable, I don't know, I have to check.
But, but yeah.
So… that would be interesting to… to dig it.
Other than that, I think we're super good.
**Giovanni Panice** 18:53 I don't know, as I said, if you want, you can move to read it, the one related to the semantic convention, and you can assign to me, so… if you want. Otherwise, if you want to leave it in the backlog.
**Francesco Gualazzi** 19:09 I don't know, I will. Everything that you want to take, I'm not going So…
**Giovanni Panice** 19:15 I'm not very…
**Francesco Gualazzi** 19:16 to take it, what's that?
**Giovanni Panice** 19:20 Oh, I mean, Antoine is full of things to do. You are full of things, so… if we don't speak…
**Francesco Gualazzi** 19:27 Are you on holiday, or what?
**Giovanni Panice** 19:31 No, well, you know that, I mean, next… the next week will be, like, yeah, it's, like, fire for me, so…
**Francesco Gualazzi** 19:39 It's not gonna be easy for me, but okay. So this was the library that I was mentioning before, so…
**Giovanni Panice** 19:45 Ugh.
**Francesco Gualazzi** 19:45 Yeah, you can see… you can see the CI is not happy.
Oh, sorry for that. The official YAML test suite contains, like, probably a thousand use cases, which are also intricated, stuff, like anchored, encoded, nested, nested keys, it's, it's, it's total…
**Giovanni Panice** 20:10 And, I mean, he's not, I mean… It's not something that…
**Francesco Gualazzi** 20:13 I didn't really use it.
**Giovanni Panice** 20:14 We need, we need the two, okay, yes.
**Francesco Gualazzi** 20:16 But, this one is actually used, and I have to remember where… I think we use it… Here, I have proof.
No.
Not here, sorry, in the call. I think we do use it already, I don't remember for what, honestly, but… Why's home.
Oh, boy.
No, it's not here. I don't remember when it's used, but I think it's… Have you been deprato?
No? Okay, never mind. Another interesting thing that I think would be, in a very decent future, would be providing a collector implementation on Zeek, that is, building on top of the existing SDK and proto primitives.
So… because the collective performance is always, something that is, concerning to many users, and despite there are a lot of work streams.
Into… and a lot of efforts into making that, First-class, performance bikes.
I don't think that nothing pits going into, no garbage collective language, without having time versus garbage collection language. So, eventually, with garbage collection, you will always hit a point where you either do some very dirty things to not incur into excessive garbage collection, or you pay the false prices, so… Providing a collector, a lightweight collector, maybe, indeed, would be such a… such a nice use case for performance-heavy.
And ingesting heavy workloads?
That is apparently a nice thing to do. It will not be as complete as the current implementation, which has tons of modules and porters and receivers, and processors, and all that.
But it would at least start to unlock, potentially, and display some of the capabilities that you can… that are available to you when you go into lower-level language, like Rexit.
But yeah, just wondering here, I don't wanna go too far with that.
**Giovanni Panice** 22:52 Okay.
**Francesco Gualazzi** 22:52 What else? I guess we're a fan, no?
**Giovanni Panice** 22:57 Yes, we have, I mean, at least we have put the priorities, we have assigned something… I mean, we have assigned some tasks for the attendee today, so I think it's…
**Francesco Gualazzi** 23:09 to you. I mean, you are assigned to this one right now, but now I will provide, S… 1… 2… Post notes of trouble.
And I also made this second page here that I hope will be filled in by someone.
So… Yeah.
IP, And… And this one is, like… Oh, I saw that. What did we do? We assigned the 1, 2, 3… Yeah, we're assigned 3 of them, and… And prioritize the rest.
**Giovanni Panice** 24:12 You can say… you can write, assign it to the attendee, and periodize the backlog, so…
**Francesco Gualazzi** 24:21 Alright.
Nice!
Oh, that's all for me, my friend.
**Giovanni Panice** 24:28 Me too. Me too, Fran.
**Francesco Gualazzi** 24:32 Yeah, then, good luck!
Every day.
**Giovanni Panice** 24:36 Enjoy.
**Francesco Gualazzi** 24:37 Howdy, y'all today?
**Giovanni Panice** 24:39 your last days.
Your last 3 days.
**Francesco Gualazzi** 24:43 days of freedom.
Enjoy those.
Tune in.
**Giovanni Panice** 24:48 Okay, so, I mean, maybe you have to update the… the attendee.
No, no, no, yes, I see, sorry, I don't know, because I confused it from the other meeting. Yes, okay, cool. Yes, yes, it's, I think it's all, it's all, clear, yes.
Well, one idea in brainstorming, if we want to add something, is to, start thinking on some, talk about, the, the, the library.
I was… well, I'm still thinking about that. As, I mean, the OpenTelemetry library is, I mean, an open library for observability, what we should try to think, to brainstorm is some interesting use case In which we can use the OpenTelemetry SDK for Z.
Okay, so, I mean, I don't know, I was thinking something like, you want to observe, I mean, some application, something really tiny, I don't know… I don't know, because, I mean.
**Francesco Gualazzi** 26:10 Yeah, or…
**Giovanni Panice** 26:12 Exactly, so we have to… I don't know. I have some S, I should search… I have some, STM32 board.
And I can, I don't know. I can try to play a bit. So, I have to search this… this board, and I don't know. It's an idea, I don't know.
**Francesco Gualazzi** 26:36 I'd be very curious to know if, if that… that works as intended, because that's… that would be… that would be… beautiful, to see it on a… on an embedded board, or, you know…
**Giovanni Panice** 26:54 Yeah. I have to… I have to investigate. If I have cycles, if I have fire, I have time. But, yeah.
**Francesco Gualazzi** 27:01 I wish you will have… So, I will also wish you NOS has…
**Giovanni Panice** 27:06 Yeah, exactly. Anyway, so Francisco, enjoy the rest of the day, so thank you very much to drive the session and to be Elways.
Yes, so…
**Francesco Gualazzi** 27:17 I will try to do my best forever and ever.
**Giovanni Panice** 27:21 Thank you.
**Francesco Gualazzi** 27:23 What?
**Giovanni Panice** 27:23 Bye, thank you. Enjoy your day, bye.
