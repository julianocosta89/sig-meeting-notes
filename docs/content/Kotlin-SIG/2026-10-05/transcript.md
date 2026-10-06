SIG: Kotlin SIG
Date: 2026-10-05
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Viorel Alexandrescu** 00:56 Hello!
**Jamie Lynch (Palo Alto Networks)** 00:58 I will.
Everyone feel free to add to the agenda now that it's actually going on the doc.
And we can give it a couple of minutes, because I know… Couple of people said they'd be, a few minutes late hanging out.
**Viorel Alexandrescu** 02:00 We have Hansen and Carlos, so there will be a couple of minutes late.
**Jamie Lynch (Palo Alto Networks)** 03:49 We could probably make a start if you want.
And I think it's, yeah, it's basically… Close to five minutes in. We can jump to discussing yours very well, if you want.
**Viorel Alexandrescu** 04:06 Right, so regarding the progress on this, right now I still have a few more changes to add to the file export functionality for log record and SPAN data. As you said, there's an issue with the CI at the moment, and I think it's regarding Test coverage, but there's also a question you left on the PR that I responded, so… I need some input on that as well, and in the meantime, I started working on the… Hold on, there's an issue. Yeah, on the OTLP HTTP JSON protobuf support, it's number 41. I saw you… You mentioned me in a discussion about it.
But I've had some issue building the project locally, and because of that, I couldn't use the Protobuf models to actually start working and… That took… that's gonna take a while.
**Jamie Lynch (Palo Alto Networks)** 05:15 Got it. Okay.
So, I think, skipping back to the first PR, did you… What needed clarifying on that? Do you need…
**Viorel Alexandrescu** 05:28 You were saying something that I initialized it with the default black hole sync, which basically is a no op.
**Jamie Lynch (Palo Alto Networks)** 05:35 And this one?
**Viorel Alexandrescu** 05:37 And, At that time, I just thought it would have been just a good default.
**Jamie Lynch (Palo Alto Networks)** 05:49 Got it, yeah.
So my understanding of Black Hole Sync is it basically just kind of ignores everything.
So.
I think… a reasonable approach here would be to maybe, like, inject the black… the sync, and then we could, like, default it to the black hole sync. I don't think this is actually… Hooked up to anything yet.
Goodbye-bye.
**Viorel Alexandrescu** 06:19 Okay.
If you have the time, put that in words, please, on the PR, so I can come back to it in case I… in case it slips my mind, but I think I get it.
Yeah, that's perfect, thank you.
**Jamie Lynch (Palo Alto Networks)** 06:45 Okay, cool. I guess I can just kind of, do you think this is in like a state where it can be reviewed as well? I can take a general look at it if that would be helpful at this stage.
**Viorel Alexandrescu** 06:59 Yeah, I mean, having a look over the changes would be… would be helpful, because there's only a couple of more things to tackle, and it's pretty much out of the way.
**Jamie Lynch (Palo Alto Networks)** 07:07 Sure. Okay.
**Viorel Alexandrescu** 07:09 anyone.
**Jamie Lynch (Palo Alto Networks)** 07:10 I'll have to note to have a general look at it.
**Viorel Alexandrescu** 07:22 I'm curious, now that we're here, is there any way to actually view what tests are failing in a pipeline? Because most of the time, I just keep scrolling through the logs.
To find out what's wrong.
**Jamie Lynch (Palo Alto Networks)** 07:39 Yeah, I mean, I think the view should be pretty much the same for everyone, but.
Yeah, so in this case, it looks like it's immediately failing on detect.
So, it'll tell you that analysis failed with reissues, but yeah, it can get pretty.
verbose with Gradle. But, yeah, this is better.
It's just complaining about, files ending on a new line, so that should be…
**Viorel Alexandrescu** 08:12 I'll get that fixed.
**Jamie Lynch (Palo Alto Networks)** 08:13 Yeah.
**Viorel Alexandrescu** 08:14 But I was curious if there's any like specific menu that can show you like failing unit tests, you know, like you can see in GitLab, which.
**Jamie Lynch (Palo Alto Networks)** 08:22 Hmm.
**Viorel Alexandrescu** 08:22 See the test suit?
**Jamie Lynch (Palo Alto Networks)** 08:28 Yeah, that… Really does feel like… GitHub should have that action. I'm not… Aware of any built-in functionality for that, which is kind of crazy.
Yeah, I know.
Yeah, I generally just tend to search for logs.
**DavidGrath** 08:52 We could could indirectly do that. I'm not sure.
**Jamie Lynch (Palo Alto Networks)** 08:58 What was that, sorry?
**DavidGrath** 09:00 So we could come indirectly cover that case. I'm not sure.
**Jamie Lynch (Palo Alto Networks)** 09:12 Sorry, I can't really catch that.
**Viorel Alexandrescu** 09:16 Yeah, me neither.
**DavidGrath** 09:19 Got typed it.
**Jamie Lynch (Palo Alto Networks)** 09:21 Sure, that'd be helpful.
Oh, CodeGov.
Yeah, that'll definitely… I have some sort of indication if… Those failing tests.
I think I will, but… Yeah, actually, it won't, because, code coverage.
CodeGov only runs once the unit tests have finished, I think, or at least the way we've configured it.
So… did you require any discussion on the… Issue number 41.
Or were you pretty happy to kind of go ahead with that?
**Viorel Alexandrescu** 10:08 What do you mean?
**Jamie Lynch (Palo Alto Networks)** 10:11 So there was this PR, which I can take a look at, and you said you'd kind of moved on to…
**Viorel Alexandrescu** 10:18 Yeah, yeah, yeah.
**Jamie Lynch (Palo Alto Networks)** 10:19 Oh, that's…
**Viorel Alexandrescu** 10:20 Yeah, regarding that, I picked it up, I picked it up again, and right now, I'm having just some local issues generating the protobuf model, which I'm supposed to use to make this bridge.
for whatever reason, Android Studio doesn't want to generate the classes from the protobuf representation, because I saw there are some files representing those models, and I just couldn't get it to work. I'll look into it further, and if there's a… if it persists, I'll leave you a message and see if I need a hand.
But, yeah, this one is, is going along okay, because now, since we have the exporters and the serializable models, modules.
Separated, I can pick those up fairly quickly and do this, implement this support.
**Jamie Lynch (Palo Alto Networks)** 11:12 Awesome. Yeah, just reach out if it does become an issue or if it kind of blocks you and I'll try and help.
**Viorel Alexandrescu** 11:19 Thanks.
**Jamie Lynch (Palo Alto Networks)** 11:24 Cool. So that's… That issue, if anyone has anything else we want to discuss, please do feel free to add items to the agenda.
So… Yeah, I had two topics myself, so… I've created a… Standalone implementation allows you to create span context objects without the use.
without requiring an OpenTelemetry SDK instance.
So I think this is one of the things that, Carlos, you, asking for and your feedback on how the publication API works.
So… Basically, right now…
**Carlos Alberto Cortez (Dash0)** 12:12 Sorry, go ahead, sorry.
**Jamie Lynch (Palo Alto Networks)** 12:15 Yeah, I was just gonna say I basically just created placeholders, and it's just function signatures at the moment. So, like, there's a function, like, create invalid spam context and create spam context.
So… I think… I guess maybe if I tag you as a reviewer, and I can add a bit more context on the PR description, if that would help.
**Carlos Alberto Cortez (Dash0)** 12:44 Yeah, I took a quick look at it, it looks good, I just need to go over details, but overall, the design is the right way.
**Jamie Lynch (Palo Alto Networks)** 12:52 Hmm.
**Carlos Alberto Cortez (Dash0)** 12:53 No.
**Jamie Lynch (Palo Alto Networks)** 12:55 Okay.
Cool. I will… Kind of press ahead with the internal changes.
needed to support.
I'm getting this to be reality rather than just a to-do.
Cool. And then the other thing.
is… it's been about 3 weeks since we shipped, so I was probably going to… ship a release sometime this week, probably towards the end, so that Jason is back and we can Kind of coordinate if anything needs to go in.
Cool.
That's all I had. Did anyone else have anything they wanted to discuss while we're all here?
Okay.
Or we can leave it there, Ben, and everyone gets a bit of time back.
Thanks, everyone.
**Viorel Alexandrescu** 14:13 Have a good one.
**Carlos Alberto Cortez (Dash0)** 14:15 Ciao.
