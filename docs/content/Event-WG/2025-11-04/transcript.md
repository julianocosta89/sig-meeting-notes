SIG: Event WG
Date: 2025-11-04
Duration: 59 minutes
Zoom Recording URL: https://zoom.us/rec/share/co97VArXs4poJHj-ERRc3vMC48j9u87dJhjL5-uJyDbEKrf_9sfbD-wTltEvz7vr.jky8t-E6OSJ5JW6q
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 00:24 Hey, hey.
I left that comment on the blog post.
Let me know…
**Pellared** 00:45 Hello, hello!
**Trask Stalnaker** 00:49 Hey, Robert.
**Pellared** 00:52 Nice to see you.
**Trask Stalnaker** 00:54 Yes, long time no see.
**Pellared** 00:56 Yeah.
Yeah, but…
**Trask Stalnaker** 00:59 In person.
**Pellared** 00:59 Next time we'll see person next week, very few.
New future.
**Liudmila Molkova** 01:07 Hello!
**Austin Parker** 01:08 Howdy.
**Trask Stalnaker** 01:09 Okay.
So we could talk about both, the… log… processor is enabled, and we could also chat, Austin, about the blog, the… we could go off-topic from blogs, after, and talk about the blog post, if that helps. I know you… you want to get that out.
**Austin Parker** 01:35 Yeah.
**Liudmila Molkova** 01:39 I also would like you to ask, kind of Austin to review another log blog. Well, the log blog.
**Austin Parker** 01:48 Blog, blog…
**Liudmila Molkova** 01:50 A log blog, yeah.
I mean, it would be nice to get it out for KubeCon.
**Austin Parker** 01:57 Yeah F to… I have to leave before the bottom of the hour, so if there's…
**Pellared** 02:21 Let's start with yours, then, Oscar.
**Austin Parker** 02:26 Yeah, I… that's fine, Trask. I'll take it… I'll go through and edit it this afternoon. I think your comment's fine.
**Trask Stalnaker** 02:35 Okay.
Yeah, I don't know, like, I feel like each time we talk about it, it's a little confusing of… I know we're trying to thread, like, a fine line there of… telemetry stability.
being a different concept from semantic convention stability? Like, the telemetry emitted by an instrument…
**Austin Parker** 02:59 Yeah.
**Trask Stalnaker** 03:00 can be stable.
**Austin Parker** 03:01 Right, I think… I think that's probably what I'll go through and rephrase this as, and just be more specific and just say, like.
Cause I… I also… I do… I think the stability normalization will also wind up impacting SemComv, right? Like… Because part of that is gonna be things like… part of… moving levels is that you have, like, published metadata, and, like, your docs are accessible in a conventional place, and, like, there's a lot of other things into it, and we need to be, across the entire project.
very consistent with, like, when… when something is X… has X stability level, that means that this, this, this, this, this, right? And it doesn't matter what that component is.
It has to meet all these criteria, and it's, like, one set of criteria, and then they're in the same place, and so any… any user can go and see, oh, this is… RC, that means these things are true.
And so… Now, some of those, like…
**Trask Stalnaker** 04:20 There might be a slight nuance between spec…
**Austin Parker** 04:24 Maybe?
**Trask Stalnaker** 04:25 ability, and… code stability?
**Austin Parker** 04:29 Well, so… I… yes, but, like, I think the… but part of… but this is also… but this is, like, the… so, actually, that's a good… Thank you for calling that out, because that's kind of like the QBQ here, right? Is that… and I… I think I said it… I don't know if I said it in the blog.
I know I said this… on calls to, like, the TOC.
Is that, like, We… The flow is, oh, here's the spec.
and we say something is stable in the spec, and here's what we mean by that, and here's what we communicate to maintainers about that, and then we talk about it, and Joe Schmo, uncoordinated end user, says, oh, this is stable.
Right? Because they hear about us… because we talk… because we don't, as a project, make a great distinction between, like, spec stability and da-da-da-da-da.
So people hear or read, like, oh, metrics is stable when we said that 3 years ago or whatever, and then the lived experience is, like, oh my god, no, this is not stable at all if I'm, like, an SDK user, because… you know, like… if you… when you saw Metric Stable 2 years ago, or whatever, and you went and grabbed, like, the Go SDK at that point in time, you definitely got unstable code. Like, you got APIs that changed, like, within every month. You know? And so… I could probably reframe the entire blog post to be like, hey, start treating OTEL as a consumer product.
Like, when we… as, like, the deliverable from OTEL is not the spec, it is the actual distributions, and that's what's changing.
**Trask Stalnaker** 06:20 Yeah, so when we, like, advertise, like, metrics are stable, like, that should mean.
**Austin Parker** 06:26 That should mean that you can download this and use it, Right, so I think, actually… Note to self.
Yeah, so, like, I'll… I will probably… I will note something to that effect, like, hey, the short version… like, what are we really talking about here? We're really talking about, like, we all need to think of this more as… a product, and not as, like, a specification that happens to have a bunch of reference implementation, you know, that happens to have these reference implementations. Now, as we are working on it, like.
like, I think the work that this SIG is doing, right? Like, we need to consider that part of our consumers are, you know.
not just… end users that want to get logs out of their application, it's… people building frameworks and runtimes and, like, you know, right? There's, like, a lot of different users and use cases.
But specifically around, like, stability.
We're way too narrow. Like, we're… we… we are characterizing things in a way that is advantageous for us.
To kind of talk out both sides of our mouth a little bit, and be like, oh yeah, metrics is stable, or oh yeah, logs is stable, when it doesn't really, like… Spec stability is a thing that… you know.
people don't care about. I think to your point in the call earlier with Milla, like, it doesn't necessarily matter what you say about the stability of a SEMCOM. Because… in Gen AI, like, yeah.
Four different companies went out and implemented it as soon as it hits the repo, because they're trying to sell a product, and they want… and their product is, you run this thing, and we give you a fancy dashboard about how many hallucinations per second your AI is doing, or whatever. I'm minimizing slightly here.
But… it… that's not, like, an important thing to them, like, they don't get value out of the slow process, and what I think would give us more value is being able to say, like, okay, we want to free these things from this… this process, we want to encourage federation of SEMCOM, and we want to be more specific about saying, these are the core things that we are going to commit to as a project, and we want to narrow the scope of what we're going to commit to as a project, so that we can build a more focused product around it.
And… yeah, I guess I've hedged a lot of this simply because… That's… a controversial suggestion.
**Liudmila Molkova** 09:38 I mean, I… I'm super supportive of the message you just delivered, that the stability of the spec and semconf is an internal thing. Our users don't care about it. What users care about are the stability of actual artifacts they're dealing with.
We can think more about them, and we can tell them not to think about, we can emphasize the stability of individual components that they actually interact with.
**Austin Parker** 10:08 Yeah.
**Liudmila Molkova** 10:08 So what we can do from some perspective, I think, from instrumentation's perspective, is if we untie those, stability of those two from each other.
that, instrumentation has a version. It could have a beige saying which version of semantic conventions it implements. It could also eventually have a beige saying how well it implements it, right? The green, yellow, red. And then.
Combining these two, you kind of get a quality of the instrumentation. If somebody external ships some whatever random shit, we could give them a beige that it's a shit.
**Austin Parker** 10:46 Yeah, like, I think… I think the biggest thing for that is gonna be just saying, like, hey, here's the actual metadata format we want people to use.
And… and giving everyone a, like… If you would like to ship a component that has… that declares stability in some way.
and you want it to be discoverable, and you want all this stuff. Here's… here's what we expect, right? We expect open telemetry.whatever, or something.otel.yaml at .well-known.
And that's where you should put your schemas, and that's where you should put the stability document, and da-da-da-da-da-da-da, right? Like… Just… Making it interpretable to people, making it interpretable to end users, making it interpretable to, like, ecosystem stuff.
And, yeah, fundamentally saying… Telemetry stability is not… code stability, right? Like, you can have highly performant, well-tested, benchmarked, stable, not-gonna-crash-your-shit, instrumentation libraries that depend on unstable SEMConv.
And it doesn't change the stability of the instrumentation. The instrumentation code's not gonna change. The SEMCOM might change.
But here's all these techniques that you have to grapple with that.
**Liudmila Molkova** 12:10 Well, the instrumentation can change, but it will change through a major version bump.
**Austin Parker** 12:15 Right, like, when it changes… It'll change in these ways, and here's how you… Like, it's not gonna change out from under you unexpectedly, and… Here's ways that, you can interpret… like, here's ways that you can migrate through those changes, so it's not… You know, like, I think one… I think a way to think about this is, like, Kubernetes, right? Kubernetes releases pretty frequently, and one thing that annoys a lot of people about Kubernetes is, you can't do… You can't skip versions.
Right? Like, you have to… like, if you're on 1.30 and you want to go to 1.35, you have to take every intermediate update, because they just don't… because the complexity of doing it some other way would be, like, horrific.
And… I think… I don't know if that's… like, I don't think we want to, like, go that far. I think we want to be able to say, like, oh, you can go from X to Y, kind of arbitrarily.
But, you know, here's… but you should… what you should be able to do, what we can guarantee to you, is that when you do that, you can sort of have an idea of, here's the laundry list of things that are gonna change when you do that.
Like, so you know what's gonna be different.
Anyway… The feedback trask.
**Liudmila Molkova** 13:47 Yeah, Robert, go ahead, I have a follow-up question to Austin.
**Pellared** 13:51 I have, like, one, connected thing, so right now in Go, in Autel Go, we are working towards stabilizing our first instrumentation library, which is instrumentation for Autel HTTP, and for the feedback that we got so far from the users.
That basically, people would like, if the instrumentation library is stable, It means that both the API is stable, and the telemetry is stable.
If we will change the telemetry, or if it will use unstable telemetry, people will freak out because they will be too hard to decide if… and if there will be uncompatible changes.
there are two ways that we could potentially use. One, make a V2, if, especially if it's an API change, then it will be in ETV2, but it will be a telemetry change, then maybe some environment or variable that will say, but it will need to be in the opt-in configuration that, by default, it still emits the stable telemetry.
And I think that these kind of things are missing in the specification and recommendations. Or, if they are.
Then, yeah.
**Austin Parker** 15:01 that level of detail would be in the OTEP. What I have in my mind is that we basically treat it like the HTTP stabilization.
And… When you… And this is one of the reasons that I wanted to normalize it, but what I was… my thought process basically is… going… whenever you update SEMCOM, or whenever you update telemetry.
Then you need to have a… Flag… you basically need to dual write.
The old telemetry and the new telemetry for a period of time.
And… that's kind of the general solution to this, right? Like, a better solution is, oh, we have all the schema transform stuff working.
But we don't. So… Until such a point that the schema transforms work, then the answer is, you know.
And I guess we could even… we could even, like, probably wrap this in… like, I think… this is what I was trying to get at earlier, though, Milla, like… A really convenient way to kind of handle this would be to say that there's no stability… that That telemetry never… like, telemetry is just versioned, and the version number always increases.
again, it's just, like, a date or something. And then in config, you pick this… you pick… you say, like, which versions do I want to write? And… Yes, there are… Downsides to that, in terms of how long you have to keep all those around.
**Liudmila Molkova** 16:59 I think it's the best user experience, and I would love to be able to build this user experience. I don't think it's feasible, though.
So, with the amount of contributions we get to instrumentations.
**Austin Parker** 17:15 Well, we also want to have less… we want to… we would like less, we would like fewer, right? Like, part of this is definitely… we don't want… we want to be able to… I think… I really don't… I do not think it's sustainable for us just to say that OTEL is the home for all of this stuff.
Right? Like, I think we have to be specific and say, here's the core things that we think are important that we're gonna support up from the project distros, and if you would like to instrument something else.
Great, here's how you should do that. You should go and try to get that native. And if you can't get it native, then you can host it somewhere else, and here's how you make it discoverable, here's the, you know, here's the metadata format, and all the stuff that you need to do to make it play nicely in the ecosystem.
But, like… I don't know, it just doesn't… it doesn't feel to me like we could… Ever have, like, a really quality, polished sort of thing If the answer is just like, oh… everything has to go into the SimConf process, and everything has to be, you know, in Contrib, and we have to… we have to own all this stuff.
**Liudmila Molkova** 18:31 I'm curious how…
**Trask Stalnaker** 18:33 If there's any disagreement with that.
**Austin Parker** 18:35 Yeah.
**Liudmila Molkova** 18:39 I'm interested, like, how many baby stress would you be ready to kill in your Java instrumentation?
**Austin Parker** 18:52 I mean, the flip side of this is… I mean, part of the problem is, there's also… there's too many… Like, for as appealing as it sounds, just like, oh, we're gonna… we're gonna do all this stuff to cut scope, like… I have people DMing me right now, asking to increase scope and start new SIGs, you know, like… and I can't say, like, oh, that's a bad SIG, or like, that's a bad idea. It's like, actually, it's like, no, we should, this should be something that we do. But we, you know… what are we gonna do? Like, we can't just keep increasing scope forever.
And I don't really want it to be like, oh, we're killing your babies, or we're making it less useful. I wanna… I would like for us to be able to… reorient and focus, right? Like, I really just want for us to be able to say, hey, these… Us saying these things doesn't mean that we think that other things are less valuable, or not valuable, or whatever.
It means that we want to be able to… like, meet people where they are. Like, if people want… if people want OTEL to be… A replacement for third, you know, for commercial instrumentation agents and instrumentation libraries.
Then maybe we have to lean into that more, right?
**Trask Stalnaker** 20:38 Alright.
**Austin Parker** 20:39 Anyway…
**Trask Stalnaker** 20:39 Back on topic.
What is our topic?
your blog post, so you're… oh, I had a follow-up question for Robert. You said that feedback for Go, in Go.
Was that users wanted telemetry stability.
I just wanted to clarify if you mean telemetry, Stable telemetry, or… Stable telemetry based on stable instrument… stable semantic conventions.
**Pellared** 21:13 Both.
**Trask Stalnaker** 21:16 Why do they care if it's… Based on stable conventions, as long as you don't break their… The telemetry that's emitted.
**Pellared** 21:30 So… First of all, we… the problem is that still we are, as a group, as Sikh.
**Trask Stalnaker** 21:41 We are postponing the civilization as.
**Pellared** 21:43 as, you know, as… as late, as… not soon, but as further as possible, because, we have a lot of things to stabilize anyway. So, if we have the stable semantics, it also helps us, you know, to… think of, for example, what are the extension hooks needed, the configuration, etc, so it makes us easier to also come up with StateBree API.
One reason… Second is that some people already said that if something is stable, they assume it's also semantic condition stable, so I think it's just more clear that if people use, you know, an instrumented library which is stable, it means that the API is stable, but the behavior is also stable, and the term that is also stable.
Okay.
**Trask Stalnaker** 22:30 But the behavior can be stable.
Like, you can, like, why can't you release stable RPC.
**Pellared** 22:40 Hi, interesting.
**Trask Stalnaker** 22:41 instrumentation today that's based on the existing semantic conventions, and you just… you wouldn't be able to change the telemetry that it emits And without doing a major version bump of the instrumentation itself.
**Austin Parker** 23:01 That… that's my point, right? Like… We should be… instrumentation should be able to say, like, hey, the instrumentation itself is stable.
**Trask Stalnaker** 23:10 the behavior.
**Austin Parker** 23:11 The behaviorist library is stable, and its API service is stable, and the way that you… like, the GoHTTP thing's a good example. Like, I think it's reasonable for people to say.
**Pellared** 23:23 4 o'clock.
**Austin Parker** 23:24 whenever I take miter bumps to this, I don't want to have to rewrite my… I don't want to have… I don't want…
**Trask Stalnaker** 23:30 Reports and alerts.
**Austin Parker** 23:31 Well, no, no, I don't want to have to rewrite the, function call, right? Like, I don't want the way that… this to let… like, because in Go, you have to decorate… you… what is it, you add… I forget if it's, like, in the current NetHTP, is it… you're adding it as middleware, or you're wrapping the route?
**Pellared** 23:56 Buff. That's right.
**Trask Stalnaker** 23:58 But that's basic code… that's basic code stability.
**Austin Parker** 24:01 Right, but that's my point. Like, when you take a minor update, that should not change.
**Trask Stalnaker** 24:06 Also, your dashboards and alerts should not break.
**Pellared** 24:09 Yep. Right. That's what our user says.
**Austin Parker** 24:11 And when you take a major, it's okay for either of those to change. My point is… we should be more comfortable saying, like, hey, this instrumentation is stable. It's stable because it depends, like, it's stable, and we're guaranteeing that as long as you don't take a major update of this.
Your dashboards aren't gonna change.
And if you do take a major… and if we do bump it, that's fine.
We will commit… we should commit to emitting both versions for a time.
Or having some… some… maybe… there has to be some migration path, right?
**Pellared** 24:48 Put a flat sugar from the ground.
**Trask Stalnaker** 24:51 I mean, I… for… for big ones, like HTTP breaking and database breaking.
**Austin Parker** 24:58 Yes, you know… For my own, sure, like, that's what… and this is, again.
**Trask Stalnaker** 25:02 This is why I… It's a lot of work.
Right.
**Austin Parker** 25:05 And this is why I wanted to add more granularity to the… SemConv, because I wanted to be… I wanted to map that migration timeline to where is this at today?
**Pellared** 25:17 Okay, so, the thing is that… Right now, if we have unstable instrumentation libraries, We can also, We can also change both the API and the telemetry Unlimited, so we have more freedom Of getting feedback from the users if the changes in the semantics are okay or not.
So, we are very… We do not do any of those frequently, nor API changes, no telemetry changes.
But at least we do not have to basically bump a major a lot of times, which is a very not-so… which is very not welcome in Go, because you need to change all your import paths.
**Liudmila Molkova** 26:02 It's not… it's not welcome anywhere, right? Even if.
**Pellared** 26:04 Exactly.
**Liudmila Molkova** 26:05 It's not welcome.
**Pellared** 26:07 Exactly.
**Austin Parker** 26:08 Again, we don't… we can't have it both ways, right? Like, I get that it's frustrating, it's also frustrating that like… It frustrates end users that… We won't stabilize anything.
Right? Like… I've said this on this call, I've said this on other calls, we need to be more confident.
We need to… we need to, as a project, we need to be able to say, we think, based on our expertise and $40 billion, whatever, that this is a good… this is good enough, and we think it is shippable, and we think that you will get value out of it, and great, we do that. And then.
We let it go into the world, and if a lot of people come in and say, hey, you missed the mark, you didn't do great, whatever, okay, we can change it, it's just code.
But, like, we can't just say, like, oh, we have so little confidence in what we're doing that every single thing is gonna stay experimental forever, because we haven't done the year-long process of having meetings about it.
Blake… Part of the… a very big critique of OTEL is that we are way, way, way too slow.
And this conversation right here is an example of why, I think. Like, we are deliberative, and that's fine, like, we're not… we shouldn't be just cowboying everything out, but we need, like… like, these are… this is a trade-off, right? Like, these are compromises that we're making, and I worry… And I think the evidence I have is that we are choosing…
**Pellared** 27:47 I hit…
**Austin Parker** 27:47 slow.
**Pellared** 27:48 comment. I think that we'll need to make a survey to assess if people really are worried about the timelines, you know, establish a session, because we only hear about people complaining.
I personally had a lot of people that were very… we are personally, as maintainers of Go, we are pissed off that it takes us, like, 3 years to stabilize anything. On the other hand, we had a lot of good feedback in person at KubeCon, that people are very happy that you are very slow and conscious. I understand.
**Austin Parker** 28:18 That I need those people to… Answer surveys when they're asked.
**Trask Stalnaker** 28:23 I…
**Pellared** 28:24 Yeah, I mean…
**Trask Stalnaker** 28:24 Do you wanna…
**Pellared** 28:25 We hear Israel complaining, but we do not, you know, hear people that are, you know, pricing.
**Trask Stalnaker** 28:30 I think it's important to differentiate.
**Austin Parker** 28:33 Robert, are you gonna be at KubeCon?
**Pellared** 28:37 Yeah, like, 4 or 5, 4 times.
**Austin Parker** 28:40 Oh, you're gonna be at this KubeCon.
**Pellared** 28:42 Yes, I will be there.
**Austin Parker** 28:43 Okay, remind… remind me to pick up this specific part of the conversation with you at KubeCon.
**Pellared** 28:50 Like, I was also compl… I was also the man who's complaining on stabilization, so stabilization thing.
**Austin Parker** 28:56 Yeah, I…
**Pellared** 28:56 You know…
**Austin Parker** 28:58 Some of this… I will say, on this call right now, I will say, There are very specific things that have led us to this blog post and this current conversation That I will be happy about to… I will be happy to tell you about in person.
**Pellared** 29:16 Okay.
**Austin Parker** 29:17 To add a little more color.
**Trask Stalnaker** 29:19 Robert, I think it's important to differentiate between, stabilizing API… like, open telemetry, like, things that are used transitively, On transitive dependencies.
Core things like that, versus stabilizing instrumentation libraries.
So, things like API, you know, Logs API, totally agree that, you know, like, in the Java, we never want… we never want to take a… we never want to do a major version bump.
on the Logs API, Traces API.
**Austin Parker** 30:05 Yeah.
**Trask Stalnaker** 30:05 API.
instrumentation itself.
**Pellared** 30:09 It would make 10 major bumps, and it would be that about that bad. Yep.
**Trask Stalnaker** 30:14 Yeah, it's okay. It's okay. It doesn't… people don't really… don't really complain that.
**Austin Parker** 30:19 It…
**Trask Stalnaker** 30:20 Much about that.
**Austin Parker** 30:21 Cool. Yeah. And then there's a… and again, like, I think the… One of the other, sort of, pieces of feedback we get is that part of the reason that those instrumentation version bumps are hard is because of, like, size and scope, right? Because if you're trying… like, a thing that I see, talking to, like, field engineers at Honeycomb, is that sort of the cross-product of all of this stuff is really, really challenging for people.
Because there's so many different versions of things, and this is part of what the idea of, like, having epoch releases is supposed to solve. It lets us sort of pin all these things and say, like, hey, boop, here's this. And I think that we'll need to consider that in the context of You know, when we talk about doing these major version bumps, because it's entirely possible that we could be in a world where, oh.
My instrumentation was at version 4… for Epoch 1, and… in 4 months, we're on Epoch 2, and that has had 3 major releases, right? And so we'll need to consider that, you know, we will have to go support upgrades from, sort of.
any arbitrary point to any other arbitrary point, which is why I'm in favor of, sort of, like, transform-based ways to do this, or dual emission, or whatever.
**Liudmila Molkova** 31:53 I… Maybe…
**Austin Parker** 31:56 Really?
**Liudmila Molkova** 31:57 maybe we should apply the principle, Austin, you articulated, that we should not… we should think about it from the user perspective. Like, the problem, let's say if we pick Python up in telemetry, the reason they don't stabilize individual instrumentation libraries they are far away from systematic convention stability, I feel. They are bundled release, and maybe something else. So… it's not even, like, let's maybe trade the stability of semantic conventions as internal detail, and try to focus on the reasons why SIGs don't stabilize instrumentation libraries. And it's probably already in your blog post, it's just a general thing for us. I don't care, like, what.
**Pellared** 32:43 I think it's also for Rust, but I think it was also for Go that instrumentation libraries were depending on APIs. So, for instance, there was no… we didn't want to stabilize Auto HTTP instrumentation.
before Metrics API was stable, because just having traces without adding, having a way to add metrics later.
is hard. So, same, like, we also want to establish a logs API as soon as possible.
**Austin Parker** 33:13 Right.
**Pellared** 33:14 it will be semantic conventions for events, so we can add it to this library. So, yeah.
**Austin Parker** 33:19 I, yeah, and I understand all of that. I also tend to think, like.
I think we've kind of gotten the worst of both worlds in this scenario, where, from a practical perspective, we've… Something I joked about a while ago is, like, maybe we should have just said, like, oh, OTEL 1.0 is traces, and then OTEL 2.0 is traces plus metrics, and OTel 3.0 would be traces plus metrics plus slogs, and maybe we should have been thinking about this as… working on it as one signal at a time, and I understand why we didn't, and I think there's a lot of good reasons for doing it the way we've done it, but what we have done in practicality is that we have basically done exactly that, right? Because when people use OTEL… when you say OTEL to most people, they think, oh, the tracing thing, because that's the only thing that's stable, and so that's the thing they use.
like… I don't… I… I… I understand… And… I don't have, like, the two, you know, the two flip answers are like, well, we either have to, like.
Be faster, and, like, get stuff out more.
by just doing more work, which I don't think is necessarily going to solve anything, because I don't think the problem is that we're not working hard. I don't think the… I think the problem is, is that, like.
the amount of people that want to use OTEL for the sake of using OTEL, like, the amount of people that, like, we have a lot of consumers, right? We don't have a lot of design partners.
And we don't have a way to sort of get… Feedback.
from consumers. We have a way to get feedback from design partners, to use some PME sort of words.
Right? Like, most people that come to OTEL, like, they just… it's like, oh, I install this, and then I get telemetry output. Cool. And they don't think about it any more than that. Other than, like… except when something goes wrong, right? Like, oh, I installed OTEL here, and I installed OTEL there, and my traces are disconnected, that's weird.
Right? Like… We have this very broad… sort of… you know… broad user base that is mostly, you know, that I think a lot of them are rightly or wrongly see observability and monitoring as sort of, like, an extra side thing that just, like, I… like, I don't think about this, I don't care about this, like, I run the agent, and it tells me where the problems are, right?
And those people aren't necessarily gonna be doing a lot of, like, exhaustive, like… you know… testing of SemCom, right? They're not… they don't necessarily care, they want… they… We're not getting feedback about, like.
is this good or is this bad? And when we do, it's like, it's because it's bad, or it's because, like, oh, I'm trying to do some… I'm thinking about people that, I'm thinking about things like query parameters and URLs.
And people coming in and being like, oh, you can't do that because we're putting sensitive values in our query parameters.
And… Okay.
Or, like, oh, this has really high cardinality in this circumstance.
That… you know… We can argue if they should have been doing that, or if they should be using a different tool, or whatever, but, like, we… we wind up having to kind of, like.
Match all these use cases that are… and that's hard to do.
Another way to deal with this, though, another way… another way we can kind of conceptualize this, you know, and I think that leads us to, like, oh, okay, so we're gonna… we have to go slow because we're not getting good feedback, so it just takes a while. We have to, like, really push and push and push and push to get feedback. Another way we can get that feedback, though, is just to, like.
If we assume that that's not gonna change, that we don't have the ability to dramatically improve that feedback loop. Then another way to handle this is just to say, like, okay, well, the practical reality is, is that people treat this stuff as stable.
or people install this stuff and then walk away and forget about it. Like, let's just approach it the same way from versioning, and let's just say, like, okay.
This bundle of stuff, boom, put a fork in it, this is one point whatever, and… here's the guarantees we make about this, and… you know, whenever we… and then we… and then we hear feedback, and people are like, oh, this works, or this doesn't work, or whatever, and we say, oh, okay, then we're gonna do a version bump. And we bump the versioning instrumentation, and it dual writes for, you know, one release, and… You know, if people take it, they take it, they don't, they don't. Like… Like, I don't know, I don't… I do not have the answer here, other than… We have gotten… direct feedback that… the current… That the status quo is not working out great for… Enough end users that it's causing problems.
And… What needs to change is more how we conceptualize this than anything else.
Anyway, I have to run, but looking forward to seeing everyone next week.
**Liudmila Molkova** 38:56 Yeah, see you next time.
**Trask Stalnaker** 38:58 Thanks. Bye.
Alright, let's talk about log processor is enabled.
**Pellared** 39:07 Okay.
**Trask Stalnaker** 39:09 What?
Why don't you want to, like, why don't you want to just spike a proposal for… How to do, like, making chained processors a… first class thing in the spec, and how to represent that in declarative config.
**Pellared** 39:37 I'm not sure, like, so… I posted in the comments how you can look into declarative config, and Tyler said to me that it's okay.
I'm not sure that… how to specify it in the… how to specify it in the specification other than supplement the teleguidelines. I mean, it doesn't need any new, you know, components of this… of the SDK or API. It doesn't need to be anything more than we already have in the specification.
**Trask Stalnaker** 40:13 Let me just…
**Pellared** 40:14 I don't know, I do not know how to basically, you know, just put it into SDK, like, copy-paste it there, or just, you know, or just coin some concepts, and say that, you know, we name… we say that this kind of pattern is named blah blah blah.
But… and do we want to have it in the SDK? Still, if it's in the SDK, we will not have any interface code like that, so… Yeah, none of those things will be normative values, I think.
**Trask Stalnaker** 40:42 What I was, imagining is… the language I was imagining the spec would be something like, In the log processor… Spec.
Saying that log processors may be… .
**Pellared** 41:04 composed.
**Trask Stalnaker** 41:06 chained.
Okay.
When creating a log processor, You know, you would pass in… a delegate.
And… that would be… and I agree, like, it doesn't… necessarily need to have, like, even a new interface, I don't think.
But it would then be, like, you would, onEmit, you would update the spec to, say, onEmit.
It first, or it… Calls the delegate prop… the delegate processor.
So, basically, adding this… Concept of having… that log processors… log processors can have a delegate.
**Pellared** 42:05 Here's… it's… it's here.
we can add more… as a new… I can put, like, a comma, filtering.
And it's also here.
**Trask Stalnaker** 42:24 So, I mean, if we think this is enough, like, this is not my end goal. My end goal, and I don't really care how we get there, is in the configuration, in the declarative configuration.
I want it to be clear that, like, that… Diagram that you wrote in the spec meeting?
That that is the way to… that… All… if a log record processor supports chaining.
So basically, log record processors.
**Pellared** 43:00 I know, I know.
**Trask Stalnaker** 43:01 either support chaining, or they don't. If they do support chaining.
**Pellared** 43:05 something like.
**Trask Stalnaker** 43:06 And then…
**Pellared** 43:07 You want to have this in declarative conceiv.
**Trask Stalnaker** 43:10 Yeah.
**Pellared** 43:12 So, I can file an issue, because similar to what we already have, where was it?
So there are those two issues which are already for sampling and composing samplers.
Like, these are here.
Basically. Oh, yeah.
**Trask Stalnaker** 43:34 Yeah, delegate. Yeah, yeah, exactly like that.
**Pellared** 43:36 So basically, it's only about the same pattern, and I think that basically whatever declarative config will do anyway, they will follow the same pattern. But the thing is that this pattern is not even, you know, there's not even an agreement how to do it from for the samplers. But whatever will be done for the samplers, basically the same will be done for processors.
They'll use the same pattern.
**Liudmila Molkova** 43:59 Wait.
The pattern is the same, but the processors… have both directions. Samplers could only be delegating.
Or not delegate. So you can have one, or there… you can have a chain.
But the top level, there is always one.
Well, log processors, we are past this point. We need to support both.
And… than… Like, the… even the line you're trying to stabilize depends.
So, the line that there is discussion on all registered Log record processors implement enabled and a call to enabled on each of them returns false.
It just doesn't work for… for chained processors.
**Pellared** 44:57 Why it doesn't For unchecked.
**Trask Stalnaker** 45:01 range processors.
**Pellared** 45:03 For untrained, it will return always true.
If one of them does not implement enabled.
**Liudmila Molkova** 45:12 So then the…
**Pellared** 45:13 exactly what work… it's exactly how it's supposed to work. If they're changed, they're basically changing the enabled, if each of them supports enabled. But it is an implementation detail, basically.
**Liudmila Molkova** 45:24 So what you care about, the top-level ones return.
False.
It's like, you cannot write this line without the explaining different behavior.
Or chained and non-chained.
**Pellared** 45:44 So, this is all… SDK… So, this behavior… it was in the SDK, log record processor.
**Liudmila Molkova** 46:00 So you need to document the chained behavior of enabled and unchained behavior of enabled.
**Pellared** 46:10 Oh, Jesus.
So, this is basically… this behavior here.
**Trask Stalnaker** 46:24 So…
**Liudmila Molkova** 46:24 Alright.
**Trask Stalnaker** 46:26 If you introduce a concept of a… if you introduce a formal concept of a delegate, an optional Delegate, or log record processors.
Then you could add… The behavior for enabled enabled…
**Pellared** 46:48 The thing is that it cannot be only a single delegate. It can be two, it can be array, depending on the processing pipeline, because you can…
**Trask Stalnaker** 46:55 Do we want that?
**Pellared** 46:58 Can we avoid… can we avoid that?
Yeah, but for instance, somebody was asking to have a different pipeline for events and for log records. So, if there's an event name, they wanted to use a different log record processor.
**Trask Stalnaker** 47:17 So we already have them at the top level. We already have… Multiple.
Do we need… Can we just leave it there? Like…
**Pellared** 47:29 I don't understand. So, for instance, you want to use a different exporter, for, you know, for events and for events and non-events.
You need to make the routing, basically, right now.
**Trask Stalnaker** 47:48 So you have one… so you would have two top-level log record processors.
One that filters… Down to one, and one that filters down to the other.
**Pellared** 48:03 Yes.
Yes, I think it was… I think I even put this example here.
Routing, event landlock process, or…
**Trask Stalnaker** 48:20 Oh, this has two… I see, this is a… I'm not really worried about, like, this is a… This is… Not, like, a generic… Hmm.
**Liudmila Molkova** 48:41 It kind of makes sense. Imagine if you want to… Augment something, or filter something, and then… Apply different logic.
That's for two different places. It makes sense to have the start of the pipeline the same, but then fork at some point later. Otherwise, you need to fork and then apply twice.
**Pellared** 49:11 So the thing is that there could be multiple patterns, and you know, this training is just one of them.
You can have been, have, you know.
you know, even this kind of train of responsibility pattern. For instance, if there's something, you know, for example, if there's an error record, an error, error log, you put it, you know, to an additional, for instance, exporter.
Sorry, Amisha.
**Liudmila Molkova** 49:42 So it sounds like the chaining is just the… all the advanced scenario, and the only reason we're discussing it here is because we want to tie enabled to the chaining.
If we forget about chaining, that things become pretty nice and clear.
Is it the case?
**Trask Stalnaker** 50:05 But is enabled is useless if you don't do chaining.
**Pellared** 50:11 Why not?
**Trask Stalnaker** 50:17 Because if you don't do chaining, you just have a list of your processors.
And you're… you're gonna have some processor in there that, like, it's gonna be really weird. You add a random processor that doesn't implement enabled, and suddenly now.
Your enabled doesn't work at all.
**Pellared** 50:34 Yep.
Only this scenario, that's correct.
**Trask Stalnaker** 50:38 Doesn't sound like a good user experience.
like, from a declarative configuration perspective, I have a good… I have a… you know, I have my log processors configured in declarative configuration. Everything's working great.
you know, these 3 that I have in there, implement, enabled.
I go and I add a fourth one in there, and now I broke everything. That's very surprising.
But this is a good example here, this is making me think more about, like, what does… and also this fact that…
**Pellared** 51:29 Just to say one thing. I agree with your concern, but I think the only way to mitigate it would be to create some new way of registering new APIs for the log record processing.
And I don't think it's a good idea. So, you know, we even agreed in Go that we'll follow the same pattern. I don't remember which, if you remember. I wanted to force the training for Go.
**Trask Stalnaker** 51:54 Yeah, yeah, yeah, yeah.
**Pellared** 51:57 But I think… to the point, you know, having stable things and similarities, I think it's a trade-off that we need to live with right now, because I think we'll just increase the complexity if you just do more and more things.
It's a little bit of food gun, I agree, because then someone can add the processor at the top, which does, for example, you know, some reduction, whatever, and then able to stop working.
Right? You can't.
**Trask Stalnaker** 52:22 I like…
**Pellared** 52:22 Second, the first one will change the attributes, and the enable will stop working, for instance.
**Trask Stalnaker** 52:30 I like the direction of going to chaining. I like the model that, like, That.
Just simply makes a lot more sense, especially for the… The log record processors.
But even all of them, like, wrapping things, so, I guess… And I mean, I… I guess until we… I'm kind of coming around to your… Point on the declarative config being… Like, how… how do we even specify… dot sub… The name of that nested thing.
Maybe that's only even relevant… Because the example you had where you could have two delegates.
And if you do have a… if trying to write in that delegate to the spec.
like, is enabled. Sometimes you want your delegate to… Block the chaining, and sometimes you want to flow it down the chaining, so… I'm not really sure how to even say that.
**Liudmila Molkova** 53:55 it could… does it have to be sad? So, if… There is delegating… let's… let's say there is the processor.
there… there could be a delegating processor. It's effectively a different model in the configuration.
Or there could be a full bar processor that you implement yourself is a custom behavior, so each of those processors Could, in theory, have its own set of configuration properties.
**Pellared** 54:30 That's what.
**Liudmila Molkova** 54:31 You don't… yeah.
**Pellared** 54:32 That's how it works anyway.
Even if we put something to the spec, that's how it will be registered and implemented.
Mmm… Most languages, anyway.
It will be still on the people who are writing the processor implementation that will be registered to the declarative configuration module, or whatever, however it is called, and how it's, you know, registered and then resolved.
I don't think you want a base class for it, basically.
**Trask Stalnaker** 55:08 Yeah… yeah, I don't see how that helps.
I'm…
**Pellared** 55:22 prospect.
Take your time, we are not merging this soon.
**Trask Stalnaker** 55:27 Can you share that, the sampler, the sampler example that you had up?
**Pellared** 55:33 So, if we go back to the comments… So, it's here, in my first response to your comment, here.
Do you want me to open it right now?
**Trask Stalnaker** 55:48 Yeah, yeah, yeah, let's look, let's look at it, just for.
**Pellared** 55:51 Because there are two, So, one is the composite sampler.
And there are a few proposals.
One is delegate, one…
**Trask Stalnaker** 56:07 I was like, okay. Yeah, and so these are…
**Pellared** 56:10 here.
**Trask Stalnaker** 56:11 These are specific, named… samplers.
**Pellared** 56:17 Yes.
**Trask Stalnaker** 56:18 And so, yeah, so I think I'm… I'm coming around to this… That until we have the named… specified… Log processor… log record processors that this… would just… doesn't matter.
**Pellared** 56:40 Yep.
And here's the second one, composable.
So here… as rule-based.
And this one, as you can see, have even rules.
And there's a sampler for each rule, basically.
This one is more advanced.
**Trask Stalnaker** 57:00 Right, but where's the delegate? Yeah, it's the delegate that I wore.
**Pellared** 57:04 Here, so we have the room bank.
Sampler, and it defines rules.
**Trask Stalnaker** 57:09 Hmm.
**Pellared** 57:10 can have a sampler. So this is even more and more advanced than whatever I presented so far. It kind of regulatory resembles a little biting one.
**Trask Stalnaker** 57:21 Right, right.
**Liudmila Molkova** 57:23 It's actually already merged.
It's already there.
**Pellared** 57:27 This one?
**Liudmila Molkova** 57:28 Yeah.
**Trask Stalnaker** 57:31 In the sky. You can already…
**Liudmila Molkova** 57:33 In the configuration. In configuration. Not sure about this one.
**Pellared** 57:38 You have reopened it. You can reopened it.
What?
**Trask Stalnaker** 57:44 Oh, look at the, you'll see if you look at the comment.
The hidden comment above there.
**Pellared** 57:52 Are you on this?
Oh.
Alright, this was helpful.
**Trask Stalnaker** 58:12 Huh, I mean… Sleep on it.
**Pellared** 58:17 Is this what…
**Trask Stalnaker** 58:18 Robin.
**Pellared** 58:18 for the configuration, Ludom UI, this is not for the spec. So how to really.
**Liudmila Molkova** 58:22 Right.
**Pellared** 58:22 the confirmation.
Okay.
**Liudmila Molkova** 58:26 I already used it in the configuration, and it already works with Java auto-configure thing.
**Pellared** 58:33 consider.
**Trask Stalnaker** 58:33 The Java thing. Yes. It's not… spec compliant. It is, yes, it is our own invention.
This… the goal here would be to have a standard Yeah, which would be awesome, because it is very useful.
Alright.
**Liudmila Molkova** 58:57 Okay.
**Pellared** 58:57 vitami wa…
**Trask Stalnaker** 58:58 We will…
**Pellared** 58:59 According to a blog post.
Yes, review and approve.
**Trask Stalnaker** 59:02 I will… I will…
**Pellared** 59:05 I will…
**Trask Stalnaker** 59:06 get… I will read through the rest of it today.
**Liudmila Molkova** 59:09 Thanks a lot.
**Trask Stalnaker** 59:10 I'll leave last comments. Yep.
**Liudmila Molkova** 59:14 Thank you.
**Pellared** 59:14 Do you have plans, huh.
**Trask Stalnaker** 59:15 See ya, yeah. See ya!
**Pellared** 59:18 Bye.
