SIG: Java SIG
Date: 2026-05-14
Duration: 59 minutes
Zoom Recording URL: https://zoom.us/rec/share/Zp7655RuE7K1YSgLvg43CRRUot3yKAO0Qr5RYK94Vm3R-4gB29P2_Sl1ulnLRhj4.ozrTHjz8HCsx13Fh
============================================================

## Zoom Recording Transcript

**Steve Rao** 02:06 Hi.
How you trust?
**Trask Stalnaker** 02:11 Hey, Steve!
Ayy.
How are you doing?
Did I freeze?
Gmail… Can you hear me?
Not sure if I'm frozen or if Steve is frozen.
Okay.
Probably Steve.
Hey!
Oh… Looks like you froze again.
Have you seen…
**Huxing Zhang** 03:11 I think there's, some bugs of, my Zoom meeting, and… every time I, open up my video, it will get stuck, so I… I… I recently, I, disabled my video. I think Steve may run into the same issue. I think he's looked stuck… gets stuck.
I don't know why, but, just, yeah.
Yeah, every time I open up the video, and they will get stuck, and they will quit.
the software… the Zoom meeting software will quit.
I'll ping, ping him.
Maybe he… he doesn't know about that.
**Trask Stalnaker** 04:38 Oh no, now I have frozen.
Oh, there.
I froze for a second.
**Huxing Zhang** 04:46 It's a difficult day.
**Trask Stalnaker** 04:49 for the, computers.
**Huxing Zhang** 04:52 Yeah.
I heard that you have put a lot of effort in the GNI segue right now. Is that true?
**Trask Stalnaker** 05:25 Yeah, yeah.
It's been… Fun to see, Ming, Wei, and Steve over there, also.
**Huxing Zhang** 05:36 Yeah.
**Steve Rao** 05:39 Yeah, I'm okay, sorry, there is something about my internet. I will join, it's okay, no.
**Trask Stalnaker** 05:46 Cool.
**Steve Rao** 05:53 Yeah, at least our issue, wrong agenda today.
**Trask Stalnaker** 06:00 Cool, I'll pull it up… Alright. Yes!
**Steve Rao** 06:20 Yeah. Yeah, the first thing is, Yeah, I want to discard is about the GNIU tier, module, in Java instrumentation for users.
yeah, I add some, class in Instrumentation API incubator.
And, yeah, I found, in Python contribute.
Yeah, there is a tool called the JNIU tier for users. There is a, individual, dependency for users. They can use it to develop their instrumentation.
Yeah, even, even though in Java there isn't so many, AI agent instrumentation so far, but, yeah, maybe, I guess, it will be different in the future. And, yeah, my question is, it's necessary for us to provide a similar individual dependency for our user in Java instrumentation or not.
And, the second question is, how we… how do we provide the, independency for user in Java instrumentation? Such as, individual dependency, like, in, Python country, like, JNIU tier, or something like, instrumentation API incubator, like, like so far.
**Trask Stalnaker** 07:55 Sure, let's start with the first question.
This is definitely the right approach in this repo.
so, yeah, this would be great. To… get in.
I didn't quite follow your second question about Yeah, maybe you can repeat your second question.
**Steve Rao** 08:23 The second question is, format for, for, user.
How do we provide the, GenIU tier dependency for users?
in Java instrumentation.
**Trask Stalnaker** 08:38 I see.
**Steve Rao** 08:39 Yeah, yeah, in Python.
**Trask Stalnaker** 08:43 Yeah, okay, I think I understand where you're coming from.
So, in the other… semantic conventions.
We're… we generally expect the instrumentations, and our instrumentation IPI is for… We don't expect it to be… really widely used, because there's only so many… HTTP libraries out there, so many database libraries. Even if everybody used… had native instrumentation and did this.
They could use this.
I think what… I think what you're getting at, is that in Gen AI, There's probably going to be a lot more need for users to… add custom Gen AI instrumentation, because the hooks, the library hooks, aren't really… Good enough to do the generically… to generically capture everything that a lot of users will want.
**Steve Rao** 10:06 Yes.
**Trask Stalnaker** 10:06 Or they'll want to enhance their experience with, like, things that aren't captured, like, they'll want to give their own agent name, or their own, different pieces of that.
So, not something we've thought about in Java.
I'm not sure that, Yeah, we'd have to think more, I think… what I've been hoping for the instrumentation API in general, because it's kind of… I don't want to say it's heavyweight, but it's… not simple. It's a little complicated, like, it's not… the best… API for… and it's not the simplest API for end users.
And… what I… like, we have this semantic conventions constants artifact.
But really what we would like to do, using Weaver.
is to generate more things for conventions, semantic conventions, using Weaver.
So… We could improve, you know, either the existing semantic conventions, constants, artifact, Or add new artifacts.
That are, like, create this spam, create, invoke workflow… GenAI workflow span, and it would have, like, hard-coded some parameters that you would need to pass in for the required parameters, and it would just be… very simple, it wouldn't have, you know, all the features of the instrumentation API.
But it would be kind of a simple… a little bit above the Using the low-level, the raw OpenTelemetry API, plus the constants.
But today, we just have the… Semantic, the… I mean, yeah.
We don't have that today.
**Steve Rao** 12:21 Okay.
Okay, yeah, yeah, you mean, yeah, maybe in Java, instrumentation, we add related class, UTL class in, Instrumentation API incubator, or Instrumentation API module is, It's a… a good.
**Trask Stalnaker** 12:42 So, I don't… I… I… There's not really a good place for it in this… repo. Like, this is the best way to go in this repo, and we should use the instrumentation API when we write instrumentation.
**Steve Rao** 13:01 Yeah.
**Trask Stalnaker** 13:02 Because we get all of the… I mean, all of the goodies that that comes with.
But if we're looking for something simpler for users.
**Steve Rao** 13:12 Hmm.
**Trask Stalnaker** 13:13 What I would point users to today is just… Right? The constants, like, if they want to set The agent name, they can use this constant, for example.
One… So, another option… the place I would explore that is over here.
Somebody was just doing this in… they were just in the Java Slack channel.
Doing this for metric attributes.
Let me see if I can find… I think they had a… Just put up a PR today… They did, yes, yes. Oh, it's here.
Alright, 11 hours ago.
So, they're introducing… Metrics, constants for metric names.
So… This would be kind of the area to explore, would be adding something for, like.
create span.
**Steve Rao** 14:35 Hmm.
**Trask Stalnaker** 14:36 API that would be auto-generated by Weaver And it would just be, like, super… Simple.
**Steve Rao** 14:45 Okay, okay, makes sense.
**Trask Stalnaker** 14:46 Yeah, Huxing, this repo is all generated by Weaver.
**Huxing Zhang** 14:53 Oh, okay.
So, actually, I have… I agree with Trask, and I think that the code shouldn't go into the instrumentation API, because I think another format is, like, you provide a… Dependency, extra dependency, that the, instrumentation Can depend on, and, it's, like, a third-party dependency that, wrap… wrap up the code there and provide a convenient way for the instrumentation code to add, to create, to, to, to create a, like, easier way to create a, create a span, like, invoke agent, and… Some sort of things like that.
It should not be directly going to the instrumentation API code.
**Trask Stalnaker** 15:45 Yeah, so, Steve, I think what would help is maybe start with the… come up with the specific use cases that customers want to do that we're trying to simplify.
**Steve Rao** 16:03 Yeah, they want to, custom their… They… maybe they don't want to use, Java instrumentation directly. They want to, use, the library.
to, instrument, instrument their own application. But, I found in Java, they can't use the, core report to do these things, because we, we just, provide some, low-layer API for user to create spam.
or a close spend in Java SDK.
But, we don't provide some, JNIU tiers for they to, add some, attributes, according to the latest, generalized semantic collection.
**Trask Stalnaker** 16:59 But how is that different than using the… I mean… I agree there could be more convenience on top of it.
But they… they can do it today, right, using the OpenTelemetry API plus these constants.
**Steve Rao** 17:21 Okay, but they need to understand the semantic convention, like, semantic convention, and know, where to add this attribute, and where to add another attribute, if we can.
**Trask Stalnaker** 17:34 I see, so which spans… which attributes are applicable to which spans?
**Steve Rao** 17:39 Yeah.
**Trask Stalnaker** 17:44 Makes sense.
And… Yeah, I mean, I think that would be a really good thing to explore with code generating from Weaver, and would be something that, you know, like the… You know, it's more ambitious than just adding these metric name constants.
But it's an idea, it's something that we've talked about for years.
I think there's general agreement that we want.
For all languages, we want that kind of a thing, where we would generate, like, a span class, and the span class would have, like, setters for all of those attributes that were relevant to it.
**Steve Rao** 18:37 Oh, okay.
**Trask Stalnaker** 18:41 And that could be auto-generated with Weaver.
**Steve Rao** 18:46 Yeah, yeah, it can do it, it's good.
**Trask Stalnaker** 18:50 Yeah.
And then it will be what I… The reason I… I… we have… since we already have the… the full-blown instrumentation API.
I… Don't want, like, another… it's already confusing with the instrumentation API and the open telemetry, like, we've got a couple different layers, so I… I don't really want to add another layer of at least hand Written hand code, like, something, but this sort of auto-generated, really straightforward, simple, like, wrapper around these semantic conventions.
I think is a great… I think that would be beneficial for a lot of the semantic conventions, and we could point people to that as a much simpler alternative to the instrumentation API.
I almost feel like the instrumentation API you know, It's great for this repository.
But I'm not sure that it's… the right… thing for end users, but I do think, like, a simplified span wrapper thing.
**Steve Rao** 20:09 Yeah, yes.
**Trask Stalnaker** 20:10 Be very nice for end users.
**Steve Rao** 20:13 Yes, yes. Yeah, maybe, in Java instrumentation, we add, all kinds of semantic convention, API in instrumentation API incubator or instrumentation API.
Yeah, we…
**Trask Stalnaker** 20:29 Dude, what? Sorry.
**Steve Rao** 20:30 We, come out, all kinds of different, semantic conventions, like, RBC database and the GNI, in instrumentation API or Instrumentation API incubator so far in Java repository. Yeah, maybe another option, we can, yeah, split, API to different layers.
Yeah, maybe… I guess maybe it will be better for users if they just want to instrumentation their own GNI application. They just need to add only one.
**Trask Stalnaker** 21:19 Yeah, and I think this is the one that I would… Focus on. This is where… this is the repository.
Where we would want to explore Those, sort of, auto… the weaver-generated… Simple, simple wrappers around semantic conventions.
And we may or may not use them in… the instrumentation repo, But that's… fine. I think they still have a lot of value for end users.
**Steve Rao** 21:58 Yeah, okay.
Yeah, so you, you will, bring this, topic to, discuss with, we were team in, community.
**Trask Stalnaker** 22:14 We've talked about it, multiple times. There's… there's general agreement, just some… nobody's done it, so…
**Steve Rao** 22:21 Okay.
**Trask Stalnaker** 22:22 I'm… I'm… I'm… I'm… I'm leave… I'm basically saying this is a… This is a fairly fairly approved.
Forward.
Obviously we have to, you know, work through all the details.
But it's just basically waiting for somebody like you, who wants to… Pick up the project.
**Steve Rao** 22:48 Maybe, yeah, yeah, in the future, yeah, I can explore something like that, yeah, if I have time.
**Trask Stalnaker** 23:03 Yeah, I mean, I know there's been other interests on, you know, maybe somebody else will pick it up at some point, but we've been talking about it for a while, and nobody has picked it up, so…
**Steve Rao** 23:14 Okay.
Yeah, okay, yeah, this season, my first.
**Trask Stalnaker** 23:20 GenAI… GenAI is a good… I think that's a particularly good use case from what I've seen for, from users.
**Huxing Zhang** 23:30 Trask, I want to add some additional comments, from Python side. I think, looking at the, Python Country repo, there's, like, folder or directory that… hosts the Jenga UTOs there, they host there, and they have… they have separate distribution.
If we do release… they do release this every, like, couple of weeks. This is the… the… this is the project that we want to… we want in Java as well, because this simplifies the user, that they can directly depend on this, UTOs and, quickly built the… JNI… either their JNI instrumentations, but not auto-instruments, and they can… they can do in their code, and… by… depending on these UTLs. And if you're looking at the release notes of theirs, they have different release cycle with the… Entire… entire project, so they can quickly evolve.
I don't know if there is some better place to host this kind of code in Java, so maybe… what I'm thinking is we… maybe we want… from my side, we… we can provide similar utility as… Python country.
**Trask Stalnaker** 25:08 So, talk to me… tell me more about why you don't want to build the same functionality into… basically moving this PR forwards.
**Huxing Zhang** 25:27 Yeah, I don't think this is a right place to place this under Instrumentation API, because this is not about instrumentation. It's actually as, I think it's a… simple dependency, simple wrapper, I think, actually, simple wrapper of the semantic convention.
how to… how to provide the way for developer to build easier… easily build the… the… the GNI spans. Just a… a wrapper based on your… your… you are saying the OTL SDK+, some attribute.
So, this is… should… this should not be placed under the instrumentation, but somewhere. Not… not only the Java instrumentation can depend on that, users can… Directly depend on that to write code.
Yeah, as well. I mean, you…
**Trask Stalnaker** 26:27 Users can directly depend on the instrumentation API.
**Steve Rao** 26:32 Mmm… Yeah, yes, yes.
But, I got…
**Huxing Zhang** 26:37 But I don't think it's, it should be placed on the instrumentation API, because it's not… nothing to do with the instrumentation. It's… it's a SDK, just the wrapper.
**Trask Stalnaker** 26:49 But it is instrumentation, it's users' instrumentation. It's their… they're instrumenting their app.
**Huxing Zhang** 26:59 this is, Java instrumentation, right? If your user use SDK, they… they can choose OTL SDK and another They cannot… they don't, what'd I say?
I think they… Can directly, it's like, for them, for them, it's like, just a third-party dependency.
It's something, like, you can look for in Maven Ripple.
You can just add that to your…
**Trask Stalnaker** 27:32 Right, isn't… isn't that what Instrumentation API is, though?
I guess I'm… I'm…
**Huxing Zhang** 27:42 But I don't think the instrument… it belongs to an instrumentation API.
**Steve Rao** 27:50 okay, yeah, Huxi, you mean, you have some concerts about, module name, Instrumentation API.
Or… Yeah, currently, current solution in Java, scenarios is, they, if a user, they want to instrument their AI agent application, they need to add, hotel Java SDK, and they also need to add an instrumentation API incubator.
dependency in their application, and they can use, a class provided by this PR, and they can, use it to, instrument their JRI application. They don't need to care about, detail of, JNI semantic commission. You have concern about, a dependency in NAN, so that, yeah, maybe, we can rename to, we can, split the, dependency to different layer… different U-tiers, like in Python.
Right.
**Huxing Zhang** 29:08 Yeah, so what I'm concerned about is how do your users see The dependency name, the name of the… if you are looking for, JNI UTOs, how do we see… actually, for example, if we provide a Maven dependency to users, what does that look like?
when they are writing code. If they are adding some instrumentation to their agent manually, how they see that?
**Trask Stalnaker** 29:44 This is the Maven dependency that they would use.
**Steve Rao** 29:47 Yeah.
**Huxing Zhang** 29:50 Hmm… Okay, But actually, that's not what I'm thinking about, but if this is the right… this is the… this is the case, and maybe I'll… check it out later, and I think… Yeah.
But, to my point of view, I would like something like.
OpenTelemetry, Jingai, Java, sort of things like that.
Java UTLs, OpenTelemetry, Jenna UTLs.
dash Java, some sort of, like, like that.
**Trask Stalnaker** 30:35 Okay, so it… I just want to understand the reasons, right? I'm not saying that it's not a good idea, or it is a good idea, but is the only concern you have the name? Like, if we renamed this package to GenAI Utils?
**Huxing Zhang** 30:55 Yeah, yeah, yeah, it would be… it should be easier for users to understand, I think. Yeah, OpenTelements, UTLs, Java, some sort of level, like that.
**Trask Stalnaker** 31:06 I'm… Where do you, I mean, is it something that… is it just a documentation problem?
I'm wondering why users even would expect to find something called GenAI Utils?
Except that if they're coming from, I guess, from Python?
**Huxing Zhang** 31:29 I think users, they are coming not from OpenTelemetry, but coming from some… writing some agent, but without their knowledge of knowing how… how does the OpenTelemetry organized.
So, what I… to their point, they… they have an agent. They write an agent without any… maybe they… they… they do, write their own agent without any framework. They read some Java code, and they want… they're looking for some, SDKs to, like, to implement the Gen AI GNI UTLs, GNI semantic conventions.
So they are looking for some UTO tools for there to, like, to… Easily build the JNI semantic commission implementation.
**Trask Stalnaker** 32:26 Yeah.
**Huxing Zhang** 32:27 Yeah.
**Trask Stalnaker** 32:28 So, maybe it's just… I mean, do we just need a new page here in the docs?
About how to do that.
Like, I guess so… What I want to differentiate is… Is this a problem?
Like, do we have the… pieces Already, and it's just a discovery problem?
Or is there more than that?
**Huxing Zhang** 33:00 Hmm… I'm… actually, I've… I… I'm not sure about that.
But, from my… instinct, the… some… Seems not sure.
**Trask Stalnaker** 33:13 me to share this?
**Steve Rao** 33:14 Yeah, I, I share this, document, documentation. Yeah, maybe this is, provided by, Gen AI, Sikh.
Oh, God.
Yeah.
That is, designed for Jane IUT, Yeah, and, yeah, maybe, this is a concept JNIU tiers, provide by then. So, I guess, yeah, for Hu Xin, yeah, maybe, he wants to follow this, concept for users in Java,
**Trask Stalnaker** 33:51 I see.
**Steve Rao** 33:53 What's for you.
**Trask Stalnaker** 33:53 So that's… I mean, that's a different angle that we could… approach this is… If we can get the, you know, in the GenAI SIG to write, basically, a specification.
for a Gen AI Utils package.
And say that languages should implement that.
Then that would… Sort of automatically open that door.
**Huxing Zhang** 34:26 Yeah.
I assume that's the… the… Let go, I want to move forward, yeah.
**Trask Stalnaker** 34:35 Yeah, if we get, I mean, yes, if we… if the GenAI SIG you know.
Puts together, you know, blesses a spec.
And says that this should be implemented.
Yeah, in all languages.
Then we would, you know, certainly… implement that in Java, and I think that that makes a lot of sense to me, kind of from what Your… it sounds like that's sort of where your perspective is.
also, like, having seen the Python one, it's like, oh, well, now, how do I do the same thing in Java?
**Huxing Zhang** 35:21 Yeah.
**Trask Stalnaker** 35:25 That would also give us a… A good place to kind of discuss the pros and cons of what can we weaver generate versus what kind of pieces, because I doubt that all of this, just from looking at the Python you know, not all of this can be Weaver-generated, like.
**Huxing Zhang** 35:47 Yeah, I think so.
**Trask Stalnaker** 35:47 Environment variable stuff, and there's some other stuff, so… Yeah, yeah, let's do that, let's… let's… Try to… And maybe you could even start that off… where would that live?
So we have the… Semantic Conventions, Gen AI repo, but that's Semantic Conventions.
We have open telemetry specification… We tried at one point, Yeah, that's probably not gonna work here. We did try… Know where it went. Oh, it never landed. Okay, so it's in the… OTAPS… It's in the old OTEPs.
there was an instrumentation API Proposal across languages.
But that wasn't really… but this… in this case, it's very specific to Gen AI.
**Huxing Zhang** 37:09 Yeah.
**Trask Stalnaker** 37:20 I certainly…
**Huxing Zhang** 37:21 This was discussed previously, I… I don't… I don't… I don't know that… Whether there is, already a proposal or not, but if not, I, I can actually, I can propose, Something… If you want to… Yeah.
**Trask Stalnaker** 37:40 Yeah, yeah, definitely, that would be great. I… I mean, it… This… I'm curious if this was… Yeah, this looks like it was… is very… I mean, was… built around the idea of Python, but… Certainly looks very extensible to other languages.
**Huxing Zhang** 38:04 Right.
**Trask Stalnaker** 38:05 The… the one question I'm trying to answer for myself, is where… where to propose it. Like, there's… I mean, the GenAI SIG, for sure.
But what repository would it actually be?
11.
**Huxing Zhang** 38:29 maybe the JDNI repository first.
**Trask Stalnaker** 38:34 I think this is the… this is the repository where it would… have to… land…
**Huxing Zhang** 38:41 Yeah.
**Trask Stalnaker** 38:43 Which… I mean, I think it's good. I think… It makes sense to me here. This is… it's basically… it's a little outside of what we typically think of as semantic conventions.
But… I think that's okay.
at least it gives us a place, a repo to target, and then we can gather feedback. So if you want to open an issue here.
That would be great.
**Huxing Zhang** 39:13 Okay.
**Trask Stalnaker** 39:19 Cool, yeah, thanks for walking me through that.
**Steve Rao** 39:22 Yay.
Yeah, just the second, agenda is about the RPC, PR. Yeah, if you have time.
**Trask Stalnaker** 39:32 Yes, yes.
**Steve Rao** 39:33 Definitely have me to, take a look at it, yeah.
**Trask Stalnaker** 39:37 Yeah, cool, it is large, but, it seems like in pretty good shape.
So… Yeah.
I think, I mean, I've run all the automatic stuff that I can against it, and, like, everything is looking pretty conformant.
So, I think it just is gonna require, now, still have to, do the human… Review of everything, and it's kind of big, so…
**Steve Rao** 40:24 What the…
**Trask Stalnaker** 40:25 bomb.
Yeah.
I will, so it… we have, if you haven't seen, we have this pull request dashboard.
**Steve Rao** 40:36 Is that… yeah, it's very…
**Trask Stalnaker** 40:38 Yeah.
And so, it's good, right?
It's at the top of the list. It's been waiting for… on approvers for the longest number of days.
So this is good, just leave it.
Leave it be.
And it will, as it accumulates age, it will, you know, at some point, it will… I will both have the time, and it will bother me that we're… it's getting stale.
**Steve Rao** 41:08 Okay.
**Trask Stalnaker** 41:12 It's also, now, is it… I didn't even check, is it implementing all the new stuff?
**Steve Rao** 41:21 Yeah.
Yeah, this is, instrumentation for software IPC framework.
**Trask Stalnaker** 41:33 I mean, is it implementing all the new RPC semantic conventions?
**Steve Rao** 41:39 It's a new, RPC. Yeah, this, is a RPC framework, provided by, Ant Group is a, is a Chinese, financial company in China.
And, yeah, maybe, there are a lot of designs similar to Java, double.
**Trask Stalnaker** 42:06 Yep.
Yeah.
like I said, it looks good, I mean, just from the basics, And it's… it will be good to have another RPC implementation.
**Steve Rao** 42:26 Okay.
**Trask Stalnaker** 42:27 So, it won't make… it won't make it into this week's release, but I think we can get it into the next month's.
**Steve Rao** 42:35 Okay, yeah, yeah, it's okay.
Yeah.
I don't have more, comments.
Or… Alright.
**Trask Stalnaker** 42:48 Well, good to see you. Oh, while I have you here, for the… Do you ever go to the… Gen AI… APAC meeting.
**Steve Rao** 43:05 Yes, yeah, I will, join… Next week, right?
**Trask Stalnaker** 43:11 Next week, yeah, I was going to ask you all, And, Minhui, if an hour earlier Would work for you.
**Steve Rao** 43:31 Yeah, you… I'd like to reschedule, reschedule the, the, the, the 10.
Cool.
**Huxing Zhang** 43:38 It's, like, 8 AM in AM in China.
If we're one hour earlier, so it will be 8 a.m.
I think I… it may be difficult for me to un… to… to attend at 8 AM.
**Trask Stalnaker** 43:59 Okay.
Alright, yeah… I just wanted to explore that, in case I… can.
**Steve Rao** 44:13 Half… or half hours.
**Huxing Zhang** 44:16 How far may be possible, yeah.
**Trask Stalnaker** 44:19 Hmm.
But, sir.
Good idea.
Yeah, because just a little… a little bit earlier would help.
Possibly even this, we could… .
**Huxing Zhang** 44:39 So the… is this, summertime, you have already changed to summer?
**Trask Stalnaker** 44:47 Yes, yes, because it's based on… China standard type.
**Steve Rao** 44:56 I think maybe we can, yeah, two half hours early.
Yeah, maybe if we don't have too many agenda, each time, maybe a half hour is okay.
**Trask Stalnaker** 45:10 Yeah.
**Huxing Zhang** 45:11 Yeah, actually, talking about the GNI meeting, I actually… I, I, I saw that the meeting minutes that, you know, your JM meeting minutes, there's, quite a lot of people attending. Actually, we are very interested in attending your, the… the U.S.-based time meeting, but I'm not sure if there is, possible to schedule that meeting to, like, some time that we can.
attend directly, so we kind of have a more discussion with your guys there. And I think… I'm not sure whether there's a lot of people from the United States, or is there any people from Europe joining that meeting?
If the… if there are… most of the, are U.S.-based.
maybe there's… if we… if you can slightly change that, maybe we can join that meeting, because I see, really, a lot of people join there, and maybe… yeah.
**Trask Stalnaker** 46:23 Now, would, would… earlier?
Like, what… what would…
**Huxing Zhang** 46:29 Yeah.
**Trask Stalnaker** 46:30 work.
**Huxing Zhang** 46:31 I'm checking about the time, it's 9 AM U… how… What is, actually the U.S. space time in, in that meeting time?
**Trask Stalnaker** 46:43 It says UTC plus 8, but I think that's wrong.
**Huxing Zhang** 46:48 Yeah, that's wrong, I think that's wrong.
**Trask Stalnaker** 46:50 I think we're minus 7.
Yeah, specific… Utc… Yeah, so Central, but… Oh, we're… right now, we're not UTCA or UTC-.
**Huxing Zhang** 47:08 So what is your… what is the time when you had that meeting in your time zone? I can check the… what is the time zone.
**Trask Stalnaker** 47:17 9 AM.
So… Euro-specific, 9, you're a specific… Pdt… 9 a.m. to China…
**Huxing Zhang** 47:37 Good.
to Chinatime, yeah, you can check. It's maybe zero in the midnight.
**Trask Stalnaker** 47:45 11 PM.
**Huxing Zhang** 47:47 11 p.m.
11 p.m. Oh, that's hard.
Really challenging for us.
I mean, so we can do… Sorry.
**Trask Stalnaker** 48:03 An… an hour earlier, I don't know if that helps at all.
**Huxing Zhang** 48:09 Yeah, if you can do one hour earlier, I can join, actually.
**Steve Rao** 48:15 Yeah, me too.
**Huxing Zhang** 48:16 Or, if you had to, like, In the afternoon.
we can… we can join, maybe… we can definitely find some time, for… from both the United States and China, yeah.
**Trask Stalnaker** 48:31 Yeah, so… The challenge is that… Monday, Tuesday, and Wednesday at the hour earlier, we have semantic conventions meeting… specification meeting and GC and TC meetings.
On those two days, and so myself and Lyudmila could not make that time.
**Huxing Zhang** 48:59 Honestly.
**Trask Stalnaker** 48:59 Yes.
We could make that time… on Thursday.
Lydmil and I also generally can make A half an hour earlier even than that.
Usually we're both online around 7.30 a.m.
Pacific time.
The challenge is… Getting… the repercussions of moving it for this many people. But I will put it on the agenda.
There has a… Actually, what will I do?
Maybe I'm tall in the… Let me check with Lyudmila first, but then, probably… maybe we could put a poll… Together… in the… Slack channel.
to explore.
**Huxing Zhang** 50:15 I really appreciated that, yeah.
And, actually, yeah, we actually… we want to have more discussion with, more people there. Right.
**Trask Stalnaker** 50:30 Yeah, that would be amazing.
I would… I mean, I would love to see this happen Thursday at 8 AM, Because… It's the next most important meeting on my calendar, to get on that special 8 AM slot, and I have one of… I have one of those… we have one of those open right now.
**Huxing Zhang** 50:55 Okay.
**Trask Stalnaker** 50:56 So, yeah, well, let's see. So that… And… Another… an option there… Could be also to have a second meeting… I know it's not ideal there.
To have a second meeting, but we could potentially do 7.30 a.m.
For half an hour.
sunday a.m. is… Right.
**Huxing Zhang** 51:47 I think 7… 7.30 is, 9… It's 9… 9.30 in the night.
**Trask Stalnaker** 51:55 I think I got a bad AI answer.
**Huxing Zhang** 51:58 Yeah.
Thank you for me at the end.
**Trask Stalnaker** 52:01 Yeah. Alright. Wow. Awesome.
7.30, wait.
Maybe I got a bad AI answer before. Oh, good lord.
So what is 8 AM?
8 AM, so 8 a.m. is 11 p.m.
**Huxing Zhang** 52:22 I remember, yeah.
**Trask Stalnaker** 52:27 There's just no good time, is there?
**Huxing Zhang** 52:29 Right.
If there's a chance that you can do at, in United States? Or…
**Trask Stalnaker** 52:52 Did I lose you?
**Steve Rao** 52:55 Mmm.
**Huxing Zhang** 52:55 I… I can hear you.
**Trask Stalnaker** 52:57 Oh, I think I lost you for a second. What were you saying?
**Huxing Zhang** 53:01 I was saying, is there any chance that you can do at the after… at the afternoon of your day?
**Trask Stalnaker** 53:12 4PM… 7 AM your time?
**Huxing Zhang** 53:20 That's really…
**Trask Stalnaker** 53:26 5PM your time.
**Huxing Zhang** 53:27 Wednesday is 8. Yes, if the… yeah, 5 p.m. for one day, I think I can manage… I can…
**Trask Stalnaker** 53:39 We're not gonna get… we're not gonna get very good attendance, I can tell you, at 5 PM Pacific, because… I know, I know a bunch of these people are, I know Aaron is Eastern, East Coast.
**Huxing Zhang** 53:54 Eastern.
**Trask Stalnaker** 53:56 I know that, Sergey, who's another important person there, is, I think he's Europe, so that afternoon wouldn't work, but…
**Huxing Zhang** 54:07 Oh, okay.
**Trask Stalnaker** 54:11 And, yeah, that late afternoon is… Tough, anyways.
**Huxing Zhang** 54:17 Okay.
That's really, really difficult.
**Steve Rao** 54:21 Handy.
**Trask Stalnaker** 54:23 Yeah… What was the morning, the 4… 7… 30 a.m.
How's half an hour… I mean, it wouldn't be the main meeting, which I think is… I mean, that's…
**Huxing Zhang** 54:46 Yeah, yeah, I think we…
**Trask Stalnaker** 54:49 Milla and I…
**Huxing Zhang** 54:54 Then, if you… if that time, we can do… we can do at that time, right?
Definitely can do that.
I think it's, we cannot find a better, more, better, better time other than that.
**Trask Stalnaker** 55:11 I added it on.
Yeah, I don't think so, sorry.
Yeah, hopefully we can… get, a few people… Over there.
**Huxing Zhang** 55:48 Yeah, I don't want to make you difficult to make that decision, but just some suggestion, if it's hard to do that, it's fine, it's fine. We can separate that.
But, I… I do think that we can… I own the Mila homework to demonstrate our work, in that maybe we can do it separately, we can have a recording and share it with… with her.
**Trask Stalnaker** 56:21 Share it with who?
**Huxing Zhang** 56:24 I said that I own a little bit of, homework that we, he, he, she, she would like us to share how we do the, like, how we do instrumentation with AI to help the.
**Trask Stalnaker** 56:40 Right.
**Huxing Zhang** 56:41 implement that. Maybe we want… she want… want us to share some, experience in our meeting, but, since that is difficult for us to attend, maybe We can do the… record, make some recordings and share with, the link.
**Trask Stalnaker** 57:02 Oh, I see with everyone, yeah. Another… so, I have a question. Does the Monday… Does the 7.30… AM, the late evening, your time… work… Would that… could that be a replacement for the Monday afternoon?
Or Tuesday morning, your time meeting.
**Huxing Zhang** 57:31 Yeah, yeah, I think, I think… what's that? Is that on Monday or Tuesday?
The, the meeting, or the original meeting? Correct.
**Trask Stalnaker** 57:40 Yeah, it's, our Monday, but your Tuesday morning.
**Huxing Zhang** 57:45 I mean, 7, the, the 9 a.m. meeting at your time, what is that?
**Trask Stalnaker** 57:52 Is Tuesday mor… our Tuesday morning your Wednesday night?
Okay. So that could be, I mean, if we met on Tuesday… at 7.30 a.m. our time.
That would give us a chance to then… At least take things that you brought up to the main meeting, like, an hour.
And a half later.
**Huxing Zhang** 58:29 Yeah, yeah, yeah, yeah, yeah.
I think so. I can… I can do that.
**Trask Stalnaker** 58:36 The other option would be Wednesday, and we can kind of go the other direction of we can bring stuff that we talked about in the Tuesday meeting to chat with you all on Wednesday.
**Huxing Zhang** 58:48 Yeah.
**Trask Stalnaker** 58:51 I'll start a chat with us in… and Lyudmila, and let's… let's… We can pick between Tuesday and Wednesday.
Because I think that those… oh, Wednesday, I think this time is maybe… But Milla might have another meeting.
But yeah, let's chat about that.
**Huxing Zhang** 59:12 Yeah, thanks luck.
**Trask Stalnaker** 59:14 Cool.
Because that would, A, that would also work, that would work better for me than the evening times that we have currently.
And I would like to at least then, if we got both Lydmill and myself.
at least we'd have more, and then maybe we can get more people, especially at this time. We could get Eastern time.
We might be able to get, like, Aaron Abbott and, Sergey, who are East Coast and Europe.
**Huxing Zhang** 59:47 Okay.
**Trask Stalnaker** 59:49 Alright.
**Steve Rao** 59:50 Okay, bye.
**Huxing Zhang** 59:52 See ya.
Goodbye.
**Trask Stalnaker** 59:55 Bye.
