SIG: Technical Committee
Date: 2026-04-22
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**Reiley** 00:23 Hey, Chuck. Josh.
**Jack Berg** 00:27 Hi, Riley and Josh.
**jmacdonald** 00:31 Hello.
Alright, I'm on call this week. I think that means I run a meeting. This meeting, too.
**Jack Berg** 00:45 That's right.
**jmacdonald** 00:46 Let me get there.
Cool.
**Jack Berg** 01:12 I'll take it, Denise.
**jmacdonald** 01:13 Say that again?
**Jack Berg** 01:14 I'll do the attendees, just, we're typing over each other.
**jmacdonald** 01:18 Oh, I haven't started. Someone's typing, I see. Riley's typing. Alright, so… This is gonna require me to get a little bit more concrete about what we do with TC triage, and then I have a topic.
It's the same topic.
the… Wait a second.
Which browser am I in? Dammit.
I have… I have to use Firefox when I'm using Google Docs.
I'll be back.
Sorry.
Hong… there it is.
Microsoft, Firefox, there we go.
Bam.
See, I don't accept my own suggestion.
Alright, my topic is to talk about the security advisories, which are flooding us this week, and probably last week.
Okay.
**Josh Suereth** 02:29 That's what I wanted to talk about, too.
**jmacdonald** 02:30 We're all on the same topic, then. Let's make sure that I know how to run us through the triage. I'm looking at the spec inbox.
No results.
I'm looking at the community inbox.
No results.
**Josh Suereth** 02:46 Oh, for the community, I added automation that will throw things into our inbox, but I got my permissions wrong in my GitHub action.
So, it broke.
Which I think means there's a community issue we need to look at. Because I… yeah.
**jmacdonald** 03:03 Got it.
**Josh Suereth** 03:03 It just… it didn't get assigned to us automatically, I think.
Or… yeah…
**jmacdonald** 03:11 Are we looking for a, particular label?
**Josh Suereth** 03:15 Yeah, we're looking for project proposals or donation proposals.
OCB Brew Tap, is that… did we already look at that one?
**jmacdonald** 03:27 I've heard of that.
**Josh Suereth** 03:32 The donation proposal, that was a month ago, though, that wouldn't have been recently.
**jmacdonald** 03:40 This is… part of packaging SIG.
Like, in some sense.
All right, well, let's… I mean, we have 4 people. I know that we're not really at the quorum we want, I suppose.
But it's now time to start.
**Jack Berg** 04:04 By the way, I'm going through, unassigned issues in the spec repo, and… assigning obvious candidates. I'll leave ones that maybe warrant discussions, but just making our time useful.
**jmacdonald** 04:16 Great. Well, let's just triage these then. It looks like we didn't find anything in the community, Josh.
Anything new?
**Josh Suereth** 04:23 Yeah, although, if you saw the comments on the one we were looking at, it had a bunch of stuff about how the TC doesn't have time to sponsor us, and we… I think Bella made an update 3 weeks ago.
Yep.
Yeah… I still think we need to respond to this eventually, and triage it.
But… without Ludmila, I don't… I don't know, like, exactly the… the state of it. I didn't look into details, it just… this seems like something we should be triaging.
**jmacdonald** 04:57 to me, it seems like yet another call for a packaging SIG, but it's not… I see the distinction as a decision about whether this belongs in packaging SIG, which doesn't exist.
**Josh Suereth** 05:07 I see.
Okay, so you're saying that we should basically mark this as triaged, and that the proposal is part of the packaging SIG proposal that's already being reviewed?
**jmacdonald** 05:19 I think that would make sense to me.
**Josh Suereth** 05:21 Okay.
**jmacdonald** 05:22 Is there a label for that sort of declaration?
**Josh Suereth** 05:24 Yeah, we added, if you look, if you just type triage, I think there's, like.
**jmacdonald** 05:31 Deciding? No.
**Josh Suereth** 05:32 Not deciding… Was there one for… just look at TC, I guess? Maybe… What did I do?
**Armin (Dynatrace)** 05:42 It might be from the spec repo?
They might have different…
**jmacdonald** 05:48 Oh, we're in the… we're in the community, repo, which maybe doesn't have that repo, that tag, that label.
**Josh Suereth** 05:54 It did, I added some… I'll look it up offline. I'll tell you, I'll take care of that one.
**jmacdonald** 05:59 Okay.
**Josh Suereth** 06:00 Because I think, unless anyone disagrees with, like, the phrasing, I'll just respond to it, of, like, how we're thinking about it.
**jmacdonald** 06:05 Okay.
**Josh Suereth** 06:06 Make sure it's triaged.
**jmacdonald** 06:08 I'll let you do that.
**Josh Suereth** 06:09 Cool.
**jmacdonald** 06:09 Back to the unassigned… Spec issue question.
Okay, we have 30 PRs… whoa.
But 9 of them need… Assignees.
I'll assign this one to myself.
Not what I can do.
**Jack Berg** 06:31 Already did it.
**jmacdonald** 06:32 You did, thank you.
Let's see… CJ's got a bunch of stuff here.
What should our process be? Should we just, like, round robin this stuff?
We used to do that. We shouldn't do that. We used to do that automatically.
**Jack Berg** 06:53 It's sort of topical, you know, so if there's some TC member that's obviously engaging on it, like.
you know, continue engaging, and just assign them to be the person that's gonna work for it. And then, you know, if it's a topic that one of us obviously covers, like entities for Josh.
Integrin, sampling for you, Josh, config for me, Prometheus for David, things like that. That's obvious. And then everything that's left over that's sort of, like, shared ownership, like.
the metric signal. A bunch of us can work on that. You know, tracing as a signal, logging as a signal, things like that. You know, we just look kind of… we look for volunteers.
**jmacdonald** 07:37 Yeah. David, I just assigned a couple that were metrics to you, but I could have gone either way on that one. They looked… they looked… Great.
**David Ashpole** 07:45 Cool.
**jmacdonald** 07:46 Who cares about environment variable carriers?
**Carlos Alberto Cortez** 07:52 I could take care of that, although Riley is already, involved in that. I don't know if you want to I can do that, or you. It's up to you.
**Reiley** 08:04 Oh, so… The ask here is, people want to explicitly specify this component covered by the spec should also be implemented in the OpenTelemetry minus XYZ language repository instead of OpenTelemetry minus XYZ language minus contribute repo. Well.
I don't think the spec dictates how the maintainers should organize, like, they want to call that, like, open telemetry minus like, C++ minus Riley, like, we don't care, right? So we don't have that guidance how, like, maintainers should treat the quote-unquote core repo versus contribute, or they have, like, multiple things. So.
I don't feel this is something the SPAC should cover. Instead.
This is something maybe we should put in a community report, gave the maintainers, like, guidelines.
Like, I don't see why the spike would want to see… you want to organize the component based on contribute versus not contribute, and this particular thing should be in contribute. My thinking is, everything in the spike is, like.
you need to follow the spec, you need to declare whether you're compliant or not, and if you want to put that in a monorepo, like 5 different repositories, we don't care from the spec.
Yeah, so the direction, like, the… like, Robert is trying to introduce this core versus contribute in the spec, which is concerning. I think the intention is good, but the way how we do it is probably wrong.
**jmacdonald** 09:42 Do you have a proposal on what to do about it, Riley?
**Carlos Alberto Cortez** 09:44 Like, yeah, that's what I wanted to ask, like, I think we don't have to discuss the details, here, or make a decision, but, either you or me can just, you know, become the assignees, so we make progress on that, one way or another.
**Reiley** 09:57 Assigned to me, I'm already on this.
**Carlos Alberto Cortez** 10:00 We're not…
**Reiley** 10:01 I have some idea how we can solve this.
**jmacdonald** 10:07 Alright.
**Carlos Alberto Cortez** 10:08 Thanks so much.
**jmacdonald** 10:11 And that will go through, hopefully… wow, we're down to 2. Move JSON object encoding for attribute debugging. Recommend.
**Jack Berg** 10:44 I think… I gotta read this closer, but I have a couple of questions about, like, kind of the applicability of this. So, it says, in non-OTLP and debugging contexts. So, like, would… Would Zipkin, Exporter be, like, a candidate for this, because it's non-OTLP?
like, if you're encoding value, any value attributes in Zipkin, is this applicable to that?
Is this applicable to, we have these standard out OTLP exporters that write OTLP JSON to files or standard out.
And those are obviously, you know, conformed to the OTLP and JSON encoding, but I think previous to these, we had these sort of, open-ended console exporters that just, like, are for debugging purposes and write data to the console, or standard out, in an unspecified format. It's just, like, whatever the language maintainers kind of come up with.
And, you know, is this applicable to that?
And then the other question is, like, toString. Like, you know, most languages have, like, you know, string representations of, you know, of data, and you can just, like, call printf or whatever.
And is this applicable to that? Like, what are the non-OTLP and debugging contexts that this is expected to apply to?
But… I don't know. I think we need to kind of hash that out in discussion, and maybe shouldn't spend a ton of time on it from a triaging perspective.
**jmacdonald** 12:37 Thank you. Yeah.
I… I also… it sounds like we're specifying what the debugging output should look like here, and I'm not sure what the benefits are.
But, true, I… I mean… I put, signee to David because he's approved it already, so that was easy. I don't know if, David, if you have a thought on this one.
**David Ashpole** 13:01 So… We have, like, a string function for values.
Right, that we use… that we actually use in a lot of exporters.
Prometheus Exporter being one of them that will, like, just call whatever the defined current string function is for, like, map types or list types.
And so… having that is nice, having it specified and consistent is nice. Like, the attributes package itself just has a string function.
Regardless of how it may or may not be used by exporters. And so, the next, like, logical step was, well, can we have a string function for… other… Types, and have it be somewhat consistent.
I think Go could definitely move forward and just define a string function for an attribute.
Without having it in the spec.
But it also seems nice.
To potentially have it, like, be somewhat consistent. I don't think this is a high-stakes… Thing. It's more of, like, wouldn't it be nice if we did the same thing?
I'm not sure if other languages already have gone down different paths, in which case I would probably say we could make this a may, or we could omit this… omit this entirely. But from Go's perspective.
It seems nice to write down how we're gonna print out attributes when we… You need to put them in error messages, or… Give them in test comparison output, or however… whatever we use it for.
**jmacdonald** 14:42 Anybody have, I guess, objections to that?
**Jack Berg** 14:46 I'm just… we should just focus on assignee, like, for now, because I think that, like, I do want to have a discussion on this. I think Trask had some opinions about this type of thing previously in the Java implementation, so I need to re-remember context, but David, if you're comfortable being assigned, then we'll just… Take care of it async.
**David Ashpole** 15:06 Okay.
**jmacdonald** 15:08 Alright, and we have an OCHAP So I'm not sure we… That's a different process for us, yeah?
And this is not new.
It's just unassigned, but we're supposed to be unassigned, right? With OTEPs.
**Jack Berg** 15:25 What we've said previously is that, like, you know, OTEPs are for all of us to consider collectively, and it's kind of an unfair burden to put them on one person.
**jmacdonald** 15:34 Yeah.
I would be willing to read this and look at it, for sure. We should all.
if I… it looks like a minor extension on top of 4719, which maybe… maybe makes me think that, you know, this… this will just happen when… when we settle 4719.
Okay, I don't think we need to do anything more on that triage step.
We'll leave the one.
OTEP. People should read it.
Yeah, okay. Looks like there's a request for a private call.
I support that.
Alright, we're gonna join a private call. See you very soon, people.
**Josh Suereth** 16:25 See you over there.
**Carlos Alberto Cortez** 16:27 So…
