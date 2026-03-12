SIG: Technical Committee
Date: 2026-02-18
Duration: 29 minutes
Zoom Recording URL: https://zoom.us/rec/share/hY2JfIYctG1nckTz2MKtwufJory-wZYE307MjhzwhT7T42q0u3a1C4p_Dl6u4ME5.CllPWhxP-2TazI5_
============================================================

## Zoom Recording Transcript

**Reiley** 01:40 Hey, Tigran.
Hey, Roddy, good morning.
Funny.
**Josh Suereth** 02:09 Hey, everybody!
**Tigran Najaryan** 02:12 Hello.
**Reiley** 02:13 Morning, Josh.
**Josh Suereth** 02:28 Oh, I was muted. Tigrin, do you need access to the notes again on a different account?
**Tigran Najaryan** 02:34 I think you gave me access already?
**Josh Suereth** 02:39 Okay, I just accepted all your changes.
**Tigran Najaryan** 02:42 Yeah, this one… So, we no longer have corporate Google accounts.
So there's no way for me to… from my work machine to be logged into any Google account, unless I decide to use my personal Google account, which I don't want to do.
on my work machine, so whenever I'm on my work machine, I'm anonymous.
That's what is happening there. Sorry about that.
**Josh Suereth** 03:10 Yeah.
Alright, we have one topic, on the backlogs.
we'll wait for everyone to show up for this.
And then… what's the next one? It's, it's… I think it's funny, actually, the, the topic.
I believe it's one that… Oh, no.
Nevermind.
This is one we probably should discuss.
Do we have… how many people do we have? We don't have quorum yet.
Right.
We can at least sort of get started, but I would like to have, do we know if Carlos is coming?
I was hoping we could get some more folks from Open Tracing Community here for this discussion, but it's, Yeah, someone asked for us to deprecate the open tracing compatibility requirements.
So, for context.NET wants to deprecate their open tracing compatibility layer.
Opentracing has an… The last release of OpenTracing was in 2019. The organization's archived, Can we start, getting rid of the… our shim packages to open tracing?
**Tigran Najaryan** 04:53 I… I don't see any reason why not, but we'll probably need to move a bit slowly here, make an announcement. Like, we're planning to do something like that.
And ask for… for… Feedback or opinions?
on Slack channels, here and there.
let it boil, I guess, for a while, and if… And if there's no, like, specific feedback that it is being still used.
Then probably should go ahead, but let's not too abruptly.
**Jack Berg** 05:26 Yeah.
**Josh Suereth** 05:26 Absolutely agree. Go ahead, Jack.
**Jack Berg** 05:28 I think we follow the path that we've followed recently with deprecating things like, the Jaeger Exporter, Zipkin Exporter, OT, Trace Propagator, Jaeger Propagator, I think those are kind of similar in terms of, their kind of status in… in… how often they're used to this open tracing shim. Just, you know, I'm going to comment on this issue, but speaking as a maintainer for OpenTelemetry Java, we virtually never get issues related to the shims, either open metrics or open tracing, so I'm just not sure these things are used.
I would like to deprecate them.
And also, with AI, come on, like… You want to migrate your open tracing code to open telemetry code? It's never been easier.
**Josh Suereth** 06:27 Is that an advertisement there, Dad? I think so.
Cool.
I, I think in terms of the triage process, we just have to mark this as whether we're accepting, and whether it's accepting needs sponsor, accepting the sponsor. So I guess the question would be, Would someone want to sponsor this issue?
here, like, now. Or should I say, accepting a need sponsor?
like, I don't hear any concerns about accepting it. It's more about how we do it, and probably needs a sponsor, right?
I don't know.
**Jack Berg** 07:03 Doesn't this fit into the community feedback classification? Like, where, according to, like, Tigrin's.
you know, thoughts about, like, kind of letting this percolate with the community. I guess what I'm kind of questioning is, if we mark that it needs sponsor, are we saying we're going to do this? It's just a matter of getting sponsorship? And is that the wrong signal?
**Josh Suereth** 07:28 Oh, I see. You're saying we want community feedback of any concerns around deprecation before we say we're going to deprecate? Like, that would be a good step. Gotcha.
**Jack Berg** 07:37 Okay.
**Liudmila Molkova** 07:39 I mean, we didn't do this with Zipkin.
Or… maybe Jaeger?
And up and tracing shim is probably less of a concern than either of those.
**Josh Suereth** 07:54 We did… we did seek community feedback before we deprecated. Like, we made announcements that we were going to deprecate and tried to get feedback. But the difference is, we proposed the deprecation, as opposed to it coming from someone else.
So that's where it's like, is there a TC sponsor who will own this issue and say, I'm going to go get community feedback and drive this successfully to completion, out of deprecating or not?
Or are we gonna ask the author of the issue to get the community feedback onto the issue?
That's kind of how I'm viewing what we're saying.
**Liudmila Molkova** 08:30 I could sponsor it, but I would ask Potter, the person who created the issue, to go through the process of checking and formally investigating if there are reports, what are the download numbers, and making the Autelio blog post. If he's up for it, I can sponsor it.
**Josh Suereth** 08:50 Okay.
To the heart.
**Reiley** 08:52 Peter has done this before, I shared a link.
You see, like, the… the sin person.
**Josh Suereth** 09:01 He's done this before. Oh, yeah, he's the one who proposed deprecating the Jaeger processor.
**Reiley** 09:09 Yes, obviously, like, he knows how to do this, and he's trying to push the same thing again.
Just because, as a maintainer, I guess you don't want to spend time on something.
**Liudmila Molkova** 09:20 Without, like, actual usage.
**Josh Suereth** 09:25 Yeah, and let's just look at this one. When we… it was ready with sponsor.
Robert stepped up to sponsor it, and we took a look at this, we didn't have any objections, there was a sponsor, so we… we went ahead. I mean, Yuri also was representing the, Jaeger, so, like, we had clear signal that it was fine.
Open tracing's a little more… go ahead.
**Reiley** 09:48 For this one, I think Carlos can probably get some connection from OpenTracing, and we should also give, like, a couple days to get feedback from others. And the maintainers should be able to pull the download numbers and usage numbers.
I remember we did that for Jaegor.
**Josh Suereth** 10:08 Yep. I… I'm going to… I'm gonna mark it as community feedback for now.
And I'll make a comment of, okay.
We discussed this.
I'd like to check on current building tracing.
Ecosystem and research vendors.
Here, but we have a potential TC, or sorry, I'll say spec sponsor.
Right.
**Liudmila Molkova** 10:36 Because it's a good opportunity for other spec maintainers that are not us, spec sponsors, to… to help.
**Josh Suereth** 10:45 And then just put this going forward.
Should I say, generally, we're, like, like, what are the criteria we're looking for here?
I want to phrase this like, can you… by the way, my cat is jumping on my hand right now as I type, so apologies. Alright, here we go, she's gone. Unless we see a major usage… major… usage.
Patterns not represented.
in the description.
of this PR, quite likely.
Proceed… There's deprecation.
Given that we advertise.
the deprecation… Well, I haven't have time with you.
community.
To, adapt.
tubes. Something like that. How's that sound?
**Tigran Najaryan** 11:41 Yeah, it's a… it's an issue, not PR. The rest looks good.
**Josh Suereth** 11:44 Oh, oh, of this issue, yeah, sorry.
Okay, discuss this… NTC meeting on, what is it, 2026?
2… 18. Okay.
Oh my god, Cat. Sorry.
I don't know why she wants to be on my hand right now, but it's… it's fun.
Only when I'm supposed to be taking notes.
Alright.
Let's move on.
Do we want to get in the habit of manually signing TC members to PRs? Have we been doing that again? I thought we stopped that.
So we had a discussion about this.
**Jack Berg** 12:28 in the… the last time we met, on February 4th, if you… down in the notes, there's, like, there's a discussion about having so many PRs waiting, and maybe not having any person that felt responsible for, like.
providing the initial feedback, helping them to make progress, whatever it is. And if I remember correctly, some of the discussion was like, hey, this is, like, the perfect thing to do with, like, a spec maintainer role, but as of now, we're the spec maintainers.
Another aspect of the conversation was, like, we used to do automated round robin assignment, but that doesn't make sense because everybody has these sort of topics that they're domain experts in, and so round robin doesn't really account for that correctly.
And yeah, so, you know, just while we were looking at that last issue, I was assigning some people to PRs that are open in the spec repo. Do we want to do that? Does the assignee actually mean anything?
Open for discussion.
**Tigran Najaryan** 13:34 I mean, I don't mind if… if we're seeing that the PRs are getting stale.
But they could be progress. If there was somebody who would push them through, then… It's, yeah, it's something that Wood could definitely do.
Jaeger Shane.
**Liudmila Molkova** 13:51 Go ahead.
I'm sorry, my impression was that it's essentially the iSignee is the person who has the context, and is the first line of review. It's not… it does not put any responsibility to merge this PR, but it puts responsibility to keep track of what's going on.
**Jack Berg** 14:15 Right. Yep.
**Carlos Alberto Cortez** 14:18 And I wanted to say that I suggest we try this at least a couple of weeks.
See how it goes, how it feels.
If that's…
**Tigran Najaryan** 14:26 Sorry, if that's the only responsibility, wouldn't that just… Be reflected if you… if you up the person as a reviewer.
Because that's a feature on PRs, right? You add the person as a reviewer, you request a review, essentially.
If that's what we expect from that person, so that they have to review and provide feedback.
if there is… if there is more than that, then… than we expect, then… then perhaps that is being reflected by the assignment to the issue… sorry, to the… to the PR.
**Jack Berg** 14:57 I think so.
**Tigran Najaryan** 14:57 I just wanted to understand better what's the expectation, really, here.
**Jack Berg** 15:01 Yeah, I think the expectation is not just, like… like, I think maybe we've all done this before, I know I have, but, like, maybe I'll provide, like, an initial review, and the author will respond to it, and it'll get lost in the noise, and I won't go and look at those again. And so, like, I think… Maybe that… maybe that is actually all bundled up in the reviewer. If you're reviewing it, you're not just, like, forgetting about it. You're gonna continue to, you know, shepherd it in one direction, either, like, towards merging or towards closing one of those two. Like, those are the outcomes we want.
And, yeah, like, I guess the, you know, is there any special distinction for assignee versus reviewer? I'm not sure.
I think yes, like, a little bit, but it's, they're not too different from each other.
**Josh Suereth** 15:51 I… I will add a context of my GitHub notifications insane.
I get, like, hundreds and hundreds a day.
Because, I'm still on all the old Scala stuff, and so I've given up. I have declared bankruptcy.
But Assigned has its own special callout in GitHub Notifications, where I can go to a dashboard that tells me all the things I'm assigned and see where they are. Now, I still have about 8, 10 things on there that, are, like, stale, and I never look at them because they have not had changes in a year.
But, for the most part, I can be responsive with assigns. Whereas, like, if you just… like, if I'm assigned as a reviewer, I don't think it shows up on that dashboard.
**Tigran Najaryan** 16:39 Yeah, that's nice. I didn't know that, that's good, yeah, that's really nice.
**Josh Suereth** 16:43 When they made an announcement about changing the notifications in GitHub, I was so happy. That was, like, the number one issue in the GitHub UI for me, for the longest time.
But that's… that's a recent change as of, I don't know, like, 3 months or something? 4 months.
**Liudmila Molkova** 16:59 And reviewers are essentially, once you open the PR, it's everybody who reviewed, right? It's still the shared responsibility of who follows up. Probably everyone, but then nobody.
**Tigran Najaryan** 17:13 Yep.
Yeah, no, I like that, especially since there is, like, an actual view where you can see all your assignments. I like that.
**Jack Berg** 17:30 I'm writing down some notes here, just like, so what are the criteria? Like, which PR should we assign somebody to? And, like, we had discussed last week, or two weeks ago, not OTAPs, right? Those are kind of this different category of thing, where it's no one person's responsibility to, to, you know, be that reviewer. We all ought to, and more of the community as well.
You know, another thing that I was thinking about as I was assigning some people, what do we do about PRs that are actually authored by a TC member? Do we assign, like, another TC member as the assignee, or is it just, like, sufficient that there is a TC member that authored it to kind of check this box?
**Tigran Najaryan** 18:10 Yeah, I don't think we need that.
**Liudmila Molkova** 18:14 But there should be somebody else with the context to review.
**Tigran Najaryan** 18:21 Yes, I agree, and we should probably expect the DC member to know how to push that through. Find the right person, make sure that the progress is being made.
Sort of, we're… we're the ones who know The process, and even if we can't make it.
Go forward, then we probably have a bigger problem.
**Liudmila Molkova** 18:42 But should we expand it to not just TC members, but all the SPAC sponsors?
**Carlos Alberto Cortez** 18:51 I would suggest, this is a small suggestion, we keep it to the TC for now, while we figure out the details. Once we're confident, we can expand that to the spec approvers.
So we don't make too much noise, you know, before we actually get the thing rolling.
**Tigran Najaryan** 19:13 So you're suggesting, Carlos, that we try this for a while, see how it works, and then extend it to other sponsors?
**Carlos Alberto Cortez** 19:20 Yep.
**Tigran Najaryan** 19:25 Yeah.
I think I agree. We can do that.
**Jack Berg** 19:31 Yeah, and I just jotted down, like, a note here, just, this is kind of what I was hearing in this conversation, like, what are the responsibilities of an assignee? What's the difference between this and just being a reviewer? And, like, my read of it is, it's like, you know, you don't have a commitment to force the PR to make progress, like, but assuming that the author is responsive, you should be sort of responsive back.
And, like, guiding that PR to the point where it's ready to get reviewed by, like, the broader set of approvers, such that it could be merged, or closed, right? Like, what this assignee is trying to do is avoid this PR going stale indefinitely.
For… like, even if it's, like, a good idea, and the author is responsive, like, that's a bad… that's a bad situation. If it's a good idea, and the author is responsive, and it doesn't make any progress, and so the assignee is sort of trying to prevent that.
**Josh Suereth** 20:30 Oh, this question.
**Jack Berg** 20:33 Go ahead. Did we do the same for the proto-repository?
Yeah, the Preda repository, the way that I think about it is it's just, like, an extension of the spec in a different repo.
Like, we… like, the TC are the maintainers of it, right? There's not a special group of people who are approvers or maintainers for the produce specifically. So, yeah, like, we wanted to split that resource out just for reasons, and, you know, but we have to treat it as an extension of the specs still.
Okay, we're 20 minutes in, I think, I'm going to just, kind of, just to prevent spending more time on this, because there are topics, I'm going to sort of do a, like, a pass at assigning people, asynchronously.
And, we can pick up next… in the triage section of the next TC meeting and see what the… what new issues or new PRs have come in that need triaging or assign… assignment.
**Tigran Najaryan** 21:43 And the way that we'll be assigning is based by, yes, on the expertise, like, whatever is the area, whoever has the most experience with that.
And if… if it's something that we don't necessarily have a subject matter expert, then we'll do round robin or something like that.
**Jack Berg** 22:04 Yeah, I think so, exactly. And, load, I think, is another thing, so if one person is… is set as the assignee for too many issues relative to other TC members. I think load should be a consideration. And, yeah, if we're doing this synchronously at a meeting with each other, people can kind of make a comment and say, like, hey, look, I'm the assignee for too many things right now. Even though I'm the domain expert, somebody else has to do this.
Hopefully that will be rare.
**Josh Suereth** 22:51 Cool.
Let's… let's move on, because we… I don't want to run out of time. We have a private topic, and we have the packaging sake, so let's talk about the packaging sake.
Who added this one, by the way?
**Liudmila Molkova** 23:10 I think I added PackagingSeq, because you and Jack were discussing that you want to talk about it.
**Jack Berg** 23:21 I remember making a message in the TC channel that was essentially like, hey, we should discuss these new SIG proposals and come up with a, a sponsorship level we think is appropriate for each.
And the packaging SIG was one of these new SIGs, along with ZIG and… and…
**Liudmila Molkova** 23:40 dark.
**Jack Berg** 23:41 what was the other one? MCP. And Dart.
SIG, Dart, MCP, Packaging.
Not sure if there's other context around discussing this.
**Josh Suereth** 23:56 No, no, I think that's exactly it, I remember now. Thank you.
Go ahead, go ahead, Ludmilla.
**Liudmila Molkova** 24:04 No, no, I said what I wanted, sorry.
**Josh Suereth** 24:06 I was gonna check quick, I think the private topic might be related.
**Liudmila Molkova** 24:13 It is, yeah.
**Josh Suereth** 24:15 Do you… so I'll ask you, Lydmilla, do you think we should move to the private topic, or do you want to discuss sponsorship levels here first, and then go to the private topic?
**Liudmila Molkova** 24:28 Fairly related, so maybe we can switch to the private link and talk about both of those things together.
**Josh Suereth** 24:34 Okay.
Okay, let's do that.
**Jack Berg** 24:39 Alright, I'll see you over there. Bye.
**Josh Suereth** 24:42 See you over in the private channel.
