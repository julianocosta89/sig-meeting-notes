SIG: Rust SIG
Date: 2025-07-08
Duration: 36 minutes
============================================================

## Zoom Recording Transcript

**lalit** 00:47 Hey? Hi, Utkarsh!
I have been driving.
I'm gonna be door office.
Just taking the calls.
**Utkarsh Umesan Pillai** 01:06 Yeah, I think Cj is probably also gonna join. I saw his message on the channel.
**lalit** 01:14 Okay.
**Utkarsh Umesan Pillai** 01:17 Hi bjorn.
**lalit** 01:22 If I.
**Utkarsh Umesan Pillai** 02:31 I just Ping Cj will be joining in a bit.
**Cijo Thomas (Microsoft)** 02:51 Hello!
Hello! Can you hear me?
**Utkarsh Umesan Pillai** 02:56 Yeah. Hi, seejo.
**Cijo Thomas (Microsoft)** 02:59 Sorry I forget to actually start the meeting earlier.
Thanks Sudkarsh, for reminding me.
Maybe it's already 5 min past 5, so we don't need to wait. Let me share my screen.
Yeah, we don't have anything in the agenda, but we can use this time to go over any
questions or discussions or release plans.
hey? Beyond, like, nice to see you back ping.
That's yeah beyond anything you want to discuss today. I think we didn't meet like last couple of weeks, so I'm not sure whether there were any
updates that occurred with the.
**BA Björn Antonsson** 03:57 No, I mean, yeah. I mean the open Limited tracing bridge has got reviewed and I've got comments, and I've
address them and
I haven't heard back after my
comment, but we'll see
**Cijo Thomas (Microsoft)** 04:22 Okay, yeah, like, some, progress is better than nothing.
**BA Björn Antonsson** 04:26 Absolutely.
**Cijo Thomas (Microsoft)** 04:28 Okay, yeah.
I was talking to like scope like yesterday. He was asking like, what kind of things are left in distributed tracing in main report. One of the main thing is, we just need to wait for the tracing open elementary changes, so we can start trimming our public Apis and see if we can get the Api to stable. But unfortunately we have to wait for this to make any changes in that direction.
I also promised like, I will write up
what at least I have in mind about the
final shape of how the distributor tracing should evolve, especially in relation to how we interrupt with the tracing one I
like. I have a like mostly ready version. I expect to share it in an issue shortly, so please do
leave comments on it, and once we all agree, it's a plan. Then we can maybe share it in a blog post or something, because this this has been like quite, quite a significant effort.
So people are asking like, What's the final story?
And when I attended the open elementary conference, like few weeks ago, like there were
lot of people who are very curious on
how are we handling the Tokyo tracing situation? So I thought.
let's write it down. And once all the people agree, then we can publish it as a blog post and keep everyone updated on how the interrupt story would evolve.
Yeah, I expect to have that like very shortly. Have a very it's a pretty big document. But it has to be took over all the scenarios. Yeah.
Any other topics to discuss. If not, we can look at open issues and pull request. Let me
start with the milestone to see whether we have.
Yeah.
The only thing which yeah, this one we already covered
this one. I believe Lilith is in the do you know, if you have oops? Sorry? Do you have some time to work on this one.
**lalit** 06:42 Sorry. Which one
**Cijo Thomas (Microsoft)** 06:44 The one which allows modifications to.
**lalit** 06:48 I'll do that.
Think it shouldn't there? No, major major comments on this.
Probably I just need to revisit and
maybe revase it. And hopefully it should be ready.
**Cijo Thomas (Microsoft)** 07:04 That's most likely. Yeah,
for the redesign in memory. Now, we don't have anyone working on it so very unlikely to make progress. These 2. I started looking. I used like some AI to write some code, so there is a open Pr
needs like some time to like polish it and make it non-traught. It's currently draft. The stabilizing of
logo enabled, I think, the spec is
fine now, but we we have, like some more complications to handle in the sense I was looking at the actual Pr where we're trying to remove the feature flag from everywhere.
Api SDK and appenders. But I think we can only do it for appender and Api, because the the spec is stabilizing only like one aspect of it. So it's not yet stabilizing. The
is enabled check in processor and
exporters, so that part is not yet solved or not yet stabilized, or we'll need to
either like we just keep it and do
the entire thing in one shot. When the processor is also ready, or we can just do a subset, we can just modify the or remove the feature flag simply from Apa and the appendius, which rely only on the Api. The SDK ones need to wait.
The Pr. Is ready. Actually, I mean, copilot has done a reasonably good job of creating the Pr. But then I realized, we touch on SDK things which is not yet stable, so I'll keep this for the milestone. Hopefully, I should have some time to it.
That's pretty much we have in the next milestone. Be.
We don't have like any update on Otlp. It's
Scott said yesterday, like he will start looking at it because we don't have Otlp exporters table for any signal, so that requires someone to
take a look at like, what's the public Api like? Are we compliant with the spec?
Are there any open issues to be resolved? A few things like that.
So yeah, once Scott is back, I think, he said, he'll create a parent issue to track all the hotel period lighted stuff and see what are blocking versus not.
And hopefully, with that we'll get a timeline for Otlp stable release.
Think like. Let's see if there are any new issues. Think this one is already responded to. This one is responded to
this one we attempted with copilot, but that didn't work very well.
**lalit** 09:48 So.
**Cijo Thomas (Microsoft)** 09:49 There is a Pr. I think we have to do it like by hand.
There are a couple of issues which I started looking at it, but I didn't finish. So this is
probably the only one we need to look at. Those are much, much older
terms of Pr. I think we do have some prs
so I'll ignore the one created by AI. They are, anyway not mergeable. So this one is stuck on
the Eccla.
This is still draft this one is again a a.
Okay. There is one to add valuable.
Take a look at that.
Yeah. This one, I believe.
had a blocking comment towards the end. So let's take a look at that.
Think Paul had a couple of fairly
big Pr, like one is to add on ending
and want to add span. Let's take a look at that because it it's been a while. So let's take a look at that.
**Paul Le Grand des Cloizeaux** 11:00 Think it's missing the change. I was on Pto for the last basically 3 weeks. So yeah, I probably need to.
**Cijo Thomas (Microsoft)** 11:10 Yeah, I think the only comment I had like last week was,
just. And I was in the call like last week. So one observation, or more, like more like a question for discussion is given. This is a breaking change, and we
don't know whether there will be more breaking changes. There are. There is a good chance. We'll have many more breaking changes in the future for tracing signal. Wondering like, should we like, club them all into a
single release, and be done with all the breaking changes
instead of doing one release which has some breaking change, and then it get another breaking change release.
I'm not sure like how easy it is going to be, but anyone has thoughts on that, because we we've been hearing a lot of complaints about constant breaking change. Unfortunately, not much we can do. But at least clubbing a bulk of breaking changes into one release and got it done would be a smoother experience for users. So any thoughts on that from
everyone on the call.
**Paul Le Grand des Cloizeaux** 12:25 What's the release schedule like? How often is the
open to the entry SDK creates released.
**Cijo Thomas (Microsoft)** 12:34 Yeah, we don't have a fixed schedule. So what I was trying to show earlier was the milestones we have planned. At least it's since the last one. It's almost a month, and we put like August in so.
3 months. So at this stage we are probably looking at a release around 3 months
earlier, if we have enough bandwidth. But since not many people are actively working as we used to have, the velocity has drastically come down, so we only need like once every 3 months or so. But this one, I put it as point
3 1, which basically means it can take like
breaking changes. The idea. What I was trying to discuss was, if you don't have breaking changes, if you like, delay all the breaking changes we can do a release which is like point 3 0 dot one. So that's right. And then, like bundle, all the breaking changes in one short.
So that's 1 idea. And we we briefly discussed, like in few weeks ago.
The
2 key things which we are tracking in the repo is getting distributed Apa to stable and SDK to stable, and for Apa we put like September end as the tentative date so one thing would be, we'll do like one release before September 29, th which contains all the breaking changes for tracing Api, even though technically, we can break it until this time, like we hold a like very high bar like, unless it's very important.
we'll not break it. And for SDK, it's end of this year. That's what we put it so to your pr like. If we merge it now and then we have like more breaking changes. We are technically we can do it like until we declare it stable
but based on the feedback we are hearing is, people are like complaining about breaking changes quite often. So that's why I'm thinking, like, should we
try to have a agreement on what breaking changes are, and even have the Pr. Ready. But
don't do it like
don't do it like with lot of gaps in between. Make sure they all like go relatively in close succession, so that they'll all be part of a single release.
**Paul Le Grand des Cloizeaux** 14:52 yeah, I think, though, that I mean the next.
the next minor version, right is also going to contain breaking changes to logs and metrics.
**Cijo Thomas (Microsoft)** 15:10 No, they are all declared stable right now, so we cannot take any breaking change for logs, and
so distributed. Tracing is the only one where we can afford, because we already marked like logs and metrics, are stable in the previous release, or the one before that. So tracing is the only one which we have like, not yet declared. And of course we have the context propagators, but these are propagators is mostly related to tracing to a certain extent, context also is, but they are technically independent. They can be stabilized separately.
**Paul Le Grand des Cloizeaux** 15:46 Yeah, because so
what? I'm not sure when you say people complain about breaking children is, do they complain about having to bump
their version, or do they complain about actual Api changes.
**Cijo Thomas (Microsoft)** 16:03 Both, actually, because when yeah, main issue is like, when we do a minor version change before one dot 0, it's all considered like noncompatible with each other. Right? So that's probably why. And we also had like, quite, quite amount of breaking change in logs and metrics over the last one and a half year.
as I expect, like tracing, would also have a similar amount of breaking change, but only us, or only thing to be discussed, they should be. Make sure it's all like bundled in one shot or not.
because for metrics and logs, which was quite spread like every release, one after another. We had like breaking changes, so it was a constant pain for users to upgrade.
**Paul Le Grand des Cloizeaux** 16:51 Yeah, yeah, I see.
**Cijo Thomas (Microsoft)** 16:52 Yeah. The.
How is touching span processor, which is not as critical compared to the Api? Because not many people write custom span processors. But if they do right here, then they'll need to undergo the breaking change.
So I have like less worry about the SDK. I'm more worried about the Api side of things, the open elementary crate, not the open elementary. SDK, one. I think I put that in my comment, like, last week, it's okay to
yeah. It's it's only in the SDK grade. And the number of people who are affected are relatively less. So it
yeah. Okay, to just do it the normal way without having to worry about meeting all the things.
**Paul Le Grand des Cloizeaux** 17:36 Yeah, I mean, I think it
makes sense to to batch, bring changes together. If
the the release that we make with no non-breaking change are like Patch, or I mean
they, they would be minor versions if we are in one dot something. But here they would be patch. But if we are gonna increase the the minor. Anyway, I don't think it's that.
I mean.
I don't think it would be less work to actually update in 2 steps versus one step, because the the stuff that you update is not going to be the same
like. In one case you might depend on Apis. That will be removed, like, for instance, the
the the Span Apis that we want to remove. Once we move out of tracing, and the the
the span exporter span processor. Api will the
having like breaking one and ranking another.
If you need to update both, it's gonna take you the same time, if it's like in one versus 2. So
I I think if we don't have more breaking change to the span processor Api
itself, I I would say it's fine to to ship ship ship changes as soon as we can, but.
**Cijo Thomas (Microsoft)** 19:08 Okay, yeah. Let's see, like how the next release goes, because we don't have anything like worthy of release right now in the
already much pr, so if there is like no breaking change merged between now and the next release, we don't need to. We don't need to call it. Like minor version, changes just depends.
And then, once the span processor and other changes are in like, we'll do the actual minor version change, which is considered the breaking one.
**Paul Le Grand des Cloizeaux** 19:37 Okay. Yeah.
**Cijo Thomas (Microsoft)** 19:37 Yeah, based on your observation, like you already spent some time in quite some time in the spam processor. Do you think like, are there like any other changes you expect. SDK, tracing SDK. Would probably have, like 3 or 4 concepts like like sampler. Then, I believe, processor and exporter.
and then the shape of the payload which we are giving to processor and exporter, that.
**Paul Le Grand des Cloizeaux** 20:05 It's yeah. I think it's mostly fine.
I can try to think of ways this could change. But honestly, I I
I'm okay with the way it is right now. Other than this this Api
the despair. I I haven't found that much stuff, that's you know.
We'd need to change.
**Cijo Thomas (Microsoft)** 20:34 Okay, yeah.
yeah. Let's see, like how it goes. And like, I'm not quite sure like how exactly we should plan for, since there is some uncertainty about what time we'll have the tracing changes in, and
that will allow us to do the bulk of breaking change for Api create, and that would be a sweet time for us to bundle all the SDK chain, although, like like you said, the amount of work users have to do is, anyway. Same, we're just trying to like.
**Paul Le Grand des Cloizeaux** 21:03 Group them in one release as opposed to 2. Yeah, thank you.
**Cijo Thomas (Microsoft)** 21:09 Yeah, any other things like, Have you like again, like any other things which you observed in the span processor, which which could.
which would result in breaking change.
The on ending is probably additive change. But any other thing which you can think of in the SDK.
**Paul Le Grand des Cloizeaux** 21:32 Yeah, on ending is compatible. I should probably, if I I can. So you know the Api reflector. I can split it in, probably in 2 parts, because the Pr. Contains like
making spans readable.
And and also changing the on and the on. An Api. I think I will make the trade for readable span.
I will commit it in one pr, and that's backwards compatible. And then the the change to the actual on end signature. We can commit it in a separate pr
this way, the we can release some stuff faster.
**Cijo Thomas (Microsoft)** 22:14 Yeah, that generally helps. Like, I'm very thankful we have a smaller peer to review.
**Paul Le Grand des Cloizeaux** 22:19 Yeah. And I, I will update the on ending. Pr, so we can merge it whenever it's ready. Yeah.
**Cijo Thomas (Microsoft)** 22:29 Anyone else had like. It looks like this one had like quite at least a couple of people reviewing and approving. So any other. Anything which you think is worth discussing in this call, or it's just a matter of like someone
maybe doing a final review and merging it.
Are there like anything which is worthy of like discussing here?
Okay, yeah, not line. We don't need to. Hmm.
yeah. Let's see if there are any other. Pr, yeah, there is one about valuable serialization.
Oh, I'm not quite sure.
What is this adding? So this is
yeah. Pendant tracing has this valuable trade.
I mean valuable feature flag, which?
Okay? I'm not sure. Does anyone have context on how
this works or why we have the Hmm survey being here?
Yeah, I don't think so.
**Paul Le Grand des Cloizeaux** 23:45 Is this for?
Well, I mean valuable in tracing, I guess, is for like structural logging.
**Cijo Thomas (Microsoft)** 23:54 Yep.
**Paul Le Grand des Cloizeaux** 23:55 So, and that's right.
I can take a roof yet.
**Cijo Thomas (Microsoft)** 24:01 It also touches the vendor for log I need to take a look at that as one, because my understanding is like valuable allows you to do like like custom structs and pass it
instead of I mean, like built in ones. And
in the appender we get a call back with valuables value.
And then we just need to figure out how to serialize the value.
B, that's what we are trying to do with. Okay, we're trying to see today.
**lalit** 24:32 See, this issue was created by you only.
**Cijo Thomas (Microsoft)** 24:35 Yeah, I know the issue. But I my sure, of course.
like, how come there is Jason involved.
**lalit** 24:40 So why, Jason is in here.
**Cijo Thomas (Microsoft)** 24:41 Yeah, because the at least the idea I had was slightly different. Let me opening.
So tracing at this like, yeah, like, you can have like this custom types, and then you can put it here.
So when you get the when you are writing a
layer or subscriber, which is what we are doing in the tracing. We'll get the fully structured value. And then we should be able to represent that in the open telemetries, log record data model, which supports like something called any value which can pretty much it's like array of basics or map of basics where the value itself can be like another one. So we should be able to like represent it following that mapping
directly like without having to like serialize it
this looks like we are attempting to pick the value.
Then seed, lace it, and.
**lalit** 25:44 So, then.
**Cijo Thomas (Microsoft)** 25:44 Totally different.
**lalit** 25:45 Yeah, probably storing as a string after serializing, or something like that.
**Cijo Thomas (Microsoft)** 25:49 Yeah, because technically like, we should be adding it in the same like structure.
**lalit** 25:54 No.
**Cijo Thomas (Microsoft)** 25:55 That's why I was not sure like, why was 3rd day involved in this field?
Yeah, I think it looks like cargo sorry the appender for log had something
similar already, because we already had like survey there.
So this may be like copying what we had
from the logo printer, but then we need to revisit like why we had this. In the 1st place.
**lalit** 26:22 Okay, I got the context now, probably, like later, I'll also review it. I think.
**Cijo Thomas (Microsoft)** 26:28 Thanks because the whole idea became
elementary data model supporting that complex. Any value structure is to represent pretty much anything using that structure. But if it's just string stringified Json, then we don't need like such complex support in open elementary, to begin with.
Yeah, if you have some bandwidth like, Please.
**lalit** 26:47 Sure. Thank you.
**Cijo Thomas (Microsoft)** 26:48 But like, why we are doing it this way. Maybe, like, there is some context, or I have some incorrect understanding or something. Yeah, even it. It has like test sets as well. So
this is the test and what we are. Oh, it looks like it is actually oh.
not a string. It is map only. So the
user is utilized as a map
with key being individual name and age and value being string. And okay, looks like, it's not just a string. Yeah, it is.
**lalit** 27:22 Oh, okay. Yeah.
**Cijo Thomas (Microsoft)** 27:24 But yeah, maybe the survey was used for like, not like, blindly string serializing.
Yeah, I mean, this is this is exactly. I mean, this matches my expectation. So maybe I I looked at the actual
coding correctly.
Yeah, this looks like quite like what I would expect.
Okay, yeah, like, let's take a look at this offline. Yeah, if anyone have, like other comments on this one like, Get to it. Otherwise we can move on.
Okay, the last Pr is, I believe, this one. Yeah, Pink.
we had like something which we found like towards the end.
Okay, now, it's just waiting for another review. Yeah.
think we we were adding this, ex, yeah, extra dependencies.
**lalit** 28:21 You and I approved it. If I'm not wrong after the Re.
Oh, okay, yeah, I.
**Cijo Thomas (Microsoft)** 28:27 So once you
once you re request the review, it kind of resets it, even though technically it's mergeable, because you had approved originally. So I can technically merge it because of the original review.
**lalit** 28:39 This is okay. I think I looked, looked at changes after this, after he removed this dependency. I looked at the changes, and it looks fine.
**Cijo Thomas (Microsoft)** 28:48 Yeah, this is this is still under that experimental feature, like, yeah. But even.
**lalit** 28:55 He. He's he's not, you know. He's not adding the complete Tokyo as a dependency. He's adding the dependency which does not add the runtime.
There was some, there was some-, some.
**Cijo Thomas (Microsoft)** 29:06 Yeah, it doesn't add the runtime, but it still has some Tokyo dependency, the sync module. It was earlier, like
or something else. But now it's
even that is bit concerning because this is supposed to be like very neutral right. This thing is supposed to be neutral
with no Tokyo specifics. And these things can be like Tokyo or runtime specific. But it looks like to make.
**lalit** 29:32 Thanks happen. You really need to take a dependency on a particular runtime implementation. Yeah.
**Cijo Thomas (Microsoft)** 29:40 Yeah, this is something we need to revisit. Like, I mean, I'm generally okay, because it's still experimental. And there is no spec support even today.
For yeah, I mean, as I mentioned, there are the spec level discussion on how to do like concurrent export.
So given, it's under experimental. I'm generally okay if it's like unblocks some scenarios. But this is something which is worth revisiting. How to do that
properly with without any spec violation, and also not pulling in unwanted dependencies.
Okay, yeah, that's the last. Pr, we want to cover like anything which is some draft. Prs.
yeah, nothing here. Since we have few people here, I'll just use the time to quickly review the
Hmm.
Was the Pr. The we oh, did we match it? Actually there was a Pr. Which contributed the Tower instrumentation, I believe.
**lalit** 30:45 Yeah, I think I missed it here.
Yeah, I mean it. It.
**Cijo Thomas (Microsoft)** 30:49 Yeah, okay, okay, so we have it. Okay, perfect. Yeah, thanks for taking care of that one.
think this is the second one we have. I don't know
whether this can be leveraged in the Demo project yet.
Because Demo already uses the Instrumentation Library.
which already has metrics. So this property is not okay.
Yeah.
But we'll see like, how else to like.
Like. Once once we release it, we'll see where else we can demonstrate this, because we. This is also something which I wrote in the original issue, which I'll share, like later, about like instrumentation libraries for distributed reasing spans, because the more
work done by instrumentations, the less users have to worry about creating edge spans the one on the server or client. They probably need to create internal spans, which is why, like switching between
open telemetry Apa versus Tokyo tracing will not be a of big difference.
But anyway, let me write down my thoughts fully before can commit alright any other
things which people want to discuss.
I I have like one small topics. It's about like enabling
the co-pilot in the report so I didn't hear any
push back so far I don't know whether you don't even notice, so we have enabled co-pilot in both
main repo and the control report, along with some other open elementary report. But in C plus plus it was met with some pushback. So Gc. Is now evaluating, rolling back, and explicitly enabling it. I
don't think that issue has resolved it. So it's still like pending. But since we have like few maintenance approvals here, like anyone has any concerns about enabling. It's right now enabled. But I'm expecting that Gc. Will just disable it for entire open elementary and ask us to enable it on a per report basis, so that it's a conscious
opt in thing as opposed to enabling repo wide there, anyone we still haven't like solved the Cla issues. Because if you look at Pr. From copilot, it cannot be merged as is because the
commit fails because it's not signing the Ccla. But assuming those logistic issues are fine like, is there anyone who has concerns with this one? Please do raise it so we can let DC or Tc know that
feedback. Yeah. But otherwise it's like normal Pr process. The Pr is created by the
co-pilot. But the approval. And everything is done like just like just like
any other pr, so when we approve it, we merge it. The code is ours, just like any other code. It's just that copilot makes it easy to do like trivial Prs.
**lalit** 33:57 I think in in C, plus plus it has been already removed.
So probably I think it's yeah. I didn't trash. He pinged me separately, asking like, if it's okay to remove it as of now and then we'll discuss. So I think it it got removed.
**Cijo Thomas (Microsoft)** 34:14 Oh, okay.
**lalit** 34:14 Gives us.
**Cijo Thomas (Microsoft)** 34:14 Some updates on this issue for me.
Cppn, okay.
**lalit** 34:22 Yeah, but I think for I have been looking into the in general terms and conditions for I mean in general policies for Linux Foundation, our open telemetry, and also how the co-pilot get up terms and conditions. I mean, I don't see any issue in which can violate that
which which can have any violation or any concerns. So I'll be discussing that in C, plus plus submitting.
Oh, okay.
**Cijo Thomas (Microsoft)** 34:51 Okay. Think it looks like gc, already clarified. It's but trust that he'll double check with full gc, on Wednesday. Okay.
yeah. Okay. If anyone has, like other questions or concerns like, please like, raise it either as an issue or like, come into the community issue. Yeah.
So again, like my plan on how I plan to use this copilot is, there are plenty of issues which we've been open for quite a while, so we'll need to go to the issue. And like, for example, like, we need to describe, like very clearly what we want to do, clear, like exit conditions, plain English, and then assign the issue to copilot and let it do its work.
That's pretty much it. And goal is like we have, like so many like small small issues, which has been like solved in one place, but like still left to say to do in other places, it's not a lot of work, but, like the sheer volume of issues, means someone has to like review it, do it at least copulate, can automate some of those trivial amount of work so hopefully that that will free us to do like more complex works ourselves.
Okay, yeah, that's all we have any other thoughts questions before we end.
Okay, yeah, thanks everyone. I will put in the slack channel when I finish writing the issue about the tracing interrupt. And then he can come in that
thanks everyone. See you. Bye, bye.
**Utkarsh Umesan Pillai** 36:24 Thank you.
**BA Björn Antonsson** 36:26 Bye.
