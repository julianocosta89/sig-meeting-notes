SIG: Go SIG
Date: 2026-06-04
Duration: 14 minutes
============================================================

## Zoom Recording Transcript

**Bryan Boreham** 00:22 You know.
**Tyler** 00:23 Hey!
**Kathie Huang** 00:24 Hello…
**Tyler** 00:25 How y'all doing?
**Kathie Huang** 00:27 Good, how are you?
**Tyler** 00:29 Good, good.
just, jumping in here really quick, trying to get set up, but we can probably start in a little bit. I think, I know Robert's not showing up today, but maybe David is. Let me double-check on that, actually.
But yeah, we can probably jump in here a little bit. Katie, I see you have something on the agenda, so, welcome, by the way. I don't know, if this is true.
**Kathie Huang** 00:58 That was my first time.
**Tyler** 01:01 Cool. Awesome. Always happy to see new faces. And… I'll miss the first 30. Yeah, okay, alright, David won't be here.
Okay.
It's a bummer.
We can jump in here in just a second, then. If you haven't yet, go ahead and add your name to the, oof.
attendees list, and if you have other agenda items you wanted to talk about, go ahead and add them there as well.
I don't think Robert's showing up, but he's got an issue here, but okay.
Awesome. Okay.
Cool, alright, we could jump in here, I don't know exactly… What this is, let SDK users turn off panic reporting.
I'm guessing Roberts… Asking if this is probably okay.
Yeah, I mean, I… Robert's not here, so, I guess it's just, like, if people are interested in, this discussion, please take a look at this issue, and then, yeah. Otherwise, he can probably jump in next time he's here.
Okay, cool. Next up, Katie, you wanted to talk about, an issue here?
**Kathie Huang** 02:31 Yes, I have a PR for, adding the Azure… an Azure Container Apps Users Detector. Some people have, like, left reviews, and I've addressed all the comments, so I was wondering, like, what are, like, the next steps to keep this PR moving forward? Cause it's been about 3 weeks since the la- the last comments on this PR.
I'm not sure if any of the people who reviewed it are here to talk.
**Tyler** 02:57 Yeah, that Mr. Alias is talking to you. let's see… Yeah, David is not here, this is Dashpole.
he is the one who's gonna be late to this meeting. I'm… I'm this guy, is what I was trying to say. Yeah. But I can… I can take another look. Sorry, I'm just coming back from, like, 2 weeks of being off, so, apologize for the delay here.
But yeah, it looks like you've got a code owner, which is, I think, kind of the important thing. And then, yeah, we can take a look at, getting this reviewed.
I can take a look at this again. I think David also is taking a look, so he can… I'm sure he's pretty active. I don't think I need to ping him, but yeah, we can take a look at this.
I think, this is… yeah, Israel.
**Kathie Huang** 03:49 physical.
**Tyler** 03:50 This is a… Hmm.
Who did you have as the code owner?
**Kathie Huang** 03:55 I think it was Israel. Yeah, he offered himself as code owner. Okay. So, maybe I'll ping him.
**Tyler** 04:02 Yeah, I think if… that'd probably be a great place to start, having the code owner, give it a review as well, and then, yeah, I think I can also take a look at that. We do require two, approvals, I guess?
I don't know… One of them has to be the code owner, given the fact this is also introducing the code owner. I don't know if there's, like, a policy thing there, but, anyways, like, David's also taking a look at this, so that should be enough. See, Sam's also on the call, if you wanted to also take a look at this, but we can… yeah, we can…
**Sam Xie** 04:33 I can take a lisp.
**Tyler** 04:35 Take a look, yeah.
**Kathie Huang** 04:36 Appreciate it.
**Tyler** 04:37 Yep.
Okay, cool. Yeah, we'll… we'll try our best to get after this. See?
**Kathie Huang** 04:43 appreciation. Yes.
**Tyler** 04:44 Yeah, thanks for the contribution.
**Kathie Huang** 04:46 So, yeah.
**Tyler** 04:48 Okay, next up is me. I wanted to mention that the Auto SDK package, which is something that we actually depend on at the, I didn't realize this, but, like, we actually are depending on this, so this is the thing that we use to integrate with the… OpenTelemetry Go Auto, instrumentation right now, which is great, and technically, I think we also use it to integrate with Obi, right now, and so that if there's no SDK backing our global API, this'll start just… Integrating with that, It's a pretty awesome feature. There's a talk or two on this one. So I think, like, we want to keep supporting this. The thing is, is that they go auto… project is actually gonna go into a deprecation soon, so… I wanted to just fork it, and just move it over here. We're, I think, the only one that actually uses this outside of the Go Auto package, so, probably just put this in an internal package, and then if, eventually, if somebody needs this, we could maybe look at finding a new home for it externally, but… Yeah, if there's any opposition to that idea, let me know. I can start working on this probably next week. I don't imagine the deprecation happening for a few months, so… We're well ahead of this, just decided today.
**Bryan Boreham** 05:59 Is the… is it moving to a different project, or going away entirely?
**Tyler** 06:04 The Go Auto Project?
**Bryan Boreham** 06:05 Well, I guess I don't… I don't know which thing is moving where, or…
**Tyler** 06:10 Yeah, there's a lot of moving pieces. Hence the problem, actually. You're kind of highlighting it. So, yeah, so the Go Auto project was… it's, EVPF-based instrumentation for Go, and it's very specific in its formulation.
Baylor was forked from this. It was completely revamped and changed a lot of, like, the protocol stuff. Bailo was then re-donated back as OBI, to OpenTelemetry. So, essentially, like, this is, like, the precursor as an, you know, to Obi.
Obi's sticking around. OB's gonna stay around. This project, the Go Auto, is not. This is something that has lost a lot of development of velocity here, so… We're trying to, you know, make it clear that this is not being supported anymore.
So, we are going to unify in the open telemetry space on Obi, going forward. Obi provides instrumentation for Go, using eBPF, and it, is not a full, you know, replacement, but there's a whole suite of things we've discussed this morning around, like.
what we want to do to get that full replacement, including things in the, operator we want to support there. There's this auto-instrumentation stuff, which is, like, this integration with manual spans.
And a host of other things as well. There's other vendors who depend on this. So, yeah, there's a whole list of things that are coming along on this one, but one of them was the fact that, like, we integrate with the global API through this, this package.
And I think we want to keep doing that, because Obi will still keep doing that, which is great. It's… It's actually extremely powerful, to be able to switch businesses.
**Bryan Boreham** 07:46 That's what I was trying.
So, I put a note in the notes, correct me if I'm wrong, so the kind of broad focus has moved to OB, But this thing, GoAuto, does some things that Obi doesn't do today.
**Tyler** 08:01 Yeah. Yeah, exactly. So, yeah, it's essentially like, I don't want to say it's, like, a tuned-down version, but it's, like, it's a pared-down, so, like, the idea is that, like, you can run this, I think, a little bit… a lot cleaner as, like, a sidecar, because it's really designed around to be, like, this very standalone thing, and it's very, like… Go-specific, like, all of the EBPF probes that are in there are, like, around Go libraries and Go instrumentation and stuff.
OB is, like, a protocol-based, instrumentation, so, like, it'll instrument all these other languages, it'll instrument, I mean, pretty much any service that speaks HTTP, gRPC, Kafka, I mean, like.
caveats included there, of course. But, but yes, like, so this is, I think, more of a Go-specific project.
it was the, you know, the precursor to Obi, so we do try to support all of, like, the backwards compatible, like, telemetry that's there. The way we do it is a little different in Obi.
But yeah, so getting rid of this, like, and pushing users to use Obi, like, from a user's perspective, like, from an end user's perspective.
I'd say 80… more likely 95% of all use cases, like, they won't notice it. If you're using the operator right now, the operator only runs, auto interpretation with this project, as an experimental feature, not by default, by the way, as a sidecar. Obi is, like, it can be run as a sidecar, it's just not optimal to be run as a sidecar. It does a lot better as a daemon set, where it can orchestrate across, you know, a whole host of things, but there's nothing stopping it.
So there's, like, things like that, like, so, orchestration layer stuff, dynamic configuration is another big one, so people that were trying to run this, like, without restarting the OB process, it's something that we are actively working on there as well.
I'm trying to think what else we discussed, like, obviously this auto SDK stuff, so, yeah, there's, like, there's small, details around it, like… Functionality-wise, from the end user's perspective, doesn't… there's actually a pretty solid compatibility story, where, like, it's almost a one-for-one, Which is, again, like, back to your original question, Brian, like, what is it for? Like, there's overlap there, is the problem, and so having a clear understanding and picture for users on, like, what we want to direct them to is kind of the goal here as well, yeah.
**Puneet Singh** 10:27 I'm not sure if I heard it right, but in the Kubernetes SIG meeting, I also heard a discussion about this particular Auto SDK being, like, there was a discussion regarding removing the support, because there was a concern on the lack of releases, and any recent updates. So, currently, the… Decision has been postponed, but they are currently kind of looking as in what is the next step to take, whether to support this operator or not, so… I suppose that is connected.
**Tyler** 11:00 Yeah, that's, I think, also one of the other things, Yeah, I'm trying to look. I don't think that… so the… the Kubernetes… I… I don't know… They… they directly import?
This auto SDK?
**Puneet Singh** 11:20 I'm not sure about that, but it was just, I think right before this meeting was mentioned, so I thought it was worth mentioning.
**Tyler** 11:28 Oh, okay. Yeah, I definitely know that, like, the Odigos guys have used a lot of this integration with this auto SDK and, like, the interoperability of manual spans, because, like.
Kubernetes API actually has a bunch of manual spans, and then if you run, like, the EVPF instrumentation underneath it, it works really well together. It's kind of like the whole… that's what I'm trying to say, like, it's a phenomenal, like, project.
I imagine they are… I don't… they're probably more talking about the Go Auto project, not the Auto SDK, like, package itself. So, yeah, I imagine, like, if they were trying to use that, which I didn't… I didn't… I don't think that they do, but… they should switch to Obi, is the answer there. And then if they're… they're specifically talking about the auto SDK, like, package that backs it, that's another question. There's definitely not a lot of releases there because it's really stable, it does very little. It's a shim. It literally is a no-op shim that, like, kind of puts data in the right form, so that eBPF instrumentation can find it. It's not… it doesn't actually have, like… it has no functionality. It's more just about, like, exposing data in the correct form, so that's why you see very little, like, development activity there, because it… Once it's in that form, honestly, you don't want to change it, and then two, like, there really isn't any functional, like, behavior at all, so, But, hence why forking it over here is something I think we can do. The only place that it's actually really used is in the Go Auto package.
which would, you know, essentially was there just to own it, because that's where it was, like, mainly, like, developed. But here in the global API is, like, the main place it needs to actually be set up. So, I guess if there's other… Go APIs that want to be backed by this, they could manually add it, but it's a very, very niche, like, component, is what it is, so… Yeah, I'm definitely, like, if the Kubernetes thing is interested in switching to OBI, like, that… I would support that, we'd want to hear a lot of feedback on that.
If they're directly depending on this package, I would definitely need to know that. I don't see it in any import lists in the package.dev, so, yeah.
**Puneet Singh** 13:30 I'll follow it up just to get more clear, on this, actually.
**Tyler** 13:35 Yeah, I mean, there's no problem if that's the case, it's just that, like, I wouldn't want to fork it to an internal place here, which is what I plan to do.
It's just, yeah, I guess that's kind of more my question.
But yeah, so that's… that's just a heads up on that one. I'll probably create an issue to do this, and then… Yeah, I'm looking… yeah, I don't see it anywhere. Okay.
Yeah, that should be it.
Okay.
That's the end of the agenda.
That has been written. I see a few other folks have added, or have joined the call, so maybe we can pause here if anybody had other topics they wanted to talk about.
Questions, concerns?
Wish I had more for you, I'm still wading through 800 notifications, sister. Get back.
But cool. Alright, if not, we can end the meeting early here. As always, reach out on Slack if you have more questions, more time to go review Katie's PR as well.
Awesome.
Good seeing you, everyone. I'll see you all in a week's time. Until then, bye.
**Puneet Singh** 14:50 Okay.
