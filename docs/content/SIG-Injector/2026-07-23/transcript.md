SIG: SIG Injector
Date: 2026-07-23
Duration: 31 minutes
============================================================

## Zoom Recording Transcript

**Michele Mancioppi** 04:56 Hello. Hi, Jack.
**Jack Berg** 05:00 I was about 30 seconds away from dropping off.
**Michele Mancioppi** 05:04 We're a little long in the packaging one.
**Jack Berg** 05:07 No worries.
**Michele Mancioppi** 05:10 How you doing?
**Jack Berg** 05:11 I'm good. How are you?
**Michele Mancioppi** 05:15 Stuff is happening. I'm always happy when stuff is happening.
The packages… First version of salt.
**Jack Berg** 05:23 There you go. Congratulations.
Is it just published to GitHub, or published…
**Michele Mancioppi** 05:31 The biggest, the reason why we're long ago, we're discussing, again.
how to, to publish in a reputable place, because Gita Pages is not handled.
And that is the pain point since day zero, and I assume it will stay the pain point forevermore.
Author records calls and gives the summaries.
And so… AI assistant.
**Jack Berg** 06:03 And it accepts instructions, like chat instructions, to… Order to, you know, get off the call?
**Michele Mancioppi** 06:12 Or you can kick it out of the cold, and that works.
**Jack Berg** 06:15 That's always been the problem, is none of us have, like, you know, admin permissions to be able to manage call attendees.
**atoulme** 06:22 Did you…
**Michele Mancioppi** 06:22 multitasking.
**atoulme** 06:24 So you did notice we had an auto AI thing sitting in the call, and if you say stop order, they kicked themselves out, which is, We're lucky this one has it. Last night, I was trying to be on the Java SIG for APAC, and it was just me and another boat.
The first time it happened, I took the Titanic Wikipedia page, and I actually fed it into the SIG program on Mac that speaks out loud stuff.
And, I think I had a very funny recap of my meeting.
But this, you know, if I can remove them, I will.
I don't think this is a good idea for people to just drop AI boats on our meetings to get free recaps. This is not how it's gonna work.
**Jack Berg** 07:10 I… It's kind of silly, because they can just go get the recordings and recap it once the recording is posted, so…
**atoulme** 07:20 Yes?
**Jack Berg** 07:21 I don't know, it's just… but people do have sort of a visceral reaction when they see these note-takers, and so… do everything we can to make people feel comfortable, I guess, but it's sort of, missing the forest through the trees, so…
**Michele Mancioppi** 07:39 This video.
**Jack Berg** 07:45 Anyways, any topics, that are related to the injector?
**Michele Mancioppi** 07:49 will be… PR will be opened in the next 24 hours.
**Jack Berg** 07:54 the PR to substitute out all of the instrumentation stuff for the packaging, or what do you mean?
**Michele Mancioppi** 08:00 No, the PR to support Ruby.
**Jack Berg** 08:02 Oh, PR to report… okay, I missed that. Great.
**Michele Mancioppi** 08:07 No, the PR for getting rid of the package, it's already merged. The stuff is done.
Busty and I got it done earlier this week.
**atoulme** 08:15 Maybe,
**Jack Berg** 08:15 I miss that.
**atoulme** 08:17 Best… to go on PTO, so we had a quick Slack thread on some of the aftermath of that. There was a discussion during the PR about the fact that it might reduce the coverage.
Of the code, but that's not the case, we're actually okay. So, we don't need to have additional tests, We're actually doing pretty well, so… Yeah, I'm very happy where this is at. So…
**Michele Mancioppi** 08:43 I mean, I'd forgotten it too, but past Michele, I really liked tests.
Well done to him.
**atoulme** 08:50 Well, maybe you were…
**Michele Mancioppi** 08:51 And packaging, also something that came afterwards, right? So we already had a pretty healthy test infrastructure, then we did also with packages.
**atoulme** 09:00 Yep.
Yeah, I mean, the tests were very, like, heavy on the end-to-end type side, too, right? It's like, let's bring this whole thing into bear.
**Michele Mancioppi** 09:12 Which is the correct way of testing this, the kind of dark magic we do.
**atoulme** 09:16 Yeah, I can't sleep at night if I don't do that in… Anyway, Yeah, we're good. So it's excellent news for Ruby.
That would actually make it really compelling for the operator, SIG, because they never managed to get Ruby support, ever.
**Michele Mancioppi** 09:34 Yeah, but the problem was the missing out instrumentation gem in Ruby, and that is something that… has been, somebody started writing it in the, in the movie SIG, and Matt from, Render Zero, has been helping to get it over the edge.
**atoulme** 09:51 Cool.
**Michele Mancioppi** 09:52 It'll get through me.
**atoulme** 09:54 That's great.
I do have an update for you all about a draft PR that is on the repo, so just so you know, one of the things that may block some adoption with the operator is the fact that the operator compiles for S390X and some other exotic thing, I think it's, eggs? Anyway, which is weird, I mean, they just added it because the collector supported it, not because I think they had any requests from anyone about this.
There is a comment from, Michele here about, hey, We can't just, support that. That's… that's not… we should have some sort of environment to test it. Now, back to this.
**Michele Mancioppi** 10:33 I am not… I cannot reproduce any bugs on hardware and operating systems I have no access to.
**atoulme** 10:40 And that makes it… either we have to say that very loudly, and almost, like, every time you inject, you have to say, we don't know what we just did, which is not what we want. Or, we get at least some level of support through testing by having GitHub Action Runners on S390X.
So…
**Michele Mancioppi** 10:59 That would be perfectly fine.
**atoulme** 11:01 Here's a long, long context on that. For about a year, I've been trying to work with IBM, and some of it's through the mainframe SIG, some of it through the CNCF, to get access to an IBM open source program that would allow us to have S390X GitHub Action Runners.
which I think is a requisite for a number of things, not just this, but I'm working on the collector, I'm working on other efforts where we just lack this type of testing.
This escalated all the way to the legal departments of IBM and the Linux Foundation.
then it stalled as of February of last… of this year.
Without any updates for 6 months.
I finally escalated that all the way to the CTO of the NCF.
who quickly resolved the lack of communication, and now we might have an update next week, and I would hope that in two weeks I can talk to you about an update that is at least meaningful from the LF side.
And so I'm not publishing anything, I'm just saying that we're… we're getting somewhere better.
if we… It's very clear, like, if we have access to GitHub Action Runners, everybody has access to GitHub Action Runners. I don't know what the capacity of that is, if it's just two boxes in a cupboard somewhere, or if it's a real type of access, where there's enough action runners that we could run multiple payloads in concurrence, or whatever.
Yeah, so if you're interested in that topic, we've been talking about it a little bit in the mainframe SIG. That's not actually the main action in here. The mainframe SIG is around semantic conventions for mainframes, which have their own virtualization and own concepts of hosts and regions and whatnot.
But… I will continue to do that, and it's not urgent, but… I understand that this is necessary for this to land.
**Michele Mancioppi** 12:59 I would say that at the moment, we have, I mean, our test coverage is pretty good.
The moment we, we see that it works.
that works, then I'm fine letting it out.
**atoulme** 13:13 Yeah, if you want, we can continue to have the same matrix that is used by the collector, which is the H3 tiers.
Tier 1 is, like, supported performance benchmark, actual real, like, we can jump on it, it blocks releases if anything doesn't work.
Tier 2 is… it's tested, we don't know if it works really well, but… We will not block release this for it.
And Tier 3 is… we compile for it.
**Michele Mancioppi** 13:43 I find that, these metrics is a profound disappointment from the user's side, and I want to have nothing.
to duplicates.
**atoulme** 13:52 Okay.
We can…
**Michele Mancioppi** 13:54 If we put out a release, it's because we believe it's gonna work.
And if it's not working, we're going to fix it.
Anything else is clauseous.
You can quote me on that.
I understand why people do it, I just want no part of it.
**atoulme** 14:11 Okay.
**Michele Mancioppi** 14:13 I don't find it professional.
**atoulme** 14:16 Well, it's open source. Is it professional?
**Michele Mancioppi** 14:20 Yeah. Yeah, I think we need to hold ourselves to our best standards, whether we do work for our employer or for the community, yes. This is a necessary thing for open telemetry to feel like a product, not like a project, which is ultimately what Stable by default wants to achieve.
**atoulme** 14:36 Okay.
Yep.
**Jack Berg** 14:38 Like, so the tension here is, like, you know, something has to give. Either the injector changes its policy to support these additional architectures, or the operator does a rug pull and, like, you know, puts the cap back in the bag.
**atoulme** 14:52 That's another possibility. We could just tell the operator SIG also, and I think that's actually workable, that first off, we won't support Injector on those two things in any short term, because it's just not gonna happen, and You guys either accept that you're going to drop support for those two architectures.
Or you… I don't know, you… just blows up whenever someone tries that, and that's not your… that's not a problem, because we're not on the operating system. I mean, I am, but…
**Jack Berg** 15:23 Do you envision the operator… do you envision the operator having a mode where it runs without the injector?
**atoulme** 15:29 Yes.
Okay, so let's talk about that. Now, the operator itself is just a mode of deployment of OpenTeometry capacities on clusters, and the operator itself defines a number of definitions of controllers that you can deploy. And one of them is the Injector, it's the most popular one by far, right? Injector.
**Jack Berg** 15:51 instrumentation, I think, is what you're referring to, not the…
**atoulme** 15:54 Yes, yes, sorry. It's the overarching definition of configurations for auto-segmentation, which is applied right now through some… custom Go code in the operator through a controller, but would be delegated to the injector in the future, because it's a much more powerful possibility.
But there are other things you can do. So you can have it, for example, defined, collectors. They can be either a demand set, gateway, just a deployment, and then you can have the configuration of your collectors being part of that.
You can also use the target allocator. Are you familiar with that?
**Jack Berg** 16:32 That's actually the one part of the operator I don't think I have.
That one's so much.
**atoulme** 16:37 It's… so, imagine you have 100 permission points on your cluster, right?
This thing is going to find out about all of them.
And then it's going to compute, based on all the collectors it can find, which collector should go and scrape which Promise endpoint.
And.
**Jack Berg** 16:57 It sort of divvies up the workload amongst all of them.
**atoulme** 17:00 Yes.
And using different algorithms, right? You can do some constant hash, you can do per node, you can do all sorts of things.
And then the collectors, when they start up, they know to go discover which endpoints to scrape based on the address of the… the target locator, and then they constantly ask again, hey, what's up? Should I go scrape something else? And then they do that in some uniform way, which is kind of nice, it's a nifty little thing. And it's actually taken from the Prometheus world and brought into OpenTeometry that way.
So, there are a number of other things like that that the operator can do.
And in general, if you think of the operator more like a distribution mechanism, I think it makes more sense.
And one of the… one of the, reasons why I was interested in the Injector was that I think the operator should be very slim, and very just, like, a configuration interface, and then a distribution package to distribute some software that is available upstream from it.
Right? So, for example, the operator should not have its own way of doing the instrumentation.
It should rely on something that does it for it. Well, that's the Injector. The operator should not be packaging its own SDKs. It should just use whatever is upstream from it. And I think the operator kind of, like, deviated from the golden path when it started to take too much on, and it slowed down either the adoption of the project itself requires too much, because people are really, like, deep into the project sometimes. Like, they're able to… understand the V1 to V2 Java semantic changes, for example.
That's… that's really commendable, like, how deep they are getting into things, but at the same time, they… They're not getting that much help from the community because people don't understand the problems the operator has.
**Jack Berg** 18:48 So… so there's… I think it's a good place to start, to try to see if we can put the cat back in the bag, if we can, like, reverse the operator's position on this. But I think there's two things we should try to avoid.
One, is, you know, we take a firm position and say we're not going to support additional architectures, and that, that prevents the operator from incorporating the injector. They say, well, if you're going to be stubborn about this, we're not going to incorporate the injector. I think that would be a net loss.
The other would be that, you know, the operator, says, okay, we want to support the injector, even though the Injector refuses to support these architectures, and so what we have to do is we have to maintain more code complexity, such that supporting the instrumentation CER has, like, two modes, like, with Injector and without Injector, right? Where it would otherwise not need that, so… Like, if we can… if we can avoid those two scenarios, it's like, yeah, go ahead, let's… let's push back.
**atoulme** 19:51 Yeah, we're good.
**Michele Mancioppi** 19:51 You see, the point is, I am not.
Against supporting those architectures.
I think we should, if we're given resources.
The fact that the operator went, goes, and nominally supports something that in reality is completely unproven on.
**Jack Berg** 20:08 Right.
**Michele Mancioppi** 20:09 That is the problem.
**Jack Berg** 20:11 Yeah, so you're saying, like, create a forcing function to be actually support… to be able to support these properly, which… which… exactly, like, I'm nodding along with that, and, you know, what I'm thinking, and I think I heard you say this at a previous meeting, and I agree with the idea of this, which is, like, look, if there's a big corporation that wants to see a particular architecture supported, lend resources. Not just the machines, but, like, also maybe the, like, contributors that can go and do that sort of debugging in the event that there are issues.
**atoulme** 20:43 That's fair.
Yeah.
**Michele Mancioppi** 20:45 Besides, I looked a bit into that.
We would have some deep-seq work to do.
**atoulme** 20:52 Yes.
**Michele Mancioppi** 20:52 support, support that. It's not something that we just, oh, we compile and, yo, it works.
**atoulme** 20:58 Nope.
**Michele Mancioppi** 20:58 There'll be dragons, right? And, I would like to see ABM saying, don't worry, SIG is gonna work.
**atoulme** 21:05 That sounds… that sounds fair. I think this is also something we should be able to push back on IBM soon.
And I… they will be okay with working on SIG on this.
And I think that would be… everybody will be better off on having this.
So, yeah, I mean, here, I think, where we are. The operator SIG right now, there's a couple of POC PRs that have been people are trying out, right? And what we will probably try to do is to create a feature gate We're in some limited fashion, right, not supporting those two OSs, because we don't care for them.
We can have people try out the injector way on the operator.
And we do that for a while, while we figure all the kinks, and we discuss all that stuff, and we continue on this IBM support and all that.
I would say 6 months from now, before Kip Conway U, for example.
would be a great time to just start to come down to where we want to go, and kind of close up all the open doors on the decision-making, and say, okay, well, we didn't get what we wanted from S390X, I think we're gonna have to make some hard choices.
If not, then, you know, we can also just let go for a little while, and… Yeah, I agree, yeah, it's not great if you have to support two code paths.
But, I mean, I am an operator approver.
I've had to support the cut path that is currently there in the operator for instrumentation.
It's not good.
It's… it's not.
It's not well maintained. We've had multiple discussions in the operator SIG about refactoring that in depth.
Duh… it's not, it's not happened. We…
**Michele Mancioppi** 22:45 Jacob was supposed to, right?
**atoulme** 22:48 He changed employers a couple times, and then now he's doing Rust and policy, so I don't know.
I mean, it's a… it's volunteer work, right? People disappear.
So, I like where we're headed, actually. I think, there is no problem at this point, we're just… we're just pointing out things along the way, like, oh, this doesn't work, oh, this thing is not supported. Okay, you know?
**Michele Mancioppi** 23:11 Look, I'm usually not as intransigent as I came across on this call, but there is a reason why.
If… if we say, if we give a pill for the Injector somewhere, we have to be reasonably certain it's going to work.
Because the injector crosses the threshold from technology to voodoo, And the loss of trust.
When that thing blows you up in production, it's immense, and I do not want that.
We reflect on OpenTelemetry.
on code that I contributed. I don't want it.
**atoulme** 23:47 Yeah, I'm with you.
**Jack Berg** 23:51 Oh, it is voodoo, isn't it? It's hard to debug.
**Michele Mancioppi** 23:54 I have… look, Instana was every little bit as voodoo as this.
**atoulme** 23:59 Hmm.
**Michele Mancioppi** 24:00 I know what happens when stuff breaks. I don't want that drama in open telemetry. We are already at the cusp of adopting, we're gonna go through the throth of disillusion soon enough.
And the further away we are from giving an experience that actually works the way you expect, the deeper the truffle disillusion is going to be.
And I'm not going to enjoy all the shitty blog posts and stuff in Hacker News and the rest of the nonsense until people realize that it's technology like everything else, yeah? And I would like not to contribute by digging the hole a couple of meters deeper.
Because IBM doesn't… cannot sort their shit out and giving us a bloody mainframe, yeah?
**atoulme** 24:41 So… You said something interesting. You said you don't want us to go through the fruit of dissolution in as deep as it would be.
**Michele Mancioppi** 24:49 It is unavoidable. It is unavoidable. I would like not to contribute to that further.
**atoulme** 24:56 you're talking here about the Gartner hype cycle, and what's really interesting for me is that you're making this comment because you think we're not through that yet, so you're…
**Michele Mancioppi** 25:05 We're not there yet. I promise you, we are not there yet.
**atoulme** 25:07 And I agree with that, and I… just a side comment on this is, like, I've been really, really wondering when that would happen for years now.
I've been really surprised about how much OpenSumtree's been able to get away, and to continue on that steep, steep, steep, steep…
**Michele Mancioppi** 25:23 Because as much as people like to go and complain on Reddit that Datadog has taken their son into slavery.
they still stick to some extent with that. The adoption curve is still going up on OpenTelemetry.
**atoulme** 25:38 It is.
**Michele Mancioppi** 25:39 You still see the gran… you hear the grumbling of, oh my god, it's difficult to set up. Yeah, we're working on that. Oh my god, not the instrumentations and data that is remotely like. Most people don't notice, because the standards which telemetry sells to is not great. I mean, the results are… you know, and Scrakand in German, how do I say it? They are… they are… I mean, you pay… you get what you pay for, right? If the instrumentations are inconsistent, the data's inconsistent, you're going to have a hard time analyzing it. But good enough. The moment you start exploding people's machines, that's where they get mad.
Every APM solution has broken somebody really hard.
I would like that not to be because of the Injector.
**atoulme** 26:28 So, you know, this is actually a panel discussion we need to have at some point.
Or even just a community topic.
about this Gartner hype cycle discussion.
I would love to have that discussion with you and others.
To discuss how we're going to organize ourselves.
To be conscious about it.
And how we're going to make sure we… this is a bit much bigger than the injector, but I… I'm very interested in making sure we have some sort of a, like, mental health resources on the side, so you can go back and say, it's fine, you know, someone touched the stove 3 times and they don't like it, and they should have known better, and, you know, here's how we're going to react to this, and what's the… What's the rapid response team for this?
**Michele Mancioppi** 27:10 There is only one solution for that. Giggo, what is your mission?
**Diego Hurtado** 27:16 To make a hotel… sorry, I feel like crap today, Tomatoes feel like a product, like a pro… yeah, like a product, like a project, yeah. Like a product.
**atoulme** 27:27 Is this a corporation size now?
**Michele Mancioppi** 27:30 No.
That is the entire reason why I'm staffing as an engineer and say, you go and make it feel like a product. That's to work. Otherwise, we are going to have a really tough time.
And I'm really proud of OpenTelemetry, I'm really proud of the Injector, and I would like it not to go down in the unknowns as something that marred the entire experience.
That's why I'm so angry about the fact that, you know, to put something out that we cannot test and we cannot debug, because that will backfire, it's a fact of life.
**atoulme** 28:03 No, I think… I think that's fair. Okay.
**Jack Berg** 28:09 So… So, how do we… how do we practically communicate this to the operator?
Is there an issue we can collaborate on about, you know.
Like, you know, starting the dialogue about, like, you know, drawing a line in the sand and saying, we would… we'd really awfully like to not support these architectures.
And, you know, we'd like to know what you think about this, because we'd also really like you to, you know, incorporate the injector as soon as possible.
**atoulme** 28:38 Well… I'm an operator approver. I back-channel some of our discussions here with them. The discussions have been happening on the private channel of the operator leads, because I don't know what they're doing. And I haven't been to the operator SIG in a little while, because it's every two weeks, and… I get… I get mired in other things. I would say… It's summer.
you have easily a month before people out of… because some of the operators, people are taking some time off, or it's just summer in Europe.
I'm not too worried, actually, about the timeline.
And actually, I like what Micheleash has done here, is that he took upon himself to go and build this.
we didn't ask him for that. There has been no coordination. It's just like, okay, I feel like it's really time for me to kind of get into this, and I want to understand what it would take, so he did that exercise so he could come into a discussion with the right disc… So, a couple things we can do, Jack. One is we could ask the operator SIG if they would like to come to our meeting and discuss this, maybe next week?
Would that make sense?
**Jack Berg** 29:42 We can try, like, let's start on Slack and just say, like, hey, we need to have a dialogue between these two groups about architecture support. Where do you suggest that happens? Like, we can do it in Slack, we can do it in GitHub issues, we can do it synchronously. Based on people's schedules, you know, one might be better than the other.
**atoulme** 29:58 Okay, that sounds great.
But…
**Michele Mancioppi** 30:04 It was a deeper discussion than usual.
With the circles.
**Jack Berg** 30:10 Good discussion, yeah.
**atoulme** 30:12 Ugh, I mean…
**Jack Berg** 30:17 Should just be a technology discussion, not an emotional discussion. I'm about to have another discussion in my next SIG about how I need to, like, say no to something somebody's asking for, because we don't have the resources to support it. So, if they want to volunteer resources, they might be able to make that happen. So, that's how it goes.
**atoulme** 30:34 It's not fun at all. But yeah, well, good luck, Jack.
Yeah, I found this discussion today was more interesting for me, because it also helps me relate to what Michele is going about, and we need more of this type of alignment between ourselves. So, I'm happy to hear what he's saying about the slow dissolution, because to me, this has been… It's my living nightmare. It's like, this is coming. And I keep telling people, like, the sky's falling tomorrow.
tomorrow, some guy's taking to Hacker News about how his Rust app never worked, after doing this.
And… like… We're just so lucky. Have a good one.
**Michele Mancioppi** 31:13 Miles.
