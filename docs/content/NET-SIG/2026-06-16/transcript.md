SIG: .NET SIG
Date: 2026-06-16
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Itay Sagui (Microsoft)** 03:30 Hello.
**Martin Costello** 03:31 hype.
**Itay Sagui (Microsoft)** 03:32 Hey, Martin.
**Martin Costello** 03:35 Nice to meet you, how are you?
**Itay Sagui (Microsoft)** 03:37 Nice to meet you as well.
How do these meetings work? It's my first time here?
**Martin Costello** 03:49 So usually there's a couple of people join, primarily the maintainers, but also a few other interested people, and we just talk through what's on the agenda, or any other topics anyone wants to bring up.
**Itay Sagui (Microsoft)** 04:06 Okay, so how formal is this?
**Martin Costello** 04:09 Not that formal.
**Itay Sagui (Microsoft)** 04:11 Okay.
Okay.
**Martin Costello** 04:18 I know one of the other maintainers isn't attending today. I don't know if either of the other two are gonna join the call or not.
**Itay Sagui (Microsoft)** 04:28 That makes my life much easier.
I've gotta… Present my case film to you.
**Martin Costello** 04:34 In the worst case scenario, if it's just me and you, we can have a chat about it, and then we can just put some notes in the issue and see what other people think.
**Itay Sagui (Microsoft)** 04:45 Okay.
**Martin Costello** 04:47 Because, yeah, occasionally, sometimes this happens, like, no one else will come to the meeting, so then it either doesn't happen, or there's a conversation, but it doesn't quite, you know, reach… reach consensus point. There's not enough people talking about it.
**Itay Sagui (Microsoft)** 05:04 Yep.
Excellent.
**Martin Costello** 05:06 But, thank you for making the time to join.
**Itay Sagui (Microsoft)** 05:09 Yeah, no problem. Not that late, as I was fearing it's gonna be in the middle of the night.
**Martin Costello** 05:14 Yeah, it's like, for me… for me, it's, like, right… well, it's not at the end of my working day, it's, like, a bit after my working day, but I always attend every Tuesday, I just… because it's kind of an important part of my job, so I make… I make sure I can attend.
**Itay Sagui (Microsoft)** 05:30 Are you based in the UK?
**Martin Costello** 05:32 Yeah, I live near London.
**Itay Sagui (Microsoft)** 05:34 Okay.
**Martin Costello** 05:35 The other maintainers, one lives, I believe, in Poland, and the other two are in the US.
**Itay Sagui (Microsoft)** 05:42 Good.
**Martin Costello** 05:49 I can see two people have the agenda open, but I don't know if that's me and you, or… oh, there we go.
**Itay Sagui (Microsoft)** 05:55 Me, yeah, that's me, probably.
**Martin Costello** 05:56 tip.
It's, it's Alan.
**Itay Sagui (Microsoft)** 05:59 Hi, Adam.
**Alan West** 06:01 Hey, Ed.
Hello. This is everybody.
**Martin Costello** 06:06 Good, thanks.
Through at you.
**Alan West** 06:09 Oh, just good.
So, Raj is gonna be out for a bit.
**Martin Costello** 06:25 Yeah, I guess he saves a Paulie's holiday for the whole year.
**Alan West** 06:30 Yeah, yeah, I think that's what he does.
Hiti, are you with Raja's team?
**Itay Sagui (Microsoft)** 06:45 Nope.
Never met him before.
**Alan West** 06:48 Oh, okay.
**Itay Sagui (Microsoft)** 06:50 I'm part of the STO ADX team, actually.
**Alan West** 06:55 Which team?
**Itay Sagui (Microsoft)** 06:56 the ADX, the Azure Data Explorer team.
**Alan West** 07:00 Oh, okay.
**Itay Sagui (Microsoft)** 07:01 What's, worse.
Heavy on observability and, telemetry.
Quite a big team in Microsoft.
**Alan West** 07:12 Cool, okay.
**Martin Costello** 07:13 That's cool. I had not heard of that particular acronym before.
**Itay Sagui (Microsoft)** 07:19 We go under several names, like, it's Custo, it's the internal name, and Azure Data Explorer is the marketing name, and now this is the new one under the fabric, Branding, fabric event house, They keep renaming us for some reason.
**Alan West** 07:40 Gotcha.
But anyways, you're under the same, like, Azure umbrella, as Roz and… Others, yeah.
Very cool. Are you up in Redmond?
**Itay Sagui (Microsoft)** 07:56 No, I'm in Israel.
**Alan West** 07:58 Oh, okay, okay.
**Itay Sagui (Microsoft)** 08:01 Let me figure out where Ratch located.
Doing the org.
**Alan West** 08:08 Yeah, he's up in Redmond, but yeah, I mean, I don't know Microsoft, the Microsoft work zone.
**Itay Sagui (Microsoft)** 08:13 We're… we're actually under the same organization.
Amazing enough.
Nope.
**Alan West** 08:18 Gotcha.
**Itay Sagui (Microsoft)** 08:19 Not directly, but we basically report to the same CVP.
**Alan West** 08:27 Cool.
Well… Martin, looks like you got a couple things on the agenda, should we…
**Itay Sagui (Microsoft)** 08:35 Nope.
**Martin Costello** 08:36 Yeah, so the… so the first item on the agenda is actually Itays.
Item, which is the pull request about lazy allocations.
**Itay Sagui (Microsoft)** 08:49 Yeah, I can present the case, basically.
we're using the OpenTelemetry client quite heavily, and we have in our services quite a lot of metrics, and we started moving to OpenTrademetery relatively recently.
So we have around, I want to say, 400 or 500 metrics. Some of them have very high cardinality, because some of them are using a database name, or table name, or something along those lines as one of the dimensions.
And so we ended up defining a relatively high max cardinality limit.
Which, you know, goes around $50,000, which is a little bit above our expected, cardinality.
But in some areas where we are running with limited capacity, like under cgroup or JobObject in Windows, we end up having limited memory, and the initialization with all the pre-allocation that it does end up Gulping, basically, a half a gigabyte of memory at least. We saw something around 700 megabyte of memory.
Which was substantial. The idea was that, basically, we defined the Marx maximum cardinality, but in… some of those dimensions, we don't know beforehand how… what their cardinality is going to be. So, for example, if you're looking at table name, we might have a customer which has two tables in his database, and we just allocated 50,000 metric points and all the other arrays over there, just for having very low cardinality, being emitted, while others might have 40,000 databases, or 40,000 tables, and we actually need that memory, but we don't know that beforehand. We don't know that as part of the process startup.
And so the idea of the PR was to lazy allocate those, Those arrays and those buckets.
And basically allow resizing the arrays as… As the usage grows, up to the original limit that was the… that was part of the metric.
Or as part of the configuration.
**Alan West** 11:32 Okay.
Yeah, I think I get the, a high level… Thing you're getting at here.
So you, you're, like, in sort of, like, a hosted kind of situation where you're trying to… Basically, your end users don't have direct ability to, like, configure their SDK. Like, you're…
**Itay Sagui (Microsoft)** 12:12 No, we're a database provider, so we're basically saying, you know, we're a database, and we're meeting our own metrics for our own observability.
And the customers will have zero interaction, zero visibility, where the client here, we're both the client and the server, in this case.
**Alan West** 12:32 I see, okay, okay, okay. So this is for your observability, not the… not the actual, like, customers, end users.
**Itay Sagui (Microsoft)** 12:38 Gotcha.
**Alan West** 12:40 But when you… when you spin up, of course, like, you know, whatever, the database, you don't have any sense of… Yeah, the, cardinality that's gonna be… In play, for any given…
**Itay Sagui (Microsoft)** 12:53 Yeah. So, the way we approach it now, before this PR, is basically we did a full review of all the metrics, and we discovered some of our metrics have very low cardinality, and those are pretty easy to fix, so some of our metrics, we just set up the max commonality to, you know, to 10, or 20, or 100, because we know the dimensions, we know the values, but some of them are customer-driven.
**Alan West** 13:29 Let's see, I'm just glancing over, see Joe's comments here, you know, and I could probably actually…
**Itay Sagui (Microsoft)** 13:38 I think I've addressed… I think I've addressed most of the comments, if not all of them.
**Alan West** 13:44 Leave me.
**Itay Sagui (Microsoft)** 13:46 I do have… theoretically, a minor one or two additional performance improvements, but I think we can do those, you know, after this PR.
Assuming this PR is going to be approved.
I think the main… Open question is whether we want this as a default behavior, or we want it behind an opt-in flag.
Obviously, I don't care either way, but I don't… I'm… Concerned a bit about in changing the default behavior for other customers.
Why are they useless?
**Alan West** 14:27 So… let's see… He has another comment… So where did I see this? Oh, it was in your description.
So… I guess one of the things that I think CJ is saying is that he's not excited about the configuration, or adding… adding to, like, the public surface area of the configuration, which is… I share that concern.
You know, we try to, our public-facing APIs, we… we try to stick to the OpenTelemetry specification, and this… this is kind of like a… implementation nuance, I guess, as I see it.
**Itay Sagui (Microsoft)** 15:17 You're welcome.
we could change the behavior to be based on an environment variable, something like that. That way, the API itself isn't… change… isn't changing, the public API doesn't change, it doesn't expose anything, but we still keep the ability to opt in to this behavior, at least until we can obviously document that, and at least until we get some feedback from users that this actually works as expected, I didn't introduce anything that we didn't expect, or something like that.
Because you can see the performance impact is substantial. Not only the performance as well, but also the amount of memory allocated.
just huge.
**Martin Costello** 16:02 Yes, something I did suggest as a comment on the issue was regarding environment variables, because it might tie in with the fact, you said something about cgroups, so maybe this is something it could, like, dynamically do based on the built-in .NET environment variables.
To… Tell the runtime that it's running in a container?
**Itay Sagui (Microsoft)** 16:27 I'm a little bit reluctant about this, because we're actually not running in a container.
So I'm…
**Martin Costello** 16:33 Alright, gotcha.
**Itay Sagui (Microsoft)** 16:34 have, yeah, I'd much rather have a dedicated flag and not try to, you know, cheat my way into this feature by setting an environment variable that is not true.
And so I much prefer having a dedicated flag for that.
One way or another. And again, it could be a temporary until the, you know, the next version, or the version after that, where this becomes the default behavior.
And you guys, as maintainers, can tell me if you guys want it to be the default behavior, I'm just… I'm fine with that, obviously.
**Alan West** 17:12 Yeah, I don't… you know, having not had a chance to really deeply think about this too much.
I don't think we'd necessarily want it to be the default behavior. I think… again, I haven't read through this whole thing, but CJO kind of gets to the… point, like, we… The behavior that we have today was… intentional.
So as to avoid… You know, complicated, like, allocations on the hot path. We… We optimized for… metrics being recorded, like… Very fast.
You feeling?
**Itay Sagui (Microsoft)** 17:54 If you'll see the reply by Ziv.
That speaks actually from my team, a little bit few comment down, down the line.
Basically, after a few minutes of metrics meeting, you're basically going to stabilize on the correct the correct size.
And… And you're gonna basically end up, you know, it's gonna be some kind of warm-up a bit in the beginning, and afterwards you're gonna be stable. I guess the question is whether the… The whole process is a short-term process, or short-lived process, where you want to pre-allocate fast, and then running, on whether it's a Long-running process, gonna be run for weeks on, and, you know, the warm-up time that's of a few minutes is really not that important.
**Alan West** 18:47 Yeah, so you'd reach a steady state, and that would, of course, benefit the longer-running apps.
**Martin Costello** 18:54 I guess is what that… ties a bit similar to my comment about containers, is, like, for users who've got, like, throwaway environments, like containers running on, like, crons or, like, serverless functions.
They probably want the opposite behaviour, because they want to start up fast.
**Itay Sagui (Microsoft)** 19:22 This is actually the reason why it might make sense to… To keep some kind of control level, whether it's an environment variable or A setting on the… on the API, on the configuration, but gives some control based on… preferred behavior.
**Martin Costello** 19:41 Thinking out loud.
maybe we could introduce a setting that's, just to make up a name, like, is constrained Environment?
Which could cover things like low memory containers, serverless, and then that setting Could feed into other things.
So that then we're not exposing a setting that's… Like, specific to how it's currently implemented, and it's a bit more generic.
And then… the new behavior you've added could then, like, be one of those things that, if it's a constrained environment, change how you do it. Because, like.NET itself tunes how it does memory allocation in the garbage collector based on those sort of heuristics.
**Itay Sagui (Microsoft)** 20:31 Never.
The concern in that side is… might be that We're gonna overload that setting with different behaviors which are unclear to developers.
On what exactly that means, or what exactly is happening, and you might end up a single option that does Several things that might not… Go together, or might not, correlate to what customers expect.
**Martin Costello** 21:02 journals.
**Alan West** 21:03 So from the standpoint of, like, if we look at this through the lens of, like.
This constrained environment context.
I would doubt that you would ever set the cardinality limit to 100,000 in a constrained environment, because I think it defaults to 2,000, which is…
**Itay Sagui (Microsoft)** 21:19 Yes.
**Alan West** 21:21 Which is… Probably works for… Many, many, many end users.
Your scenario… probably is more the outlier. I'm just guessing. I mean, honestly, I don't have any data on this, so I can't say any of this super confidently, but… Right, you're… you're not in, like, this, like, constrained environment situation.
Personally.
**Itay Sagui (Microsoft)** 21:49 Well, the process itself is constrained. I mean, we're running with 6GB of memory, and taking half a gig… We're running with 6GB, and taking half a gig only for telemetry is… A huge number.
**Alan West** 22:06 Yeah, okay.
**Itay Sagui (Microsoft)** 22:11 But I do agree that the concept of the… or the wording of the limited or constrained environment might be misleading, because we're saying.
slightly different or slightly opposite thing. We're saying we need constraint, on the other hand, we're actually talking about Allocating a huge amount of… or supporting a very large cardinality limit.
But just in a lazy fashion.
So, they're not exactly contradicting, but might be… cause some confusion.
We could go with something like dynamic cardinality limit, and not say that it's a lazy allocation, just say that the limit is dynamic.
Or something along those lines.
**Alan West** 23:09 Yeah, that kind of, though, suggests that, like, the cardinality limit changes.
to adapt to, you know, the size or something like that, but that… that I don't think is really what… year after. You just don't want to go, like, a cap. It's a kind of a max.
**Itay Sagui (Microsoft)** 23:25 Yeah, I do have to say that the original issue is that cardinality limits refers to a limit, you know, to… you know, it's a maximum limit, and not necessarily a pre-allocated, warm everything, create everything beforehand. Or at least that was my understanding when I first read it, until I actually went ahead and looked at the implementation and saw that it pre-allocates everything Because limit says limit, doesn't necessarily mean that I'm going to emit all those, and we need to allocate all the memory for them.
But again, that's… that's already one… water under the bridge here.
**Alan West** 24:04 Yeah.
So names and what we call it aside, I… I'd still want to think about this some more.
Personally, I don't know where you're at, Martin, but… I… I think… I think avoiding changing the public API, would be a… Good thing.
I would at least… it would at least alleviate, you know, some of the controversy that I think you'll probably get with this PR.
For myself included. But CJO commented on it as well. And maybe going with an environment variable of some sort.
And then… the other thing that I would personally need to kind of refresh my memory on is… Probably want to talk to CJO, because… He worked on this pretty extensively back in the day.
like you said, there were intentional reasons why it was designed the way that it was, and I'd want to… Talk through any concerns you might have.
on that front. But again, if it were… if it were an environment variable, That we did, It might alleviate some of those concerns, and certainly if we, you know, didn't have this be the default behavior, you know, like, we didn't change the behavior today.
And this was opt-in.
I think that would alleviate some of the concerns.
**Itay Sagui (Microsoft)** 25:52 DJ, is that CGO Thomas?
**Martin Costello** 25:56 Yes.
**Alan West** 25:57 Yep.
**Itay Sagui (Microsoft)** 25:57 Okay, so he's also from Microsoft, I can ping him as well.
Yep, yep.
**Alan West** 26:01 You can, yeah, he's… He used to be one of the maintainers of the .NET SDK.
And he and Raj I don't know that they're on the same team anymore, but they were at least at one point in time, so they…
**Itay Sagui (Microsoft)** 26:20 Two of us report to the same manager at the end, same CVP, so I… I can have a direct chat with them, that's not gonna be a problem. I can easily… pings them, and… At least get their thought on the subject, and… ask them to at least review the PR and comment on it.
**Martin Costello** 26:42 Yeah, also, if you… as you probably don't interact with Raj much much, it sounds like, Raj is going on extended leave at the end of this week.
So if you want to reach out to him, you probably need to do that in the next couple of days. Otherwise, it's not back until August.
**Itay Sagui (Microsoft)** 26:58 Okay.
So, that's first thing tomorrow morning.
**Martin Costello** 27:05 Yeah, it sounds like… The use case, like, is valid, and there's probably other use cases that would fall into the same bucket. It's just how do we design it in a way that makes sense Sort of long-term.
Good old naming.
**Itay Sagui (Microsoft)** 27:30 Yep.
Yeah.
**Alan West** 27:33 Exactly.
**Itay Sagui (Microsoft)** 27:34 I think the first thing I can do is… Move over to, Move the behavior to… the flag to be a… Environment variable, and so that's gonna be at least pushed back on some of the resistance that is, you know.
Makes sense, obviously. But at least we can… It can make people more comfortable with this behavior.
**Alan West** 28:03 Yeah, I think that's a good thing, and yeah, and we can… we can bike shed over… over the naming of, you know, what that environment variable should be called and whatnot, but… you know, yeah, make an initial… Suggestion, and we can go from there.
**Martin Costello** 28:18 Yeah, there's some prior art. If you search the repo, there's some prior art for, like, variables that start with, like, hotel.net experimental.
**Itay Sagui (Microsoft)** 28:29 Okay.
Yeah, I can see, I can see, I can see a few of them.
Okay, no problem. I'll take a look at those and see.
Exactly how they're implemented, and… Yep, no problem.
**Martin Costello** 28:51 Cool.
**Alan West** 28:52 content. Yeah.
**Martin Costello** 28:53 Yeah, I think… yeah, I think there's… there's enough.
here for you to, like, continue working on it, but yeah, I think we'll just need to finalize The nitty-gritty details before getting to, like, the point of… merging.
**Itay Sagui (Microsoft)** 29:10 No problem.
**Alan West** 29:14 Hmm.
**Itay Sagui (Microsoft)** 29:15 Okay, so I'll issue a fix to the PR, and I'll also ping CJ and Raj to see if they can chime in on what they think about it.
**Martin Costello** 29:28 Okay, cool.
**Alan West** 29:30 Sounds good. Thanks.
**Itay Sagui (Microsoft)** 29:32 Thank you, guys.
**Martin Costello** 29:38 I know it's late for you, Itay, so feel free to leave the meeting, but obviously you're welcome to stay if you wish.
**Itay Sagui (Microsoft)** 29:46 Okay, thank you.
**Martin Costello** 29:50 So the other item I put in the agenda was the end of last week.
Someone from the profiling SIG opened an issue… asking, hey, when's the Don Aresky SDK gonna do profiling?
And, it was… for me, it was on very short notice, and, Matt was kind enough to go along to the meeting.
To see what was going on there.
And… Not to put you on the spot, Matt, have you got anything from that meeting you'd like to share?
**Matthew Hensley / Grafana Labs** 30:27 Nothing that would be, surprise to anyone here. The profiling SIG was unaware.
of the distinction between, like, the .NET Zero code and SDK.
They assumed it was more aligned like the Java agent is, where the Java agent's kind of the default.
for everyone, and they were unaware that, the zero code's already a profiler, or consuming the profiler slot on .NET Framework, so… It's, yeah, it's mostly just giving them some background on some of the .NET implementation difficulties, and They are gonna send some folks along to comment on this issue.
Seems. I see there's a couple… Nope, there isn't yet. But yeah, they said they were gonna have some folks from some other vendors that are experienced with .NET profiling.
Come take a look, and… Potentially weigh in with their experience.
**Martin Costello** 31:31 Okay, cool. Thanks, Matt. Yeah, I figured I'd just bring it up, as it's probably going to eventually be a thing.
We need to know about it and know what we're gonna do about it.
But that was mostly it. It was more of an awareness thing, rather than a, we suddenly need to do something.
**Alan West** 31:54 Yeah, I'm aware of… the prototype that the auto instrument… I mean, I guess Peter is claiming it's more than just a prototype.
Hmm.
Anyways, I'm aware of it in the auto-instrumentation, though I've never actually used it. It sounds, though, that it's not… I wonder what it's doing, because if it's not… sending data over OTLP.
Then… That's probably the main thing that the profiling SIG would want.
Because, right, they're looking to stabilize the OTLP data model and all that.
So… Yeah, they'd probably be… the auto instrumentation group would probably be a great one to… Work with on that.
if… We wanted to support something separate and apart.
from the Auto Instrumentation group, then… I don't… do any of you have, expertise with any, like, profiling libraries within the .NET ecosystem that… Could be used to… achieve the goal? I'm not, personally.
**Martin Costello** 33:19 I am not. I've just used, like, the high-level tools.
And I know there's loads of gnarly C and C++ in the profiler, I spare it.
**Alan West** 33:29 Right, yeah, the… the auto-instrumentation uses the Microsoft Profiling APIs, which… Enables you to… do thread profiling, and, well, all, I guess, all sorts of profiling, memory profiling, and… And whatnot. And… my knowledge of profiling within the .NET ecosystem is, like, that's the de facto standard, is, like, a tool that leverages the profiling APIs.
Which, the auto-instrumentation… product is.
So…
**Martin Costello** 34:05 Yeah, I think if we did have to go down that route, my only concern is The sort of weird… Cyclical chain of… SDK's got… Build the models.
But then, where would the profiler live, and then what does zero code do?
And ideally, we wouldn't have to have any native code in the main SDK repo.
Because otherwise, we're, like, doubling the number of languages people need to know about.
Initial settings.
**Alan West** 34:43 Yeah, you're thinking, like, if we were to implement something on top of the profiling API that's… that's separate from the auto-instrumentation product, then, of course, that would be implemented in C++.
**Martin Costello** 34:57 Yeah, and then how do… how do they… how do you use the two together? Because there's the whole, you can only have one profiler, and then also there's the complications of how do you… Have the right native dependencies.
Get installed with the app at runtime.
Because I've seen many different approaches for that, and I've never seen… never seen a nice one.
**Alan West** 35:23 No, I know, I know, that's a whole… That's a whole quagmire. And… to the point of, like, the one… only one profiler running at a time, there was a group at Microsoft at one point that I think was trying to tackle that problem, but I… I've been so far removed from that space for a number of years now that I've not tracked whether there was ever any progress to that. There was some… there was some work being done by this group So that you could run multiple profilers. And… it was typically, like, use cases where, like, there were two products using the profiling APIs, but they were basically meeting, like, different purposes. Like, you might have some security product or something like that that leveraged the profiling APIs in an entirely different way than, like, an observability product.
Wood, and so they didn't… There was no reason for them to not be able to, you know, run together.
Because they didn't conflict with one another.
In a way.
**Matthew Hensley / Grafana Labs** 36:29 So I dropped a link to the, project you're talking about, it's… Not production ready?
It's not.
**Alan West** 36:37 Yes, this is… Matthew Hensley / Grafana Labs 36:38 Yeah, they…
**Alan West** 36:38 instrumentation engine, yes, I've spoken with this team years ago. Yeah.
**Matthew Hensley / Grafana Labs** 36:43 So, they… you can see, like, the… some of these years, like, how long it's been, and they never… like, this is apparently used at Microsoft?
But they have not upstreamed all their internal improvements, it's just kind of frozen.
Here, because the newer versions of the runtime support this natively, in a way, with, like, notification profilers, so you can wire up a second one for some messages, and it… they can cooperate like the intention was here. The rub being, of course, that not available on .NET Framework.
Can tell you, from my experience, we're getting asked pretty regularly. It feels like… almost weekly now, about, profiling .NET Framework apps.
There's a whole lot of end-user demand for it.
**Alan West** 37:40 For sure.
Yeah.
Anyways, yeah, this is probably not really much of a thing, but in any case.
Yeah, I really feel like, for the .NET ecosystem, I really feel like if… Profiling is of interest, then… the… Auto-instrumentation product is Probably the product for you.
**Martin Costello** 38:16 On a sample size of 4 on this call. That's not me. I like the idea of having profiling, but I want the control.
**Alan West** 38:30 Yeah, I mean… I… I would hope… you… what you control specifically over profile, and I guess the way that I was thinking about it is, like, again, I haven't actually used the Iowa instrumentation product all that much, but… but my… My hope would be that you could still use the SDK, right?
Or is that not true?
You could use the SDK for, like, configuring trace metric, and log kind of behaviors, and… Right.
**Martin Costello** 39:02 Okay, yeah, yeah. Oh, yeah, that's fine. I thought you meant more, like, you don't touch your app and Big Black Box takes care of… takes care of it for you.
**Alan West** 39:13 Yeah, like, basically I'm saying, like, I'm not… I… I… I'm with you, like, you know, I appreciate having the fine-grained control, that just using the SDK allows I'd be okay, though, with, like, you know, running the black box so long as that controlled It's still available to me.
**Martin Costello** 39:43 Yeah, because I think some solutions, sometimes they require to run, like, additional side containers, or things like that, and… or install other things on your box, and, like.
for the stuff I run personally, like, that's so overcomplicated, I would never run it.
Whereas dropping… adding a few DLLs to my app and setting a few settings is relatively simple.
**Alan West** 40:14 Yeah.
**Martin Costello** 40:17 But yeah, obviously, not everything has to work for every use case, but .
**Alan West** 40:23 That said, I wonder if, like, you know, again, not knowing anything about this product, I can't say for sure, but I wonder if it could be implemented in such a way that it could be run independent of the… auto-instrumentation product. So, like, it could run as part of the auto-instrumentation product, but it could also be run independently. So, like, if you were an SDK user.
then… you'd use the SDK as you always have.
But then… You'd run this specific Profiler that's just, like, this extra thing, and you just gotta figure out how to run that in your environment.
**Martin Costello** 41:03 Hmm, yeah.
**Alan West** 41:06 That kind of a model might be kind of neat, if it were possible.
Needless to say, obviously this group is the group that has the, the expertise.
That they've built up.
So, I think that they're the best group for the, profiling sake to probably… interface with.
**Martin Costello** 41:42 Yeah, I think that makes sense. Yeah, I figured I'd bring this up just for discussion.
As… whichever way it goes, we're gonna need to be involved in… at some level.
**Alan West** 41:56 Yeah, it's cool. I mean, it's… Profiling.
It'll be exciting when it's a thing.
**Martin Costello** 42:04 It's also… it's also, like, inter… it's… it's… it definitely is interesting, because… some of the performance changes I've made in the last… 6 months, have been from me digging through profiles on the apps that I put hotel in, and going, what… why is, like, metric writing in the top 10?
things.
So, there is a sort of a virtuous feedback cycle of having it, that it feeds back into this as well.
**Alan West** 42:36 For sure, yeah. No, profiling is super valuable.
I… I mean, I use it, Relatively.
Regular basis.
For diagnosing things. Usually at development time.
You know?
**Martin Costello** 42:53 Hmm.
**Alan West** 42:53 I'm somewhat skeptical of, like, the people who are like, I want real-time profiling, things that are running, like, in production all the time.
But, Yeah, that kind of use case where you're, like, actively developing, and you just want to, like, take a profile and get a sense for…
**Martin Costello** 43:09 Yeah, I don't run it in, quote, production on a lot of the things, but I do on a handful of things, because every now and again.
you've got nothing else to do. Just have a quick poke around and see what's there. And there's nearly always something you've never considered just lurking.
It's like, why is that happening?
But yeah, it's definitely more the… more the edge case than the default behavior.
**Alan West** 43:41 Cool.
So yeah, Matt, are you… are you gonna continue to be engaged with the profiling group, or you just kind of, like, made an initial intro or something?
**Matthew Hensley / Grafana Labs** 43:52 I'm happy to… stay involved. I work a lot with the auto instrumentation.
Or at least end users trying to use it.
And I've been looking into profiling, that's how I could find the CLR engine.
Thing immediately is just in my notes.
So, happy to stay involved, but I'm gonna be, out on PTO, starting.
Shortly here, so… you'll, you know, Somebody, wants to have a meeting.
About it, feel free to go ahead and… Do that, and we can see what we can come up with.
**Alan West** 44:30 Cool, okay.
Grafana, 6 weeks of PTO, are you taking 6 weeks?
**Matthew Hensley / Grafana Labs** 44:36 No, I'm taking, like, two and a half.
**Alan West** 44:40 Nice.
**Matthew Hensley / Grafana Labs** 44:43 So that's why I was like, if someone really wants to get the ball rolling, like, you know, if the Zero Code folks want to start things, like, there's no reason to wait till I'm back.
**Alan West** 44:57 True.
Alright, cool.
Any other thoughts from anyone?
Sounds good.
Well, take it easy, y'all.
**Martin Costello** 45:17 See you next time.
