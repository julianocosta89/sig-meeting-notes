SIG: Swift SIG
Date: 2025-08-14
Duration: 63 minutes
============================================================

## Zoom Recording Transcript

Ariel Demarco 00:01:28 In a nutshell.
nacho 00:01:32 Thank you.
Ariel Demarco 00:01:35 William?
nacho 00:01:37 Tobyan.
Vinod Vydier 00:02:05 Hey, people.
nacho 00:02:07 Vinat.
Vinod Vydier 00:02:09 Maybe not.
Ariel Demarco 00:03:11 Okay, so… Hi, everybody.
I think we are.
Out of right now.
I think we can start.
So, topics, from last week.
First off, it was the… repository division follow-up, so… I think Bryce… had this thing about going to create that Swift Country repo, and he was going to follow that. I don't know if he was able to do it.
I'm not sure if you know something about that.
nacho 00:03:46 Yeah, I, I… Yeah, he… he started talking with the committee and asked for it, and I think there were, yes, some steps that he had to follow up. I don't know if he finished that or not.
Ariel Demarco 00:04:01 Okay, so….
Vinod Vydier 00:04:02 So, just to be clear, what goes into the contract?
nacho 00:04:06 Yeah, that sounds good.
Ariel Demarco 00:04:08 everything but Open Symmetry PR and SDK. But the other day, I was reading, like, Alex PR, ….
nacho 00:04:18 Yeah, what?
Ariel Demarco 00:04:18 I think we have to discuss a bit on what things should go into that PR.
nacho 00:04:22 Yep.
Ariel Demarco 00:04:23 Into that, repository.
Vinod Vydier 00:04:26 Okay. Now, because there is the two separate efforts, right? One is the API-SDK separation.
Then the other is the… this is a… so that is… We know what can be separated, but what about contribib? There is not a lot of… contrib or instrumentation that is out of… outside of the API SDK, right? So… I think that's something that we will… I mean, it'll be a light rapport for now, and hopefully… As we add more.
But for now, there is not a… like, other contribib, right? I'm kind of comparing it to, like, Java or… Hotel Contrib. Hotel Contrib is the classic example that all the other repos follow.
The hotel contrib is, like, 100 times bigger than the… Hotel.
With the main hotel repo.
Put a collector repo.
Which is… yeah, which is the exact inverse here, right?
So….
Ariel Demarco 00:05:25 Yeah, I think that in that repo, it's going to be all the exporters that we have in the repository. I don't know if the URLs, all the instrumentations are going to be in the country or not. That's something that was… thinking, yesterday while reading the repository. And there's an open telemetry concordancy thing, that… is the one that we have as a separate product, but it's the one that made us bump to iOS 13, as far as I remember.
I was reading about that, because yesterday, when we reopened the issue about splitting the repositories.
I was looking at what… why we needed to… to bump to IS13.
And I saw that probably the main reason was that OpenTelemetry concurrency stuff, that I don't know where it should live at, if it's going to be on the OpenTelemetry Swift as another product, or it should go to the contrary ripple.
Alex Cohen 00:06:24 What's really interesting here is I put a PR up, like, about an hour or two after we spoke about it last week. I don't see that anyone has commented on it or anything like that. I mentioned… I mentioned that it existed. So I feel like we should probably go through it, because everything that you guys are talking about here is… is in there, and it shows what I think we should do.
with… With the division, I put, there's a folder that I created that's called Contrib. That would actually be the new repository. And I moved everything in there that should move to the new repository. Reason being that it makes it a lot easier if we start by moving things into that folder, and then doing a filter and creating the new repository from that to keep all history and whatnot. But, … you know, I put the PR up here asking for feedback, and so that we can actually move forward with it, because we could do this pretty fast and get everyone on board quickly and… and get things rolling, if we wanted to.
Ariel Demarco 00:07:27 Okay?
Alex Cohen 00:07:27 So, I mean, the questions that everyone is asking are.
partly already answered in the PR.
as is, what would go into what, if we should do this or not, and we can move the PR around until it ends up as exactly what we want.
Right? And when that's done, we can… we can actually do the real split.
nacho 00:07:50 Yeah, I've been taking a look, to the PR, yeah, and yeah, and I thought it would be better, yeah, to talk here in open than… Because I think, yeah, it's… it's more meaningful in an earlier stage. I have seen that you moved Everything that had any dependency?
Except, the atomics one, to the country, and you left all the… all the rest, including some instrumentation.
Alex Cohen 00:08:21 I don't think I left… did I leave any instrumentation? What I tried to do here was, yes, move everything that had any types of dependencies, because that's one of the big reasons that, other people who… who have forked, this repo, don't use this repo, is because of all the… all of the packages that come along with it that no one uses, except a couple… a few people, right? So that's… that's actually the real big issue that, personally, I want to get rid of.
And the other people using it also want to get rid of. So, I sort of left everything in this repo that has no dependencies.
Or things that are probably always going to be used regardless.
Such as the… the stud-out exporter, right? That's… that's probably something that everyone uses while debugging and things like that, so it makes sense for it to be there. The concurrency, exporter, makes sense as well.
So that's… that's what I try to do with this, and keeping as little dependence as possible is… should be one of the goals, I think, when we do this split.
Ariel Demarco 00:09:33 Yeah, I saw that you also got rid of The other, … dependency, this one, the atomics, you create.
Alex Cohen 00:09:43 Yeah, I looked into it to see why we used it, and it's one INT32, this one specific INT32. So, I mean… I feel like it's easier to just create our own small little package that handles it, and we could remove a lot of these functions that are not needed, but I don't think having one… a new… a pretty large dependency just for 1 in 32, is worth it.
Especially when we can fix it on our own like this pretty easily.
nacho 00:10:12 Yeah, I also saw that URL session instrumentation is missing, from both?
….
Ariel Demarco 00:10:19 Not sure. It seems he… it's here, inside… the sources… Is… in… in the country.
Panda repo.
nacho 00:10:30 So it's… Okay, yeah, but it's… But it's not in the products.
Ariel Demarco 00:10:36 Oh, oh, oh, oh, you mean in the package Swift here should have a product?
Oh.
Alex Cohen 00:10:43 So, that's a great thing that you could comment on the PR with, right? I'm… I'm not going to remember that you just told me here. If you….
nacho 00:10:50 Yeah, true, but….
Alex Cohen 00:10:53 Comments?
nacho 00:10:54 Yeah, but… yeah, I don't… Yeah, for me, we should… I don't know why you… I don't… I would like to have something understandable for the users.
So… Or we just have… the basic API and SDK in our repo, and all the rest in another.
Or we have something that… can be understandable from, for the users. For me, this is a bit… like, we have some exporters. I know they are the biggest parters, but we have some exporters here, some exporters in the other repo.
For me, it looks a bit confusing for the users.
So… I could understand having the concurrency here, because it could be, like, base library, but… I would move… the rest of the exporters, and also the… Those executables also to the country.
Alex Cohen 00:11:59 Yeah, Nacho, that actually makes total sense. I am… I would be 100% agreeable with that. The problem with it is that anyone who wants to use the most… the simplest exporter that usually has no dependencies basically ends up with all the dependencies, all the packages in their projects because of that. So… I tried to make it a lot simpler for those people. Personally, I don't use any of them. We might use one once in a while.
But I only use SDK and API, and Embrace only uses SDK and API, but say Datadog uses the stud, exporter, right? Standard output exporter, then they're going to complain right away that the problem has not changed.
Which is going to lead them to keeping with their fork. And that's… that's something that we want to strive to not have here. We don't want people forking this off and causing problems.
With all of the other people that actually fork off or use the OpenTelemetry SDK, and not being able to merge the same versions in SPM or any other packaging system.
nacho 00:13:15 Yeah, yeah, I… yeah, I can, … I can understand, yeah, that's… that's true.
… Yeah, but even then, I think if you are using STD auto-exporter, it's for debugging uses, and probably if you are doing that, you usually don't have problems with Big downloads in your… main matching. I think the main problem for Datadog was, for example, having that in the CI, where it took a lot of time to download all the packages, basically, more than on the developer's, ….
Alex Cohen 00:13:52 I think it's a little bit of both. They don't want all of those locally either.
nacho 00:13:56 Anyway, I wouldn't take… any consideration on what Datadoc asked for, because they have never been any positive about this, and they haven't, been lying about this project and what we were trying to do, so I would like to….
Vinod Vydier 00:14:13 Yeah, dude.
nacho 00:14:14 to keep them… what they do with their… I don't mind what they do with this library. They have been absolutely destructive with this project since the beginning.
I worked at Datadog, I know them, and they have been, like.
Many times about this, so I really don't want to take any decision based on what they ask for.
We should take the decision on what? The people who Are in this project, who help with this project.
And not with those that, have never committed a second of their time to this project.
Alex Cohen 00:14:52 So I would like to focus on the people that's here.
nacho 00:14:56 That uses the product, and that ask for help, and who… Participate in a constructive way.
Yeah, that's my position. So….
Alex Cohen 00:15:06 I understand your position, and it makes sense, and I… somehow, I feel I… I would have the same position.
But that's not reality. Reality is Datadog uses it, and it gets in the way of other businesses because of the way they're using it. We're only… Embrace is only one of those businesses that… that is having trouble because of what Datadog is doing with OpenTelemetry. Now, if it continues that way, we might need to do the exact same thing, and what we want is everyone to use the same….
nacho 00:15:38 Okay.
Alex Cohen 00:15:39 That's, that'.
nacho 00:15:39 That's why I ask it, people here, like Martin or Ari, what is your opinion about this? What… do you use other exporters? Do you use other things that we'll have to import, apart from the API and SDK?
Ariel Demarco 00:15:57 So, what I, what I think is, I've been reading the other repositories, even when I, when I share the response with the data dog in that data log issue, That's… the country repo has most of the exporters, but some exporters, for some reason, are in many of those repos, like in the Go and the Java, they are in the main repository, some exporters, like, for example, the… I don't remember in Java, but, for example, the… the… the one that uses gRPC uses… that exporter, it's on the main repository stuff. Maybe you can leave the default exporters?
I never opposed to that.
having all of them in the other repository, it's also nothing that I'm opposed to, because probably if you are using one of the custom exporters in memory, persistence, standard output, or something like that, probably you are using another exporter, and maybe you want to use the… Devase, Protocol Exporter, or some of those.
So… If that's the case, you're probably going to download the whole other repository of contrib.
But I have no strong opinions on it. I think that… Either having the exporters in this one, in the main repository, let's say, and in the contract, it's the same for me.
… I think that it's more understandable if we can leave everything in the country.
But… That's basically… I have more… Questions around the open sedimetry concurrency, but maybe we can discuss about that when we finish about this.
Yeah.
Alex Cohen 00:17:37 I, I mean, concurrency… is only for… I only left concurrency in there because it had no, had no dependencies, and was basically the same as SDK or API, whatever it's based off of. But, like, I really don't feel like it should be an area of contention. If someone says, no, I feel it should be in the contrib, then I, like, I 100% move it there.
If… if that makes it not a topic of discussion.
Ariel Demarco 00:18:04 Yeah, my question is… … I don't remember, because I wasn't here when it was created, this new product slash target, but why we have this… API. Like, it's, it's a… it's an API, so it's more comfortable for people using the new concurrency mechanisms and stuff like that.
Alex Cohen 00:18:30 Yeah, it doesn't really have too much in it, and I'm not sure if anyone using OpenTelemetry would end up using the concurrency package or library product versus just using OTEL within, like, regular code, non-concurrency code within their systems.
Ariel Demarco 00:18:49 My question is mostly because, like.
If at some point we want to move to the new concurrency mechanism, we'll probably have to change the OpenTelemmetry API.
interfaces?
So, I don't see why we have an open telemetry package, per se, or product.
But that's why I think it's more of a discussion another type of discussion, I don't see any reason of having an open elementary concurrency target.
….
Alex Cohen 00:19:18 Yeah, that's totally true.
Ariel Demarco 00:19:21 It basically, as you can see, depends on OpenTelemetry API, so it's kind of in the middle between an SDK and an API.
So, maybe in the future, it's just changes to the OpenTelemetry API target, and that's basically it. But maybe you, Natche, or Bryce, or somebody that was here, like, Vinod, you guys know way much more better than I do why this OpenTelemetry concurrency was created.
nacho 00:19:51 Yeah, it was basically a contribution from a user who really wanted to.
Alex Cohen 00:19:56 No. Use it.
nacho 00:19:57 That way. And it was not distractive, it was….
Ariel Demarco 00:20:02 Yes.
nacho 00:20:04 Yeah, so it was adding value for some people, it could add value for more. It's not the standard API.
So we separated into a sep… into another target. That was basically the… the reason. I mean.
They wanted to have this interface, and… It was probably easier.
Alex Cohen 00:20:24 Well, that clears it up. It was a contribution, so that simplifies it.
nacho 00:20:29 Yeah, it, yeah, it can be moved to country, if decided.
Alex Cohen 00:20:37 Perfect.
nacho 00:20:38 Yeah, I totally agree, Abra, about the atomic.
Vinod Vydier 00:20:43 Yeah, we talked about moving it a few times.
nacho 00:20:47 Yes, the one as well.
Yeah, and also because I think… was it Swift Atomics, the library that doesn't allow you to To build, … … Sorry, missing the name now. An XC Framework with it?
Because of the… Oh, yeah.
So it, it's really, yeah, we, we, we, we, we could probably, remove it.
Vinod Vydier 00:21:15 High time, high time you brought it in, yep.
Ariel Demarco 00:21:18 No, it's.
nacho 00:21:18 That's true.
Ariel Demarco 00:21:19 It's super big.
Yeah, you're right, Alex. It's a big thing.
Alex Cohen 00:21:26 Like, I would….
nacho 00:21:27 I don't… I… Yeah, I think I added that.
Long ago, because it made sense.
Probably in the old metrics, what was more used.
… Yeah, because using an atomic for something that's incrementing looks like a natural fit, but now that we moved to the new metrics.
I think that, yeah, we would remove that other use, from there, and….
Ariel Demarco 00:21:55 Okay.
Alex Cohen 00:21:55 not only is it almost not used, but all it's… it's only used for, like, an ID that gets incremented every time a class gets created or something like that. It's, like, the… the minimal use of it is… it's… it's… it's crazy.
nacho 00:22:08 Yeah, yeah, yeah.
Alex Cohen 00:22:09 We had that import for… for that.
Ariel Demarco 00:22:12 Yeah, here. Huh.
I see.
Okay, good catch.
Getting rid of her dependency.
That's great.
nacho 00:22:23 Yeah, I think it was used in the old metrics.
Ariel Demarco 00:22:26 Yeah, yeah.
nacho 00:22:27 Dundees.
Definitely.
Ariel Demarco 00:22:30 Okay, so, going back to… sorry, guys.
Going back to this… so, in terms of these exporters.
Are we planning to have them?
Here, or move them to the contrary.
I'm not opposed on any of those, so I'm okay with it. To having clear or having a contract.
Alex Cohen 00:22:50 I think to be super clear, about what we're doing, I think, Nacho's totally right, we should just move them to contribib. Anything except API and SDK should go over to contribib.
And maybe, if there's enough requests after that, we could end up moving it into the main repo in the future, if it needs to be.
Ariel Demarco 00:23:14 Okay.
I agree with that.
Alex Cohen 00:23:17 start with something that's extremely clean, only API and SDK in the main repo, and… And then… move backwards if we need to for anything specific.
While trying to keep it dependency-free.
Obviously.
Ariel Demarco 00:23:33 just….
Martin Holman 00:23:34 For you to remember it.
Just to be clear, we're talking about the… the non-Contrib repo, the primary one, will have no exporters in it, or…?
nacho 00:23:44 Yep.
Ariel Demarco 00:23:45 Yep.
Only the definition.
nacho 00:23:48 Only the API and the SDK.
So it's….
Vinod Vydier 00:23:52 That's not how the other repos are set up.
Martin Holman 00:23:54 Yeah, I think that's pretty non-standard.
Vinod Vydier 00:23:57 Yeah, that is… that is definitely not standard. In fact, it's not….
Martin Holman 00:24:01 You should be able to use just the main repo if you don't want to do anything special. Like, if you just want to send OTLP data.
You should be able to just use the main repo and not… Use Contrope.
Vinod Vydier 00:24:14 And that is part of the spec as well. So, having the open source exporters as part of the Project was there way before Contra Bever came up.
Give up.
nacho 00:24:25 Okay, yeah, that's another… possibility, … Having OTLP exporter, the default, the HTTP one that's basic and has no big dependencies.
But that also may… I mean, because the other… the gRPC one is the biggest exporter we have in terms of dependencies and complexity added to the repo.
Vinod Vydier 00:24:54 And Nacho, also the Prometheus and Jaeger ones, that's also part of the… They had it in a spec.
nacho 00:25:00 Yeah, yeah, I mean, yeah, we are… I know that that's in the spec, and we should… I mean, what the spec says is that the project should have support for all of that. It doesn't say in the same repo, or in different repos, or wherever. We are not breaking any functionality, but we… what… The, the, the thing is.
separating the… that was what Alex proposed last meeting.
was moving, … Many of those libraries.
or all of them into another conscript repo, so we… will then make… Such big dependency chain.
For the uses of the library for the most basic uses.
If anyone is gonna use Something more than that, he will have to… Have both repos and import the libraries that they need.
From… from the exporter.
So it will be, instead of just importing OpenTelemetry Swift, you will have OpenTelemetry, and OpenTelemetryShift, both of them.
You will import the… and once you have that, you could use the same libraries that you have now. But the difference is that it will be built differently.
Vinod Vydier 00:26:18 Yeah, I think that's, I completely agreed. The only thing is, I think the way it was initially designed, it was, … contributors for all the… like, if you… if you follow the collector contributors….
nacho 00:26:32 For third party, you mean?
Vinod Vydier 00:26:34 Yes, yes. For people….
nacho 00:26:35 distribution from… from third party and not….
Vinod Vydier 00:26:37 Exactly.
nacho 00:26:38 code that we maintain in the project, yes.
Vinod Vydier 00:26:40 Exactly, that's why it's called Contrip.
Alex Cohen 00:26:43 Yeah, I almost feel that Contrib is not the right name for the other repo in the case of the… of… of… Swift, just because of how SPM works. Now, we're… like, all of this is because of how SPM works, right? It's the… it… it doesn't allow us to do something really simple that we would like to do, and we have to live with it. So maybe contrib is not the right name for it.
Vinod Vydier 00:27:08 Yes, we are going from one end of the spectrum to the other end of the spectrum, and, you know, breaking some things in the process of, you know, like, if you have someone who's using OpenTelemetry Java, or OpenTelemetry Collector, or any other OpenTelemetry projects.
they would see something different because of the way SPM works, right? And this is exactly what Nacho brought up, … Way back when we were talking about this. And just to clarify on the Datadog position, they have attended all of two meetings.
The whole of the project.
So, I think, you know, they should put it in a contribib, I completely agree, but yeah, they are not the number one user, because we have a lot of other users that are I mean, but yeah.
nacho 00:27:52 But yeah, this is clearly not because of Datadog. … It's because, Alex And embrace, ask for it, because it… Was good for them.
And for the… for the uses?
Ariel Demarco 00:28:08 Yeah, I think it's good for the mobile community as a whole, like, any… anybody that, have a… has a project and all that stuff and uses the Macs on Mac stages.
nacho 00:28:17 Anyone who has a CI.
Ariel Demarco 00:28:20 Yeah, anyone who has a CI will have problems with downloading 300 megabytes for a dependency that, in theory, should be short. Like, OpenTeometry API and SDK API are interfaces, and SDK are just implementation of them, so… I think that's… that's the main reason why. I think that… the way Datadog pushed that, I don't think that was the greatest way of doing it, but in the end, it's part of what the community or the mobile community tends to ask.
Vinod Vydier 00:28:48 Yep, yep.
Alex Cohen 00:28:48 But to be fair, when Datadog asked for it.
I mean, I read through the, the, the issue, right?
nacho 00:28:56 Alex, you don't know all the things that they have done internally with the committee and, and, and… They have been, … They even, … I don't fi- sorry, I don't… they demanded to the committee that they forced us to separate API and SDK into different repos, because they said we were not following the spec. And they opened a… they opened a formal issue with the committee.
Alex Cohen 00:29:28 Hmm.
nacho 00:29:30 With full of lights, and things like that, so….
Alex Cohen 00:29:33 Yeah, no, I totally understand, but all of that… all that happened for a reason, hopefully it's in the past, and we can sort of get them on… different people are working on it now than the people that used to work on it.
nacho 00:29:45 the same people. I work with them, so I know them.
Alex Cohen 00:29:49 I understand you work with them, but other people than you have worked with them.
And other people do get along with them well, and… and can work well with them, so I think… I think we need to… move on from Datadog as the bad guy.
nacho 00:30:03 Yeah, totally, that's what I said. Let's move on. Let's turn… We are not taking decisions because of them. We are taking decisions because The users of this project and the people who contribute ask for them.
That was my position.
Ariel Demarco 00:30:19 So, coming back to the… We are spending way too much time on Zoom.
nacho 00:30:24 Yeah, they're feeling.
Vinod Vydier 00:30:24 One user, yeah, one user where they showed up twice. That's the whole point of this, … Pushback, and, you know, we don't need anyone to proxy support or, you know, talk on… advocate for on behalf of one user.
Ariel Demarco 00:30:39 I don't know, just… I think that we should just make decisions regarding this exporter stuff, considering what you said, you know, shall we just don't name it country, the New Repo, and when asked price to… I know he's talking with somebody to open this repository. Shall we that name differently? Shall we keep the protocol exporter and the HTTP exporter as part of the main repository? I think those decisions are the ones that matter today.
nacho 00:31:11 Yep.
Martin Holman 00:31:11 I feel like calling it not… I feel like calling it not… like, not using contribrib just makes things confusing, because, like, lots of people go between the different OpenTelemetry repositories, and if they're like, why… why does Swift have this… a contribrib we pron name something different? That seems a little confusing just for a name.
Ariel Demarco 00:31:31 Yeah, I understand that, but … that… the thing… the same thing… the same thing goes if they start reading the country, and suddenly they see exporters and stuff that should live in the other repository, so maybe we should make a decision and be explicit in the README or even in the documentation of the OpenTelemetry site.
So we explain why we're doing this. I think that there's a limitation on our tool, and the most widely used tool, because it's great… it's part of the language itself.
we should just explain why we're making this decision. And that's basically it. Either we are using Contrib with all… a bunch of stuff that shouldn't live in Contrib, or name it another way and say, hey, this is named in this way because of this or that.
Martin Holman 00:32:18 And what's… when you say other stuff that shouldn't live in Contra, what are we talking about there?
Ariel Demarco 00:32:23 So, let's say, open as I mentioned, protocol exporter gRPC.
That is one of our biggest problems, because it depends on gRPC, and gRPC per se, depends on other Swift, NIOS stuff, and big repositories. So, that's why it's either country slash other, with stuff that By default, in other repositories, leave in the main repository.
Martin Holman 00:32:49 Yeah, got it.
nacho 00:32:53 So if you think it's gonna… I mean, this is not a taken decision, right? It's like, we are gonna explore if it makes sense. We thought it will make sense, and that's why Alex is working on that PR.
But if you are, … Clear no to this change because of Any reason, it's not a decision taken, so… Yeah, we don't want to create problems too… To the… to the people that's using the, the library.
Right? So, … I don't think it will… I mean, the thing is, you will have to depend on if you are using URL session instrumentation or any other exporter that we have right now, it will.
You will have to import another repository, but… For those users, it should be the same. I mean, it will download everything.
And, anyway, right? Because we will be importing both repositories, so all the dependencies will be there also. Also, I think one of the improvements that it gives us is that we can update some, … some exporters or some independencies to a higher iOS version, for example.
We can't have something like that.
And not… and be able to support the API and SDK on a… lower version of the SDK, because we don't have to… We don't need to have the same version for all the packages.
I don't think it's… that's… that's really good or not, because if you, depend on one Of the exporters, they… they will have to keep the same, the same limitations for the… for all of them.
But that's what SPM provides us.
Okay, so let's continue with this topic, right? For the next meeting, it's still, … … Good.
And… and if you have any feedback, yeah, there is the… there is a draft PR.
That you can also add your comments. And we should all leave our comments there.
But as it was the first time it was here. So maybe… The idea… also the… the execute tables there. There were some execute tables in the… in the main repo now.
… right?
I don't know.
Ariel Demarco 00:35:21 Yeah. … This one.
Table metrics, I mean, Tracer, Cocorative context. Maybe those should move.
Alex Cohen 00:35:42 Are we okay keeping the basic tests, API tests and SDK tests, in the main repo?
nacho 00:35:50 I think we should keep the tests, yes.
Ariel Demarco 00:35:53 Yep.
Alex Cohen 00:35:54 Yep.
Ariel Demarco 00:35:55 Yeah, having testing at a repository will be cumbersome.
nacho 00:36:00 Yeah, and that's something that must also, we must… We must test also the other repo versus the released version of this one.
And… and we… we must find a good way to… To be consistent on releases and things like that.
Between both.
That now could be… I mean, now we could have separate versioning for the API and SDK and the exporters?
if we have different reports, we can have some different versioning, but I think that will be also probably, … Adding complexity.
Ariel Demarco 00:36:47 Okay, so then we can then discuss this exporter thing, and we shall continue with other topics.
Or wanna continue with this one?
nacho 00:37:01 I think we can move on, yeah.
Vinod Vydier 00:37:02 So, are we keeping the, the basic, the open source exporters in the same… Perfect.
Ariel Demarco 00:37:10 I think it's something… a decision to be made, but….
Vinod Vydier 00:37:13 Okay.
Ariel Demarco 00:37:14 We can… we can discuss it later, or even start.
discussing in WR.
Uganda.
you can argue in this comment, considering… I know, Martin, if you have a problem, for example.
in Honeycomb or stuff like that, that maybe it would be better to have them on the main repo, or even what you said on the chat, Vinod, you can… Added here.
Maybe that'd be good.
Martin Holman 00:37:39 That makes sense. I think I was just like, if all the exporters live there, then everyone's just gonna get both repos, and it's like, there's no split. Like, you should be able to use the small repo that we're making independently. Otherwise, everyone's just gonna use both, and we haven't done a bunch of work for seemingly not much point.
Ariel Demarco 00:37:57 Yeah, I understand.
nacho 00:38:00 Yeah, I don't know if having a simple… yeah, like, having a simple, OTLP exporter HTTP that has no dependencies That's interesting.
Martin Holman 00:38:12 And, like, if the gRPC exporter is the only one that's causing issues, then, like, maybe we have 3 repos, like Contrib and then gRPC exporter, like, if that's what… Yeah. The main issue we're trying to solve is… maybe that would be….
nacho 00:38:26 Yeah, I think it will be much easier if Apple fixed SPM and just downloaded the dependencies of the libraries that you are linking with.
That would be perfect, but yeah, they have had many years, and they have no turning.
So we… Exactly.
Martin Holman 00:38:42 Is… It's just because it's downloading the data, right? Like, is it… Yeah.
nacho 00:38:48 Yes, yes.
That's the main problem, is that it downloads lots of repositories, and it It doesn't even get a… it clones the complete repository.
It doesn't get a snapshot or something that could be much better either. So, yeah, great.
Ariel Demarco 00:39:08 It basically does all the downloading, tree dependencies, and then figures out, okay, what product are you going to use? Oh, this product that doesn't use all the added dependencies.
And that's… that's the problem.
Martin Holman 00:39:22 The problem locally is a little bit further than that, because if you make any changes.
Alex Cohen 00:39:26 Within a subpackage.
within a project, then, if you're in Xcode, which most people will be.
At some point, then it doesn't automatically update, you need to reset the packages, and then it downloads everything, like, everything again.
So, it's like, every time you make the smallest changes, add a file or something like that, you need to reset everything. So, it's… it's just problematic locally, but especially for CI, for people paying for the time that all of that takes.
Martin Holman 00:39:59 Locally, I can see. I feel like CI, I don't know.
That seems like it must be, like, sense.
But locally, it definitely makes sense, for sure.
Ariel Demarco 00:40:11 Okay, so… Another topic from last week. If you can, go and add your thumbs up to the PR, so the owner can go and see this, and maybe do the… the releasing Cocoa Pots, because… He hasn't done it.
Alex Cohen 00:40:27 He hasn't done.
Ariel Demarco 00:40:29 No, I think he didn't.
Let me go and check it out, so… Let's go… see… Oh, I have to check it out in a couple bots.
… Let me check it out.
No. Latest one is 3.8.0.
So… he doesn't.
Alex Cohen 00:41:13 Maybe we give him another week, and if he hasn't moved on it, we just do what… You folks have been saying is we copy in under a totally different name, private package.
And… just do that.
Ariel Demarco 00:41:27 Okay.
nacho 00:41:28 Yeah….
Alex Cohen 00:41:30 It's a bit ridiculous.
nacho 00:41:32 Yeah, that, that….
Ariel Demarco 00:41:33 Oh.
nacho 00:41:34 This is for the… for the cocoa pots, right?
Ariel Demarco 00:41:37 Yeah.
nacho 00:41:38 We are waiting for it, for the 2.0 version, final.
Ariel Demarco 00:41:42 No, I don't think we are waiting for that, because it's a pod that was never pushed, as far as I know, so it's… it's something that… it was not working before, as far as I understand.
nacho 00:41:54 Okay.
Ariel Demarco 00:41:55 So it's… it's nothing really, really new, but in the end, we're gonna… Move it away, eventually.
This contribution doesn't go.
nacho 00:42:04 Okay.
Ariel Demarco 00:42:06 New decision on view, … So, I think you added this, Alex?
Alex Cohen 00:42:12 Yeah, so I'm just, … I wanted to hear someone talk about why the… I was under the impression we made a decision on what we were going to do with you at the previous meeting, and it changed all of a sudden without Like, I understand that the maintainers have purview and all that stuff to do this, but I thought maybe it would be discussed and not just said, this is what we're doing and that's it?
nacho 00:42:36 Yeah, we have.
Alex Cohen 00:42:37 And if that happens a lot, people that are coming to the meetings, like, are gonna feel like they're not really having, you know, basically what I wrote here, that, like, it's not… what we're talking about is not really valued, and the decisions can be changed on a whim.
nacho 00:42:53 Yeah, true, true. Yeah, that's true. That's not what we have talked before. The reason… I mean, this was a conversation we, we had, the maintainers.
because Bryce was, doing the changes, And after… some work, he, realized that we… Should rename everything.
to be consistent with… we should have to rename everything that had view in the name to Metric View. That was the initial, decision that we took.
And… yeah, and … we took that decision internally, or the maintainers ourselves, because we were planning to release 2.0, and this was a… Thing that will change that release.
So that… that… that was the reason, that it was not talked here, or wait for this meeting, because we were planning to release 2.0 final release this week.
And that didn't happen.
because of the data compression, I think?
So, that's the reason. The thing was.
That renaming view to metric view implied that everything that had a view now wouldn't be consistent in naming if it didn't change to metric view also.
So that meant… That many classes had to change their name?
Just to solve a problem of… using… of using… The view, name, or… that classes, if you use OpenTelemetry SDK or OpenTelemetry IPA in a… in a class with SwiftUI, that's not gonna be so common.
We don't expect that to be so common.
So we finally decided not to change anything. That was the….
Alex Cohen 00:45:06 Those were the, … those were… those were the arguments used when we had the debate the first time, and you guys….
nacho 00:45:14 Yeah, that's true. And we, and we….
Alex Cohen 00:45:16 the way.
nacho 00:45:18 Yeah, I was… Pushing for renaming?
And I think that was the person who was Pushing more for renaming?
And I changed my view when I saw how many changes had to happen.
Ariel Demarco 00:45:35 one….
Alex Cohen 00:45:36 I'm assuming that.
Ariel Demarco 00:45:37 that I suggested, and I think that maybe we can review, is maybe do this change for this 3.0 thing.
We're going to do, so we don't stop 2.0 from going on production or live.
But we can do the change, so… as… As… for some reason, this could happen, if you are importing SwiftUI, importing OpenTelemetry.
Maybe I can do this in the new repository, or the new version, the 3.0, and… to the change. Eventually, we can do all… we can… do all the changes and the renaming of not only the view class, but other classes that has the view in its name.
Maybe it's something we can do, ….
nacho 00:46:24 And that's something also that… I would expect the compiler to… Not fail here in the future?
One thing is a protocol.
Po is a protocol, … the SuiteView IView is a protocol, and the OpenTelemma GSDK View is a class.
And the usage usually is a struct that's, implementing a protocol. I would expect the… the… compiler to not fail. If you are implementing a protocol with a struct.
It cannot be a class, right? So… ….
Ariel Demarco 00:47:05 It could also be.
Alex Cohen 00:47:06 Yeah, it's not in those cases where it fails, it's when you're passing it as a parameter somewhere.
So if you're passing a view as a parameter, which happens all the time, … at that point, it will fail, because it doesn't know what view it is. Is it going to be the protocol that you're using, or is it going to be the OpenTelemetry view? Also, I wanted to point out that view is not the only problem. There's also a class called, or a struct called span.
in Foundation, nonetheless, in Swift.
Yeah, that's true. Which can also be a problem.
nacho 00:47:43 Yeah.
And that was added also to the conversation last week. It was… and the thing was, are we gonna change all our names just because Apple is starting to use?
The same class names that we have?
And… Clearly, we cannot do that.
Alex Cohen 00:48:07 Yeah, I agree.
Ariel Demarco 00:48:07 I'm… Somebody tested that? He goes.
By default, Foundation is imported in every single file.
And the span… struct, if it's part of foundation.
… Should, by default, have a collision.
Isn't it?
Just… War.
for everybody to know, this is the Swiss fan.
And supposedly, it's been there since I was 12. I don't know if it's a retro-compatible feature or something like that. They just released, because this is kind of new.
Alex Cohen 00:48:47 It's backported, actually.
Ariel Demarco 00:48:49 So, if it's backported, maybe… I don't know if somebody has X126? I don't.
Maybe they can test it out and see if there's a problem when compiling?
If there's a problem, then it's a blocker.
….
Alex Cohen 00:49:07 There's a chance there won't be a problem, because it uses generics.
So, to be a type, you need a type of element in there, whereas Vue, you don't.
Ariel Demarco 00:49:21 Yeah, maybe.
Alex Cohen 00:49:22 But anyway, the basics is, like, I don't want to spend more time on this because I understand what you know, the organization here wants to do and has made the decision. But, thinking of it in a way where we have it this way, so it needs to be this way, which causes problems to other people, which… which goes… which, you know, has problems with the… the global namespace of something that the first party is actually exporting, is probably… for most customers of this product, probably not the right way to look at it. We should try and get out of people's way, and not get in their way. This is explicitly, purposefully getting in their way.
Which can be an issue, even if we pointed out a workaround for it.
nacho 00:50:21 Yeah, that… That's true, yeah.
But the renaming made… us renamed too many things, and we… Don't expect that to happen.
frequently, having SwiftUI. Import SwiftUI and import OpenTelemetry.
In the same file, like a usual thing to happen.
Ariel Demarco 00:50:57 Okay, … any new topics that we want to add? If not, we can just review some issues or PRs. I raised a VR with some tests, but….
nacho 00:51:08 We'll review that later.
Ariel Demarco 00:51:12 In new topics?
Alex Cohen 00:51:15 Second, I have a question.
on the same topic, I'm just… does anyone know where Observable is in the… in the SWIFT libraries.
Ariel Demarco 00:51:24 Yeah, underscore, … underscore.
Alex Cohen 00:51:30 No, but is it in SwiftUI? Because if you need to import SwiftUI into a file.
Where you have your models and stuff.
or things like that, or coordinators, or anything that might actually use OpenTelemetry, you have SwiftUI that's important.
Ariel Demarco 00:51:48 It's not in SwiftUI, it's an observation framework.
Alex Cohen 00:51:52 Yeah?
Ariel Demarco 00:51:52 It's another one.
Alex Cohen 00:51:55 Okay.
That argument won't work then.
Ariel Demarco 00:51:58 It's independent.
So… I just have this… PR, … Year.
So, I have a questionnaire on this, maybe… You guys know what's happening.
It's failing the tests on iOS, macOS, and tvOS. It's weird, because it's working on VisionOS.
But the V layer is saying, unable to find device matching I.O. Simulator.
And the destination of OpenTelemetry Suite Package says.
It's only macOS, Driver Kit, and macOS.
But for some reason, it's working on VisionOS, so… All of this seems to not be installed. It's even saying PGN OS is not installed.
So, it's… it's kind of weird.
I don't know if you guys know what could be happening.
Alex Cohen 00:52:57 But do you have a place where you have to install all the expected platforms, required platforms? Usually there's a step in actions where… Where all the platforms are installed that are required.
Ariel Demarco 00:53:13 So, basically, it's running on macOS 15. As far as I know, macOS 15 has all the… has Xcode with all the simulators.
nacho 00:53:26 Yeah. My quest.
Ariel Demarco 00:53:28 15 runner.
Alex Cohen 00:53:29 Yeah, I understand that, but you have no step to make sure that all the simulators are created that are required to run it. Like, you can… if I go onto my Mac, I can delete all the simulators I want, and then if I run tests, and I expect them to run on those simulators, the tests are gonna fail, because the simulator just doesn't exist.
Ariel Demarco 00:53:49 Yeah, yeah, I understand that, but… Why?
nacho 00:53:51 Yeah, but….
Ariel Demarco 00:53:52 It's that….
nacho 00:53:52 You only added two methods, right? And it fails.
Ariel Demarco 00:53:56 Yeah, yeah, it's, it's, it's basically this. It's, it's… You know, the, the, the… the bug we had the other way, the other day, and the contribution that had no test, I basically had a test to it so we don't forget about it. It's just that this beer is super, super simple, and for some reason.
We started having issues.
And my question is, we did some changes to something related to the CI in those… in these days.
Nope.
Because this is… is weird. I understand what Alex points out, but… I had never had this issue with macOS runners.
Because they should have the… the… the simulators, so….
nacho 00:54:44 Yeah, that, that, that, yeah, I have also, seen that before, and it's really strange. We have not changed anything, so it has failed repeatedly.
Ariel Demarco 00:54:55 Yeah, I made 2 runs. I rerun this.
Two times.
For some reason, keeps… keeps failing, keeps failing.
And it's weird, because… it works on VisionOS, and it shouldn't, because it's Vision OS.
for iOS and iPadOS completely.
nacho 00:55:14 Week.
We can try rerunning any of the… of the other….
Ariel Demarco 00:55:20 Yeah, sure. I think we're gone.
nacho 00:55:22 We'll rerun the… the one that….
Ariel Demarco 00:55:25 All five shows.
nacho 00:55:28 The… the… one of the… Dependencies changes that… Not our, … Yeah, I have also rerun another pull request that automatically was created for an update.
… But, yeah, probably something….
Ariel Demarco 00:55:52 Yeah. Maybe it's something weird, I'm… Just rerunning helps, but it was weird.
nacho 00:55:58 Yeah, definitely it was, yeah.
Ariel Demarco 00:56:01 So there are two new issues, as far as I saw.
these two.
how should we create meter provided in 2.0? I think this… person is right. So, if you go to… create a meter provider builder. The ENIT is not public.
So, it was pointed out that this person should use MetroProvider and the builder static function, but it actually returns a no-op meter provider builder. So, my question is, shall we make this They need public, or shall we… return a meter provider builder.
With some specifics.
nacho 00:56:50 I think the builder… Should be created by the… SDK?
So probably something not being well initialized?
Ariel Demarco 00:57:00 Yeah, let me go.
nacho 00:57:01 Yeah, that… That's probably… Bryce, ….
Ariel Demarco 00:57:07 this is the meter provider builder, so the need is private, so they say use meter provider SDK, To do it with the static method, and this is the static method, builder.
And it basically returns the NOAP builder.
But in case we want to create a… the other builder, the one that I was looking before, the meter provider builder, You would have to provide some sort of… Thanks.
So… I don't know.
nacho 00:57:43 But the build… there is a build method there, right?
Ariel Demarco 00:57:47 This one, yeah.
And this creates an SDK.
nacho 00:57:50 Okay.
Ariel Demarco 00:57:52 But if you go to the SDK, basically that is what it's saying, use the meter provider builder static function.
If you go to it.
It basically returns to no op.
interprovided viewer.
And it returns a NOAP meter probability builder, so I don't think this was done… this wasn't… Purposely.
To return this.
So we either have to change this.
So, it returns an actual builder.
nacho 00:58:32 Yeah, I… Yo, yo….
Ariel Demarco 00:58:41 Because the init of the metrics provider SDK is kind of big.
And basically, the builder, the meter provider builder is what's doing that.
So, I really don't know what's the best way to do it. Like, there are two solutions to this problem. So, either make public the other one, or this return the actual builder.
nacho 00:59:02 Let's, let's, let's ping Bryce here.
Okay. Because I, I… I… I think there is something in that… flow that's… Probably the build… that builder shouldn't be there, because it should… I… Be created in another way.
Ariel Demarco 00:59:27 Great.
The last one… Hope bye, Dave.
And the last one is gRPC from metrics not working in 115.0, so… Here's the light.
It's an old version, I don't know if we made some fixes or changes.
to gRPC.
metrics.
for metrics?
nacho 00:59:57 ERPC format is not working.
Ariel Demarco 01:00:00 Yep.
nacho 01:00:01 No, we have not changed anything, I would say….
Ariel Demarco 01:00:06 I think Binop answered this.
nacho 01:00:09 Yeah, I… That was a nice answer from Vinat.
ask for patience? Yeah. ….
Vinod Vydier 01:00:20 Yeah, we need to look at… make sure that all these things… so users are, you know, seeing the things that are breaking, yeah, we need to… Maintain the stuff.
nacho 01:00:30 Maybe there are some… Changes in the collector?
Because that version, which is that version, that 115?
Siro is the collector.
Some new version of the collector that's failing?
Ariel Demarco 01:00:54 Isn't this… 115.0, it's the collector version.
our version.
nacho 01:01:04 Is it our….
Ariel Demarco 01:01:08 sour.
Vinod Vydier 01:01:13 Yeah, we should also actually ask, what is the version of collector that this user is using?
nacho 01:01:16 Yeah, we have… our version is 1.17, but… Because sometimes we, we… I've seen in the past that the collector change things?
And… and makes it incompatible with… no, Collector is 138.
Ariel Demarco 01:01:36 Okay, I'm, I'm… I'll wait for this to answer, and then we can move forward.
The other issues that were reviewed last week didn't have answers from… From anybody? Here, you, you answer natural?
Yep. And the other one….
Vinod Vydier 01:01:53 The latest version of the collector is, … 138, or…?
0.132, right? So that is definitely not what… Yeah, he's talking about, I think, … Yeah, but they did mention 115, right? So….
nacho 01:02:09 115, it could be hour, that he's using our 115 version, probably.
Vinod Vydier 01:02:14 Yeah, no, Collector never had this one-point version. I think it's… that is a new thing.
So it was always a zero-point releases.
So, yeah, this is something that is definitely our version, not the collector version.
nacho 01:02:30 But we have been updating the collector on our tests also.
Vinod Vydier 01:02:34 Yep, yep, yep.
nacho 01:02:35 Because it would have been….
Vinod Vydier 01:02:37 We've been to….
nacho 01:02:37 More or less in sync.
Vinod Vydier 01:02:39 Yep.
We've been making sure that Protobuff is updated right now.
nacho 01:02:44 Yeah, but probably there is something in Protobath that needs to be updated, that could be a… something that has happened in the past.
Yep. Changes in the protobath, … Definitions that we have not catch up.
….
Ariel Demarco 01:03:02 Good.
Okay, I think that we can wait for… For him to answer this question, so we can fully test this and see Why it's not working.
Okay, I think we are running out of time. We're 3 minutes late.
So, I think that's… Boise.
Vinod Vydier 01:03:22 Thank you.
Ariel Demarco 01:03:24 See ya, everybody. See ya next week.
Martin Holman 01:03:26 Peel.
