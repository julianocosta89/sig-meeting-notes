SIG: Project Tooling SIG
Date: 2025-10-23
Duration: 31 minutes
Zoom Recording URL: https://zoom.us/rec/share/BPgI-Cn9WRmJqMCzLIcZiozN2pokm0iu8v-88bb0PUUX2qQC2JEn3I_bN7Hto9De.vKlvKC8Kaw8Lovt0
============================================================

## Zoom Recording Transcript

**Austin Parker** 01:24 Hello.
**Trask Stalnaker** 01:26 Hey, hey!
**Austin Parker** 01:29 How's it going?
**Trask Stalnaker** 01:34 Pretty decent, pretty decent.
We… I did bring up the blog in the, JavaSig.
**Austin Parker** 01:46 Chris, how'd that go?
**Trask Stalnaker** 01:47 We didn't have, enough time. We got to it at the end of the meeting, so…
**Austin Parker** 01:53 Oh.
**Trask Stalnaker** 01:53 Just a little bit of discussion.
But I think… We just have to figure out what it means for us, like, What things that we need to… mark stable, like, we have internal instrumentations that do just, like, context propagation, parts of the Java agent that are, like, modules, instrumentations inside the Java agent that do say propagate, that we… Haven't marked stable, but we probably just can, because they don't emit any telemetry.
**Austin Parker** 02:33 Yeah, let me… And I need to…
**Trask Stalnaker** 02:41 I think one of the bigger problems is we need we don't have a lot of stable instrumentation yet, I think only HTTP.
**Austin Parker** 02:50 Yeah.
**Trask Stalnaker** 02:51 Makes, essentially, we would have no users who are not opting in to the unstable flag.
**Austin Parker** 03:00 Yeah, and I mean, I think… I think my point is, that's fine, right? Like…
**Trask Stalnaker** 03:05 Yeah, I agree.
**Austin Parker** 03:07 I don't think it's… It's not…
**Trask Stalnaker** 03:10 It pushes us in the right direction.
**Austin Parker** 03:12 Yeah, the point isn't to say, like… the point is just getting us to… Go on the record and say, like, hey.
We want you to move towards, like.
stability, and we want to figure out what are the things stopping you from getting there, right? Because the… Part of the challenge, I think, is that we're… we… we just don't… makes a lot of it just so we have to commit, right? Like, we have to be able to, as a project, commit to saying, like.
Maybe it's not the greatest thing, but we're gonna ship it and support it for 3 years.
**Trask Stalnaker** 03:56 Well, you know, that has helped us on the Java agent side a lot, is that we did a major version bump already.
**Austin Parker** 04:06 Yeah.
**Trask Stalnaker** 04:07 And so it's not a scary end-of-the-world thing.
For us?
**Austin Parker** 04:13 Yeah, like, I just want us to be able to kind of say, like, at each SIG level, say, here's the stuff that, like, here is the stuff that We have high confidence in.
here's… here's a new section of stuff that, like, we effectively have high confidence in, but we were blocked for ticky-tacky reasons on saying it's stable, or it's beta, or whatever. And then here's a bunch of stuff that maybe we don't. And, like, making it a lot easier to kind of say, here's the… Here's the lines.
Right? Like… And just… and let people know, specifically.
Hey, this is what you're getting.
When you install something.
And these are the expectations you should have when you install something.
**Trask Stalnaker** 05:07 The other open question for me is… Can say something like, messaging instrumentation.
**Austin Parker** 05:20 Yeah.
**Trask Stalnaker** 05:21 There's no stable SEM comp, there's no stability SIG anymore for it. It's gonna be a while.
Can we… Mark…
**Austin Parker** 05:35 I think we would mark it beta.
**Trask Stalnaker** 05:36 gene… the SEMCOM itself.
**Austin Parker** 05:40 Yeah, I think that's… because I think… because right now, correct me if I'm wrong, but… SEMICOM doesn't really have… SEMICOM is basically stable RC or experimental, right?
I think we just need to add beta in there, basically.
**Trask Stalnaker** 05:57 And so, would you… would… I noticed in your proposal, you mentioned that… that Instrumentation could be declared stable on top of beta…
**Austin Parker** 06:10 On top of beta subconf, yeah.
What I'm basically… my thought process here is basically this.
SEMCOM is not… like, the stability of SEMCOM is something that ultimately telemetry consumers have to care about, but it's also something that… like… Are safe to… like, they're safe to break?
In… with the… in the… in the sense that when you break a SEMCOM, it's sort of an additive break, right? Like… I guess there's exceptions to things like changing unit types.
Like, if you change the unit type of something, then that's a breaking change, and you don't change the name of it.
But… I think that's a good example of, like, okay, like.
Maybe we say, hey, this is in beta, the value of this metro… of this thing is afloat.
And then we find out, through usage, that it should be something else.
Well, it's okay to version and make that breaking change, because it was beta, we're not guaranteeing stability, we're not saying, hey, this is perfect and flawless, we don't necessarily have to give you the full 3-year support window, but we need to provide a migration path.
for beta… from beta to RC, or whatever.
Like, I think that's fair.
And it's not… shouldn't be a reflection of, like, the actual instrumentation, because, like, the Kafka instrumentation, for example, Kafka client instrumentation.
the stability and performance of the Kafka client instrumentation has less to do, I think, with the telemetry it mitts versus, like, the actual… Methodology of doing the instrumentation.
**Trask Stalnaker** 08:07 So for this, you mentioned, like, LTS… 3, 3-year LTS. That is a long time in the OpenTelemetry world.
**Austin Parker** 08:23 Well, I say 3-year, because that's what… that's the… that's what we've already promised.
Three years…
**Trask Stalnaker** 08:30 is… I mean…
**Austin Parker** 08:32 And APIs.
**Trask Stalnaker** 08:33 Yes, I'm fine with that on SDKs and APIs.
**Austin Parker** 08:37 I mean, we could change it for SimConv.
**Trask Stalnaker** 08:43 And… distribution, instrumentation.
**Austin Parker** 08:47 Yeah, I mean, we can… I guess my point is, like, we can say what we want to say, right? Like.
**Trask Stalnaker** 08:52 Got it.
**Austin Parker** 08:52 point… The problem I have now, I feel like, or the thing that I want to… I think the thing that I said at the end is sort of the real crystallization of this. Right now, there are too many, like.
I would rather us be able to say, here is sort of this… Slightly more narrow set of things we are driving towards as a project.
And here is the threshold that we're gonna say, hey, this becomes, like, okay to… Add in.
And… We should really focus on, like.
sort of the operator experience, like, the user experience here, and not necessarily the user experience of, like, the API user, because, I mean, they matter, but, like, if I'm… Like, here's a good example. I was talking to… I was… I've been taking this and, like, going back internally, and I asked a bunch of our sales… our field sales engineers about this the other day.
I was like.
Because this was coming, this came up in an internal thread about, like, sort of hotel reliability, and what they said was interesting, which is basically, well.
For a lot of people, we just tell them, go install the Java agent, and it just works.
Or go do Go instrumentation, it just works. But for the people where it doesn't, it really doesn't.
And we, the project, never get those, like, things, because the sales engineers are incentivized to, well, let's… Well, you know, let's do whatever as fast as we possibly can in order to fix the problem, in order to, like, keep the deal on track.
And so we never… so that's one of the places, like, sort of the feedback loop is breaking, because when people do have these problems, those problems either get managed for them, or people do some sort of weird hack, or whatever, and we just never hear about it. And so, the real, you know.
the goal behind the goal, I guess, is Let's be more clear about… What we want to ship… what we want to deliver to people, in terms of… Functionality for Motel.
what cadence we want to regularly deliver that on, like, not just… You know, every month you have a bunch of dependencies, but, like, there should be a slightly slower… You know, slower update channel.
That is easier for people to kind of plan around, and update documentation for, and do benchmarking for, and whatever.
And… Like, focus people on, like, we want the stuff that's in those core packages, like, we want this stuff to just work out of the box, like, we want this to be a really good experience.
And some of that does mean that for stuff like SEMCOM, we should be able to say, hey.
For messaging some kind of, people are using it.
Like… We aren't… we don't necessarily expect it to change a ton about the shape of the telemetry that it's emitting.
a… Certainly there's things that, you know, we would change if we go through a stabilization process, But… We need to kind of accept that, like, we can't… Tell everyone, stop, wait, like, we can't… we can't tell everyone to just stop and wait until, like… Everyone goes off, and… huddles in the SimConf corner, and does the process, right? Like, I remember when we started this whole SimConf stabilization thing, and it's like… You know, oh, it'll take 6 months or whatever to get through them, and it's like, it's taking a lot longer to stabilize individual SEMCOM, areas.
Right?
Like, I think we can just deal in reality here and say, like, okay, for stuff that isn't… For stuff that we produce.
We can relax a little bit and say.
The telemetry that an instrumentation emits might be unstable. It might be in beta quality. And if it's in beta quality, then here's what that means. It means that it can change in the future. If it does change, we'll support it for, like, 6 months.
like, two full… like, two full release cycles, right? Like, I think if we… If we say, okay, there's gonna be a… project release every quarter, or every 3 months, you know, every 4 months, however long, whatever we want to say the cadence is. We can say something like.
Beta Semcov, when it changes, the instrumentations only have to support it for, like, 2… 2 release cycles, or 3 release cycles or something, right? We pick a number.
And during that time, you'll be able to dual send.
**Trask Stalnaker** 13:56 So, yeah, I mean, I think that kind of fits already into the stabilization process, where we would, once… I like the idea of, like, marking messaging. I mean, messaging is kind of already frozen, because we started that process of stabilization.
But it's essentially saying, hey, almost we're marking lots of things as beta, and… Whenever stabilization occurs.
There won't be a breaking…
**Austin Parker** 14:30 Yeah, there may be breaking changes when these things stabilize. There probably will be, but…
**Trask Stalnaker** 14:36 We already have that opt-in process and the guidance on how long you're the…
**Austin Parker** 14:41 I think a lot of this is just saying, like, some kind… like, telemetry semantic stability can change in a different way than, like, code.
**Trask Stalnaker** 14:52 the instrumentation stability.
**Austin Parker** 14:53 Yeah, like, and you, like, the actual code is gonna change in, you know.
like, API civility's super important, 3-year deprecation makes sense. Like, changing from… messaging.
food.bar to messaging.food.bar.baz, feels like something that, you know, if I give people a 6-month heads up.
And say, hey, during, like… on January, whatever, you know, on the next version.
This is gonna start dual sending, and then… it's gonna pop up a notice that says, like, hey, FYI, this is now this, you have this long to update it.
You know, to update your alerts, update your whatevers. Like, that, to me, feels like a pretty good amount of time.
Right? And we also have ways for people that are… maybe they're on, like, a yearly cycle, right? Like, okay, you know, or maybe they stagger these things, or whatever. It's like, okay, that's why schema transforms exist, right? That's why the transform processor exists. Like, there's ways that you can… Modified…
**Trask Stalnaker** 16:06 Shit.
**Austin Parker** 16:07 Yeah. Huh?
**Trask Stalnaker** 16:08 Or not exists.
**Austin Parker** 16:09 Well… Sure, but even with the transform processor, there's ways that you can modify these things on the pipe in order to… like, handle changes, right? Yeah.
And I don't think that that is a… alien thing, necessarily.
to… End users. Elementary end users.
**Trask Stalnaker** 16:32 Yeah, we definitely… the project took a very aggressive initial stance on telemetry stability.
**Austin Parker** 16:40 Yeah, we were very conservative.
**Trask Stalnaker** 16:41 Which…
**Austin Parker** 16:43 I'm not sure it's served us well.
**Trask Stalnaker** 16:45 Yeah, yeah, I mean, it was… Yeah, I like the idea of backing off somewhat on that.
What about the, long tail of… components and semantic conventions, because that… one of my worries is that with this new guidance.
All of the collector receivers, you know, and random instrumentations that we have.
They're… if they're gonna want to… mark themselves stable, and so they're gonna crush the semantic convention SIG repo by trying to.
**Austin Parker** 17:32 I think… I mean, I think in that case, like, we use the same things that we are now, and we say, like, hey.
this is what we're working on now. Like, if you want to stay… like, stabilization is a project, not a, like, one person goes off and does it.
And we add the same sort of, like, quality gates or whatever that we would add for, you know, moving thumb and disable, and saying… I think we kind of have this, right? Like, if you want to come in, start a project, you have to have Sponsors, you have to have, like.
Contributors, you have to have a plan.
And s… You know, if someone comes in… Oh, go on.
**Trask Stalnaker** 18:14 What's the place for distributed, ownership of SEMComp? Because I know that's one of the things that… the semantic convention, SIG, and the Weaver project.
**Austin Parker** 18:27 Yeah.
**Trask Stalnaker** 18:27 Like, kind of see as…
**Austin Parker** 18:29 Yeah, I think a lot of it is…
**Trask Stalnaker** 18:30 to not become the… like, we don't want this SEMCOMF rep repo to become the junk drawer of all. Right.
**Austin Parker** 18:37 I don't want that either. I think the, you know, in my mind, it's just, like, organizations or… like… authors of software should own their SEMCOV, right? Like…
**Trask Stalnaker** 18:49 So could a collector-receiver own its own SIMCOM?
**Austin Parker** 18:53 Probably.
Like…
**Trask Stalnaker** 18:56 kind of what… I mean, I… I like that idea. I'm not sure, you know, we haven't done it yet, and I'm not sure how that would play out, but I…
**Austin Parker** 19:05 I mean, I think a lot of it is expanding out the Weaver idea and saying, like, really what we're talking about isn't SEMCOM necessarily, it's telemetry schemas. Like, SEMCOM should literally be actual… Semantic conventions, and then there's, like, a slightly more… narrower version of that that's your schema, that's your telemetry schema. And if you're publishing a receiver.
Or an exporter, or a processor, an instrumentation library or something, then there should just be sort of a… you know, at the root of that, there should just be a YAML file.
That is your telemetry schema, right?
And… Now, if I'm a cloud hyperscaler.
And I say… and I have a bunch of my own things.
and I want to provide extensions to existing SEMCOM, or I want to provide… I'm AWS, and I… I have all of these semantic concepts that are already very well understood.
For me, then it's like, okay, you know, that's more of, like.
my SEMCOM, and I'm gonna publish that in some sort of, like, well-known location, or… or publish that as, like, a discoverable schema or something, right?
But… I think it's… I think the… to step back a little bit, I think a better way to think about this is really just… is to kind of lean into the instrument… like, first-party OTIL instrumentation libraries exist to implement Like, they exist to implement spec, and the spec for those is SEMConv.
Because that kinda… Answers a lot of… like, that makes a lot of questions very simple to answer.
Like, with the exception of the collector?
Which is… I don't have an answer there. But it makes it very simple for everyone else, because it's like… because it's, you know, again, if you're… You know… As an end user, it makes it really easy to understand, like, what… what can OTEL do? Makes it really easy to understand if you are a, like.
External developer, or you're a framework developer, or you're, you know, whatever, And you wanna know… like, what library… what part of this… of your libraries or your things should be instrumented? How should be instrumented? Well, you look for stable semicond, right?
And then maybe you add your own. You add your own schema on top of that.
But I, I think the… the real… Like, the real takeaway should be… we should be doing… Trying to do fewer things at once, and do those things better.
And be a little more… Realistic about, like, what are the things that are stopping us from, sort of.
shipping… code… Getting it into people's hands, getting, you know.
Like, what's stopping us from being able to do that? And I think part of it, you know, in my mind, is… again, we're trying to do too much. We have… there's… and it's fairly impossible, I would say, to… Like, I don't know, I don't have a good way to… Because everyone's gonna, like, everyone's problem… Is gonna be their biggest problem?
like, from an end-user perspective, right? Like, if… your boss says, like, oh, we need to use OTEL, and… You download it, and then it doesn't work for, like, your particular thing.
Like…
**Trask Stalnaker** 23:17 So you're migrating… you're migrating off of another APM, and OTEL is missing one instrumentation that you need.
**Austin Parker** 23:26 Right, like…
**Trask Stalnaker** 23:27 And instrumentation then becomes, like.
**Austin Parker** 23:30 Right. And my… what I would like… what I think makes sense as a solution here is to be able to make it easier for other, like.
And I even said it in the post, it's like, we really, like… really want the ecosystem to kind of come through here. Like, we want people to be able to build extensions to OTEL in a way that… It still makes people broadly… makes things broadly compatible with a, you know, broadly compatible.
And doesn't, like, lock you out of things, or lock you into something, or da-da-da-da-da. But, like… I don't know, people friggin' use LeftPad, like, people install all sorts of random junk from package managers. I don't think writing instrumentation is… like… I do not necessarily feel like writing instrumentation is that hard.
In a lot of frameworks, or a lot of libraries, especially ones that are, you know.
designed to have hooks, right? Or designed to have, like… Some sort of, you know, request callback, or whatever, right? Like, this isn't… A lot of things have, like, logging hooks, right, or instrumentation hooks already.
And it shouldn't be that difficult for people to go out and say, like, oh, I'm gonna write… you know… I'm gonna write a… plugin for the Java agent that's compatible with This thing over here.
And we can focus, then, as a project, on, like.
the core installation, configuration, operation, da-da-da-da-da. Like, if we can ensure there's a really solid base.
You know, makes it easy for people to get started.
That is tested, vetted, works in all the, you know, has vetted configs, you know, that it just works, right? Like, I don't… I don't know, like… I don't see a lot of other… Options is the problem, I guess.
Other than… other than, like… Do even less.
like… well, either do a lot more, or do a lot less, I guess. Like, you could, you know… We could say, like, okay, our goal is to be this, like, full replacement for everything, and… You know, be more opinionated.
Because if we were more opinionated, that would open up… that would make a lot of things a lot easier, right?
Example, like, if we were more opinionated and said, okay, you… We're going to assume that you always have a collector.
So now we can make assumptions about, like.
We can make assumptions like, oh, the SDK doesn't need to have all this state management.
**Trask Stalnaker** 27:01 detection.
**Austin Parker** 27:02 Right, like, we can push a lot of this stuff off to the collector. That would make a lot of people very happy, right? That would… that would make… A lot of things… happenable.
But we don't want to do that, because that's not what the spec says, right? And we're trying to be… Very general, very generic.
You know, conversely, we go the other way and say, like, okay, we're doing too much, and, you know, now we're just gonna focus on… the spec. We're gonna be spec first, we're all gonna sit around and IETF this ship, and like… Write specs, and just put them out there, and let other people go off and implement them, and… Make everything take, like, 5 times as long.
And I think that… That's also… like… really challenging.
Like, that doesn't feel… good to me, because it doesn't feel like we're actually making anyone's life better.
**Trask Stalnaker** 28:06 And it's not the community that has been built.
Right, it's also not what people want. Yeah.
I mean, I…
**Austin Parker** 28:14 Perhaps most crucially.
**Trask Stalnaker** 28:15 I like what?
the… the community… I mean, I feel like the community is… like… Pretty much on target as far as, like.
Not too much, not too little, in terms of scope.
Is just the, it's just drawing that, I think, that really clear stability line… Yeah. …down… down the middle.
**Austin Parker** 28:40 I think this process will get us there, right? It'll get us towards being able… I really think that every SIG just should be able to say, here is sort of the minimally useful I have minimal use, like… here is, like… the 80% you know… Does what you need it to… Hotels…
**Trask Stalnaker** 29:01 stable, and if the 80% isn't stable, that becomes, like, I feel like… The part of this whole process to me is moving that stability Concept up to job number one.
**Austin Parker** 29:15 Right. Getting to the point where it's like, we… here is the 80%, here is the average, or the thing that we think covers 80% of the use cases.
And we're gonna focus on stable, making sure that that is stable, and it's tested, and it's perform… you know, and we stand behind our performance guarantees, and it's well documented, and there's, like, really good docs for it.
da-da-da-da-da-da-da-da, right?
**Trask Stalnaker** 29:39 We're gonna…
**Austin Parker** 29:40 Really?
**Trask Stalnaker** 29:40 We're gonna snow freeze, yeah, we're gonna slowly…
**Austin Parker** 29:44 Leopard. Everything. Snowtail.
**Trask Stalnaker** 29:46 everything else.
**Austin Parker** 29:49 Yeah, and everything else is just gonna be like, we will get to it.
Like, at the end of this, that's when that stuff starts to come back in. And in the meantime, if you, motivated individual, would like to run with one of those things, great! Like, go off and run with it. And figure, and let us know if it doesn't work, right? Let us know if there's structural impediments.
**Trask Stalnaker** 30:10 For wind, yeah.
**Austin Parker** 30:12 But I mean, because it really shouldn't… it should be pos… everything is so designed to be so composable and extensible, it should be possible for people to go and do some of this stuff independently of us.
**Trask Stalnaker** 30:23 Yeah, but so much of the value of the community is… Is that, is having the community, and it's very hard for people to build that kind of community.
**Austin Parker** 30:39 I… I mean, yes and no, like, Kate's does it.
Like… There's plenty of Kubernetes things that are not, like, part of core Kubernetes.
And Kate's is also bigger, but… I do have another meeting to get to.
**Trask Stalnaker** 30:54 Yeah.
**Austin Parker** 30:55 So…
**Trask Stalnaker** 30:56 Chat.
**Austin Parker** 30:56 Good chat. Talk to you later.
**Trask Stalnaker** 30:58 Cheer. Bye.
