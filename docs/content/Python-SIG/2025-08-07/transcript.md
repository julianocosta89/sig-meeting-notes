SIG: Python SIG
Date: 2025-08-07
Duration: 23 minutes
============================================================

## Zoom Recording Transcript

**lechen** 02:34 Hello! Everyone.
**tammy.baylis** 02:39 Hello!
**John Scancella** 02:40 Hello!
**lechen** 02:59 Yeah. So as usual, please add your names to the attendees. List on the signals if you can.
and any any topics or Prs or issues you want to bring up. Here's the form to do so.
Alright, we can go ahead and get started. Yeah, share my screen real quick.
Everyone sees the signals right now. That's what I'm presenting.
**tammy.baylis** 04:09 Yes.
**Paulo Vital** 04:11 Yeah.
**lechen** 04:12 All right. So yeah, welcome to another iteration of the python. Sig.
Yeah. Any any topics you want to discuss is the form to do so. Pr reviews stuff like that. Any administrative things we can just go ahead and get started with the 1st topic. Tammy looks like you have a question about the probability sampler the experimental one. Pr. I think.
**tammy.baylis** 04:38 Yeah, thanks. Leighton, hopefully. Quick question, famous last words. But this contributor is doing a 1st implementation in python for the consistent probability sampler that's still being spec'd out, and I think it's supposed to be a much better version of the trace id ratio sampler that no one should use. So it'd be great if Python has had it too. Java has it? My my question is, should this be in the contrib repo, as they initially put into pr, or should it go.
**lechen** 05:14 Mr. Big to the core. Repo.
**tammy.baylis** 05:17 But with like an underscore, to hide it as an experimental sampler. That's that's my question for the Maintainers.
**lechen** 05:27 Yeah. Good question. Yeah. I think your answer in the comments. At least, this is my opinion. Makes a lot of sense. We already have precedence with putting experimental components in the core repo. So I don't think I don't see why this wouldn't want to be able to go in. We also have already, like a kind of a pattern in which we have the samplers defined in SDK trace so we we could possibly like added there, too, just with an underscore. So I think that's totally fine. At least for us like contribute has always been a more.
not only for experimental, but like sometimes, like vendor specific components or 3rd party components would be more suited for there. So I I'm totally okay with adding it for the repo.
**tammy.baylis** 06:33 Okay, great thanks. Yeah. So I'll I'll continue review on the core. Pr, that they put in and not look at the contrib.
Thanks. That was my question.
**lechen** 06:44 Nice do they?
Quick? Question the consistent sampler. It's like a sweet oath.
Different. Sampler is right.
**tammy.baylis** 07:00 Yeah, I think so. And yeah, I haven't gone into it yet, but I'm I'm wondering if they could like, maybe repurpose the existing always on, always off samplers.
I also don't fully understand, like what the consistent probability sampler is supposed to do yet, so I have to keep reading to to better know? Like, if if each one's needed. Yeah.
**lechen** 07:29 Yeah, I'll have to take a look at the spec as well. I'm not too familiar with this. But yeah, perhaps we can like do something with the namespacing and everything.
Sampling, experimental little bit awkward. But yeah, not a huge deal. But I think we just need more reviews on this. So any other comments on this? You are alright sounds good.
It's moving right along redeem. Is that how you say your name? Sorry are you in this chat right now.
**Ridhima Satam** 08:07 Yes, that's right. Yeah, I can share my screen.
**lechen** 08:16 So this is your Pr, right here.
**Ridhima Satam** 08:19 Yes, that's my Pr. I want it to be reviewed. By the community. I got some couple of reviews, though I have a question. I'm not sure if this community can answer, like, I have to attend the semantic conventions. But there's a question there regarding the attributes. Yeah, this one.
So this is the Langchain instrumentation. Llm span. We are generating. And earlier, we had this system attribute where we added the the system. Name there like. So for Langchain, it's if I'm using the Chat Openai it would. So if you go in the description as well of the Pr, you will see you get the chat open. Yeah. But then they introduce provider name, and then system was deprecated, and the actual provider would be just the open. AI!
So that's 1 doubt I had.
Oh.
**lechen** 09:22 Yeah. So I haven't personally attended the generally I see in a while.
But we do have some experience in dealing with the deprecated attributes.
Previously, like. Historically, we've always kind of taken the stance that because our instrumentations are all experimental.
It's generally understood that all of the attributes would be an experimental state. Meaning like people who depend on, or customers who depend on these instrumentations, should expect with a degree that, like some of these attributes would disappear or be deprecated. We did have a caveat behind that behind the Http semantic conventions in which, you know.
it was determined that strategically, we wanted to support even deprecated attributes due to the sheer amount of people that use them. And we didn't want to break I'm not. I haven't been actively following Jen AI semantic conventions, but I don't know if we, if there was efforts in kind of pursuing the same degree of support.
But I think I think we would need to kind of settle that first.st otherwise we would just kind of snap to the the new semantic conventions. Pretty simply.
I'm not sure if anyone else in this group has been following any of that or if there's any guidance from other languages, what they're doing in terms of deprecated attributes.
**Dan Gomez Blanco** 11:14 I guess there is.
Sorry. I don't think I've got like apart from the Http. The Http case that you mentioned. Not sure if I've got anything else to add but as well here, if this is like, this is new functionality that's being added right, it's a new.
Is this a new sort of instrumentation? So then, I guess that makes a difference in terms of like, you know.
changing it, changing it deprecated value, quite a deprecated attribute compared to adding something new. Right? I guess.
**lechen** 11:50 I don't think I think the land chain instrumentation already exists.
Or is this net new?
**Ridhima Satam** 11:57 Yeah, this is the new one we have started last time. We just started the 1st year of the skeleton files of the.
**lechen** 12:05 Oh!
**Ridhima Satam** 12:06 Jane is.
**lechen** 12:06 We've never really.
No, we never released this. Oh, okay, sorry I I was under the impression that we were making a breaking change or something.
If that's the case, like I would go ahead and just use the.
Is this Jenny system being replaced by Provider name? Oh, it does look like it is.
**Ridhima Satam** 12:27 Yes, it is it. It shows slight difference, like, if you go to the description of the Pr. I have put down like how it would appear. And is there an importance keeping them both like if in the description of the pr right at the top.
**lechen** 12:41 Yeah, yeah.
Okay. So then, then, this is great. Oh, sorry. Go ahead, I interrupted. You.
**Ridhima Satam** 12:46 Yeah. So the second is the AI system. Chat Openai, because we are using the Chat Openai Lang change chat open here. So system we have, we use to add Chat openai. But now I see you get provider name as well. In the metadata of the attributes. So in the yeah. There you have the just open AI, which is the provider. So in this case, is there any value to keeping both?
I mean, it's already replicated. I'm asking like, but that's the difference we're using. Planchain, at least.
**lechen** 13:22 Yeah, yeah, we're so this is a net new instrumentation. I would definitely recommend not implementing deprecated attributes.
We wanna keep our kind of span service as simple and as least redundant as possible.
Besides, from lang chain, though this does open up a kind of a newer question of like which of our instrumentation support?
Test still the old deprecated attributes separate from your Pr. Of course.
So I think we would have to do something similar in which we would make an effort to migrate all of them as well, but at least for your Pr. Definitely stick with the non duplicate attributes, and and you don't have to include Gen. A system.
**Ridhima Satam** 14:10 Okay.
yeah. So that that's just my question. And then just please take a look at the Pr.
Believe you.
**lechen** 14:23 Awesome. Yeah, thanks. Thanks for contributing.
Okay, cool.
Let's move right along to Keith's. Pr, let's see in a details.
**Keith Decker** 14:41 Right. So there's an ongoing initiative here to generate a utils package for making instrumentation around generative AI easier. This is the skeleton that we're building and looking at, getting like we did with line chain and weviate to get the the package started.
So, just looking to get the Pr. Reviewed. I had a question there which you just pulled up there about the Bootstrap, that I'm not entirely sure how how we handle that when this won't actually have any instrumentation, because it's utilities around additional instrumentations that would be built.
**lechen** 15:33 Yeah, this is a good well, this is great. Let me see, I haven't taken a look at it directly. This design, Doc, but any kind of you know, removal of like boilerplate code and like functionality that is common is definitely well received. Is this the sorry me?
Is this like the skeleton of it?
**Keith Decker** 15:57 Yeah, so that we could get the the package started, and then the implementation will come in a second pr, like we're doing with blank chain and media.
**lechen** 16:07 Yeah. So the the Bootstrap. Like, just to answer your question, yeah, the Bootstrap is only specifically to used in auto instrumentation we use? I believe, open telemetry. Bootstrap. This is so that you know.
we have a, we have a process that like scans, the user site packages and installs automatically instrumentations that are related to those.
So you don't actually have to add this this only pertains to instrumentations. We have this packages to exclude, because we, we didn't want to apply this to certain instrumentations automatically with Bootstrap. So no need to add this. We also have like like a test utils second. We don't have that in here. So.
**Keith Decker** 16:58 So, since this doesn't have anything in the actual instruments. Dictionary.
**lechen** 17:03 Oh, yeah.
**Keith Decker** 17:04 Okay, so I'll remove that entry. Thank you.
**lechen** 17:07 Yeah.
**Keith Decker** 17:08 So yeah, if we could. I'll remove that and then update the the requirements around. SDK, I have Redeemer. I know you're here we this package, we don't rely on open telemetries. SDK, right? That would be part of the actual instrumentations around utils. Are we going to be using the SDK in this.
**lechen** 17:33 Yeah, I wouldn't expect a dependency on the SDK, if it's a instrumentation utility package.
**Keith Decker** 17:41 Okay, so I can upgrade the or update those 2 things and get the Pr back into review today.
**Ridhima Satam** 17:49 Oh, there's 1 thing I want to say here, this SDK utilize the utils package is under the Gen. AI instrumentation, so it will be at the same level where other instrumentations are. So even that doesn't make a difference. Like you said that file, we don't have to add excluded packages.
Is the is the place? Okay?
**lechen** 18:14 Yes, it's it's what Keith called out. If it doesn't have an instruments section in the it's Pipe project so it won't get picked up by the bootstrap, I believe.
Yeah.
it being yeah. As a skeleton. Pr, this is great, like, I don't think there's anything wrong with this? Yeah, definitely, I don't think we wanna have a dependency on the SDK, and yeah, anyone who's interested.
Oh, wow! It was like a full blown design, Doc, nice
**Keith Decker** 18:59 So there's some light reading for you.
**lechen** 19:02 Yeah, yeah. So like, yeah, anyone's interested in reviewing this. We'll get this in as soon as we can.
**Keith Decker** 19:11 Okay.
Thank you.
**lechen** 19:13 That's nice cool, all right, onto the next topic.
Alright, John, let's join this call.
**John Scancella** 19:27 Yeah, I'm here.
**lechen** 19:29 Hello!
**John Scancella** 19:30 So just trying to contribute back I was, you know, taking a look through some documentation. Saw that like the examples only some of them like have. Oh, here's the link to like where this exists in, like the Github repo. So just saying, Hey, I'll I'll probably raise a pull. Request soon to to fix those Rst files so that each of them points back to the correct place in the repo. And then, while I was there. I also noticed kind of this discrepancy between what the Github documentation is saying and what the hotel documentation was saying.
I don't really know which one is correct. Should it be experiment, both experimental, both in development.
just was hoping to maybe get some clarity on that.
**lechen** 20:23 Yeah, that's actually a great question. So let me let me address both of those things. Yeah. So the 1st thing is, yeah, very welcomed to fix some of these documentations and like, Read me's and everything. I'm glad you're seeing it as a we kind of either missed it, or it's just out of date and not like this is how it's supposed to be so definitely any any kind of discrepancies that you see feel free to question them, because we haven't like it's a lot of maintenance to upgrade sorry update documentation like over time. So definitely, we probably miss something.
Secondly, for your question about experimental versus development.
Yeah. So like, I think there's a little bit of a drift between terminology between what open telemetry uses and some sigs. I believe we took the terminology right from like the see the glossary, or something like that.
Oh, this is hilarious! This is my Pr, what the hell?
What is this?
Oh, yeah.
right? I see. Yeah. So we've always used experimental. And it's like, it's it was just a historical thing. Like way back when we created the the readme we just want to be consistent with the actual source of truth.
which is the open telemetry website. So we'll probably be changing that to development anyways. So.
**John Scancella** 22:01 Okay, cool great to know.
Thanks. That's all. I I do. I'm using my lunch break for this, so I'll probably skip out here in a few minutes, but hopefully I'll I'll get the full request in the soon. Ish.
**lechen** 22:18 Awesome. Thanks, Jeff.
Cool, I think.
it's all the list of topics right now. Does anybody have any other things they want to bring up.
I think we recently did a release actually like 2, like a week ago, or something. Yeah, so we won't have another release for another 2 or 3 weeks or so. So we have ample time to get our Prs in. And yeah, I think that's pretty much it. If nothing else. I'll see everyone next week.
everyone some time back.
**Dan Gomez Blanco** 23:02 Okay. Thank you.
**lechen** 23:02 Thanks. Everyone.
**John Scancella** 23:04 Thank you.
**Emídio** 23:04 Thank you. Bye-bye.
