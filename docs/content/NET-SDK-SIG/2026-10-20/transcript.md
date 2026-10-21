SIG: .NET SDK SIG
Date: 2026-10-20
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 00:22 Helen.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 00:26 Hey.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 00:31 Non-zero chance it's just us, since… guess Alan's… -Oh.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 00:36 Oh, yeah, of course.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 00:40 And I know Raj said he'd be spending his time between this and, I guess, Rust or something, so…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 00:48 Yeah, Sophie was here last week.
Was he here last week?
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 00:53 Think so.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 00:56 Hey, Navya.
**Navya Sharma** 00:58 Alright.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:28 Let me share my screen.
Cool, so there's not much… on the Kinder… Probably won't take long to go through.
Any other Meetings are here, so… enabled the… Mentioned last week, I submitted a PR for the Anthropic scanner.
They scanned it before they merged the PR, so it was slightly unexpected. Excuse me.
So we got the scans on… Friday overnight?
There was nothing in there that we thought was important enough to need to request CVEs for.
But, all the fixes for the things that was found, almost all of which were low, were next day in 120.1.
There's a bunch of bugs it found as well that I'm gonna try and get fixed.
For the next release, but they're not urgent.
someone from the GC, no, TC, sorry, has asked us to try and set up a email alias.
To be the CC for those, I need to chase someone on how do we get that set up, instead of having the individual names.
And I'm gonna onboard Contrip to the same scanner once we've got to zero open Anthropic scanners on the SDK repo, just so we don't have… Two fire hoses of issues pointing us at the same time.
And then the only other thing I had related to that, or partially related to that, we were gonna… think about merging the .NET 11 PRs and doing a new release candidate this week. I'm wondering how long we should wait until I move those out of draft.
In case there's any more bugs.
from the Friday release, or the release today.
That's just an open question, really.
Anyone have any thoughts?
Feedback, thoughts on either of those items?
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 04:01 Well, let's see… the current release date for .NET 11 for GA is November 10th, it looks like.
So… We have a little bit of time, We held it for… Till the end of next week.
If we wanted to be extra sure, that would still be… Yeah, that'd still give a full week before the… 11 release.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:33 Maybe we'll give it till this time next week.
Just ask the same question again.
Because, yeah, the only… Thing with leaving it later.
is… How many people would actively actually install it and deploy it in their window?
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 04:56 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:00 But yeah, I'll, I'll defer that question to next week. Gonna leave it there. So, if there's any issues with today's release, hopefully we'll find out about them.
Tomorrow or the day after at the latest.
That was all I had on the agenda, Matt or Navya, have you got anything you'd like to discuss?
**Navya Sharma** 05:27 No, I think I joined in to… In case I…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:45 Have I accidentally muted my audio, or did you drop off then?
**Navya Sharma** 05:48 Can you hear me?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:49 Can he know?
**Navya Sharma** 05:52 Oh, sorry, yeah, I think I dropped off.
By mistake. But I was here just in case anybody had any reviews on my PR, but I don't think we were able to get to that, so that's fine.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:03 Yeah, I did get a message from CJO at the end of last week, that he knew that he had to look at it and was meaning to, but as he's in the middle of changing jobs, I guess he's been a bit busy.
**Navya Sharma** 06:17 Yep.
Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:19 He does, he does know.
**Navya Sharma** 06:23 Yes, thank you, I appreciate it.
Also, is there any… if there's any, issues… I haven't been seeing a lot of help-wanted issues.
I'm just wondering if there'd be more to come.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:37 There's none I'm aware of right now.
The one… there's a few recently opened issues, don't have Help Wanted on them yet, because they're waiting on something somewhere else.
So is there a decision on, like, which, which, which of, like, two options should be taken?
Or they're waiting on, like, a spec change somewhere.
But, yeah, we do try and mark them as help wanted when stuff comes along. But also, if there's… things… use… C that might, like, be, like, obvious things to change.
that we just don't have an issue about, then feel free to, like, you know, propose a PR, or open an issue about it.
I can't think of an example off the top of my head. For example, there was a minor PR got opened today by one of the other approvers.
To, like, update a bit of out-of-date documentation.
And so, if there's anything…
**Navya Sharma** 07:46 Oh, okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:46 If there's ever anything you spot, it might just be lurking, and we haven't necessarily create an issue to track it. Because sometimes when stuff gets found.
I don't know about the others, but I'm like this. If I find a problem and it's quick to solve, I'll just fix it, because it's as much effort as opening an issue asking for someone else to fix it.
**Navya Sharma** 08:10 Yeah.
Makes sense, yeah.
I just haven't… I think… I haven't also been… On top of it, but yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:20 No, no, that's cool.
**Navya Sharma** 08:22 In the.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:24 Always, always glad of people to get involved, and also, just reviewing, reviewing or chipping… chiming in on other people's issues or poor requests.
Like, the more room area is fine.
**Navya Sharma** 08:38 Okay, I actually was not, I didn't know… what the appropriate, review thing was there, because there are, like, set reviewers as well, right? So I wasn't sure if it was kosher to just review anybody else's PR.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:57 So, if… feel free to, like, take a look at other people's PRs, like, it's… it's also a way of learning.
But, like, if, like, something's, like, trivial, then it's maybe not necessarily worth the rubber stamp, but if something's not clear.
Or you have a question about it.
Feel free to comment on a PR and ask the question on it.
It might be you've spotted something that didn't… someone didn't think of.
**Navya Sharma** 09:28 Gotcha.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 09:30 Especially, more eyes are always good, and things like, hey, we're changing how histogram buckets are… managed, and it's… the math is, not easy. So, more people looking at that is always great, stuff like that.
**Navya Sharma** 09:47 Gotcha, yeah. I have been looking at it, but just not dropping comments. I'll probably just continue doing that.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:55 Yeah, that's fine. Cause, because also, as well, you know, like.
if there's a PR that keeps falling through the gaps and no one looks at it for, like, 3 weeks, and then there's a really obvious problem someone's missed.
if you were to look at something earlier, then that would be like, oh yeah, that was an obvious mistake, I'll fix that. So even though it might not necessarily get it merged faster. It at least gets the wheel of PR review and comment addressing.
**Navya Sharma** 10:29 Right.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 10:34 Let's have a quick look at the issue dashboard. Oh, the PR dashboard as well, to see if there's anything… of interests.
And we compare it.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 10:46 It's something to think about for next week while you pull this up, Martin, for the .NET 11 PRs. I know, obviously, we're going to be dropping support for end-of-life runtimes.
Didn't know if we, with this Anthropic scanning, we might end up backporting some patches.
I know we typically have avoided that, but…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:07 I'll reach… I… while I went for my dinner, I had Claude whirring away on… the… the bug ones, but I haven't… I haven't looked at what it's done yet. If there's anything… that seems important, we could do another patch release this week, but I think when I scan… read what was left over this morning, and I think Piotta had a look at it as well, that, there was nothing that seemed like it was important enough we'd need to worry about backporting. But yeah, ideally we don't have to deal with branches.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 11:47 Well, just a random thought, since so far these not been… super serious problems, I mean, they're more theoretical ones, but… never know.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:57 Yeah, I think the worst one we had was, If you sent too many scrape requests to the ASPNET Core Betrix endpoint, you could air-memory it.
But… You shouldn't be putting your metrics endpoint, you know, for randos to call anyway.
So, it was, like, one of those, yeah, you can do that, but you shouldn't be in the position where that's possible.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 12:25 Nope.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:31 Is there anything interesting here that's new?
I open… budget… these two.
might be worth anyone having any comments on. One of the Anthropic scan results?
was about… Verifying the permissions on the directory where the experimental disk retry stuff lives.
I intentionally left that out of today's release, because it's a braking change, but Raj had some feedback on how it would just immediately break and start something using it from starting up, so if anyone's got any opinions… on… Sort of balancing the security improvement with not breaking people's stuff.
Feel free to chip in on the comments on there.
And… this is something I had Claude wearing away at for a while yesterday.
It looks like it's a big PR, but it's mostly moving… Test classes into… into collections.
Because… the CI seems quite slow, and historically, we've had it running in a, like, don't ever multi-thread anything mode.
So, I've tried to fix that and, get it so that you can basically run everything in parallel now, but it did require touching quite a lot of files.
But, if I just run .NET test on my laptop now, it takes 3 minutes to run every… all 25,000 tests.
Which is a definite improvement in wall clock time.
So, it'd be good to get some reviews on that, it's just… I'm just mentioning it because it's relatively big.
But hopefully it makes local dev loop faster.
This is also, just mention this one as well. His, This came out of one of the Anthropic scans, but, I don't know if it's a coincidence or not, but there happens to be a spec issue that got opened in the last week.
About the same topic?
which is… OTLP Explorer has, like, retry stuff baked in, but it didn't explicitly call out that the timeout should be for the whole set of any retries you might do.
Because some of the implementations at the moment re- kind of reset the timer when it does a retry.
We're in the naughty list.
So, that came up in the hand traffic scan.
But, we're just holding it back until this PR gets merged, so in case the spec does something different to what the fix does, and then we'd have to fix the behavior again.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 15:43 I don't think just .NET's on that list, I think it's everybody, right?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 15:46 I think it's everyone but one.
Oh, no, you're right, none. No one does it correctly, based on the, the spec change.
Maybe they're non-compliant to different degrees.
Sorry, did I interrupt someone then?
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 16:12 No, no, I just said yay.
I like the table down here, where you get into, here's the ones we checked, and all the ways they deviate, and… Yeah, I looked… I pulled it up.
Myself, it's like, none of these have the same behavior at all. Not just they're not compliant, like, it's all over the place, so… Those are my favorite spec issues.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 16:40 Yeah, so there's that one. I think everything else… It's mostly just… Unaddressed comments and merge conflicts.
And then over… check issues, because issue… that's the PR dashboard.
Hmm… it, it's… I mean… Rated since last week.
Yeah, so Steve opened an issue today.
Related to tweaking the hosting startup behavior.
I've got a comment on it, so it seems reasonable to me.
To at least try it out.
I think it could theoretically break someone, but I don't know if anyone is actually doing… any behaviors that would cause the problem with a slightly different startup order. But if anyone has, Opinions on that, feel free to comment on the issue.
And then we had a request from someone to support directly writing UTF-8 strings into the OTLP.
Exports.
It sounds reasonable to me on pa- paper, because this person seems to be… logging lots of JSON serialized attributes, so I can see why they would want to avoid the intermediate strings.
But the PR is… quite chunky.
So… I'm not… I'm not so sure on the implementation of it, but I had clunk food.
Take a look at it, and leave a bunch of feedback earlier, so… If anyone has any improvements on the… sorry, not improvements… opinions on the approach in this PR.
They'd be welcome.
Because it seems like a reasonable thing to do. It's just… I will.
Yay, buffers.
And in Contrope… There's a… that's waiting on Pure to… I think… are you still chatting with this person about the Kafka stuff, Matt?
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 19:08 Yeah, I need to leave a few comments, but I've been reading through it, trying to… make sure it all looks good. So, we're gonna get there. It's just… it's a lot of plumbing because of… Kafka happened. Producer and consumer APIs, and they're totally separate.
And the driver and everything, so you get to do everything twice.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 19:30 fun.
Okay, cool, there's a PR I've left some… I think someone is… where's the… It's like a link to, linked to, sort of… So, even though we did close this issue.
Someone's been doing some refactoring that would work us towards being able to do NoSQL sanitation. So, they've done a couple of PRs refactoring things so that we could move towards maybe doing it. So, I've been reviewing those, I think they're probably worth taking, but I don't know whether we'll actually go as far as, taking the NoSQL stuff.
Given the… I don't think the rest of the… database providers support it properly anyway? I forget the conversation we had in the original issue about whether or not we cared about it or not.
Yeah, that one. Configurable query text serialiser.
And was there any share?
No, and no new contributions.
So… Is there anything else anyone wants to chat about?
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 20:58 I don't have anything.
**Navya Sharma** 21:03 Me neither.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 21:05 Okay, cool. Let's call it… For today, then. Thanks for coming both. See you next time.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 21:12 Nope.
**Navya Sharma** 21:14 Thank you, bye.
