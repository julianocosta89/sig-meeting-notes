SIG: Go Compile Time Instrumentation SIG
Date: 2025-11-27
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Yi Yang 00:00:08 The table.
Timo Zhu, where you go there?
Ziming Liu 00:04:45 We might be comfortable.
You will lose your mind, as well.
A million in there.
It's closed out.
That's amazing.
Kemal Akkoyun 00:17:20 Hello.
Przemyslaw Delewski 00:17:22 Aye.
Kemal Akkoyun 00:17:23 Sorry for the misunderstanding.
Huxing Zhang 00:17:27 Hello?
Kemal Akkoyun 00:17:34 Alright, who wants to lead the meeting, or, like, who's supposed to lead this one?
Huxing Zhang 00:17:42 Yeah.
Przemyslaw Delewski 00:17:43 I just…
Huxing Zhang 00:17:43 picking, the latest agenda there, and it seems that last time was mine.
It's my turn.
Kemal Akkoyun 00:17:53 Okay.
Is it… who's next? Oh, no, no, your turn. Okay.
Huxing Zhang 00:18:01 Last time. Last time is my, my… I'm the… I was the facilitator, I think.
Kemal Akkoyun 00:18:09 Who's next? I'm still trying to open the doc, sorry, just opened my…
Huxing Zhang 00:18:13 I think it should be Roman, but since Roma is not there…
Kemal Akkoyun 00:18:20 We can pick the next one.
Huxing Zhang 00:18:22 Paris Mac, I think it's…
Przemyslaw Delewski 00:18:26 Okay, do you hear me?
Huxing Zhang 00:18:28 Yes. Right.
Przemyslaw Delewski 00:18:31 Yeah, so let me… give me a minute, maybe.
Huxing Zhang 00:18:35 Okay.
Kemal Akkoyun 00:18:48 When is the last… last time we met? These dates are… Seems wrong, like, we copied overwriting from the previous one.
And I think we met… 3 weeks ago, maybe beginning of November?
Przemyslaw Delewski 00:19:06 I don't remember.
Huxing Zhang 00:19:09 Yeah, that's true.
Kemal Akkoyun 00:19:12 Good.
Huxing Zhang 00:19:13 Yeah, the tip… the date was the… looks like it's wrong.
Kemal Akkoyun 00:19:21 Okay.
I guess… There we can start. We have, I think, the biggest agenda item right now. I don't know how to put that in words. I guess we have some disagreements on instrumentation, and… We should discuss that.
Huxing Zhang 00:19:40 Right?
Kemal Akkoyun 00:19:43 I… so, discussion… let's say discussion on instrumentation tethering, right?
Huxing Zhang 00:19:51 Yeah.
So, Kimu, can you, first elaborate your proposal, what do you want to achieve?
Kemal Akkoyun 00:20:02 Yeah, I think, so, I'm doing two things in that PR, right? One of them is, I believe we have prematurely abstracted the instrument part, whatnot.
And, like, I've seen that a pattern that, like, we don't need that facility right now. Even, like, I think it was wrong for us to, like, without even adding, fully-fledged instrumentation, we just, like, added the abstraction in place.
And now, like, when I started the ad, like, it doesn't, like, sit right with me.
Like, one is about, like, removing the abstraction, right? And let it emerge eventually, right? We add 10 more, like, instrumentation, maybe 20, and then we will see, and we will try to abstract that, if it makes sense, right? That is the one thing.
We can say that, like, removing the… premature obstruction.
The… I think the second discussion point, was… About, like.
Having a single join point, or, like, doing this indirectly in the standard library.
So I don't know how to put that. Like, how do you feel about that? I think you have some, like… first of all, maybe I should explain what I'm proposing with there, so…
Huxing Zhang 00:21:35 Right.
Kemal Akkoyun 00:21:35 We have… A way to… at a join point, which is, like, start and end hooks, right? And we do that in the standard library.
I am not opposed to, like, removing that whatnot, but I'm… what I'm suggesting is we should have more join points, like, we should have a way to… directly inject the Golk on TripRepo, for example, by, I don't know, like, changing an import path and having a wrapper, whatnot, like, we should enable more.
Do you disagree with that? First of all, let's go with that. Like, do you disagree with having more joint points, or, like, advices?
Huxing Zhang 00:22:18 Yes, I want to ask a question, so what's the benefit of introducing new way of information styles?
Kemal Akkoyun 00:22:28 Flexibility. Obviously, flexibility, like, there are a lot of ways to do… inject these things, and so we… we've been writing a lot of integrations with Orchestrian, right? We already have a lot of experiences, and we actually built the tool and give that to the other engineers, whatnot, and they… then we… give all these tools to them, and they really come up with, like, really flexible and creative way to put integrations, because it's… it's really hard to find a single thing to… and put… trying to put everything in one place.
You can achieve that, as you did.
You are controlling all your instrumentation in the long suit, right? That's your strategy. You are, like, in the business of also doing the instrumentation, which I don't want us to focus on as a SIG, right? We are building the tool, we should be enablers, we should be flexible, and there might be tons of people that write their instrumentation, right? One of the things we did is, using the Go module system in Orchestrian.
you can write a module, and you can put a rule file in there, and when Orchestrian downloads this module, we also, like, maintain a orchestrian.tool.mod file, or Go file, whatever you would like to call, it… you can say that, okay, import that package, which is an integration, and if you download that package, and if you see a rule file in that module.
You know how to inject that module, right?
it gives you a tremendous amount of flexibility. That means, like, if you… you can actually have any Git repo, and say that you… you're a writer of the Go Redis package, and now you realize that OpenTelemetry have a way to, like, inject the instrumentation in compile time, you can just write a rule file.
like, and you don't need to change your instrumentation, you just, like, have all these tools and come up with a flexible way and provide this to your community, right? We are just the tool builders.
And we see that this is working, right? This separation of concerns. I want us to evolve there, but not, like, from the day one, right? One of the things we did with Orchestrian, we also maintained all this instrumentation within the repo itself for a while.
And then after we see that, like, the patterns are emerging, and now we have the correct separation of concerns, we move them out. And now, like, the people that write the integrations are different then.
Like, people write the tool.
So I want us to have the same thing, but otherwise, we are so few people, right? So… We can't, like… even review all the possible instrumentation PRs in the future, right? Because we wouldn't know, like, we wouldn't know how that package works, how that, I don't know, let's say that someone will come up with a Kafka library, and they know how to instrument that, but we wouldn't know that, right? Like, we will have some expertise, but it will be harder.
So… and this is also STEM goes forward, like, I'm not saying that, okay.
We will keep all these before and after logic, so if you just get the tool part, and in long suit, you can, like.
maintain all your instrumentations, but the tool can come from the upstream. You can write your own instrumentation. So this doesn't block any of the progress, or you don't need to throw anything away. So that's my suggestion. So, give the flexibility, give the separation of concern. Yes, it will be different, like.
directly different integrations, because I can write, like, 50 other ways to instrument HTTP layer, right?
So, that's, like, overall my suggestion about Yeah, that.
Przemyslaw Delewski 00:26:12 I think that nothing stops us from that, so we have a tool, we can write a rule for different type of instrumentation. Now, the question is if we also should provide these integrations. But as you said, probably that's your suggestion also to provide these integrations, right?
So, so to have…
Kemal Akkoyun 00:26:37 as the beginning, we should do that, because people don't know how this tool works, right? We need to have enough examples at the beginning, and this is also, for us, this is like dogfooding, right? This is also.
Przemyslaw Delewski 00:26:48 Yes.
Kemal Akkoyun 00:26:48 our tool. We will write them at the beginning, right? We will use the expertise from the orchestrian integration, we will use the expertise from long-suit integrations, because we have a bunch of those, right? And then, after these things are emerges, maybe we will say that let's have a dedicated repo.
Przemyslaw Delewski 00:27:06 Right? Yeah, but… Do you think that we should provide only basic instrumentations for, let's say, HTTP and gRPC, and maybe a few more, or all the set that you already have in orchestrian or Long Suit?
Kemal Akkoyun 00:27:26 I think this depends on the, like, for example, the tool right now we have.
So all the integrations we write, we cannot just convert them as is, right? We cannot just, like… so it's a work, so they will give us some… guidance, right? This is the way they did an orchestra, and this is the way they did it in long suit, and I can actually write a new one, right? That would work with our tool. So, since it's work, and I'm… and it depends on the contributors, right?
I'm trying to onboard people from my company to write integrations with these tools, and if they have some time, and they will do that. Because, like, our goal, from our side, we want to ditch orchestrian eventually, and migrate to this tool.
use this tool for everything. We will rewrite our integrations anyway, right? We… and this will happen. This is our agenda. So, that means, like, all these Integrations will be possible to be used by the community as well.
And we screwed through, like, the next thing is.
We should, like, advocate hard this tool, and maybe we can go to these, like.
libraries, third-party libraries, or, like, there is a registry in OpenTelemetry that you put, like, different components of your SDK, right? Which actually has the instrumentation.
We can maybe go to those libraries and propose to add a rule file. We can write them for… write the rule files, like, initial rule files for them, and then people also can use the registry for their instrumentation.
Przemyslaw Delewski 00:29:05 Yeah, so I agree with two points that you mentioned. First is that we… I think that we over-engineered this architecture for these integrations. For me, it's too complex, for now. Maybe… That's my point of view, but I think it's too complex. And the second point is that… because we are not experts in all these libraries, we cannot provide the, you know, the best instrumentation. So this is something that we should leave for people that know how to do that.
Kemal Akkoyun 00:29:43 Yes.
That's my, also, definitely my goal.
We should eventually, like, help people to write rule files, and they should maintain these.
Przemyslaw Delewski 00:29:55 Yeah.
Huxing Zhang 00:29:56 What I'm thinking is, you know, when we are developing a plugin or in this instrumentation library, we can provide the guidance or examples for the developers.
Why there should be, another third-party library that can live, live… without this… this repository, this makes me think that we have to separate this to, the basic tool and the instrumentation is separate into two repositories, and they will separate the con… like, people knowing about this report, or this project, or this SIG, and I don't… I think that will be not good for me as… right now, because I want to concentrate the… this, project in, for two purposes. One is the basic tool, tool for inject, inject code. The second one is the instrumentations that we provide. We provide good, Good quality instrumentations as far as we can, but we still provide the way that we can Let other third-party developers or, other people to write, by following the guidance that we provide, or they learn from our existing instrumentation, they can write instrumentations as well. That's my point. So, that's what I'm seeing.
Kemal Akkoyun 00:31:42 But, like, do you think the things that we are saying right now conflict with that?
Huxing Zhang 00:31:48 I'm… I'm concerned about that we… What do you mean, is to, like, to… write the third-part library instrumentations in the Go Country? Do you… do you suggesting that we are going to write code in the Go Country report?
Kemal Akkoyun 00:32:09 No, no, no, no, no. I'm not suggesting that at all. We should.
Huxing Zhang 00:32:14 Okay.
Kemal Akkoyun 00:32:14 have all the tooling in our tool, like the join points, some aspects, so that, like, I can grab something from the goal contrib, and write a rule file for that.
Huxing Zhang 00:32:27 Right? Okay, so all the codes are in this repository, right?
Kemal Akkoyun 00:32:34 the defined code, like, we have the tool, right? The injector part. Let's say that an injector. The code, an injector, we have that. I don't want to have, like, a special instrumentation code.
for the things that are already available. So, I will check… let's say, let's get the example of HTP, which is, right now, I'm familiar with the Gorkcon trip, right? They have… what they do, they provide a special transport And they also provide this special handler, so you just wrap your handler with that, right? So, I should be able to get that handler method, and somehow inject that to the customer code, without changing anything in the GoCon trip.
Right? We should be able to have that join point, that pattern matching, that advice we have.
And we have some similar things that we did with orchestra, and it's achievable. Or let's say it's nearly impossible, right? And we can have two things.
a thin wrapper around that library, really thin, that would help us to fit the drawing points that we have, and we can First, put that in our repo.
experiment with it, it works, and then we can propose that additional API changes to the GoCon trip, right? We can say that, okay, this is just a pin wrapper, like, calling this your method in a different way, or introducing some different types, but all the functionality, all the business logic still maintained by someone else in the GoCon trip repo.
And we just, like, inject that, right? Like, the whole idea is to just enable other things.
Huxing Zhang 00:34:15 Okay.
Kemal Akkoyun 00:34:15 Eventually, we can also say that, like, this is one of the things that I would like to discuss with people in KubeCon, if I can find some contrip maintainers. We can actually put the rule files into Constrip repo, right?
we can write everything, put the rule files in there, and it's just an additional YAML file for them, but the advantage would be GoModule System would package that file.
And if we have a, like, an import path, in the… we can gen… we do generate this for orchestrian, for example, when we instrument, right? They can pick these things. And if they pick, okay, I'm gonna use the… HTTP instrumentation from the GoCon chip, and I've just… I will have an additional import file, just a Go import, and we will just download… we know that there is a rule file in there, and tool will discover that and inject the code.
Przemyslaw Delewski 00:35:09 Yeah, this is something that I wanted also to ask, whether we should have these rules in our repo, or maybe somewhere else in other repos.
Kemal Akkoyun 00:35:19 I think we can start with having them in our repo right now. We have a concrete, like, when we know the API is somewhat stable, probably this is the V1, right? Before V1, we say that, okay, like, we are not going to change these YAML files for now.
At least we… if we don't introduce any breaking change. That's why we're gonna have these rule files, to the GoCon trips, and we can start moving them out.
Przemyslaw Delewski 00:35:47 Yes, that's probably good to… You know, good idea to have, first, to have everything in our repo, and then maybe we can start discussing also with other teams how we can distribute these rules to other repos.
Kemal Akkoyun 00:36:04 Yes.
Huxing Zhang 00:36:05 I got another question, a detailed question, for take the net HTTV as an example. If we, as you mentioned, we… grab the code from the go contribute, and we write a thin wrapper in our repo, and just call the code in the go contribute right.
And do the, does there, is there another choice that will, for, as, let me think… We, we, shall we, implement another way that we provide direct library, change the library, at the start and hook to that code? So there's a two implementation, two ways of implementation. Shall we keep two… Both of the two implementations, or we just choose… Only one. Well, what do you say?
Kemal Akkoyun 00:37:03 I think we can have two. We can have two. We don't need, like, this is what I write in this Slack channel as well.
There is no single way to do these things, right? As a developer, I would prefer to keep all the changes in my code, right? The user code.
Maybe you think differently, and you are okay with patching the standard library HTTP server, right? You should have been able to have the choice, right? What I don't like to see, which is I'm reviewing in the PR, in our instrumentation, kind of dictating some code in our package, right? Which was the SAMCO instrumentation and the instrumental abstraction. It was in our package. They shouldn't live in there, right? If you want to add that sort of, like, instrumentation, it should be encapsulated to its own package. That's why I put the SAMCO for HTTP in itself, right? Because it's only related to the HTTP. So, you can now… go… this is… we call that, like, HTTP instrumentation in that package, but you can go to the instrumentation directory and add a new way of adding, like, you can copy the same code and put there, and you can keep still having the same thing.
And you just, like, it's a matter of, like, using which instrumentation. Right now, we don't have a way to… no, we can choose that, I guess. It depends on, like, we need to come up with that, in the rule file.
Not to rule far. No, no, it should be possible, right?
It depends on where you execute the rules, right?
Huxing Zhang 00:38:43 My concern is that we will provide to, like.
Two kind of way of instrumentation, and there may be… A duplicate works.
One… paper.
Kemal Akkoyun 00:38:57 That's… that's, again, like, our goal shouldn't be maintaining the instrumentation, right?
We will… our, like, end goal shouldn't be instrumenting, though, like, maintaining the instrumentation. So… right now, I'm okay to provide two ways in the repo, because we are experimenting, right? But eventually, the instrumentation code, for example.
all the abstractions you have, it should live in long foot, right? In your repo. And then you can use that. You just import the tool from this repo, the upstream repo.
Then we don't need to think about that.
Przemyslaw Delewski 00:39:36 Yes, but…
Huxing Zhang 00:39:37 Okay.
Przemyslaw Delewski 00:39:39 Yeah, I wanted only to say that I agree with this direction, so in the long term, we should, you know, have all these rules somewhere else, and we should only provide a tool for doing the core stuff, in fact.
Huxing Zhang 00:39:57 So, what you mean is that this project, this repository, will eventually only be responsible for injecting codes, but they will.
Kemal Akkoyun 00:40:08 Yes.
Huxing Zhang 00:40:09 Okay. But, So… so if the developer who wants to utilize, like, instrumentation that has been written by someone, you will recommend they to, like, go to find another repository, and they will, Search… search the instrumentation there, but this… not go to this, project.
Is that what you mean?
Kemal Akkoyun 00:40:40 We can have a default, like, another repo, like GoContrip, right? We can have Go instrumentation contract repo.
And we can have some… I don't know, sanctions, or, like, standardized?
instrumentation that we… endorsed, right, from the OpenTelemetry community.
But this doesn't say that, okay, if someone wants to have their own set of instrumentation with their own way, and they have their, like, abstraction, they can provide that repo as well. Tool wouldn't mind. Okay, I'm going to pull the, like, the instrumentations from that repo, and I will use them.
That's a choice to the user.
And this will enable, like, say that you are a platform engineer, and you have a private repo, and you have a private way of doing things, and you can write all your, like, instrumentation in private, and pull just the tool from the upstream, and use your private instrumentation.
Huxing Zhang 00:41:46 Okay, I got what you mean.
That's not, actually, that's not what I'm… was thinking, because we… actually, we would like to donate both the tools and the instrumentations. That's what I mean by our original purpose.
Kemal Akkoyun 00:42:05 You can do the… you can still do the donation part, right? We can have that repo, and there's this, like, Alibaba, or, like, I don't want how you would like to call that, long-suit instrumentation, right? And it's still open source, it's donated, you can be the maintainers of that.
And then, like, if people want to use that, they can use that. Doesn't change anything, right? It's just a separation of concerns.
Przemyslaw Delewski 00:42:28 But I think that it's also a good time to rethink all the architecture of both tools, and, you know, maybe build something also better on top of that.
Kemal Akkoyun 00:42:41 Yes, exactly, like, I… there are things that I don't like how we do in orchestra, and now we have the, like, an experience, and now we can actually build on top of that, right?
Przemyslaw Delewski 00:42:54 Yeah.
Kemal Akkoyun 00:42:54 our choice, like, that we are writing the same thing third time, so maybe third time is the charm, so let's see how it goes.
Przemyslaw Delewski 00:43:04 I have also one question regarding your PR.
about this HTTP instrumentation. I was wondering, because this PR is very huge now, I was wondering, maybe, if that would be possible to, you know, to split that into, let's say.
two parts, maybe. One part which would be about this instrumentation layer, this generic code.
And the second part, which will be strictly about HTTP instrumentation rules, and so on.
Kemal Akkoyun 00:43:37 that I can, like… please comment on the PR. I can just first separate the removal part, and I can, like, separate, like, the addition part. Even for the addition part, I can try to slice and dice that. Yeah.
I already, like, did several iterations on the PR. The initial version was using all the, like, the abstraction that we have.
But then, like, I change things and try to simplify. But yeah, I can slice and dice it more, and I also need to rewrite the gRPC PR after these changes, because the gRPC one also using the old way.
Przemyslaw Delewski 00:44:16 Yes, I was… I think that it would be very useful, because we could then discuss, you know, this generic part also. Maybe we could re-engineer that, and also simplify more, and so on. So… That's my point.
Kemal Akkoyun 00:44:34 Okay, I will try to, like, split that.
Xabier Martinez 00:44:40 Anyone else? Yeah.
Kemal Akkoyun 00:44:42 Please, yep.
Xabier Martinez 00:44:44 Hello, Aishabi, that it's the first time I'm joining to this group. I totally agree with this approach. We are talking about keeping things simple. Like, we have the tool, and it should just have, like, a stable core, and try to focus on things like, finer grain instrumentalization, all these things.
And I also agree that we can start, like, putting all the instrumentation packages from Long Suite to dire repo, for example, but it's quite important to define the interface between those two repos or those two tools. Like, even.
we are going to talk with the contrary repo maintainers, for example. We need to give them a propulsion, like, how we're going to connect.
those packages could live in an Orepo, or inside of repo, for the, like, in the moment, but… We need to define, sadly, how they're going to connect.
And those two reps, or those two walls.
Because it's not so important, like, where we put things right now, but… How they are going to connect, and… We should work on that direction.
Przemyslaw Delewski 00:46:09 Definitely. I think…
Kemal Akkoyun 00:46:11 Yeah, go ahead.
Przemyslaw Delewski 00:46:13 Yeah, I think that this is something that will evolve over time, so we will learn how we should do that, and probably we'll abstract the right interfaces along the way.
Kemal Akkoyun 00:46:26 Yeah.
I also think that our interfaces are the hot points and the join points, like, however you would define that. Like, if we have enough of them, we can actually make fit any library to inject, right? We… I don't think, like, we will… We can get away by not changing anything in GoalCon Trip.
Right? But if it comes to that, we can, like, as I suggested, we can have some simple, like, wrapper in our codebase, make sure that we figured out the least obstructive, like, API we have, and then we can say that, okay, like, we want to add this tiny change to the goal constip, right? We already, like, this is our reasoning, we are writing these rule files, and we've been, like, using that, and it was stable, and can you add this?
Right?
Xabier Martinez 00:47:25 Yes, like, basically. And also.
I think it's important, like, benefit from all the… the instrumentation that, we have already done, like, for example, from LawnSuite, because We kind of start thinking about, okay, other guys can start contributing and maintaining those roles.
But, you need a bit of traction to the repo. Like, it's hard to start getting traction, to put production ready without… or only instrumented HTTP or gRPC. Like, it would be cool, like, to have a package of tools already instrumented.
But, that's maybe a future discussion for the future.
Kemal Akkoyun 00:48:17 Yes.
Exactly.
I would like to call for consensus. I think this is some of… one of the things that it's been done in, like, RFC meetings, or, like, similar community meetings, that make sure that we are on the same page for the future. So… I am, like, one of the consensus, the first thing I would like to propose is our repo will eventually only be responsible for injecting code.
Do we have an agreement on that?
Przemyslaw Delewski 00:48:49 Yeah, I think, from my side, we have…
Kemal Akkoyun 00:48:53 Okay. Anyone disagrees?
Cool.
We will try to, like, the second call of four consensus is, like, we will try to enable Other instrumentation libraries as much as possible, right?
This could be GoConstrip, this could be Longshirt, this could be something from the Datadog, this could be some third-party thing… library that provides their own rules.
Huxing Zhang 00:49:24 I have a question about this, and so what you mean is to, like, for one kind of, like, framework, take a negative HTTP, and as an example, we will have, multiple kinds of rules that developer can choose, but they will achieve the same purpose. They can be library patch, or can be, like, a wrapper of the framework. So we… we will provide both, both kind of roles, and the developer will going to choose, and what we would like to use. Does that mean… what you mean?
Kemal Akkoyun 00:50:09 Yes, eventually it will be like that.
That being said, since we will have a… that's the second, like, the third point, we can have an official repo of instrumentation, right? And in that official repo, we can discuss, actually, whether we would like to have two ways of instrumentation for the same thing, right? But I think it's a… it's a different discussion point, and it's in the far future, right? It's, like, a choice that we need to make. But, like, the second point is about enabling these patterns, right?
I can create today a third-party instrumentation marketplace repo and put a bunch of rules in there that would enable our tool And maybe community will love that. Maybe love my instrumentation things, and they will use that.
The nice thing about, like, this tool, it's flexible enough, and you don't need to just think in terms of instrumentation. You can also use the tool for forcing security rules, right? It's quite possible.
If you are able to, like, inject a HTTP wrapper, maybe you can have a middleware, which do all the security things for you, and it's totally out of scope of OpenTelemetry, but people can use that, right?
Yeah, we should enable those patterns as well.
Przemyslaw Delewski 00:51:32 And it might be that the developer will not like our instrumentation, and he will write his own, right? So it might be a third option, for instance.
Xabier Martinez 00:51:44 Yeah, I was also the…
Kemal Akkoyun 00:51:46 private use case.
Xabier Martinez 00:51:47 I was thinking also that having a simple interface, it could be really interesting for the developer, like, okay, we are instrumenting well-known tools, but imagine that in my service, I have, some functions that I want to instrument. Maybe I can just have, like, the default instrumenting, so I just write YAML on my repo, and I get those functions automatically instrumented. So I just tracked the, the open, like, the instrumentation of the service from the code. So instead of using the libraries, I can just also instrument my functions directly.
Kemal Akkoyun 00:52:26 Next.
Exactly that.
Huxing Zhang 00:52:32 So we are going to, not… we are not going to have any preference on any kind of rules on this report, right?
You… you…
Kemal Akkoyun 00:52:41 Eventually.
Eventually. Like, we will… we will add some instrumentation right now, because we need to experiment, right? And we need to help people to easily use these things. But eventually, let's say before V1, we will separate them out.
Huxing Zhang 00:52:58 Okay, from our experience that we have, actually, we have choosed the library patch, the way of library patch, because we actually have some… hiccups in the other way. We want to avoid that, so we choose that. But, I… I think if the… the report is, big or wide enough, they… they will eventually… people will have to… they will recognize, which way of, is better, and then I think that's… That's good for me right now, if we provide such kind of things. Both ways we provide to the developers and let them I think developers will vote, finally, they will find to… find a way that… which way they will… which is the better way, and they will choose. I think that's… right now, it's good for me right now. Okay.
Kemal Akkoyun 00:54:05 Okay.
I'm also trying to respond to the Zoom chat.
Yes, I… write some responses to the Yi Yang. He's, like, asking, some clarification questions on whether we will have, like, two different instrumentation codes maintained in their separate repositories. Yes, this will enable that pattern. We will have… Then… that's the third point. Let's say that I think I don't see any disagreement, and let's call for consensus. We agree on the second point, right?
We will try to enable other instrumentation libraries as much as possible.
In their own, let's say, in their… on… Repos… or modules.
Huxing Zhang 00:55:02 Okay.
Kemal Akkoyun 00:55:03 Does anyone disagree?
Huxing Zhang 00:55:05 Okay, I agree with this, and the detailed name of the repository, they are not deciding right now, okay, right?
Przemyslaw Delewski 00:55:16 Yeah.
Kemal Akkoyun 00:55:16 But nothing, nothing is designed. The third point… I don't, like, right now, even, like, for the third point, we don't even need to decide, right? We, like, we can leave that as is, right? Whether to provide a central repo, what goes into the central repo, we don't need to have a consensus on it yet.
Right? Let's focus on building the tool, and making sure that we enable everything.
And, yes, then, like, I think everyone wants the same goal, and this was just, like, clarifying the details, right? And… I think we have that consensus, and when the time comes, we can talk about having the repo, and how does that registry look like? Should we put, like, different like, vendors… different instrumentation code from different vendors in that registry, we can discuss, right? Like, that actually makes sense, as the Yang's question, like, maybe in the official repo, we can say that, okay, these are written… these instrumentation written by Alibaba, these instrumentation are written by Datadog, and these instrumentations are written by Cabe.
Pick whatever you want. This is… just not a kingmaker. That would be a way, or we can say that, okay, we know… we have some opinions on instrumentation, and we will have a single way to instrument.
We can also do that in the registry.
But let's not, like, discuss that I don't think. Do you want to discuss, or do you want to have a consensus on it right now, or we can… we should… we can discuss it in some other time?
Przemyslaw Delewski 00:56:58 Yeah, we can postpone that.
We are not there yet, so, you know, we probably will decide.
Sometime later.
Xabier Martinez 00:57:11 So, we need to have, like, the common interface, and then we should also focus on making the tool a bit user-friendly, like, hey, I need to… I want to import, easily, these roles from this repo. I want to skip these… these ones, this kind of, this kind of features.
Kemal Akkoyun 00:57:29 Yeah.
Exactly.
Maybe, like, for example, one of the things that I'm forcing is, right now.
We are also using the metrics, right, instead of traces. I think, like, some of the things I would definitely want to have… I'm using Prometheus for my metrics, and I don't want an open telemetry metrics in my instrumentation.
Probably we need to provide a way to do that, right?
Which is a quite common case in CNCF ecosystem.
So yeah, like, nothing we put in the instrumentation code in the repo right now, it's not written in stone. It will evolve, change.
And then… Before we won, we will decide.
Like, how do we… how do we approach the default instrumentation?
Alright, any questions?
All right, we only have 2 minutes, but do you have any other things to discuss?
Huxing Zhang 00:58:39 I think this is the… the most important one.
Kemal Akkoyun 00:58:44 Yeah.
Przemyslaw Delewski 00:58:46 From my side. So, one of the action points, as I understand, will be to split this, pull request, right?
Huxing Zhang 00:58:53 We were testing.
Kemal Akkoyun 00:58:55 Yeah.
I will take a note of that, but you can definitely suggest that in the PR as well. I will be on PTO for the rest of the week, but… I will try to fix that when I'm back on Monday.
Przemyslaw Delewski 00:59:11 Yes, career.
Kemal Akkoyun 00:59:20 And yeah, like, go on to the PR and… Tell me what you don't like. Thanks for the reviewers already.
Those are, like, really nice inputs. I'm trying… I will try to address those as well. But the nice thing is, it works, and it works with our demo repo. I don't know if you already, like, pulled that and tried the demo application and whatnot. The Grafana dashboards need some… improvements, but, like, people can just, like, run the demo and see that everything works.
All right, then, thanks everyone. We are at the top of the hour, and we can close this meeting.
Huxing Zhang 01:00:03 Okay.
Przemyslaw Delewski 01:00:03 Okay, thank you very much.
Kemal Akkoyun 01:00:06 Why?
Xabier Martinez 01:00:06 Thank you. Bye. Bye.
