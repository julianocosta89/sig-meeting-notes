SIG: Technical Committee
Date: 2025-08-06
Duration: 32 minutes
============================================================

## Zoom Recording Transcript

**Tigran Najaryan** 00:29 Hey? Josh! Good morning.
**Josh Suereth** 00:35 Morning.
So I'm a little slow here, computer a little bit
me.
**Reiley Yang** 01:53 Okay bye, bye.
**Josh Suereth** 02:06 Sorry. I'm just responding to some profiler stuff. I wanted to get my thought down before we got started, so let me start rendering our Doc.
Sorry, guys.
Oh, okay, how's everybody doing? Seems like a late week.
**Tigran Najaryan** 02:32 Business as usual.
**Josh Suereth** 02:36 Yeah.
Oh, if we're if we're just chilling, I I set up a new aquarium.
I'm a i had a big aquarium out in my living room, and I had clownfish in here.
and I'm swapping.
So I'm going to upgrade my saltwater aquarium.
and I'm pretty excited. So eventually I'm going to move all the freshwater things I had into here, and then have a have a big saltwater tank.
But I I should have done this a year ago.
because everything in the Aquarium land is about twice as expensive now in the Us. As it was like a year ago.
So I'm finding, anyway.
**Reiley Yang** 03:27 To the connector.
**Tigran Najaryan** 03:27 Because of the tariffs, or what is it all comes from China.
**Josh Suereth** 03:31 It's it's the tariffs. Yeah. So most of the hardware comes from China, and most of the fish are
like, I usually buy aquarium bred fish, and I try to buy from people who are local near me to try to encourage, like the hobby, not, you know, impacting the environment. But one of the things I realized was, even if it's not made.
even if a tariff doesn't impact it right? The cost because of the tariff on the cheaper stuff means all the premium stuff had to raise their price. So even if it's made locally, it's still a higher price bar.
Otherwise people wouldn't believe it's premium right?
**Tigran Najaryan** 04:15 Yeah.
**Josh Suereth** 04:16 Yeah, well, I guess.
**Tigran Najaryan** 04:16 That. That's what happens right? The cheap stuff gets
more expensive. The the expensive stuff kind of it compresses from the below. Right? That's that's that's market.
**Josh Suereth** 04:26 Yep, yep.
so, but it leaves me feeling like an idiot like I. I had planned to do this 2 years ago.
and I didn't take action until about December, because it takes anything with aquariums. Just takes a long time. You have to plan well ahead. Nothing good happens quickly, is the turn of phrase. So it's kind of like open telemetry a little bit, anyway.
But it it, I just man. I wish I'd started earlier, because I, anyway.
that's that's my random. Let's chat while everyone joins. I think we have 5, so we could probably get started. Now.
Lyudmila can't join. I think Jack is still out
that leaves Bogdan as the only one left that I think we're missing. Is that right?
Okay.
oh, let me make this a little bit bigger. So 1st off, let's let's get started with 5 of us. There is a new Sig
that was founded. This is a donation.
and they're calling it the injector Sig. If you remember this thing, this was.
It's the thing that inspects environments and figure out what figures out what environment variables to pass to inject configuration into sdks and Apis.
**Tigran Najaryan** 05:50 Is this a splunk donation.
**Josh Suereth** 05:53 I believe this is a splunk donation. Yeah.
**Tigran Najaryan** 05:54 Okay. Okay.
**Josh Suereth** 05:56 So
they created a sig for that, because we accepted the donation. But we added the process of requirement, level or sponsorship requirement after the Sig was created. So the decision we have to make today is what level of sponsorship do we think the injector Sig needs?
I think we can figure out who who? Who would be the sponsor later, but at a minimum. It has to be a you know, escalating sponsor.
**Tigran Najaryan** 06:31 Okay. So this is, I guess this is fairly independent of the technology, right?
It doesn't they? They need to know a bit about how to inject this stuff so that it works with the language as the case.
But I don't think is a whole lot of coordination involved here.
Correct me if I'm wrong, so
I don't necessarily see the need for, like
higher level of sponsorship in this case.
**Josh Suereth** 07:05 I actually, I I'm concerned that it's the opposite. I think that they will have a lot. Let's see, was it an issue or pull request.
Hold on donation.
Objective?
yeah. I I think that they might have a lot of back and forth with the configuration. Sig.
**Tigran Najaryan** 07:34 With the configuration sick, so that what for? For the configuration of how the injection is done? What for.
**Josh Suereth** 07:46 Yes.
like like, think of it this way. They want a consistent standard for what environment variables they inject and like controlling SDK remotely, and they want it to look the same, regardless of language, if possible. So I actually see that, you know initially, maybe phase one doesn't have a lot. But I see, like a phase 2 or phase 3, involving a lot of coordination.
We offer integration via system, the environment variable. Yeah.
So especially with the configuration sake, trying to change how environment variable stuff works for for injecting config. I think that they're the 2 of them will be will need to coordinate right? Because if if the if they're building something that works on the old end stuff and we're trying to move to new files like, what what's gonna happen.
**Tigran Najaryan** 08:39 Okay.
I guess. Yeah, that's probably fair.
**Armin (Dynatrace)** 08:51 Then the Tc be the the glue between the 2 6,
because it's not done via the spec. It's happening outside the spec, right? It's happening in the config
repo and and their their group.
**Josh Suereth** 09:06 Yep.
I think if we look at this.
I don't remember where the due diligence was done.
It was Jack. Yeah.
let's take a quick look at the due diligence, because I think we had a set of recommendations right
intersection with the operator.
Acceptance requirements. Let's just look at that. Because so this, this might give us an idea.
must strip out finishes of code, maintain its future requirements, must add support for open telemetry, 0 code instrumentation solutions must add support for declarative configuration. Right? This is the part where I think you know, config and them will be working together must add support for all standard environment variables and should evaluate evolving towards Ld preload should evaluate demand ability to support other operating systems. Yeah, this this stuff is independent. I think this is this is more. What I was concerned about
is this, is this visible? To try to make it bigger.
**Tigran Najaryan** 10:17 It's funny.
It's fine.
**Josh Suereth** 10:19 Okay.
I, anyway, to to be, I guess. To be be frank, I my opinion here is we should.
I'm okay with an escalating sponsorship as long as maintainers or or leaders of configuration. Sig and injector Sig are working together
**Tigran Najaryan** 10:50 Yeah.
**Josh Suereth** 10:51 Otherwise I think this might need some guiding sponsorship to kind of navigate the complexities that we're talking about here.
**Carlos Alberto Cortez** 11:03 But
correct me if I am wrong. But I think that such guidance would be needed for the future requirements, not for the current stuff, right? Which is like
making the project part of hotel. If if you want to face the future requirements as part of the
kind of immediate objectives. Then then, of course, we need some PC member there.
**Josh Suereth** 11:27 That's actually a good point. Maybe we should go back and ask for a charter of what phase one is going to include to make our decision, because if they're planning to immediately tackle this in phase one that would change my opinion here. Yeah, I like that, Carlos.
I'll take a note.
All right, follow up desk for phase, one initial contacts.
It involves configuration, support, configuration file support.
Okay, sponsorship save membership.
Okay? Does this? Oh, you can't see what I'm typing.
Alright.
Does this seem reasonable?
**Tigran Najaryan** 12:32 Yeah. Sounds good to me.
**Josh Suereth** 12:34 Cool, awesome thanks. Let's move on. That was
only about 5 min. But we started 5 min late. Okay, next up. This is just a heads up the Php donation process. I think I only need about 5 min for this. Tldr elastic wants to donate a Php auto instrumentation capability. So the way this works. It's a set of C plus plus libraries that hook in and inject the Php
inject the SDK implementation into Php, so if you're using the Api, you get tracing, you get metrics, you get logs. Whatever from Php instrumentation. The Php maintainers are supportive. There is one technical concern that they've raised that we need to walk through. That technical concern actually comes from datadog who has an alternative implementation.
Datadog is also supportive of working together, going forward.
So I actually think that this is going to be pretty good. I'm going to detail out what that limitation is. It relates to how a user can define a dependency on the SDK, and how the injection actually happens. That's part one part 2 of this concern is basically our Php maintainers aren't necessarily C plus plus developers.
So we will want. With elastic comes some C plus plus support. And I think if we talk to datadog and their agent, and we work on this together hopefully, we can address that concern. But that's more of a thing we'll mention to the Gc. Because from a technical standpoint that appears to be the right way to hook Php. To get a lot of flexibility. What we want.
all the questions that I was asking you know of like, Hey,
you know, will this work with existing php instrumentation? The answer is, yes, so I'm actually pretty excited. I was going to hold, and we can decide. If we want this to be public or private, A,
in the next Tc. Meeting I'd like to invite the Php. Maintainers to join us.
and then we can just ask them questions about how they feel about this donation. I'll write up a document
initially with them on, like the due diligence things that we think we want to see and concerns and get them to help flush it out. But we can ask questions about what we want to see there
wanted to run it by anyone. See if there's anything any concerns we have
earlier that I could add into this document, or make sure that we talk about next week.
**Tigran Najaryan** 15:08 There seems to be slight overlap with the with the previous injector, right the way they describe it.
How the this they say that there's a there's a native operating system package. You install it and enables the
the instrumentation without requiring changes to the applications.
I don't know what exactly is the mechanism they use, but it kind of sounds like
at least the the initial, the hook part have you in? They sort of do some sort of injection. I'm guessing.
which is clarify that there seems to be an overlap here.
Not a bad thing. But
if it is, then then maybe we'll need to figure out who owns, which parts.
**Josh Suereth** 15:55 The the. So from what I understand from the maintainers, the existing the existing injection
is not as flexible as the new proposed injection. And so it's actually, from their point of view, it's almost a straight up win. There's like one thing we'll want to ask to fix with this injection.
But yeah, you're right. It's duplicative with what's there today. It's just the maintainers actually think this is the right way forward, because it's better for Php users to to move towards the style injection that elastic is using.
**Tigran Najaryan** 16:25 Sorry, Josh. I wasn't probably clear. I mean the the new Sig that we we are. We created for the injector.
The overlap, I think is with what they are doing there.
**Josh Suereth** 16:37 Oh, you think, does this? Okay?
**Tigran Najaryan** 16:38 The very new one.
Yeah, the the.
**Josh Suereth** 16:42 Thank you.
**Tigran Najaryan** 16:43 Dominated, transplant.
**Josh Suereth** 16:45 Yeah, okay, that's a good thing to call out. I'll I'll investigate that, and I'll I'll ask. I think Antoine's leading the splunk.
**Tigran Najaryan** 16:52 Yeah, yeah.
**Josh Suereth** 16:53 Yeah, I'll talk to Antoine and and find out if he thinks there's overlap here.
**Tigran Najaryan** 16:58 So with the Php auto instrumentation, I'm guessing there is. There's 2 parts to that. One is
the injection itself.
How you essentially inject the the open telemetry instrumentation into your Php.
Application?
There is.
I guess this is the question. Is there a second part as well, which actually does extra instrumentation for some of the Php. Frameworks and stuff which supposedly needs to be, which is in in php, I'm guessing, or it just uses the existing instrumentation that php, open clients Php already has.
It's more of a question I don't know.
**Josh Suereth** 17:38 It's leveraging a diagnostic hook in Php. If I understand it. If you're familiar, like a lot of languages are kind of adding these, I think Python has one now like a debugging Api. Php has one as well, so I think it's leveraging that Api to inject. So from what I understand. And again, I'm at still the 10,000 foot level, because I'm not deep in Php. And I'm relying on the Maintainers to do the due diligence for the most part, and I'm just
validating from what I understand from the 10,000 foot level it is. It's using that diagnostic Api, and it's doing some of this instrumentation, but mostly through basically saying, Hey, import this. This Php module.
**Tigran Najaryan** 18:20 Okay, but that's the mechanism. How to inject something right?
What is being injected is the second question.
and that what part depends on
the particular framework Php framework you're using or the libraries you're using. My question was about that. Are they also contributing some new instrumentation for some frameworks that we don't support today
in in open 7 php. Instrumentation, or
or this just uses the existing open learning. Php, instrumentation.
**Josh Suereth** 18:54 I think there might be some new stuff, but I'll have to take a look from what I understand. It's mostly
let's take a look at this. Hold on! I'll pull up the issue for you.
I'll put it here.
**Tigran Najaryan** 19:11 Or I cannot waste everyone's time. And we can follow up with that offline. Yeah, yeah, okay.
**Josh Suereth** 19:26 Oh, it! It also changes. How telemetry sent to be non-blocking. That's another thing. It does.
So it actually like the communication path out of the SDK has changed.
**Tigran Najaryan** 19:38 That, I guess. Okay, that that part is a bit weird as a bit.
That's that's supposedly the the responsibility of the of the SDK of the exporters, except to use open
Php. The existing implementation of that.
**Josh Suereth** 19:56 No, no, no, no, no! It only needs to use the Api, we in Java. This is the same in Java. The auto instrumentation overtakes the SDK,
it is not the actual SDK that's running. It is an auto instrumentation. SDK, the only thing we've required for auto instrumentation is that the Api is upheld.
We do not require the SDK to be upheld.
so like the this is, this is this is the same thing is true, for most of the other auto instrumentation that I'm aware of. But basically you can take over the SDK and make it more efficient
if you, if you're able to, or you can somehow highly tune it for your auto instrumentation. Use case as long as the Api continues to work. If someone has a dependency on the Api.
**Tigran Najaryan** 20:40 Okay? So the the other question I have is, does this elastic solution use existing copentry, Php instrumentation? And I mean this, this repository. I posted the link, there is a Php instrumentation
repository. Is it completely independent? From what open clarify already has or
uses the Php instrumentation as one of the building blocks essentially of the solution they have.
**Josh Suereth** 21:09 I'm not.
**Tigran Najaryan** 21:10 Completely independent. I think that's not great. They are essentially creating a parallel development truck here.
**Josh Suereth** 21:17 Maybe.
**Tigran Najaryan** 21:18 That.
**Josh Suereth** 21:19 That's that's, and if if we were to import it, we would not even I don't think we'd even allow that right of like, hey, yeah, you can be completely independent. Now, I'm pretty sure that this is in addition to things that are available in open telemetry.
**Tigran Najaryan** 21:37 Okay, can we have some bit more clarity on this.
**Josh Suereth** 21:41 Yeah, yeah, that's it's a good call. Let me let me add that to the notes. Follow up with Antoine.
**Tigran Najaryan** 21:48 Did A. Did a due diligence happen on this this thing? Who did the due diligence.
**Josh Suereth** 21:54 With the due diligence is is happening right now. Basically, there's a private thread with Bob and Brett and I. And I think, Severn.
As the Gc. Delegate, and we're kind of discussing it on there like concerns, things to look at.
**Tigran Najaryan** 22:11 Who is who is the who is leading the due diligence from the Tc. Side.
**Josh Suereth** 22:15 Me! Me!
**Tigran Najaryan** 22:17 Okay. Okay.
**Josh Suereth** 22:18 That's why I'm bringing you an update. Yeah.
**Tigran Najaryan** 22:20 Okay, all right. Good. Thanks.
**Josh Suereth** 22:23 Confirm this. Uses. Existing presentation will be, contributed and non duplicative.
Yep, okay.
Cool any other concerns there.
**Carlos Alberto Cortez** 22:48 They say that they want to provide support for OP. Amp.
That's interesting as a future thing. I could be curious about that.
**Josh Suereth** 23:00 The.
**Tigran Najaryan** 23:00 That's something I will support.
Yeah, all of the languages.
**Carlos Alberto Cortez** 23:06 Not sure but that's kind of my my concern that I am afraid I mean, we don't have to discuss here, like many languages around handling, you know, with different values and stuff like that. But anyway.
**Tigran Najaryan** 23:16 So. Yes, and and I try to keep an eye on the the different OP. Initiatives that are going on.
There's 1 in Java as well right now.
So I
I kind of. I'm happy to take. Also take a look at the open implementation with this Php donation as well.
**Josh Suereth** 23:38 Yeah, should we? Should we discuss off? I'm actually kind of curious. What's what's the status of it? And how? How do we see it with hotel and the spec like, is it? We're at a place where we're starting to implement it across hotel. Is that a thing we're trying to do consistently. I know that this is a feature people want.
**Tigran Najaryan** 23:56 I mean, I think it's ready to be adopted.
It is in a in a state where the the fundamental capabilities are quite stable. We have been adding new features to opump
continuously in the last year or couple years, but
the fundamental. The basics have been there
for quite some time now and haven't been changing so essentially, the ability to connect to send service updates to get configuration remotely, that has been there for
for years now, and hasn't seen any
any changes or any significant changes. So
I think it's it's no longer a moving target. I think it's ready for adoption. If you look at it like that, right? And we have a
reasonable, reasonably complete implementation reference implementation in goal collector implementation is ongoing.
And I I don't. I don't think that
anything major is going to change at this stage in the basics, in the fundamentals. So I think it's it's it's yeah. It's a good time for us to consider adopting it
with a subset of capabilities in the sdks, like the the sampling we discussed right yesterday
to receive the the sampling or some other, anyway. So a subset of
settings that you would normally configure on an SDK on any SDK any language. SDK, I think it's a nice capability to be able to do it remotely, and L. Pump is essentially built for that. It is what it is designed for.
So I think we should encourage now
the the adoption of it by by different language sdks, or or or to instrumentation solutions, or
any of this right? Any. I think it's a it's a it's a good extra capability in this donation from my perspective.
**Josh Suereth** 25:59 Right. This. What what I'm curious about is, do we need a dedicated effort to make it consistent across hotel, like consistently used, consistently adopted consistent SDK features that give you that capability. This is a project that needs to get run.
**Tigran Najaryan** 26:13 Yeah.
So like, I said informally, I have been trying to do that by just maybe following what is happening.
particularly both on the collector, and on the on the Java more new. I guess new effort is a Java version of the opa, and I'm the maintainer of the Go version myself.
I can continue doing that. I I don't know if we need more, I guess.
I don't know more than that to to be consistent there may. Maybe we can discuss that.
**Josh Suereth** 26:51 Okay.
Cool. So
just to to wrap up the Php due diligence, I'll follow up on the OP. Am. Support question. We'll confirm that it it definitely uses hotel instrumentation. And if everyone's okay, schedule
right? And Brett and Bob, I knew it was 2. B's my bad
Brett and Bob for Tc. Meeting for open questions.
Alright, so I'll schedule Brett and Bob to see if they can come to the Tc. Meeting next week or the week after, so we can do a bunch of questions on the due diligence. I'll try to get these answered ahead of time.
Does that sound good?
**Tigran Najaryan** 27:41 Yep. Sounds good.
**Josh Suereth** 27:43 Cool.
Alright
tiger, and I would encourage you to to. So that's the end of this one for OP amp. I would encourage, maybe thinking about formalizing a project to kind of run OP. Amp. Through open telemetry
right? And and be like, what does it mean for open telemetry to support off Amp all the way down. Yeah.
**Tigran Najaryan** 28:05 Yeah.
Okay. Sounds good to me. Let me think about it.
**Josh Suereth** 28:10 Okay, cool. So go ahead.
**Tigran Najaryan** 28:14 I just
okay. Anyway, I'll think about it. I don't know if it needs to be. It probably doesn't need to be a separate seat. Maybe we just expand a bit.
The responsibilities of the current opamp seek.
And because it's sort of narrowly focused on
on the collector implementation right now and on the the protocol itself. So we need to expand a bit what it is responsible for and bring the. I guess the idea that we're now rolling out our pump to
other, to to all of the some of the languages.
and sort of invite, I guess the representatives of the of this language, as the case, who who are adopting opamp to be part of the discussion that is happening in that sip.
**Josh Suereth** 29:00 Yeah, yeah, I think this goes to the new project proposal. Thing that we've been discussing with the Gc. Of smaller project proposals with like narrow deliverables coming forward. So I think that, like the way I would phase it is, that's like phase 2 of OP, you know, phase one was protocol.
It could be phase 3, like phase 2,
phase 3 might be, yeah. So yeah.
**Tigran Najaryan** 29:24 Okay, yeah, yeah.
**Josh Suereth** 29:26 Cool.
What I want to do is make sure we are using our attention wisely.
So that's why with OP amp. I would really like to see it make it through. But I would also like to make sure we're not overloading our ecosystem or maintainers with this. So if this comes out of the left field with like urgency. Let's make sure we're prepping people for it and accounting for it in terms.
**Tigran Najaryan** 29:51 Yeah, yeah, just to be clear, I completely agree with you. I don't want to overdo that, either. I don't want to start a new project.
you know, conflammatory with the goal, adopting OP-amp everywhere
I like. How it happens right now more naturally, where individual Sigs or language implementers, they decide that they like O. Pump! Enough
that they would like to adopt it, and then I engage with them to make sure that that adoption is done
in a consistent manner.
I think I like this approach more like that. That natural flow of things here.
I don't necessarily want that. We go and talk to 10 different language, Sigs, and tell them now is the time to sort of do all pump adoption and make this a top-down effort. I don't want that
the way that it is happening right now, sort of bottoms up and individually, one by one, with with every every language, SDK doing that whenever they are ready whenever they see the value in doing so.
I like this approach because it also spreads a bit my effort over time, so that I can actually contribute meaningfully. If I start doing it for 10 different seats, it needs to be an actual project with the significant
time commitment from my end, which I don't necessarily have right now.
**Josh Suereth** 31:22 Gotcha.
I think I think that's that. That's fair. So that's actually the answer I wanted is, basically we should consider it organic for now.
and we should not consider it part of the project, and if a if an SDK asks like, Can I defer this? The answer is yes, for now.
**Tigran Najaryan** 31:49 Yeah, yeah.
**Josh Suereth** 31:49 Right.
**Tigran Najaryan** 31:50 And just to be clear, I'm not saying we should be hands off of it
right? We should absolutely be in that process. And and I'm trying to do it myself at the moment we can formalize it a bit more to say that. Yes, this is a project that this is following.
and we will be doing it, for for example, for Collector for Java, and possibly for Php. Next. And that's where we are right now.
**Josh Suereth** 32:13 Cool.
Okay.
all right. Shall we move on? We have 30 min left. Should we move on to the private topic.
**Carlos Alberto Cortez** 32:28 Think, so, yeah.
**Josh Suereth** 32:29 Okay. Alright. I will see you all in the private channel.
