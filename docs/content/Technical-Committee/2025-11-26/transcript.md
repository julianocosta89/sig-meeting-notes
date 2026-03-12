SIG: Technical Committee
Date: 2025-11-26
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Armin (Dynatrace)** 01:46 Let's see if we are able to get quorum today, because half of the US might be outright.
**Tigran Najaryan** 01:53 Yeah, it's the Thanksgiving week. A lot of people take extended vacation.
Let's, let's wait a few minutes, we'll see who joins.
**Reiley Yang** 02:29 Hey, Army, dealer.
**Tigran Najaryan** 02:34 Hey, Riley, how are you?
**Reiley Yang** 02:37 Hey, not so bad. How about you?
**Tigran Najaryan** 02:40 Good.
**Reiley Yang** 02:43 Yeah, that sounds better than my situation.
**Liudmila Molkova** 05:16 Hello, hi everyone.
**Reiley** 05:20 Hey, Linda.
**Tigran Najaryan** 05:23 Hmm.
**Joshua MacDonald** 05:34 Hello.
**Tigran Najaryan** 05:35 Whose week is this?
**Armin (Dynatrace)** 05:37 It's me. I'm not taking. Let's see if we get some agenda items as well. Carlos is just around the corner. I think he said he's 5 minutes late, so… With him, we would be 6 people, that would mean quorum. Do we have any agenda items? I already checked the spec inbox, that one's empty community inbox as well.
**Tigran Najaryan** 06:10 Must be the Thanksgiving week.
**Armin (Dynatrace)** 06:12 Feels like it, yeah.
**Joshua MacDonald** 06:18 I sure feel like it's a Thanksgiving week.
**Armin (Dynatrace)** 06:21 Boop.
**Carlos Alberto Cortez** 06:22 Is that the reason why nobody is sharing their, you know, camera?
**Armin (Dynatrace)** 06:29 I think that's just a coincidence, I can…
**Tigran Najaryan** 06:31 Here you go, Carlos.
**Armin (Dynatrace)** 06:32 Bring you.
**Tigran Najaryan** 06:35 You're missing my face?
**Armin (Dynatrace)** 06:47 All right. Carlos, are you going to surprise us with any agenda items today? Because otherwise, I think…
**Carlos Alberto Cortez** 06:55 Yeah, only the cutting one.
the latest feedback. Jack is not here, but probably can provide that for him.
offline. Tina, you were not here the last week, I think, so you… or were you here? I don't remember.
**Tigran Najaryan** 07:09 I will not, no, I was traveling last week.
**Carlos Alberto Cortez** 07:12 Okay, right. So, because I can probably just provide a quick update on this one.
So, let me just paste the… The link in the dock here.
So, whoever is driving, you can, like… Share that, maybe.
Who's driving today, by the way?
**Armin (Dynatrace)** 07:34 Me? Does it not say?
dead again?
**Carlos Alberto Cortez** 07:38 Sorry.
Bye. Bye.
Oh, yeah, you're right. That's right, yeah, great. Okay, yeah, so I guess that… oh, Jack, you're here. Great.
just a small update after talking with the latest, you know, points, that Jack brought.
So, you may remember… so it went in… Talk to the Android.
See, and to the, to embrace people So, maybe we can move, to the… there's a new section called cross-compatibility, which is a very, very short section.
I think it's down.
Can we move the screen? Oh, yeah, perfect, sweet.
So, yeah, the first one is a, Yeah, okay, maybe down, I'll do it… Maybe it can probably… yeah.
Actually, probably it's easier if I share myself for a second. I think it's… yeah, there's not a lot of… thank you.
There's… there are not many changes, but yeah, there are some clarifications, with what's happening.
Oh, there we are.
Okay.
**Reiley** 08:50 Yeah.
or beginner.
**Carlos Alberto Cortez** 08:52 Yeah, so the first one is actually even probably before that. I was talking to the Android people, on what they would require, you know, because they were talking about one of the potential benefits of having a Kotlin SDK is that the Kotlin, sorry, the Android stick can go and use that instead of using the other one.
And so the Java SDK doesn't have to expose many things, you know, to… to be able to work on their Androids. So the first one is that they said that this is indeed, as Jack mentioned, something that could happen in the future, not in the near future, and they would recommend it themselves that… the, you know, this API and interop layer, which uses the Java SDK and the Could exercise more, make sure that, you know, it's in a good actual position, you know?
On the other hand, I had… I was under the impression that, that Android didn't use metrics, but it seems they use… they do use metrics, so in this case, it's not like… traces and logs would be enough, they would have to actually go and implement the entire metrics pipeline before the Android can, you know, can try to use this. So the benefit on that side would be, like, way down the road, but not immediate at all.
And then they could consider, like, you know, messaging the agent and going 2.0 or something like that.
So, the benefit is there, but it's gonna take longer than expected.
The, the second thing is we were thinking about cross-compatibility, Jack, and this is, an important one, and basically they said that how this would compile is that Currently, at this moment, Going with this platform, I really expect that you will have platform-specific stuff, and they have this mechanism called actual… Expected and Action, which is kind of an interface style where you go ahead and just declare… well, I don't know if we have some pictures here.
But, I think it's in the next section where they mentions, yeah, this is how they exercise that, but basically you have Your common, you know, section of the code, and then you have a separate module where you're abstracting platform-specific stuff.
And the idea is that So, for Android multiplatform, the dream, most of the time, is that everything is in this section, in the common.
one. But very often, there are things that you can access for platform-specific stuff, and then you have a module, or a separate section at the very least, where you can actually go and do other stuff. And this is how we would… how Kotlink would be importing, eventually, the Android agent, platform-specific, you know, answering this case for them. So this is something that is taken care of, so to speak, it's something that Code the multi-platform provides, so we are good on that regard, I think.
Other than that, yeah, you can go and take a look at the actual examples there. Oh, by the way, yeah, there's a… well, this is not a big example of how they are doing themselves, you know? This is how you are doing that. But yeah, Joshua was mentioning the last week, also Gradle helps, you know, doing this kind of source sets, differentiation.
Okay, so, yeah, the last thing, remember, where was he putting that? Oh, yeah, that's… that's for the… you may… yeah, Tigran, you were not here, but we were, talking between us that, given that this new SDK and how it can be problematic to bootstrap and all that.
We would require a TC, sponsor at the guidance level, at least, you know? So I think, hope that makes sense.
And finally, one important, interesting thing… well, it's not important, but very interesting is that Empreys mentioned that they are using this SDK in production at the moment.
So, So this is a good thing that I chose it's a good signal. It still needs some messaging to make sure that they properly implement the specification, test more the Java part, probably, and then, of course, implement metrics. And implement other stuff, like, for example, sampling, which they don't.
Do we have any comments other than this?
**Tigran Najaryan** 13:22 It's most… mostly the same as we had the week before the last one, so… I'm fine with this approach. Seems like the bit that we're missing is the sponsor. Have we decided on that?
**Carlos Alberto Cortez** 13:34 Yep.
I could be… I offer myself, you know, I'm still around. yeah, I think it will be around until at least for a couple more months. After that, I'm not sure. I'm considering some options.
I may stay, I may not stay, so that's the only problem. Like, I would be more happy to be, like, let's say, December, January, February, probably.
After that, I'm not sure.
So, I could be totally on board on being the, the TC sponsor at the guidance level.
**Tigran Najaryan** 14:14 Okay, I guess it would be… Probably useful to try to understand what The team's timeline would be, if they are… Happy with doing all this work in the next… Three months, as you said.
And she'll be fine.
**Carlos Alberto Cortez** 14:30 Yeah, Yeah, I think that… well, they were saying that to, well, this is, of course, a very, passual, or I don't know how to call it, but, like, the estimate is not, like, very serious, that a couple of months to finish what Auretics is without taking into account metrics. Metrics is, you know, its own beast, so to speak.
So, yeah, I think that at least that would be a good start, trying to, you know, and which is also my recommendation, that they finish what they have now, which is traces and met… and logs, sorry.
Realistically speaking, I don't know whether 3 months is enough, especially that December is, you know, I think people will be working half month, most likely.
We'll get started.
**Tigran Najaryan** 15:19 I think it's okay, Carlos. If you… if you stay, then you can obviously continue. If you decide not to stay, then… And the project is not… In a shape where it… if it's in a shape that it still needs a sponsor, we can find somebody else, right?
**Carlos Alberto Cortez** 15:36 Yeah.
Yeah, hopefully by then, if there's no progress, and it should be.
there should be enough progress by then. I can provide some of the feedback that I can, you know, that I… that I can give.
And, you know, information, and hopefully, at least as I said before, at least two signals would be stable, you know, by then.
**Tigran Najaryan** 15:57 Yeah, unless we already have someone else who wants to take it over from the beginning, I don't know if we have.
**Carlos Alberto Cortez** 16:04 Yep.
So, if that's all, then I will pass that back to the… to the GC with our observation. I think that, for me, the biggest question besides the GC sponsorship level was what, whether We should provide, like, these requirements as requirements, or things that should be done right after we accept the donation.
You know, especially the first one, like, validating that the API plus the interop layer, which uses the Java SDK behind the scenes, is something that they should, should be required prior to the donation, or if you don't, as the first step, once these donations have been accepted.
If we don't have an opinion.
**Jack Berg** 17:02 we can just let the GC decide on us. I know that if.
**Carlos Alberto Cortez** 17:06 Some of them have an opinion that this should be done after the initial, like, right after, like, the first step.
Yeah, that's what I know. Some of them.
**Jack Berg** 17:16 I mean, I sort of… I sort of did a cursory pass at this and found that there was a bunch of things that weren't conforming to the specs. So, like, you know.
But we write that off as, you know, just work that needs to be done still, so that's fine. And so, what is this question? So, for the work that does exist, is the API structured in a way that reflects the spec?
**Carlos Alberto Cortez** 17:45 It is, but, so there's… I mean, I don't know if I'm answering your question, but I can provide an example.
Like, a lot of the SDK-level interfaces exist at the API at this moment.
So, there's implementation there, but the interfaces themselves, like, is, like, readable span there in the EPA.
**Jack Berg** 18:07 Yeah.
**Carlos Alberto Cortez** 18:07 How do we move around.
**Jack Berg** 18:08 I think I remember that, yeah. Goofy stuff like that.
**Carlos Alberto Cortez** 18:13 Yeah, well, there's implementation there, so it should be fine, I would guess.
**Jack Berg** 18:17 I guess, like.
I don't… I don't know for certain that any languages other than the ones that I've been a maintainer on, Java, you know, are… adhere to the spec strictly, right? So, like, I guess… Is this setting the bar higher than we have set for other languages?
**Carlos Alberto Cortez** 18:40 Right.
**Jack Berg** 18:42 We have the TC review process, where the TC can come and, you know, review your API or your SDK prior to stabilizing. We don't do that very often, or at least we haven't done it very often recently. You know, I think that should be on the table, but, I would guess that there's examples of Languages going stable without doing that review process.
**Carlos Alberto Cortez** 19:13 Yeah, actually, that could be… sorry, Lamila will make a good comment, but yeah, the idea would be, like, we accept the nomination, for example, and there are no releases at all, once this is accepted, until they're having a proper tissue review, and, you know, everything we're satisfied with.
So that could be, like, principal requirements.
**Jack Berg** 19:32 Yeah, and I understand, and I guess, I guess thanks for saying that very clearly, but, I'm not… I'm not set on that, because that seems stricter than what we have, what we've done in the past. Like, if we're thinking about this not as a donation, but as a new greenfield language implementation.
We haven't set those types of strict requirements.
**Liudmila Molkova** 20:00 It would make sense to ask For the compliance before donation happens, if we see a significant risk that people would donate and disappear?
Is it the case here?
**Jack Berg** 20:17 I think if they donate and disappear, we have to scrap this project.
**Carlos Alberto Cortez** 20:21 Yep.
**Jack Berg** 20:22 Right? So, like, we've talked recently about finishing what we start. Like, you know, if ideas are proposed at the spec, and they stay in development forever, that's probably a signal that, like, we should review them and delete them. And I think there's a similar thing going on here. So they're setting sort of ambitious goals for this, and, you know, we should… I guess, assume the best, that they're going to be able to deliver on these goals. But if they kind of ghost it, then we're kind of back to where we are today, which is the Android project being built on top of the Java SDK, and, you know, limitations, like the key limitation being no support for Kotlin multiplatform.
**Carlos Alberto Cortez** 21:06 Yeah, I do agree on that. I think that if that happens, well, sorry, like, we are just scrapping the project, you know?
**Jack Berg** 21:13 Yeah, I mean, we can solicit other people to come and take it over and pick it up. We can try that, but… Yeah, I wouldn't have a lot of.
**Carlos Alberto Cortez** 21:22 Yeah, there's, there's… Yeah, there's a lot of interest by people in the issue that embrace open, but we will have to go and see. Very often, you know, in open source, people are excited because they want to collaborate, but… like, are they actually going to put enough cycles? Like, it's not the same big, like, you know.
somebody who contributes for a feature randomly than being an actual maintainer. But yeah, we would have to see that. And the GC is aware of that, I think.
**Jack Berg** 21:50 Right, the difference being, maintainer is like a job, like a full-time job, and contributing is something you can do part-time, or, you know, you can moonlight, you can do it after work.
**Carlos Alberto Cortez** 22:02 Yup.
**Jack Berg** 22:13 So I would relax this to, like, this is… I guess I wouldn't make this language, like, normative. Like, no releases are allowed until the TC does a review of the API and SDK for spec compliance. This would be something that they can strive for, but they should have, I guess, autonomy to figure out how to proceed forward.
just says we've given autonomy to other language SIGs.
**Carlos Alberto Cortez** 22:45 Yeah, I agree with that.
So, since I hear silence, I guess I will go ahead and scrap this part, just say that this will be a priority after this is donated, and yes, like.
An important requirement after donation is that they don't do any release until the TC, which will… it does not be part of the DC, guidance part, like… and probably have even somebody else from the TC, I don't know if it's too much, like, somebody else from the TC to have two reviews, let's say.
If we are too concerned. But anyway, we can state that in the future.
Okay, in that case, if that makes sense, I will just, massage the doc, pass it to the GC later today, so they can make a call.
**Liudmila Molkova** 23:48 Thank you.
**Carlos Alberto Cortez** 23:50 Perfect.
Yeah, thank you for the comments, by the way, that's, yeah, you know, trying to see the angles that you'd see.
And that's all from my side today.
**Armin (Dynatrace)** 24:04 Thanks. Riley, do you want to go ahead with this topic?
**Reiley** 24:07 I have a really quick ask, so, In our previous meeting, we talked about stability.
And we have different understanding of what stability is, so I put a list of concrete questions to… see if we can align on that. So I saw feedback from Josh, haven't seen feedback from the rest of the TC members.
Take a look and reply to the Slack channel.
That's all.
**Tigran Najaryan** 24:52 Okay, looks like we're done for today.
**Armin (Dynatrace)** 24:56 Yep, no more last-minute topics.
**Tigran Najaryan** 24:59 Thank you, guys.
**Armin (Dynatrace)** 25:00 Alright, that's a lot of anything.
**Carlos Alberto Cortez** 25:02 Yep. So…
