SIG: Governance Committee
Date: 2026-04-15
Duration: 51 minutes
Zoom Recording URL: https://zoom.us/rec/share/9R8Rr9w70WtKcrrmjpbs9mmjvr_EQD4z6KPCpFnmaeXFzFIo_oJUl-NC4k7gwxNu.3Bn4DHNPGQtjAUwf
============================================================

## Zoom Recording Transcript

**Austin Parker** 01:39 Hello.
**Marylia Gutierrez** 01:40 Hello.
**Trask Stalnaker** 02:30 Hey, Austin. Hey, Maria.
**Marylia Gutierrez** 02:33 Hello!
Hello, cat.
**Trask Stalnaker** 02:43 Yep.
**Austin Parker** 02:48 I, You have food. I fed you.
You got two foods.
We got wet food and dry food.
**Marylia Gutierrez** 03:05 Now, he wants a medium food.
**Austin Parker** 03:08 M… People were mad that our wet food was cold this morning.
**Ted Young** 03:24 Used to have a very, very cranky, big cat that we called Hiss.
big farm cat, and he would not eat his cat food. He would only eat the dog's food.
But one day we discovered we'd actually been feeding the dog The same cat food.
Because the dog did not care.
It was really just, he would only eat out of the dog's bowl.
**Juraci Paixão Kröhling** 04:01 Nope.
**Austin Parker** 04:14 Yeah, this one, I think, eats enough. Oh, God.
**Marylia Gutierrez** 04:20 Yep, look at the belly.
**Austin Parker** 04:24 I think you get enough food.
I don't think you need more food.
And she's dense. She's like… Not… It's all muscle.
Muscle and flab.
**Ted Young** 04:45 Outdoor? Master.
**Trask Stalnaker** 04:47 Indoor, outdoor?
Okay.
**Austin Parker** 04:52 We don't let them outside.
It would murder the birds.
**Ted Young** 04:59 Yes.
**Juraci Paixão Kröhling** 05:08 So, I think we have Quorum.
**Ted Young** 05:10 No.
**Alolita Sharma** 05:20 Hi everyone, good morning.
**Austin Parker** 05:23 Blue?
**Trask Stalnaker** 05:24 AE…
**Marylia Gutierrez** 05:25 Oh.
**Juraci Paixão Kröhling** 05:48 So, while items are added to the agenda, just wanted to remind everyone about the liaison check-ins.
I heard from maintainers that not all GC liaisons are doing check-ins, so please do the check-ins. This is the one thing that we actually have to do every single month, so please go there and talk to… to your, Sikhs.
Please.
**Trask Stalnaker** 06:24 I'm bad at the ones that I'm, like… involved… heavily involved in, like, kind of separating that role sometimes.
Cause, like, I kind of just… I know what's going on, and, like, I, like.
So it feels weird to check in in that.
capacity.
**Marylia Gutierrez** 06:46 Yeah, for example, like, for the JavaScript, I am very involved, and I am the liaison, so I still, like, do the check-in, because that creates, like, the opportunity for someone to bring something. So I have, like, the questions that I do every time, so it's always, like, now it's check-in time, so you know what that thread is about.
But the important is just, like, oh, anything they want to bring it up? And a lot of things that I bring is anything… any person that we should be promoting, like, now, for, like.
as soon as I joined, like, several, like, of the 6, I was able to promote somebody. So I think I have, like, about 6 or 7 people by now that were promoted just because I brought out the topic and saying, like, who is working on what, and things like that. So just by bringing sometimes the topic is very helpful.
**Juraci Paixão Kröhling** 07:30 Yep.
In my case, I do have a special channel for the check-ins, like a private channel, only with the Sikh leaders, and the whole purpose of the channel is to ask those questions, like.
**Alolita Sharma** 07:41 Yeah.
**Juraci Paixão Kröhling** 07:41 The main maintainer track.
Because that creates also a safe place, or a safe room for people to bring things that they don't want other people to see.
**Alolita Sharma** 07:50 I've noticed that works well, actually. I agree with you, Judas.
It's, definitely works well.
**Pablo Baeyens** 08:10 Should we… Is there anything to talk about stability graduation? We have the 10-minute… Slow.
**Ted Young** 08:22 I can certainly talk about that. I mean, I've been trying to thread the needle. I put my item down below, but it's part of this.
between trying to get the packaging SIG put together and, you know, stability has kind of forced us to figure out an approach to stability.
The thing we're looking at now is, like, actually trying to just have a big bundler distro that's stable versus unstable, and some kind of flag, that gets you one versus the other doesn't look like… A very viable approach to apply.
across different languages and different approaches to installation. One thing that is universal going forwards is declarative config. That's a thing we'll have everywhere.
So, looking at… Being able to maybe, for one, have a more universal way in declarative config for enabling and disabling packages.
And then maybe looking at, you know, some kind of policy or something, that would allow people to enable and disable in blocks, like, unstable.
Maybe using that as the approach, and then being able to go to SIGS, and, you know, the degree to which they can all do the same thing, it's fine, but if something is in one particular language, just works differently enough, it needs to be a little bit different.
You know, there's room for that as well.
But that's what we're thinking about proposing as, like, our next stab at this.
**Trask Stalnaker** 09:58 I like the idea of, kind of, the declarative configuration first.
approach.
We did, it's probably not… that directly… useful, but, check out the cement… we did the… we did move the semantic convention stability opt-in stuff into, the declarative configuration, schema.
So you can opt in to different versions of the, major… different major versions of different… different domains, like, you can say, I want, V2 of RPC, and V1 of database, and so on.
**Ted Young** 10:45 Hmm.
**Trask Stalnaker** 10:46 And also, there's an experimental… I want the experimental stuff.
**Ted Young** 10:51 See you.
And SIGs are able to implement that with their contribrib ecosystems?
**Trask Stalnaker** 11:01 Yeah, yeah, we've implemented it in Java, at least.
**Ted Young** 11:05 Great. Great. Okay.
I'll touch base with you guys about what you're currently doing.
Because that solves two problems for us. One, it gets the stability stuff firmly out of the system packaging SIG's hair, because we can say we're just going to go forward with trying to package up what people have today, and if we can package it up and deliver it that way, great. If we can't, you know.
the end of phase one is, like, delivering that feedback to those SIGs and figuring out what they need to do, but then we can have, like, the effort for… stability configuration to be something that's just separate from how the bits are being packaged up, so we don't have to put that burden on that SIG.
And that's where a lot of the concern was coming from, in terms of that SIG needing a lot of involvement from all the maintainers. It's more about, like, how do we manage the Contrib ecosystem?
So, we still have to solve those problems, but at least it's not… All wrapped up in system packaging anymore.
I think the other concern, you know, which we kicked off at the, at the SpecSIG this week is just that we were under-resourced for managing Contrib in most languages, right? Like, so doing anything with contribib… Seems like something that… doesn't have resources.
We can look at trying to make managing Instrumentation packages less work through… You know, better tooling and things like that, but that… that seems like… like, something we have to figure out our way forward, and so we're gonna be dedicating time at every SPECSIG meeting going forwards to to try to work through that with the different SIGs, just to figure out what our plan is. For stability, for, you know, marking things stable, also for updating things to the latest semantic conventions and maintaining things in general.
It's just something that is critical to us now, but, you know, no new resources have materialized, so… How do we do it?
that's what I've got on that front, so I'm gonna keep pushing on that through the… spec meeting and talking to maintainers in different languages to understand the state of contribib. I'll try to put together some kind of report soon. Next week is Grafonicon, so that's gonna be a little bit of a mess for me. I'll be able to attend the spec sig, but when I get back from that.
I can start trying to… To help get us more organized.
**Trask Stalnaker** 14:22 Just to carry over one comment from the spec meeting that was… Interesting… Because it kind of contradicted one of the things we were imagining, this idea that if we create… if we Say that, hey, if you're stable, we'll bundle you into the… System package, you know, and distribute to you super widely.
We were, you know, thinking of that as a carrot to get maintainers to make marketing stable.
And… I think that it was brought up that there's a counter-argument there that, some maintainers will feel that that's actually a disincentive, to mark things stable, that then it's gonna go out to, like, so many people, and it's all… the… The reason why some people aren't marking things stable already, again, back to the contribib issue, is that it's not, like, a… that don't feel like there's dedicated maintainership of that going forward. It's not something they want to sign up. Nobody's really signing up to maintain that going forward, so it's actually… Kind of a double-edged sword there.
**Ted Young** 15:48 Yeah, and the new plan is a reflection of that feedback, right? We're hoping this would be, like, a great… piece of cheese, and it seems like it's really not. So, let's just try to…
**Trask Stalnaker** 16:01 Work on the contribib thing first.
**Ted Young** 16:03 decouple these efforts from each other. If we're gonna use declarative config to manage, you know, what you can install, then it's okay to ship these system packages and have them have unstable stuff in them, because it's just a flag that… that people can add.
And even the idea that, like, you only want this table stuff as the default, I mean, we are saying that, but the… It may not actually be the case of what users want, or at least not want for a while.
Depending on how quickly we can move to stabilize things.
It was also pointed out that if we mark things stable, then we won't be able to upstream them natively later, because the, you know, MySQL will say, well, you already made it stable, so why should we bother? I don't think I buy that argument.
But… It's good to be having the conversation with maintainers, at least, and getting their feedback.
Are there stability-related things, or… Graduation.
**Pablo Baeyens** 17:23 it's on the OTAB.
The stable by default auto?
I guess Houston, or… I don't know.
You want to go ahead.
**Austin Parker** 17:40 I… yeah, there's… I believe there's some comments on it that I need to go through.
I haven't yet…
**Alolita Sharma** 17:56 Yeah, I think last time, Austin, that's what the last… point towards, right, that you were going to.
**Austin Parker** 18:02 Yeah, I saw there was some more comments that came after the last spec meeting I was at that I need to go through. I've just been, Busy with other stuff.
I haven't heard anything… let me double check… Pick.
Toc… So… last update I have is from April 1st.
Eoc was talking to the New York Times… I haven't heard how that went.
**Alolita Sharma** 18:42 Austin, we reached out, but I think we reached out to Emily.
And she's on… you know, she's, I guess, changing… she's not gonna be on the TOC anymore, so…
**Austin Parker** 18:54 Yeah, Dems… neither Dems nor Emily are gonna be at QC, but they're committed to wrapping this up before their term ends.
**Alolita Sharma** 19:01 So I'll get the folks to reach out again, I think.
**Austin Parker** 19:04 Yeah.
**Alolita Sharma** 19:05 the KubeCon thing.
**Austin Parker** 19:07 Yeah, I just pinged them for an update, but what I heard, from my conversations at KubeCon, they're committed to getting this across the line before their TOC term ends.
**Alolita Sharma** 19:19 Okay, because I talked to Dims at KubeCon, and he said that, Again, they were going to discuss it, so maybe they did after, right after. KupCon.
**Austin Parker** 19:29 Yeah, I… they said, I have… the last update I have is for April 1st.
**Alolita Sharma** 19:34 Okay, cool.
**Austin Parker** 19:36 But I… I pinged them again.
The only other… Not graduation thing, but… I… also… Pinged… anthropic folks I know, again, about the, Claude access… Or… the project.
I have not seen anything.
Check our email real quick.
**Morgan McLean** 20:13 Are they opening that up to open source projects?
**Austin Parker** 20:19 Yes, but, like, there was a form that we filled out, like, over a month ago.
**Morgan McLean** 20:29 Oh, this is just for General Clark, okay, yeah.
**Austin Parker** 20:31 Well, I mean, it's to say, I mean…
**Morgan McLean** 20:33 This is not the new mythos thing.
**Austin Parker** 20:35 I don't know if the Mythos thing is included in it, or it…
**Ted Young** 20:43 They've given out a limited number of seats, and they've given some to the Linux Foundation, right?
**Austin Parker** 20:49 Yes.
**Ted Young** 20:50 Yeah, I think…
**Austin Parker** 20:50 Those are for Linux.
**Morgan McLean** 20:52 I have to imagine that would be the priority of your life, yeah.
**Ted Young** 20:54 Yes, exactly. It doesn't seem like that has trickled down to the CNC.
**Austin Parker** 20:57 Yeah, there's… So the… specific program, there was a, like, Claude for open source…
**Morgan McLean** 21:09 I saw that.
**Austin Parker** 21:10 And I don't know what the relationship between that and a glass wing is, if there is even a relationship.
**Morgan McLean** 21:15 There might not be one at all.
**Austin Parker** 21:17 But the thing that we apply for is the Cloud for Open Source, Cloud for Sec… now, the thing is, though, is that the Cloud for Open Source, Cloud for Security thing does sound a lot like Glasswing, because it's basically, hey, this is an automated Cloud Code thing that goes and, like, looks for security vulnerabilities.
That is a thing we applied for.
I, yesterday, asked my contact there to poke the people again. I… All I can assume is they are just, like, super overwhelmed with demand, and also, like… you know, I don't know how often you all spend looking at the Claude status page, But, Yeah, there's… Yet another downtime today.
So… Things over there seem… Exciting.
I imagine.
I will update folks as soon as I know anything else.
**Ted Young** 22:39 So, just to follow up to my last item, since we were already talking about the system packaging SIG, the final blocker was TC sponsorship. Tigrum was saying he'd be willing to be an escalating sponsor if we delegated sponsorship to Anthony.
I'm totally down with delegating to Anthony. I've been working with him on this project for a while. He's very knowledgeable of it, and he's been involved in OpenTelemetry for a long time.
They both work at Splunk. I don't have any problem with that. If… So, just checking with the GC, everyone fine with that? Anyone have…
**Morgan McLean** 23:18 Which Anthony's this?
**Ted Young** 23:21 And fun.
**Morgan McLean** 23:22 Oh, Antoine. I was like, which Anthony works in Antoine?
**Ted Young** 23:29 me and Michael.
**Morgan McLean** 23:29 Well, then he said they work at Splunk, and I was like…
**Ted Young** 23:32 Bastard. Yeah.
**Morgan McLean** 23:34 I wonder, like, have I been.
**Alolita Sharma** 23:35 Oh, so…
**Morgan McLean** 23:35 out of touch.
Alright, Antoine, yes.
Yeah.
**Ted Young** 23:44 Yeah, so if there's any… unless anyone has, like, any blockers, that's what I like to propose. That gets us the TC sponsorship, and given that we're taking, kind of, the stability stuff out of the mix, and we're also scoping it down to a Phase 1 that isn't requiring a bunch of, like, maintainer involvement, we're gonna say we're gonna package together what we can without the maintainers having to do a lot of work, and then we're gonna present that to the community. It feels like that… that whole thing is now unblocked and free of the… the other concerns that we had, so… If the…
**Trask Stalnaker** 24:19 TC's happy, I'm happy.
**Ted Young** 24:21 Sounds good.
I wish I could always… I wish that was always true, but I don't…
**Morgan McLean** 24:30 It's generally true.
**Ted Young** 24:32 It's often true, yeah.
Cool. Anyways, that's all I got.
**Pablo Baeyens** 24:42 Cool, I guess I'll… cover my… topics quickly. So, jack was working on… Changing the data model, through these work streams.
thing, he closed the PR… Day before yesterday, I think? So we opened, part of it that I think should be not very controversial, so I would appreciate a review.
On that one, that's 3366.
And then the other PR that I would like a review on is the one adding the details for… the MCP project, that one just needs another approval so that I'm able to merge, but it… It should just be, like, I need some links.
Then… The other one was about the sick, like, I see…
**Alolita Sharma** 25:43 Yeah, Pablo, I have it actually on my list. I just got delayed because of KubeCon.
He just was out sick.
So I'll get that set up right away.
**Pablo Baeyens** 25:55 Okay.
**Alolita Sharma** 25:56 Yeah, yeah.
**Pablo Baeyens** 25:57 Thanks. I'll let them know.
**Alolita Sharma** 25:58 Yeah.
I commented on the issue also, so…
**Pablo Baeyens** 26:05 Cool.
They should know then.
Then the other thing I had, there was this issue because of another instance of bundleism on, Google Doc, in this case, the one from the specification.
Meeting notes.
**Alolita Sharma** 26:20 Did they, like, wipe it out? What happened, Pablo? Do you know?
**Pablo Baeyens** 26:23 I think so, yeah, I think it was just entirely deleted, but I didn't see it.
**Alolita Sharma** 26:29 And they couldn't recover it from the history of COVID?
**Pablo Baeyens** 26:32 Yeah, it is recoverable. Okay. It's just that there's some.
**Alolita Sharma** 26:34 Somebody just deleted stuff.
**Pablo Baeyens** 26:37 Yeah, there's some people on the… GitHub issue, talking about maybe removing the ability to edit anonymously. I think at the very least, we should offer that option to SIGs if they want to.
But I wanted to.
See what people thought.
**Marylia Gutierrez** 26:56 Yeah, I was gonna say, like, we can start with the ones that, like.
People are having issues, and it's also a way to test it out, how this works out for that sig.
And then we can share with all the others, but at least for the two that had problems, we can do this. We already did for the other, or no, am I crazy? No, I think I'm crazy.
**Pablo Baeyens** 27:19 Yeah, I think we did it for the profiling.
**Marylia Gutierrez** 27:21 For the profile, yeah. So, so far they didn't say they didn't have any complaints. We can do a check with them, again, just to see how things are going, but I don't see why we cannot do it with other, but we should let maintainers know that that is an option. Maybe they Don't think about it, but yeah.
**Pablo Baeyens** 27:45 Okay, I… Good comments on the issue to that effect, like, saying, Any maintainer that wants to… can request that we… Restrict permissions on their meeting notes?
And… I had a third thing, but it's, like… Guess we can combine it with Mariela's topic about security vulnerabilities, so, yeah.
I'd like you. Go ahead.
**Marylia Gutierrez** 28:12 So, yeah, I think that is a topic that is in a lot of people's minds, just, like, how to find security issues, and tried to get a little more ahead, before a lot of things start to get open. So I know that a few SIG is already doing this, so I know, like, I was talking, like, today with Jack on the skills that he is creating for Java, .NET, also talked with them, how they were finding. I did similar things for the JavaScript.
But it's like… each person is using a different prompt, and is finding, like, different things. I even, like, gathered the prompts from all the others, and tried again on JavaScript, and it's finding more things. But… so we… what I'm doing now is, like, gathering, like, options, and I want to share with maintainers, because I already talked with the… all the six that I am liaison. I'm like.
you should do a check and see if you can find things to stay, like, ahead. But at the same time, we want to have a little more, like, example of things that are working out.
things that we can find, but I don't want this to be a public thing, because that would basically say, like, hey, people don't want to hack us, this is the exact thing that we are checking. So my idea right now, basically, I'm gathering info, and if anyone here is also doing something, please let me know.
But then I need to decide where to put this information, because I was thinking.
We have… so we have the SIG security, so on that one, I was… Thought of putting just a general message, basically saying, kind of like, okay, you should be doing this check, but if you want, like, more details, talk with a GC member to get access on the things, and maintainers… yeah, so I was thinking it could be the admin, or there is the other one that is about… is hotel private or something? But yeah, I was looking for ideas of where I can put this information. Is admin… have only maintainers?
Only maintainers? Okay.
So yeah, maybe I can create, like, a folder there with examples. So yeah, so right now, just gather information. If anyone has anything, please let me know so I can put it there as well.
And also, yeah, provide the guidance to people, just, like, what I'm doing is, like, telling them, if you find something, do not just open a regular issue of, like, hey, I found all those things. No, go through the proper channels, or just have the PR and things like that.
**Austin Parker** 30:45 So, related to that, I don't know if folks saw the message from Jack, in GCT, or… Or upload… Yeah, it was…
**Pablo Baeyens** 30:57 Yeah, I want to talk about that, I don't know if…
**Austin Parker** 31:01 I feel like it's related.
**Pablo Baeyens** 31:02 public… But.
**Austin Parker** 31:04 Oh, actually, that's a good point. We… Hmm. What else do we have on the… Agenda.
**Pablo Baeyens** 31:18 We're good. I think the other topic should be fast, so we could…
**Austin Parker** 31:22 Yeah, can we, yeah, can we…
**Alolita Sharma** 31:25 Yeah, the other one should not take much time.
**Austin Parker** 31:28 I would like us to talk about it privately. Yes.
Yep. Alright.
**Pablo Baeyens** 31:33 Let's do that.
**Marylia Gutierrez** 31:35 Okay, cool.
**Alolita Sharma** 31:35 Time box, or for 5 minutes or something?
**Austin Parker** 31:39 Yeah.
**Marylia Gutierrez** 31:42 Should I move to the next one, then? Yeah.
**Alolita Sharma** 31:44 Fairly.
**Marylia Gutierrez** 31:45 Yeah, for my next Jewish comic.
**Alolita Sharma** 31:47 So.
**Marylia Gutierrez** 31:48 So, like, first one, just please review is that script to basically flag people that are no longer active.
It's been there for a while, no more feedback from the community, so I'm assuming it just should be good to go.
The next one is, so I… we are creating a new survey for end users, but this one, I'm actually trying to focus on helping maintainers on, like, what should we be focusing, like, what are the things, because I have a few SIGs that I'm talking, and they are just like, oh, I don't know if I should deprecate this version, or still support this version, because I don't know what people are using. So, I want to have questions that are… gonna help drive, or, like, roadmap, or things like that. So right now, I'm just putting all the things that people are sending me to this file. Then I'm gonna try to compile and have little things, like, more generic, or just combine things that are, like, repetitive to make.
the… the… the person replying life a little easier, but if… if you can also reach out to your SIGs and ask if they are interested on anything, let me know. But try to focus on questions that are… have… an actually, basically, an action can… that can be done. So, for example, people were sending me, like, oh, are you happy with the SDK? I was like, yeah, people can say, like, no, I'm not. So what are you gonna do with that information?
**Alolita Sharma** 33:13 Yeah, exactly.
**Marylia Gutierrez** 33:14 Now, if you ask, are you having specific problems? Are you having performance problems? Like, tell me what is wrong that you want to, like, focus on, that you can actually do something about it. So that is the type of question that I'm, trying to focus on for the survey.
And get those orders.
**Alolita Sharma** 33:30 So, Marilla, do you plan to kind of have some… in the survey, kind of have some questions based on that? Or is it the other way around, where… We are just asking maintainers for… You know, different types of specific, actionable.
**Marylia Gutierrez** 33:48 So…
**Alolita Sharma** 33:48 They're hearing from the.
**Marylia Gutierrez** 33:50 No, no, so the… the survey is for the end users, so the maintainers want to know, like, what I should be focusing on. Can I stop supporting node 10. Can I stop that now, or still somebody using… is that… Type of thing.
Yeah, so they… I'm gonna… so my idea is to have, like, the first page, very, like, generic, and then people can select which language that they use, because if I have very specific… language questions, I don't want it to show to everybody, like, what do you think about the agents? I don't use Java, so why do I need to care about this? So then all the next pages are specific per language.
**Alolita Sharma** 34:26 I see, I see. Okay, got it.
**Marylia Gutierrez** 34:34 And, yeah, those are my, my outings.
**Alolita Sharma** 34:37 Okay, very quickly, I had a couple of items just for… for sharing. I think we can just, the CFP is out, so again, a good time to kind of start sharing with our maintainers channels and different channels. I'll… maybe… Severin, is there… can we just post on different… Sigs, SIG channels, or… Do we assume people already know about the CFP, and…
**Juraci Paixão Kröhling** 35:05 So, I believe the community managers are tasked with, making this communication, talking to them.
I don't know, Austin, you are, you are, managing the managers?
**Alolita Sharma** 35:17 hasn't hurt.
**Austin Parker** 35:19 No, I saw that it was open, I, I'll ask.
**Alolita Sharma** 35:26 Okay, no, I mean, I can ask too, so I just wanted to call that out.
**Austin Parker** 35:29 Fair enough.
Yeah.
**Alolita Sharma** 35:30 Yeah, I mean, it's just easier for folks to know about it. More heads up is good. The other thing I just had a.
**Juraci Paixão Kröhling** 35:38 Thank you.
**Alolita Sharma** 35:39 Yes, sir.
**Juraci Paixão Kröhling** 35:40 Everyone's small comment between that? Yeah, so, I would like to… I think I talked to Austrian privately about that, but I think the community managers can be, or should be, dealt with the GC the same way as SIGS, like, with one liaison, to make it easy to communicate, so that, you know.
We have… a communication channel, an official communication channel. So, we can try that now with this one here, so perhaps, we can, we can have Austrian to communicate that, or to ask them, and to synchronize with them.
Nothing against you doing that, Alolita, it's just that, I think that having one person being the liaison for the community managers is also helpful and useful.
**Alolita Sharma** 36:21 Yeah, yeah, definitely. Agreed.
**Juraci Paixão Kröhling** 36:24 Okay.
**Alolita Sharma** 36:26 Who is it right now? Is it Austin?
**Austin Parker** 36:28 Now it's me, but if someone else would like to do it, I'm not gonna complain.
**Juraci Paixão Kröhling** 36:33 So, I'm fine, taking that. I think I also mentioned privately, if you… if you want to offload, I'm happy to take.
**Austin Parker** 36:41 Yeah, just let them know.
**Juraci Paixão Kröhling** 36:42 Okay, I'm handling the hotel… global hotel nights and so on with them already, so I use.
**Austin Parker** 36:48 Yeah, it's nice.
**Juraci Paixão Kröhling** 36:49 Talking to them.
**Alolita Sharma** 36:50 Yeah.
That sounds good.
**Austin Parker** 36:52 I'll let him know.
**Alolita Sharma** 37:05 Okay, very quickly, the second topic was just that, I saw Jurassi, you and, Severin had already reviewed the post. I just thought that, you know, reading it, as a user who may not have a lot of context, it seemed like Bloomberg was, kind of claiming that all these, you know, issues exist in OTEL, because OTEL was the example project. And this went out, actually, on, the Linux Foundation, you know, call-out for OpenTelemetry in collaboration with Bloomberg, you know, kind of doing this huge project… initiative.
Hmm.
So I wasn't sure, you know, if we were cool with… this kind of call out, because it seemed like, you know, we were… we were in the midst of all these issues where Bloomberg was going to come and help us with some of the folks contributing. I thought it was just a volunteer program when initially Jurassi and Severin had, you know, discussed this with the GC.
So, it was just an impressions thing, more so than anything else.
Did folks have any comments on this? Or… didn't care.
**Morgan McLean** 38:27 I hadn't seen it.
**Juraci Paixão Kröhling** 38:28 It's interesting.
**Alolita Sharma** 38:29 I didn't see it either, I saw it.
**Morgan McLean** 38:31 Yeah, so, like, Bloomberg basically is taking a whole bunch of engineers, and for each one, for two weeks, they're gonna be focused exclusively on hotel contributions.
**Austin Parker** 38:38 Yeah, I also was not aware of this, so…
**Severin Neumann** 38:41 No, no, no, no.
**Morgan McLean** 38:41 I like it.
**Severin Neumann** 38:42 So, I mean, I have talked about this for a few times, and then maybe now, now I've.
**Austin Parker** 38:47 It's good.
**Severin Neumann** 38:48 Not like people recognize it.
This is a mentorship program going for 10 weeks. They're not, like, dedicating 2 weeks on that, let me be clear on that. They can spend… time on OpenTelemetry during that time. They have selected around about 40 engineers for that, and those are experienced engineers, right? This is very different to another mentorship program. This is very different to… whatever, outreachy, LFX, or Google Summer of Code, because, like, these employees… and what was interesting is, like.
a lot of them have open telemetry experience already, right? They're end users, they're, like, implementing something within within Bloomberg on OpenTelemetry.
So, yeah, they're really eager to do something on that, so I'm very happy about it, and if there's any concerns, let me or Yorasi know. I mean, we're closely involved with them.
**Marylia Gutierrez** 39:48 And also, I know that there is the project board that they are using, because I know I was helping out, like, Victor, like, find issues to put it on that, so if you are also having, like.
issues that you think they would be able to work on. I don't know what is… if he's putting a label, or he's just putting on the project itself, but I guess, well, maybe reach out to Severin or to Vitor, and they can put it on the board.
**Severin Neumann** 40:17 Yeah. I mean, that's maybe one of the issues that we have, like, we have a few maintainers that help with mentoring.
But we don't have, like… for example, they're very curious about Python and C++, but I understand that they… Python and C++ maintainers don't… volunteer for being mentors in this project, but I'm really eager to see them, like.
picking up some of the work they get from Bloomberg, because what's very important to Bloomberg as well is, like, that this is a sustainable program, so they really hope that people stick around, right?
**Alolita Sharma** 40:49 From… from the company, right? From their side.
**Severin Neumann** 40:52 Yeah, this is not like… this is not like, oh, do this for 10 weeks and then stop doing that, like, they have something they call Bob Hours or something like that, don't ask me what… That abbreviation means, like.
charity time, like, they can spend, and they said, like, yeah, you can spend this on those open source contributions, like, I don't know, a few hours per month.
And they have done this before with other projects as well, so… yeah.
**Alolita Sharma** 41:17 No, no, I think the project is fine. And Severin, again, I do know that you did share the initiative, but I think the way the blog post read, was probably something you guys didn't see, ahead of time, or did you review the blog post?
**Severin Neumann** 41:36 Yeah, they did a blog post, I have to admit, like, it happened during a time where I was not, like, paying full attention, and it was like, hey, we have to get this out within a few days, and CNCF was also very eager to push this out really quickly.
But of course, we can… we can also apply changes, right? If there's anything specific where you say, like, hey, this wording should be different, yeah.
**Alolita Sharma** 42:01 Yeah, because, I mean, I… again, I… I think… The only… only point I wanted to make is that, hey, you know, can we pitch the positive things also that'll come out of this whole initiative, which I think kind of got over highlighted… didn't get highlighted enough.
Because, again, you know, everyone who's contributing time, as well as what, you know, folks are kind of, Mentoring on, some of the areas, you know, some of the projects that need help. Maybe it's a great opportunity to highlight that, too.
So I just wanted to call that out, because, again, I think it… it was… it was shared across the industry, you know, by the Linux Foundation.
Yeah, that's all I had. Jurassi, you had the next topic.
**Juraci Paixão Kröhling** 43:01 Yeah, no, the next one is, mostly a question about the hotel network, SIG. So that was originally, I think, the hotel eBPF repository, and then it went into network, so eBPF network.
Apparently they… didn't have any Sikh meetings since January.
I think Ted is the liaison there. Apparently, one of the maintainers, is not even, like… Basically, it looks like it's a dead sick. Is it dead, or is it not… is it not dead yet?
I think we talked about that before.
I think Ted mentioned, that we are gonna try something.
**Morgan McLean** 43:45 When we talked about it last, it was still being maintained by Jonathan Perry, but what I can see here is he hasn't had any commits since last November.
**Juraci Paixão Kröhling** 43:54 Yeah, and no SIG meetings since January, so I think it is effectively dead.
**Morgan McLean** 43:58 Yeah, and he was the main person.
**Juraci Paixão Kröhling** 44:00 God works.
**Morgan McLean** 44:01 So if he stepped away, then I think it's done. Yeah.
**Pablo Baeyens** 44:04 Yeah, I've heard the same thing from the data of maintainer that is listed there.
There's no activity.
**Juraci Paixão Kröhling** 44:11 Should we then archive the SIG, like, the repositories, start a procedure for that?
I think we've given enough Time, choices, chances…
**Morgan McLean** 44:22 Yeah.
**Juraci Paixão Kröhling** 44:25 Okay.
Ted, you are the liaison, do you have the capacity, like, the time capacity to do that?
**Ted Young** 44:31 Yeah, sorry, I've not been paying attention that…
**Juraci Paixão Kröhling** 44:35 Okay.
You mean, on a SIG, or right now? I mean, do you need me to rephrase, or…
**Ted Young** 44:44 But…
**Juraci Paixão Kröhling** 44:45 No, I mean, you are not paying attention to the SIG word, you are not paying attention to what we are talking about right now.
**Ted Young** 44:50 No, I was not paying attention to the… to the network.
**Juraci Paixão Kröhling** 44:53 Oh, okay. Okay, cool, okay, alright.
**Morgan McLean** 44:56 It looks pretty dead, I… yeah.
**Austin Parker** 45:01 This is where having scarf would be useful, because we could actually see if anyone was using it.
**Morgan McLean** 45:10 I agree.
**Austin Parker** 45:11 Anyway… I think we should probably go ahead and start the archival process.
**Morgan McLean** 45:20 Yeah, the only recent commit was, Samir changing his employer name.
That's the only commit since January.
And the last real commit… was… before November… probably mid-November of last year.
Of, like, actual functionality.
**Juraci Paixão Kröhling** 45:45 So perhaps it would be also interesting to see what is the repercussion on eBPF in general. Like, I know that during the beta donation, there were some comments about network.
**Morgan McLean** 45:58 I was… I can speak to that. So, I had proposed that the folks… I'd set up some conversations between the people working on EBPF profiling on Obi and on OTEL Network.
I think the profiling and OB conversations are pretty fruitful. The network one, it's just its own implementation. My understanding is it's a much older implementation, it has dependencies on, like, every Linux kernel revision that are quite painful.
But for whatever reason, they did not want to change it. So, as far as I know, there are no dependencies, there's no coordination there at all. They're entirely distinct.
But I think the next step would just be, like, Ted or someone reach out to Jonathan Perry, and just find out what's going on, and then start to bring up the fact that, you know, this is not active anymore, and it certainly doesn't look like it, then we're gonna want to archive it.
**Marylia Gutierrez** 46:49 It is the… it is the same scenario, or maybe somebody's already looking to this, for the goal instrumentation.
That one is also barely active. If you look, like, for the past, like, months.
**Morgan McLean** 47:03 Is that because that's… was that one… that one, I think, is meant to be replaced by Obi? Is that accurate?
**Marylia Gutierrez** 47:10 So I.
**Morgan McLean** 47:10 I thought that was the.
**Marylia Gutierrez** 47:10 Because I, yeah, like, I know that people mentioned, like, during KubeCon, like, oh, they were considering, like, shutting down, because if it was…
**Morgan McLean** 47:18 People will work on it, too.
**Marylia Gutierrez** 47:19 Yeah, the much, like, renovates. But I don't know if that…
**Morgan McLean** 47:25 Tyler is someone would know, like, there's a lot of… it's a lot of the same people on both. I understand their intent was to just basically shift it all to Obi, but I haven't checked in with Tyler on that topic in a while.
**Trask Stalnaker** 47:36 Marillia, which repo is this?
**Marylia Gutierrez** 47:38 Go instrumentation.
**Trask Stalnaker** 47:42 Oh, not compile instrumentation, okay?
**Morgan McLean** 47:44 This is the runtime instrumentation, yeah.
**Trask Stalnaker** 47:46 Okay.
**Juraci Paixão Kröhling** 47:47 Thank you.
**Morgan McLean** 47:47 Your intent was that Obi would just supersede it.
**Juraci Paixão Kröhling** 47:50 Yeah, I mean, so this is on me, the Go instrumentation I'm the liaison for. I… and even during this month's check-in, I just told them, like, pretty please, tell me that you're alive, like, give me something, like, tell me, scream at me, because it's been, like, 4 months that they didn't even react to my messages on… on the check-ins.
So, it feels that as well, like, as a SIG, right? So, no people from the originals are reacting at all.
Regionals here have been the people who've donated the code back then.
And for the new people, I see they are more active on Bela right now than Go Instrumentation. So perhaps… on me now is, based on what we discussed, I can just go there to the SIG check-in channel and ask them, like.
Should we also put a plug here?
**Morgan McLean** 48:40 Yeah, the difference, though, is I think that one, it may be on their side, poor communication, not yours. But, I… from chatting, when Bela came in, and, like, OB started.
that was, like, something that we had discussed wanting to make happen, is just have it be replaced. And so that one, it might be their reaction, it's like, yes, please, like, that's why we haven't been active.
**Juraci Paixão Kröhling** 49:02 Okay.
Yeah, alright, so I'm gonna propose that and see if that's a reasonable next step for the CEO.
Cool.
**Pablo Baeyens** 49:12 Could we jump to a private session?
**Austin Parker** 49:14 Yeah, I'll start on a call.
**Morgan McLean** 49:16 You can send it the link on Slack.
**Pablo Baeyens** 49:19 he left, so I guess, yeah.
**Alolita Sharma** 49:21 Okay.
**Morgan McLean** 49:21 I sure hope so.
