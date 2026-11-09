SIG: Prometheus WG
Date: 2026-11-06
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

David Ashpole (Google LLC) 00:04:02 I think I just opened the, The issue for entity support, or entity… hotel entity info or whatever, based on our conversation last time. So, but we… hopefully… Are we close to getting your pull request merged? I think we settled all the… various little… differences, I think.
krajo (Grafana Labs) 00:04:29 I… maybe. Yeah, it'd be… We can take some time here to look at it.
There were some questions about what whether to update the spec or fix the code. I saw you open some PRs, I… I think I commented on all three?
I hope.
David Ashpole (Google LLC) 00:04:50 trip.
krajo (Grafana Labs) 00:04:50 So, yeah, I think we are close. I just had a really rough week, mostly because of Bartek.
David Ashpole (Google LLC) 00:04:58 Oh, yeah?
Oh, it must have been a great week, then. You guys were doing, like, cool Rust stuff, and…
krajo (Grafana Labs) 00:05:06 Yeah.
I mean…
David Ashpole (Google LLC) 00:05:08 Yeah, yeah, you don't sound like…
krajo (Grafana Labs) 00:05:12 Yeah, it's cool. I mean, to be fair, I've been coding since 95.
Earlier, if you count Commodore 64.
So… Rust is, you know, N plus first language, like, I don't care. But, like, I do care from… Like, there's a… Like, we need to think about what… the Grafana opinion and stance on these things, and I was busy with that, basically.
But I told Bartek that, you know, you really screwed up my week, and that's… I mean, I wasn't able to really focus on Remote Ride 2 stuff either, so it was… He's lost.
By the way.
David Ashpole (Google LLC) 00:05:57 Okay.
Cool. I… I guess I'll ask.
I… I didn't… I don't think I saw anything on the JavaScript… Mega PR.
krajo (Grafana Labs) 00:06:12 Did you open up the yard?
David Ashpole (Google LLC) 00:06:14 Yeah, yeah, oh. Week.
krajo (Grafana Labs) 00:06:16 Yeah, like I said.
David Ashpole (Google LLC) 00:06:16 It might have even been open a week ago. It's still a mega PR, and introduces, like.
8 distinct features in one.
We had said last time that, like, that's probably okay, can't get worse, but… If you'd prefer me to break it up, just let me… let me know if that's…
krajo (Grafana Labs) 00:06:36 Yep.
David Ashpole (Google LLC) 00:06:37 The only real way to make progress, you know?
krajo (Grafana Labs) 00:06:40 Yeah, yeah, yeah, I think, like, last, Yeah, so this week has been really crap, but, hopefully next week I can bet… can get back to more normal Burke.
Also, it didn't have the titles on call for 3 days out of 5, like, that's just… Yeah.
David Ashpole (Google LLC) 00:07:00 Is this, like, a 24-7 on-call?
krajo (Grafana Labs) 00:07:02 12 hours.
David Ashpole (Google LLC) 00:07:04 Okay.
krajo (Grafana Labs) 00:07:05 Because we have to follow the sun. Yeah, still, it's… yeah, yeah.
And I'm really getting, you know, like.
not great feedback from my manager that I don't focus on operational stuff during on-call, but, like, Bye.
Yeah.
I guess we're waiting for Arthur?
David Ashpole (Google LLC) 00:07:41 Let's start with our… yeah, sure, we can wait for Arthur, that's fine.
krajo (Grafana Labs) 00:07:45 Oh, no, it's 5 minutes past. Yeah, yeah, let's start.
Something, yep.
David Ashpole (Google LLC) 00:08:02 Do we have anything on the agenda? Otherwise, I'm gonna go through… Open stuff that we've got and see if… if we can discuss anything or move anything along.
krajo (Grafana Labs) 00:08:14 Well, I, I, I would, you know, we should take a look at the… spec PR to see if there's something we need to decide, or… Are we good on that?
David Ashpole (Google LLC) 00:08:26 Looks like nothing on the agenda. Yeah, we'll go to the spec PRs then.
This one… This one… This one, and this one.
So I think we're still just waiting on… Okay, so Arthur commented, and it looks like we should update the implementations first.
krajo (Grafana Labs) 00:09:05 I… I don't know, maybe I reckoned… Say if he thinks we need to change the spec.
I, yeah.
Oh, yeah, right.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:09:19 I haven't looked at this in a while, I have to say.
Let's see… Oh yeah, I remember leaving that, comment, and Arthur… Responded to that, basically.
So it kind of looks like some work is needed.
But I think I need your feedback on that, krajo.
David Ashpole (Google LLC) 00:09:49 OpenTelemetry Go. Interesting.
krajo (Grafana Labs) 00:09:53 Yeah, I was just, before the meeting, researching a little bit.
And I think you're right in that It can introduce some weird behavior.
Because… the… So this is about the zero threshold.
And if it… If the zero threshold is zero.
Or onset in the exponential histogram side.
The spec currently says that we should set it to the default on the native historian side.
So you said something… Yeah, so if you don't set it or it's zero in the OTLP, then… We would set it to… 10 to the minus 128.
And, the issue is that that might potentially overlap with an actual bucket.
Because the buckets can go down to 10 to the minus 1000 or something.
So… mmm… My first impression is that it's a spec issue, so maybe we should fix the spec?
And, and say that if it's set to… if it's onset or zero, Then we leave it at zero in the… native storage side as well.
Or… Possibly say that the… set it to some really low value, although I don't know if that can even be done. Like, so yeah, I'm… I'm not super sure about what to do.
David Ashpole (Google LLC) 00:11:36 Prometheus, does… does Prometheus require zero threshold to be… Like, are there any requirements around what it has to be?
krajo (Grafana Labs) 00:11:46 No, it can be zero. It can be any possible…
David Ashpole (Google LLC) 00:11:49 Zero threshold to 1 if I really wanted to, and that would be valid in terms of the data model. Okay.
So yeah, so I think this sounds… I think this sounds like a bug.
the thing Arve found?
Or, like.
krajo (Grafana Labs) 00:12:04 Yep.
Yeah, I have to research a little bit more, but it does sound like a bug, yeah.
David Ashpole (Google LLC) 00:12:14 And then, let's see, here are two… This one is always wrong.
And then… The other one, I think, is sometimes wrong.
krajo (Grafana Labs) 00:12:34 Yeah. For this… For the stabilization, is it enough to fix the spec? Do we have to wait for the… SDKs too, and… and… Correct or to fix it?
David Ashpole (Google LLC) 00:12:45 it… So normally, stabilizing the spec you… like, the… so this is for SDKs, right? And we can kind of take this with a grain of salt, because we're not an SDK. So normally the… the way it works is you should have 3 compliant implementations.
krajo (Grafana Labs) 00:13:02 Hmm.
David Ashpole (Google LLC) 00:13:03 Right, because otherwise, the… the worry goes, like, you'll… you'll have one compliant implementation and two non-compliant ones, you'll stabilize it, and then it'll turn out that, like, the other two can't implement it.
I think that's a concern here, right? But the spirit of it is, you should try and get your stuff compliant.
krajo (Grafana Labs) 00:13:28 Okay, yup.
I find sometime. And… Maybe OpenPRs, it should be very easy to… Fix in the implantations as well.
David Ashpole (Google LLC) 00:13:46 Yep.
This applies even to…
krajo (Grafana Labs) 00:14:14 Prometus, yeah. I haven't looked at the Prometus.
David Ashpole (Google LLC) 00:14:18 I don't think you can pass the zero threshold if you do a new const histogram? Maybe you can.
krajo (Grafana Labs) 00:14:29 I wonder what we do in the… What do you appear… endpoint in… Improm… I bet we just pass it as it is, and don't care, which is probably… Simplest.
David Ashpole (Google LLC) 00:14:47 Okay, so it looks like there's a bit left to do here. And you're okay driving that cryo?
krajo (Grafana Labs) 00:14:52 Yeah, sure.
David Ashpole (Google LLC) 00:14:53 Okay.
krajo (Grafana Labs) 00:14:58 Oh, no, the… one of the links was Prometus, basically, this… where we just simply set the diff… oh yeah, I actually remember now that I think I did the original code, because at the time, the OTLP didn't actually carry.
Yeah. The zero threshold. So… or even if it did, there was no interface to actually read it.
Okay, yeah, yeah, okay, this is bringing back long, long… 2-year… 3-year-old memories? I don't know.
David Ashpole (Google LLC) 00:15:31 Good memories. Okay, we got Jack's approval here, so I'm gonna click the Merge One Ready button for… Hotel Histogram Optional Sum.
krajo (Grafana Labs) 00:15:40 Okay.
David Ashpole (Google LLC) 00:15:45 Nice.
Then we have the big PR that we've been working on for a while.
krajo (Grafana Labs) 00:15:55 Yeah.
David Ashpole (Google LLC) 00:15:59 Do we?
krajo (Grafana Labs) 00:16:01 No, I asked, it seems…
David Ashpole (Google LLC) 00:16:05 I'm gonna resolve this.
krajo (Grafana Labs) 00:16:07 Nope.
David Ashpole (Google LLC) 00:16:14 Okay, this is tracked separately.
krajo (Grafana Labs) 00:16:24 you're fixing this, I think, right? Or you fix this. Or, I mean… You have a PR open.
David Ashpole (Google LLC) 00:16:30 I don't know if it's open or merged.
krajo (Grafana Labs) 00:16:32 Oh, maybe Margin one, too.
David Ashpole (Google LLC) 00:16:36 I can at least link to it.
is merged. Look at that.
krajo (Grafana Labs) 00:17:04 Oh.
Yeah, the question is then, is it enough for us to… for me to update the spec PR, so this PR, to say that… Like, document the intended thing that is coming in that feature lead.
David Ashpole (Google LLC) 00:17:31 I mean, from my point of view, there's… This is the only Prometheus scraper.
that really follows the spec, so I think we're good on implementations. We could look at the simple Prometheus receiver one, but we've never cared before, so… And the second is that the existing language… I mean, we should go update it someday, maybe. The existing… this is just preserving existing spec language, right? So the spec previously said Nothing about instance label or anything.
But do you still need… you still need to update this PR, though, right?
krajo (Grafana Labs) 00:18:06 Yes, yeah, yeah, yeah. I'm just asking if I should update it, and I can update it, yeah. That should be easy.
Yep.
Oh yeah, this is actually done, because I now added the remote ride specific.
Paragraph.
David Ashpole (Google LLC) 00:18:31 B.
And this is the same thing, right?
krajo (Grafana Labs) 00:18:40 Same, exact same thing, yeah, yeah.
David Ashpole (Google LLC) 00:18:47 I don't know if I need to comment, too.
Just generating GitHub spam.
krajo (Grafana Labs) 00:18:52 Yeah, this is the explanation. I think we understand this by now, Pugi.
David Ashpole (Google LLC) 00:19:03 I don't think we're gonna make any spec changes to… on this front, in this PR.
krajo (Grafana Labs) 00:19:08 Nope.
And, yeah, and it's doing the same, so if you want to copy-paste this text, it's going to be the same in the next.
David Ashpole (Google LLC) 00:19:25 This is just… Because every time you point an AI agent at this PR, it's like, warning!
krajo (Grafana Labs) 00:19:32 Oh, yeah, yeah, yeah, sure.
David Ashpole (Google LLC) 00:19:33 to me.
krajo (Grafana Labs) 00:19:34 No, I would want to resolve everything.
Just in case we forget something, because there has been a lot of discussion.
Oh yeah, we haven't addressed this one, actually.
I think for me to…
David Ashpole (Google LLC) 00:19:50 this upstream?
krajo (Grafana Labs) 00:19:54 So this is… wait, this is… Yeah, this is Prometus tool TLP. I mean… I don't particularly care that much, like, if in the OTLP model, you allow empty string as a value, as opposed to Prometus model, like.
Be my guest, I don't… And then…
David Ashpole (Google LLC) 00:20:18 They're not equivalent, but, like, for example, resource detectors, if there's some sort of optional, like, oh, I'm on AWS, and I'm not sure if I'm gonna detect X.
then they'll usually not attach it, right? I feel like we should behave… Kind of like a resource detector here.
krajo (Grafana Labs) 00:20:37 I mean, if you open a PR, I can review.
David Ashpole (Google LLC) 00:20:40 Okay.
krajo (Grafana Labs) 00:20:43 Triage.
David Ashpole (Google LLC) 00:20:51 Meh.
krajo (Grafana Labs) 00:20:55 Yeah, it doesn't really affect the spec.
Because it was never written there, and I'm not suggesting a change, so, like… I'm kind of glossing over this a little bit.
Or the spec is closing over this a little bit.
Oh yeah, I think you added that to the PR.
To actually handle the scheme as well.
David Ashpole (Google LLC) 00:21:25 Did you?
It should be the pre-relabel, or the post-relabel scheme, yes.
krajo (Grafana Labs) 00:21:32 Yeah, yeah, yeah. Okay, then that should be resolved, because then that's already fixed.
Or, although, no, but then it na… Does this need an update as well?
David Ashpole (Google LLC) 00:21:44 There's an inspector fee.
krajo (Grafana Labs) 00:21:46 Yeah, I think it's the same thing as the previous one, that it needs the spec to be updated with the… The new reality.
David Ashpole (Google LLC) 00:21:58 Okay.
I refreshed the page, and it came back missing all of my changes.
krajo (Grafana Labs) 00:22:04 Oh, no.
David Ashpole (Google LLC) 00:22:06 So we… So this needs a spec update.
krajo (Grafana Labs) 00:22:11 Wait, what does it say? It says, from the scheme label on the target.
No, I think that's correct now.
That's… that's pretty much correct, so I think this is… Yeah, I can check, but I think I don't need to update it.
Yeah, that's… yeah, that's what it is.
David Ashpole (Google LLC) 00:22:43 Boost name that doesn't look like an address.
this is resolved by the PR, or is it not?
krajo (Grafana Labs) 00:22:52 I think… I think this was originally raised by you, maybe, actually, that We are basically doing string manipulation, and even if the the split string looks like crap and doesn't look like a hostname, we still put it into the host name, and then I guess the question is, is that fine? Do we want to be clever about this, or just leave it at… leave it at that?
I'm okay with just leaving it at the current.
David Ashpole (Google LLC) 00:23:23 This spec sounds correct.
krajo (Grafana Labs) 00:23:26 Yeah.
David Ashpole (Google LLC) 00:23:27 Right? Because it has… unless it is an unspecified address, which… More or less, it's like…
krajo (Grafana Labs) 00:23:37 Yeah, that's the wild card.
address.
David Ashpole (Google LLC) 00:23:52 So, sorry, so do we want to check the upstream implementation and make sure it aligns with this? Is that the ask?
The conclusion here, and we're happy with this language.
krajo (Grafana Labs) 00:24:01 I'm happy with this language. I think somebody somewhere raised the question in some… somewhere where we were like, okay, but what happens if we split by the colon, and then the part before it isn't an IP, and isn't, like, maybe a valid hostname? I don't know what that would mean. So, I'm a little hazy on the details of what we wanted here, to be fair.
Well, I guess it's a question, like.
Do we want to validate, or do we just accept whatever is there and write it into… Several does.
I mean, that can be a choice, I mean… If somebody, you know, relabeled into some crap, like.
Should we judge what they did? Like, I'm not sure.
David Ashpole (Google LLC) 00:25:00 Wait, no, no, no, this… this is… We're no longer parsing this from instance, right?
krajo (Grafana Labs) 00:25:05 Yes.
David Ashpole (Google LLC) 00:25:05 So it's now actually the address used.
krajo (Grafana Labs) 00:25:09 Yeah, but that's after relabilling.
David Ashpole (Google LLC) 00:25:12 Yeah, but I guess… so I guess what you're is, if… like, this is actually the address that the collector tried to get something from, right? Like, this is known.
krajo (Grafana Labs) 00:25:21 Yeah, yeah, if it's not valid, then it doesn't work. You're right, yeah, this is… okay, yeah, you're right, that's…
David Ashpole (Google LLC) 00:25:26 Okay.
krajo (Grafana Labs) 00:25:27 Oh, this is great, because we… we are… We are validated by.
David Ashpole (Google LLC) 00:25:32 Or if you put an invalid one in, then you will get up.
You know, zero. Yeah.
krajo (Grafana Labs) 00:25:40 Okay, that sounds good.
I think then… then they're good.
David Ashpole (Google LLC) 00:25:45 Take the value before…
krajo (Grafana Labs) 00:25:49 You opened the PR on this one, so that's… Yeah. Results.
David Ashpole (Google LLC) 00:25:54 We already have a comment here.
Top. Yep.
Update this somewhere…
krajo (Grafana Labs) 00:26:01 Yep.
David Ashpole (Google LLC) 00:26:08 I'm just gonna… yep.
We're doing this in a follow-up, right? So… Do we wanna… do you want me to open an issue to track this?
Or will we just mentally…
krajo (Grafana Labs) 00:26:41 I don't trust my mental capabilities to remember anything basic at this point. There's too many things going on.
David Ashpole (Google LLC) 00:26:46 ridiculous.
krajo (Grafana Labs) 00:26:54 This is… Is this the only thing? This is one of two things that keeps… Duh… tube instance, Side, a little bit different between the receiver and the remote right receiver.
The other is, you know, the split into the namespace crap that we should talk about also.
David Ashpole (Google LLC) 00:27:16 Yes, yeah.
krajo (Grafana Labs) 00:27:18 Yeah, I think it would… it can be a good follow-up, like, it sounds… Like, not that super important, to be honest.
David Ashpole (Google LLC) 00:27:31 Just… Hmm.
I think this is resolved.
Yep.
Let's just resolve it.
krajo (Grafana Labs) 00:28:11 I think I already did it as a… you can look at the current version. I think I did write, must feel.
So, it should be resolved.
David Ashpole (Google LLC) 00:28:25 Well, I won.
My comment was, avoid.
krajo (Grafana Labs) 00:28:30 Oh.
David Ashpole (Google LLC) 00:28:31 comment was, don't do that, but…
krajo (Grafana Labs) 00:28:32 Oh, yeah, yeah, but then, yeah, but then you have to work out what to do with the empty… so that's the same follow-up as before, basically.
But I… yep.
That's why I linked the other.
David Ashpole (Google LLC) 00:28:45 So this, this one here.
krajo (Grafana Labs) 00:28:47 Yes.
Yeah, that sounds good.
David Ashpole (Google LLC) 00:29:03 Yes, I already asked you to update here, that's fine.
krajo (Grafana Labs) 00:29:07 Nope.
Well… Oh, that's done. Yeah.
I'll do the header.
David Ashpole (Google LLC) 00:29:20 Done?
krajo (Grafana Labs) 00:29:21 Yep, yep.
Have you looked at… That's a question to all of you. Have you looked at the new… structure.
David Ashpole (Google LLC) 00:29:31 I don't think this has come back up in my queue.
Okay. But I think after I resolve all these threads, It won't come up.
krajo (Grafana Labs) 00:29:44 This is actually a pretty interesting one that Arve raised.
About the… the scheme, and… metrics path.
David Ashpole (Google LLC) 00:29:53 Okay.
Yeah, the… The context was just, like, you were looking for all the internal labels?
I agree that we should stick with Prometheus. I wonder if we should add type and unit as well, and consider dropping those in favor of populating the actual metadata when we get those labels.
krajo (Grafana Labs) 00:30:17 That's… that's a separate qu… Well, this…
David Ashpole (Google LLC) 00:30:22 But they're handled the same as name, right? So if we're dropping name, maybe it makes sense, but most people aren't going to enable that feature gate.
krajo (Grafana Labs) 00:30:29 Right, but, yeah, I think, yeah, we can… Think about that, but… Specifically here, Arve pointed out that Schema and metrics path is dropped in the receiver, but not dropped in the remote right receiver.
David Ashpole (Google LLC) 00:30:48 Yeah, so, by the way, I agreed with yours, and we merged it.
krajo (Grafana Labs) 00:30:53 Oh, okay, super.
David Ashpole (Google LLC) 00:30:54 See, this, yeah, this is resolved.
krajo (Grafana Labs) 00:30:56 Yeah, the crazy thing about this was that I tried to trace where it's coming from, like, why did we ignore them in the first place, and I couldn't figure it out. Well, LLM couldn't figure it out. It traced it back to 2019 Open Census.
And… right in the first PR without an explanation, these are there.
And I think it might have been just a misunderstanding, basically.
David Ashpole (Google LLC) 00:31:21 I agree.
Actually, Arve, are you okay with that resolution? I know this… I think this was one of your…
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:31:31 I think it's hard… I mean, I don't have any strong feelings around this. It was just, like, an inconsistency, I found.
I don't really… I don't really know so much about it, like, I think it's the first time I saw those labels.
David Ashpole (Google LLC) 00:31:47 Cool.
Let's see… Yeah, I'm okay with doing a bug fix here. Does someone want to volunteer to do that bug fix?
Oh, you marked this as resolved, krao.
krajo (Grafana Labs) 00:32:13 I think I just added labels with empty values, as Arve suggested, if I remember correctly.
David Ashpole (Google LLC) 00:32:20 No, that's… that's fine.
Let's, I'm just gonna unresolve it till we have the tracking issue open.
krajo (Grafana Labs) 00:32:52 Okay.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:32:56 If you open the tracking issue, you can assign it to me.
David Ashpole (Google LLC) 00:33:24 This is different from the Prometheus receiver.
krajo (Grafana Labs) 00:33:27 Yes, there's a service team space stuff.
David Ashpole (Google LLC) 00:33:30 Is this resolved, still?
krajo (Grafana Labs) 00:33:35 It's not resolved. What do you mean? Sorry.
David Ashpole (Google LLC) 00:33:43 Sorry, is this thread?
krajo (Grafana Labs) 00:33:46 I mean, you… you also commented in… the next comment is from you, so… and you opened a PR, so I think you can resolve mine. It was kind of a note to reviewers that, hey, this is a difference.
So, yeah.
we can resolve that, because you have mirrors. And this is very interesting, like, I'm… So, it's, the spec is a little bit… I don't know. Not inconsistent, but, like.
Takes different things into consideration at different… Points, and that's… that's… that's fine.
But, like, it says that when we go from Prometus to… auto… then… You know, in the receiver, we just copied the job into the service name, and in the remote right receiver, we split the job.
Into two, along the slash sign.
To have the namespace and the name.
And then on the other… direction, OTRP to Prometus, we say that all the service namespace, service name, and service instance ID are the identifying.
So we should create the job from… an instance from that.
So that's… that's the background. And… Yeah, I… I agree that it's kind of… weird to… Assume that just because there's a single slash, it means namespace and name?
But then again, it's written in the spec, so people might take it that way, that it should be that, so I'm a little… yeah, I'm not… Super sure about what to do with this one.
If you should keep it or not.
David Ashpole (Google LLC) 00:35:48 I think this reminds me a little bit of, like, the UTF-8 stuff, where we, like, we know that most of the time, if you see service underscore instance underscore ID, that it was service.instance.id, but… Because we don't know for sure, we don't… Like, we don't try and swap it back to what it used to be.
Yeah, I guess… Historically, I think we've found that People don't like it when we make assumptions, because there's always someone that you… Break who's doing something weird.
And I think that's likely to be the case here.
krajo (Grafana Labs) 00:36:32 Yeah, but then the… as I pointed out, I think you need the migration guide, basically, if… because if somebody did depend on this behavior, and then we, you know, we introduced the feature gate to move eventually to a state where we don't do this splitting.
Somebody…
David Ashpole (Google LLC) 00:36:51 I was just gonna say, I'm a little bit less concerned about the remote right receiver than I would be about the Prometheus receiver, just in terms of, like.
The user base and stuff, but… I mean, thankfully, it's pretty easy to do the split via OTTL if you want to.
krajo (Grafana Labs) 00:37:15 Oh, did you…
David Ashpole (Google LLC) 00:37:18 That's what that ends up looking like.
krajo (Grafana Labs) 00:37:21 Oh, you give a workaround, basically, if somebody runs into this. Okay, that's… I guess that's less input than what I suggested, which is that they… Use no translation and keep identifying inputs and all the shebang, so… Yeah, as long as there's a workaround, I'm fine with this.
David Ashpole (Google LLC) 00:37:53 Okay.
krajo (Grafana Labs) 00:37:57 But, like, that's just my opinion. I don't know if others looked at it, or, like, what.
David Ashpole (Google LLC) 00:38:05 Let me make sure… Looks like Arthur's on this and you're on this.
krajo (Grafana Labs) 00:38:11 Yeah, I'll review again. I haven't seen that you updated, sorry.
David Ashpole (Google LLC) 00:38:14 Oh, that's cool, it's fine.
I'll blame Bartek.
krajo (Grafana Labs) 00:38:18 Yeah, yeah, please do.
Is he now a manager or something? Because I've seen him, like, offer jobs on X, I mean, Twitter.
David Ashpole (Google LLC) 00:38:30 No, he's the… he's the TL for Google Managed Prometheus.
krajo (Grafana Labs) 00:38:35 Okay.
David Ashpole (Google LLC) 00:38:39 So I think that's all the comments on here. I think they're mostly resolved.
Some small updates.
Some bugs to file.
And one PR that will wait on… one PR to merge upstream.
And then I think we're… I think we're mostly on the same page with this. I will do a re-review, to make sure that there's nothing… nothing I missed, but hopefully then we can get this… get this put to bed.
krajo (Grafana Labs) 00:39:06 Yep.
David Ashpole (Google LLC) 00:39:08 Awesome. Thank you for driving this.
krajo (Grafana Labs) 00:39:11 No problem.
David Ashpole (Google LLC) 00:39:14 Okay, and then I opened a pull request.
This was, I think, from one of the threads, actually. So this is… We were talking… oh, this is the, batch.
Undefined behavior when two series result in the same job instance pair.
This was an issue, you opened Cryo.
krajo (Grafana Labs) 00:39:38 Yep.
David Ashpole (Google LLC) 00:39:40 And then… And then I think my proposal was just to add the requirement, but to make it only a requirement within one scrape payload or batch.
krajo (Grafana Labs) 00:40:00 Oh, you mean one batch in remote track receiver, right?
David Ashpole (Google LLC) 00:40:04 Yes.
krajo (Grafana Labs) 00:40:05 Yeah. And what, I'm trying to remember, so… Okay, yeah, I will, I will review this. I, yeah.
David Ashpole (Google LLC) 00:40:14 I think… oh, maybe I didn't CC anything, but let's…
krajo (Grafana Labs) 00:40:33 Okay.
David Ashpole (Google LLC) 00:40:39 C.
And then I think that's it for spec PRs.
Do we want to pop over to spec issues?
Sure, okay.
krajo (Grafana Labs) 00:40:52 As long as we leave a little time at the end about the default changes discussion.
David Ashpole (Google LLC) 00:40:58 I mean, if we're ready to have that…
krajo (Grafana Labs) 00:40:59 platinum, yep.
David Ashpole (Google LLC) 00:41:01 If we're ready to have that, I say we just have it, because we've got 20 minutes, and…
krajo (Grafana Labs) 00:41:05 But R2 is not here, that's my only thing.
David Ashpole (Google LLC) 00:41:09 That's… that's fine, we can wait till after QCon, then.
Yep.
Let's see, so I did open this just before the meeting.
So, last week, I talked about How we could represent entities.
in the… Prometheus… or, yeah, how we could represent entities in the Prometheus data model.
And so this is the… the proposal for that. It's what I talked about last week, with the addition of A single label for the identifying keys.
And… Another label for the, descriptive keys.
So this… this would not have any dependency on looking up schema URLs or anything like that.
it would be fully backwards compatible, and I think more importantly, would not stop us from stabilizing the resource spec as it is today.
So… Those all seem like, like, good reasons to… At least have this open, and, But maybe to add it as a separate development section, so that we can stabilize the rest of it, and then… Play with this and see if it… if it works well.
Appreciate thoughts. If people like it, I can go ahead and open the pull request, but I will wait.
At least until your refactor is merged before I do anything.
krajo (Grafana Labs) 00:42:41 Yeah, I think that was one thing that we talked about, if you go back, please.
There was one thing that we talked about with Arve after the last meeting.
That the… the kind of the joint key between metrics, target info, auto identity info, is it… is it still job instance, or what… where's the…
David Ashpole (Google LLC) 00:43:00 Yes, so it's still Java instance.
Anything that joins with Target right now is joined on Java and instance.
So this, this, this example is from an SDK exporter.
krajo (Grafana Labs) 00:43:13 Oh, yeah, yeah, because…
David Ashpole (Google LLC) 00:43:14 No job and instance on anything, but whenever you go from SDK to collector, you get job and instance on everything.
krajo (Grafana Labs) 00:43:20 Okay.
David Ashpole (Google LLC) 00:43:21 Like, yeah.
krajo (Grafana Labs) 00:43:26 And I see that.
Do we want to discuss it now, or should we go and review?
David Ashpole (Google LLC) 00:43:33 I'm happy if there's any feedback you have, or thoughts, I'm happy to answer questions, or if there's alternatives you want to chat about.
krajo (Grafana Labs) 00:43:47 That's the one thing that… Like, so… The way you anchored the… IDs, and the keys are… Just, comma separated the strand.
David Ashpole (Google LLC) 00:44:04 Yep.
It's not, like, amazingly ergonomic, but… It seems like the best we can do.
krajo (Grafana Labs) 00:44:22 Isn't there… A spec on how to… Inc. code… Arrays.
David Ashpole (Google LLC) 00:44:34 Yes, there is.
krajo (Grafana Labs) 00:44:44 I'm just wondering if someone would… Argue that we shouldn't make up new encoding and just follow But… It was something to do with…
David Ashpole (Google LLC) 00:45:19 This is me.
I know that guy.
Okay, it's in common.
I was like, where is it?
What the heck?
Mapping to RTLP, there we go.
krajo (Grafana Labs) 00:45:56 Yeah, I'm sure I saw it somewhere, like a general… Discussion of how to encode Veer things in.
David Ashpole (Google LLC) 00:46:06 Actually, I can assertion.
krajo (Grafana Labs) 00:46:07 Things, basically.
David Ashpole (Google LLC) 00:46:08 JSON…
krajo (Grafana Labs) 00:46:10 Yeah, maybe Jason.
David Ashpole (Google LLC) 00:46:23 Raise…
krajo (Grafana Labs) 00:46:26 Yeah.
Yeah, that's the thing that I was remembering.
So…
David Ashpole (Google LLC) 00:46:37 Let's make sure this follows that, I think, is the…
krajo (Grafana Labs) 00:46:41 I think that makes sense, even though, like.
I agree that it looks, like, neat to have just the commas, but, like, probably want to be… consistent… Across the board.
Yeah, just, you know… Try and see how it looks.
David Ashpole (Google LLC) 00:47:19 Sun amaze.
That's, that's definitely something we can do.
Anything else?
krajo (Grafana Labs) 00:47:41 Fyi, there's a new change coming to the MTT spec.
To add, the scope type and scope.
Two entities?
But I think it fits…
David Ashpole (Google LLC) 00:47:56 I mean, yeah, it fits this well.
krajo (Grafana Labs) 00:47:59 Yeah, it fits as well, it… yeah,
David Ashpole (Google LLC) 00:48:02 Oh yeah, this is Dimitri's thing, right?
krajo (Grafana Labs) 00:48:04 Yeah, and you know that he's… Chris…
David Ashpole (Google LLC) 00:48:08 Meetings.
krajo (Grafana Labs) 00:48:08 block, yeah, and, yeah.
And… never to be seen again, basically. What was the gist I got?
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:48:24 His colleague was gonna take over, right?
krajo (Grafana Labs) 00:48:27 Yeah.
But we'll see. I mean… Oh, question.
David Ashpole (Google LLC) 00:48:34 Okay, cool, that's good feedback.
Cool.
What else? We're already tracking all these… What's left? Oh, are we tracking… Arthur's not here, but it sounded like… We were interested in changing the default for translation strategy.
I don't know if you want.
krajo (Grafana Labs) 00:49:02 Yeah, that's the thing that I would have liked to discuss here.
David Ashpole (Google LLC) 00:49:05 Okay.
I will open an issue. How about that?
Okay.
krajo (Grafana Labs) 00:49:10 Sounds good.
Yeah, auto-repending issue for… Prometus… And I put it into the 4.0 project, so that's tracked there.
I'm also… well, this is a little bit underrated, but I'm thinking of Putting an issue in… 4.0 to have OpenMatrix 2.
enabled.
That would be nice to achieve.
David Ashpole (Google LLC) 00:49:45 Inc.
krajo (Grafana Labs) 00:49:52 My manager's going to notice that.
I've been… I've been reporting on this stabilization for more than half a year now, and now we add another issue. That's… that's going to go down well.
No, I'm just joking.
David Ashpole (Google LLC) 00:50:10 I feel like… the hard issues are the ones where people disagree. I think if everybody just agrees on this, then it'll happen.
Quickly.
krajo (Grafana Labs) 00:50:19 Yeah, yeah, yeah, yeah.
David Ashpole (Google LLC) 00:50:26 Promote them as metric labels.
So I think we… Was this already fixed by a different… This was fixed by your earlier PR.
Not by this one, right?
Like, we already specified.
remember where the previous one was. You had a separate PR that changed it so that service That the service ones get added.
Yeah, yeah, yeah.
Let's see if I can find that.
krajo (Grafana Labs) 00:50:57 Yeah, there's a PR on it in Prometus from an outside contributor, but… they are not responding to my comments, so I might take over and ask Arve to review. I'll just take their comments, and I'll By fixes to the tests that they did.
And then it would actually…
David Ashpole (Google LLC) 00:51:16 But I will go ahead and mark this as… Fixed by that? Is that good?
krajo (Grafana Labs) 00:51:26 I don't think I opened this, so…
David Ashpole (Google LLC) 00:51:30 Surreal. Surreal. Opened this a while ago.
They're no longer dropped. They're not added as metric labels.
I guess they are to target info.
krajo (Grafana Labs) 00:51:47 Yeah, I'm getting to the area, retaining the target info, yeah.
And again, 4.0 Prometheus would default to this.
Yep.
David Ashpole (Google LLC) 00:52:46 Hmm, this might be something we want to track on Prometheus?
So, OpenTelemetry has been using this include-exclude pattern.
For deciding which attributes to promote and which not to promote.
This is used in the declarative config.
I think… It might be… it sounds like it's worth… Sounds like it's maybe worth, Thinking about this for Prometheus 4.0.
Thoughts?
krajo (Grafana Labs) 00:53:35 I mean… I… I vary a little bit that it's too easy to shoot yourself in the foot with it. You provide some wildcard, and we have some limits on number of labels, I think 40 for targeting for, but I mean, I'm not the best person, too.
Say here, to be honest.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:53:58 I also think it's a really ugly idea.
But I don't know what users… are calling for, if you see what I mean.
I did accept this option to… To promote all resource attributes by default, and then just say which not to… which not to promote.
I think it was a horrible idea, but it was, you know, it was… someone wanted it, so I merged the PR to do it.
So I have the same, you know, like, gut instinct about this, that it's, like, Someday that's definitely not recommended for the… for kind of the reasons that Garyo mentioned.
But… but if people, you know, absolutely want this, And if it's important to be, consistent with Auto on this, you know, it can be done, of course, but I would not recommend doing it. Or using this option, if you see what I mean.
David Ashpole (Google LLC) 00:54:55 I think this is maybe just about the configuration pattern.
Like, it sounds like you already mostly support Or do you… yeah, you already support an exclude list?
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:55:10 of, like…
David Ashpole (Google LLC) 00:55:11 include all of them and exclude. So, I think… I think the ask is… the question for us is, should we try and… standardize… The configuration option for this, so that it looks the same on… the SDK exporter on Prometheus. That's the only question.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:55:28 I spent to you.
Isn't a difference, the support for pattern matching?
Or am I miss, getting something wrong?
David Ashpole (Google LLC) 00:55:39 Are you familiar at all with the include-exclude?
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:55:43 This is from Hotel.
David Ashpole (Google LLC) 00:55:45 So this is from the declarative configuration thing.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:55:48 Yeah.
David Ashpole (Google LLC) 00:55:49 It's… it's reused.
anytime there's, like, a SDK component, like metric views, or… Resource detectors.
Deciding which resource attributes to detect or not to detect.
It has this glob.
pattern, where… Question mark, not just a single.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:56:09 Yum.
David Ashpole (Google LLC) 00:56:09 star matches many, right? So it's… all it is is, like, a standard for how to choose from a list of things.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:56:17 What?
David Ashpole (Google LLC) 00:56:18 What to include and what to exclude.
I think it's… the question for us is just, do we want to adopt that in our… Configuration… spec, and have Prometheus adopt that in 4.0, or do we not.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:56:30 I think I understood that. So, what would be new, you know, in practical terms to Prometheus would be the support for pattern matching, right?
I mean, pattern must be saying which, which, resource attributes to promote.
David Ashpole (Google LLC) 00:56:49 Right, so you could say, I want service.star.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:56:52 Yeah.
David Ashpole (Google LLC) 00:56:53 Instead of having to say… so that… It seems potentially useful to me.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:57:01 Yeah, yeah, so I think I… I think I understood, so I'm… that's kind of what I was thinking, about, like, whether to… The Prometheus should support patterns in which research attributes to promote or not to promote.
I think it's like a food gun, that's what I think. I think Kikra agrees with me. So, but as I said, you know, if people absolutely want this, you know, then… he should probably support ISC.
just like I, you know, I approved, supporting, promoting all attributes by default, or not, well, not by default, if you enable it.
Like, I think that's a terrible sitcom, but people want it, so… So I was okay with it. So I just have the same gut instinct about this.
David Ashpole (Google LLC) 00:57:59 I… I feel like this is less of a foot gun than the… Do everything and have an exclude list.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:58:05 Hmm.
David Ashpole (Google LLC) 00:58:06 Potentially.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:58:07 I agree, I think it's, you know, it's more surgical.
So it's, I agree, I agree, it's less of a fit gun. So, I think… just in my opinion, you should just, like, weigh, you know, you know, A, how many people, or how, how desired, or… how important is this to users? And B, How important is it to, to, to harmonize with OpenTelemetry on this.
So that's just… I'm just seeing, you know, I'm just seeing the pros and cons, that's all.
David Ashpole (Google LLC) 00:58:40 Yep.
krajo (Grafana Labs) 00:58:41 Yep, I agree.
David Ashpole (Google LLC) 00:58:44 As, as a plan forward, I'll plan to survey… What all of the existing… Prometheus… no. All the existing OTEL to Prometheus converters do.
So we can see what the current state of the world is.
And I can propose… Or I can figure out what a spec would look like if we decided to do one, and then I'll open the issues, and we can discuss on the issues. So I'll put forward some proposal, and then we can decide if we want it or not. Does that sound reasonable?
Arve Knudsen (Raintank, Inc. – Grafana Labs) 00:59:28 Yes, to me, to me, it sounds reasonable.
krajo (Grafana Labs) 01:00:51 We use the project in GitHub, not Milestone.
Just… Yeah, yeah, yeah, don't look… don't look for milestone, because it's the…
David Ashpole (Google LLC) 01:01:33 Check.
And we have 2 minutes left, so I'm gonna stop here.
Cool.
Awesome. Well, I will be out next week. I'm not sure if we want to cancel.
Actually, I might not be out. No, I'm gonna be out. I'm taking Friday off, after KubeCon.
I'm… In my defense, I'm working on Sunday, so… For the maintainer day.
Bye.
krajo (Grafana Labs) 01:02:02 I could use a week where I focus on some stuff, so I'm okay to cancel.
Next, next Friday.
David Ashpole (Google LLC) 01:02:15 Leave a message in there.
Oh no, I just saw Arthur's message. Okay, well, thanks everyone for joining. I'll put a message in Slack so we can cancel for next week, and I'll see everyone in two weeks.
Arve Knudsen (Raintank, Inc. – Grafana Labs) 01:02:31 Peel, bye-bye.
