SIG: Swift SIG
Date: 2026-09-10
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Yasura Dodo** 01:09 Hello?
**Vishwan aranha** 01:11 Hey, guys.
**Bryce** 02:00 Hello!
**Vishwan aranha** 02:03 Hey, Bryce.
**Bryce** 02:04 How we doing?
**Vishwan aranha** 02:05 Pretty good, how about you?
**Bryce** 02:07 I'm doing well, thank you.
**Vishwan aranha** 02:11 This week, like, flew by, so…
**Bryce** 02:13 Yeah, I was like, wait a minute.
I swear that we just… we just had this meeting. It couldn't have been more than 7 days ago.
**Vishwan aranha** 02:22 Probably because of Labor Day, like, it was a long weekend, so…
**Bryce** 02:24 Yeah, yeah, Okay.
Oh, that's not… That's not right.
There we go.
We'll give a minute for Nacho to, join.
Others don't show them, alright.
**Nacho Bonafonte** 05:13 Oh, sorry, I'm a bit late.
**Bryce** 05:19 No worries.
All right, let's get started. So, topics from last week, issue cleanup.
I think we did a decent job. I spent some more time after the meeting and, removed a couple of additional issues that were… You know, already solved, or… not relevant anymore. So, we can keep an eye on that as well. I ran the GitHub LLM against it, and it didn't find anything else but issues that have existing PRs that can be closed once those are merged. So, that's good.
Vishwan, this was, in last week. I didn't see a topic on this added, is that… oh, here, your session…
**Vishwan aranha** 06:07 So, I think we discussed about the… just removing that async, but then, I got a few comments, and I, like, added all the information there, like, just wanted to do a quick follow-up, like, 1183 itself, like, now focuses on, like, explicit linked reset.
For, like, things like sign out and, like, account changes. So, it basically keeps the existing behavior where spans and logs refresh the session.
The only updates that I have done is, like, following the review that I got is, like, Are, like, very minor, so it doesn't change much of the existing, existing code, so is there anything else you'd like to change before it can, like, land, or any other questions you had, for that? And, I have added them in, three chained PRs, so that it's… one depends on the other, so it's… and the other two I have kept in draft, for obvious reasons, so it's like, if you guys have a chance to look at it and see if anything else needs to be updated on those PRs.
That'd be great.
**Bryce** 07:11 So, yeah, 1183 is the first one to look at, then.
**Vishwan aranha** 07:14 Yes.
**Bryce** 07:15 Okay, very good. Yeah, thank you for updating that. I'll take a look after the meeting, and then hopefully we can get that merged if there's no additional, changes requested. Have you had a chance to look at that Nacho?
**Nacho Bonafonte** 07:33 No, sorry, yeah, this… my personal laptop broke this week. So I have been, yeah, I have been just trying to, yeah, move most of my work to another.
Yeah. Yeah, for example, I had no Slack installed here, so that took me some time to get into it today, sorry.
**Bryce** 07:57 Okay.
No problem. I'll take a look as well. Alright, so, this next topic, Vishwan, did this get resolved last… last meeting? I don't remember discussing it.
**Vishwan aranha** 08:08 I think it was just discussing one of the PRs I had open for something, but I don't recall much about that, but yeah, I think it was resolved. I didn't have any follow-ups.
**Bryce** 08:18 I'll just… I'll remove it from the list then, so we don't get stumbled on again next week. Approver access for Ben and Vishwan.
Yeah, I think you guys have been contributing quite a bit, but maybe Nacho and Ari and I can discuss that a little bit more.
**Vishwan aranha** 08:37 I've been, like, reviewing all the PRs and cross-checking everything, so if… I just wanted to know, like, is there any, things we need… any criteria we need to meet to be approvers, or something like that?
**Bryce** 08:52 I don't think there's a strict set of rules that we have other than the general CNFC rules, so we'll take a look at those and, make a decision, but I think that we probably will err on the side of Adding you, for sure, because, you know, more help is always appreciated.
**Vishwan aranha** 09:14 Thank you, appreciate it.
**Bryce** 09:15 Yeah.
Session PR review, I think…
**Vishwan aranha** 09:19 It's the same one I discussed, so it's, like, this continuation of that.
**Bryce** 09:22 So we'll take a look at that one, And, alright, so let's skip over to HTTP Logs, metrics, Exporter, Bug Fixes, PR.
So… yeah, we have this one in the core, I saw, which it seems like a good idea. Is this, is this, Yasura's? Is this yours?
**Yasura Dodo** 09:42 Yes, it's mine.
**Bryce** 09:43 Yeah. Yeah, so we'll take a look at this as well, and, I think… to this question, we will do a release once the rest of this stuff lands, to get it all in one, one go, because it's gonna be our last CocoaPods release, barring any hotfixes that might necessarily need to go out.
Okay.
**Yasura Dodo** 10:07 Because, like, yeah, yeah, because, like, this is the kind of, like, the main thing that I want to do it for my project, and… Maybe, like, if he cannot release, I need to focus, but, like, at least, like, I like to get them to merge into the main branch, so easy to fork and easy to, release the new parts from my Octop, report.
Okay. Is it possible that we can merge in, maybe.
**Bryce** 10:38 Yeah, we could… we could do an intermediate one if it… if… if, one or the other, if these ones take too long, yeah, we can absolutely do that, that's no problem.
**Yasura Dodo** 10:48 Okay.
That's good. Thank you.
**Bryce** 11:13 Okay.
Alright, thread sanitization.
Oh, it's from… it's from Billy. Is Billy here?
Yeah. I guess it's just… who added these?
Maybe he's in… is he in the wrong, meeting, maybe?
**Billy Billy** 11:40 Amir.
**Bryce** 11:41 Oh, there you are. Oh, it's just the… oh my gosh.
I've never seen, our meeting so full.
You were off the end of the list, I didn't even know you were there.
Usually there's, like, 4 people in here, but…
**Billy Billy** 11:55 It's a… it's a new era.
**Bryce** 11:57 That's right.
Alright, thread sanitization. This resolves 53, wow.
Oh, but this is on core, okay.
I was like, that's an early issue.
Do you have anything to say about this, Billy?
**Billy Billy** 12:14 Just that I added, like, thread sanitizer approval workflow to both the repos. The core one is, kind of a long one, I would expect, like, you know, definitely need an extra pair of eyes on this one, and then, I also added it to the main repo, and the approval workflow just found, like, a couple of, like, small issues. I think someone spotted, like, one, When, like, small knit on the other one, but, yeah, I think this would be an approval, ACEL approval workflow going forward.
**Bryce** 12:50 Cool, yeah.
I'll take a look at that after the meeting. Nacho, if you could also take a look if you have the time.
That'd be… that'd be good.
Cool, dude.
**Nacho Bonafonte** 13:02 Yes, I will try to take a look, yeah.
Now I have counting all this working.
**Bryce** 13:11 Nice, alright, right on.
Thank you, thank you, Billy.
Alright, any other topics that we want to discuss today?
Maybe we can do a quick review of, any other newly opened PRs or issues?
**Vishwan aranha** 13:35 Also, regarding the cleanup, I saw a couple of tickets that were still open, so I did not… I took some of them to work on, and I update… I added a PR for one of the issues that I thought was necessary.
But, I wonder, like, there's still more left that need to be cleaned up, or anything that is obsolete now?
**Bryce** 13:58 from what I saw, I, I… I mean, there were a couple of things that, like, I wasn't really sure about that, if they were, obsolete or not, but I think it comes down to, like, the issue might need to be investigated, and then that determination needs to be made.
So, if it's open, I think that it's perfectly fine to pick up and dig into.
Yeah, was that one, was it this one here?
**Vishwan aranha** 14:27 Yes, yes, that's the one for OS logs, and I saw a couple of them from 22, 23-something, so I did not know, like, if that was, like, outdated.
This one started in 2024, but then I saw latest comments from February 13 as well, and I saw… and I went through the code and investigated and saw that it was still recent.
**Bryce** 14:51 I was supposed to use Vishwan Green West.
Yeah, Okay, yeah, cool.
And this doesn't have any problem with, like, Linux or anything. Yeah, seems like it's good.
Cool. Yeah, I'll take a closer look at that.
**Vishwan aranha** 15:27 Thanks.
**Bryce** 15:30 If you can.
Okay, so 2 days ago, that's your… That's the, sessions stuff there.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 15:45 Sessions one, I think it has two approvals, like, from non-maintainers.
**Bryce** 15:51 Okay, you know,
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 15:54 It's a… it's a small code change, just flushing But, yeah, bigger part is the test.
**Bryce** 16:03 Right, yeah, next… yeah, it's the chain… yeah, this… that's right, yep.
I remember seeing that. Was there a reason why… I thought that I proved this, but I suppose God.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 16:12 No, there was no approval, but I just pushed in a small change to the test, but…
**Bryce** 16:19 I see, I see, okay.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 16:20 Okay, yep.
**Bryce** 16:21 Alright, we'll get that approved and merged.
Thank you. And then add HTTP error-only response payloads… Yeah, I love the… love the activity. This is good. Sorry I haven't been able to approve these ad hoc.
Just been… my schedule's been tight recently.
But yeah, I think we definitely need to get some additional approvers in.
For sure.
So that we can speed these things along. You guys are definitely bottlenecked, it seems.
Cool, alright, let's look at the issues really quick.
So… I think payloads on YouTube.
We would like to keep recording spans and response metadata for every request while choosing between buffering all response payloads or buffering payloads for… oh, I see, okay, so should record payload, okay.
Okay, current behavior errors here, so I was trying… Turns true.
Is this… is this a bug, then? That the… The configuration is not respected, or…
**Nacho Bonafonte** 18:03 It's something that we broke recently. I see, okay.
**Bryce** 18:06 So it only… it only has a session available, right? Is that… so it's not able to actually check the HTTP response?
In the callback?
Or maybe it just is more convoluted, like, you need to cast it to a… But it's not even… it's just the session. It probably doesn't even have the active response on it, or the active request on it, does it?
**Nacho Bonafonte** 18:50 So he, he just wants to have more options.
So it's not something that broke, right?
**Bryce** 18:55 No, I don't think so, I think it's just the…
**Nacho Bonafonte** 18:57 It's just that he wants to add extra control, whether he wants the… Yeah. The record.
**Bryce** 19:04 Yep.
**Nacho Bonafonte** 19:05 Okay…
**Bryce** 19:08 Response payload record mode… So, all HTTP errors only, yeah. I think that's reasonable.
Okay, very good.
I like these issues that are opened and then come with PRs, that's, like, the best thing ever.
**Nacho Bonafonte** 19:27 Yes.
**Bryce** 19:29 And then… I think we already talked about this.
Yeah, here are the session stuff, and then that… Shouldn't record payload has… I think we've already… this is already… Yeah.
Oh, that's related.
I thought that this got fixed. The, the should record… oh, no, this is… this is the same thing, right?
Is this one up here? No.
Seems related.
I'll have to take a closer look at that. I thought that that was, I thought that that was, resolved.
And then there's the… the re-merge.
of OpenTelemetry Core. Okay.
Yeah, well, we'll take a closer look at that one. Let's hop over to SwiftCore.
Oh, no.
Alright, let's pop… let's look at the issues, so… Baggage propagators accepting unbounded inputs on extract. -Oh.
Love it.
**Nacho Bonafonte** 21:39 Yeah, that looks reasonable.
**Bryce** 21:41 Very straightforward him.
And here we have the tests here.
Cool.
Take a little bit of a closer look after the meeting, get that merged and approved, or approved and merged, whichever order.
And… I think that was the only new issue on here, yeah.
Cool.
Alright, anything else anybody wants to discuss?
No? Alright.
Get some time back today, then.
Alright.
Well, we'll get those… all these issues reviewed and merged.
**Vishwan aranha** 22:38 That's case.
**Bryce** 22:40 Alright.
Good rest of your week, everybody.
**Yasura Dodo** 22:44 Thank you, guys. Bye.
**Bryce** 22:45 Bye.
**Vinod Vydier (New Relic, Inc.)** 22:48 What?
