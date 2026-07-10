SIG: Python SIG
Date: 2026-07-09
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 01:38 Hello, everyone.
**Tammy Baylis** 01:46 Hi all.
**Erdenesaikhan Tserendavga** 01:48 Hello, everyone.
**shuwpan** 01:50 at home.
**Riccardo Magliocchetti** 02:36 Welcome everyone to this week's Python SQL.
We're waiting a few more minutes for more people to join. In the meantime, please add yourself as an attendee to the notes.
And also feel free to add any topic you want to discuss.
And let me share the link to Reynolds each. Okay.
We share the same data.
**Tammy Baylis** 03:00 Yeah, split second you beat me to it.
**Aaron Abbott** 03:44 Hello, everyone. How's it going?
**Tammy Baylis** 03:49 Hey, Erin.
**Aaron Abbott** 03:52 Great idea.
**Diego** 03:53 Aaron.
**Aaron Abbott** 03:54 Mmhm You.
**Riccardo Magliocchetti** 04:54 Okay, it's in video five. I think we can start.
Tammy, do you want to do the…
**Tammy Baylis** 05:03 Yeah, I can do that.
Let's switch screens.
Thank you.
I'm… Hello?
Okay, we'll finish at 9 10. So no status.
Let's look at this one.
June 4th exporter OTLP protobuf HTTP auto append signal path and base URL past is endpoint.
Tyson?
Okay.
Doesn't it do this already?
Hmmm.
**Riccardo Magliocchetti** 05:51 I'm not sure.
we do that.
**Tammy Baylis** 05:54 Yeah.
They haven't, linked an issue or anything… But they do talk about what the change does.
Oh, we've had some comments already.
Lucas has had a lift already. It's treated as is.
But, preference to keep the same, yes.
**Diego** 06:26 Can you please tag me in the conversation and ask me to review this PR, because I… I'm working on a… On a similar exporter, and I should take a look at this.
**Tammy Baylis** 06:41 Okay, thank you, dear.
Think.
That's the case. I'll put it in. It's already being reviewed. Might as well say it's ready for review.
Next one.
Aws lambda instrumenter. Add Sqs. Context. Probably.
Lucas… May 31st issue.
Yeah.
Mmhm.
Stale. Yeah, this is this is ready for review.
Handling encoding exceptions in OTLP exporters.
50-50… unhandled exception. That's not good.
totally agree.
Okay.
Had some reviews already.
Oh, but hold off.
Okay, then… We don't have a hold-off column, but I'll just leave it in no status for now, unless… There's a preference.
Fast. Api, add pi dot typed marker.
Hmm… I don't know if the other instrumenters are doing that, but I think that would be easy to have an opinion on.
**Riccardo Magliocchetti** 08:52 Yeah, but, like, we don't run type checking on most of instrument… instrumentation, so…
**Tammy Baylis** 08:59 Okay.
**Aaron Abbott** 09:02 I think this file indicates to the consumer that it should read the definitions from this library. So if like the interfaces.
the… annotated, then I think this might still be helpful. But, yeah, I agree, it's a little weird to just fix this one instead of… fixing more of them, and it would be nice to know it typed checks beforehand, too. At least the public API.
**Tammy Baylis** 09:29 Okay.
So I ask if it type checks the public Api.
**Aaron Abbott** 09:39 Yeah, or is there, like, an issue? Did they…
**Tammy Baylis** 09:41 No, they didn't create one.
**Aaron Abbott** 09:43 Okay, so I mean, maybe we could… Yeah, I mean, that's what I'm saying, so downstream type checkers consume its inline annotations. So I think it's reasonable, assuming that the ann.
**Tammy Baylis** 09:56 Yes.
**Aaron Abbott** 09:56 Just ask for some clarification on that.
**Tammy Baylis** 10:18 Maybe. Why.
Oh.
Does it not change?
Yeah, it it's on the board in the correct column.
It's 9 10. I will stop that for today. Where?
Oops.
Sorry. Stop share.
Okay, back to you, Ricardo.
**Riccardo Magliocchetti** 11:02 Thank you.
Okay, you're done, Fiosh.
Anyone want to feel what they're working on this week, feel free to.
And then to the topics. Carlos?
Start of state PRs.
**carlosalberto** 11:18 -Yeah probably this can be skipped. Yeah it was just like the remaining items from last week's discussion and thank you Ricardo for commenting on like what status of these ones. Probably we can only briefly discuss the second one which is also getting review.
Sorry, need some eyes.
Yeah, that one. I think if I am correct, that's the one that Mike needs to provide some feedback.
on.
Maybe a different one, or maybe Mike, yeah.
Yeah, like, I.
**Riccardo Magliocchetti** 11:52 I think he may ask for feedback from anyone around. But yeah, last one is Mike.
**carlosalberto** 11:59 Yeah.
Yeah, I think, and also Mike's comments here, they seem to be resolved. The last one was about CIA failures.
Yeah so that's up to the maintainers but that's probably the only one that I would like to get people eyes on. The rest are yeah like Ricardo clarified on the doc what's the current status.
So that's great.
**Riccardo Magliocchetti** 12:46 Okay… Yeah, this, OpenQuest, and I think the first year in, this election, we'll probably close them.
But maybe you can take just a quick look.
Yeah, like, this one is adding, like, this is trivial, but I don't know, like, this is, used in memory spanning support only for testing, and very adding, I'm exercise to avoid to To be unbounded, unbounded.
The API is trivial, so we may just nurture.
One thing I noticed, but probably we are still referencing a list, and now the… The container is a deck.
But other than that, it should be… Easy. Okay.
And the other one, yeah, is of the Olympic Kafka Sport.
I've already commented on the issue.
Like suggested to just use the, the one from the collector.
Okay.
So if anyone has any other opinion, yeah.
**Aaron Abbott** 14:00 Yeah, Ricardo, on the in-memory one.
Do they set the max length by default, or is it just a new parameter? Okay, it's a new parameter.
**Riccardo Magliocchetti** 14:09 Yep.
**Aaron Abbott** 14:10 I see.
Yeah, seems reasonable, but I… I don't know why you would… Use this thing in a… in a setting where you are worried about, like, the memory. I don't know, maybe they have some Like, usually this is only used for tests, I guess, but I think it's alright, it's a really simple.
**carlosalberto** 14:30 But you can ask them, or I can ask, just put a, you know, a comment there, like, hey, like, this is kind of, this is fine, but you're neutral, so if you have, like, any requirement, please just tell us.
So for future reference, people know why this was added, you know.
**Riccardo Magliocchetti** 14:48 Like I asked to explain a bit.
And they said, that… If you have like low running processes, it may be helpful, but yeah.
probably you don't want to accumulate memory that way if you're long running processes I guess.
**carlosalberto** 15:07 Yeah, that feels very odd, by the way. I hadn't seen that, that comment, by the way. Sorry for that. Yeah, that's kind of odd, what he… well, anyway. I would say that's up to the maintainers. I don't think there's any, in-memory exporter in another language that limits the number of items so it's up to you I would say it's a optional parameter So it wouldn't hurt anybody.
If valid, but it's up to the maintainers.
**Aaron Abbott** 15:38 Yeah, I mean, given the simplicity of the change, I think it seems reasonable to me, but… Yeah, it would be interesting to see.
you know, I don't want to just tell this person they're holding it wrong or whatever, but I'm a little confused on the… Okay, long testing scenarios, etc. I don't know, it seems reasonable, but what do you think, Ricardo?
**Riccardo Magliocchetti** 16:00 And I just like update the.
That, the doc string, And approve, then we'll move on, like, it's… I think it's fine.
Diego, you have your hand raised.
**Diego** 16:17 Yeah, I also agree with Carlos here. I see it as something that's harmless.
And… Pretty sure someone had some use for this. If not, they wouldn't.
I've opened the PR, Yeah, I'm okay. I'm okay with Yeah, I agree with Leyden, it's… Harder to explain why you don't need it.
**Riccardo Magliocchetti** 16:50 Okay, Diego, you are next one.
**Diego** 16:53 Right, so… okay, that's just a friendly reminder, but that PR has, like, a ton of approvals, so… if we could just merge it, it's also a PR that actually removes code.
So that's my favorite kind of PRs.
So if you like the… At least just so.
First, it'll be great.
**Riccardo Magliocchetti** 17:22 Yeah, like.
**Aaron Abbott** 17:22 Is this waiting on anything in particular, Ricardo?
**Riccardo Magliocchetti** 17:28 Well.
Depends, how many downstream user or events we have.
I guess. I think we… I already checked, when we duplicated this.
Maybe. I don't know, like, I remember I checked the Open Elementary stuff.
Because you broke, well, maybe it was something else, anyway, like.
I can probably do, like, a GitHub search and see if we have any.
User out there.
But, I'm fine removing, I'm just a bit worried about creating Arm for downstream using, yeah.
**Aaron Abbott** 18:09 Yep. I think we did add like deprecation warnings to all this as well, right? So people should have been alerted and we gave them a pretty long period. Is there anything else? I think we kind of agreed that we would just remove it.
**carlosalberto** 18:29 If you are super, super, super worried, you can probably go write a blog post saying that, hey, by the way, if you're using this, this is gone.
**Liudmila Molkova** 18:44 I'm just checking and it doesn't look like OpenLLM uses them and they've had a long time to adopt.
And they've used them in the past, and it seems they've changed them to something else.
**Aaron Abbott** 19:03 Yeah, I think I'd be in favor to just do the removal, Ricardo. I think it was always in this underscore package.
we've given, you know, the warning, and I think you've done… you did a lot of work on this, Ricardo, to… I think you talked to Pydantic folks and Open Elementary, so… Yep.
**Diego** 19:23 I.
**Riccardo Magliocchetti** 19:24 Bye.
**Diego** 19:24 It'll be a valuable life lesson.
For anyone whose code breaks.
If we remove this.
Kind of kidding here.
**Riccardo Magliocchetti** 19:45 Thanks.
Next.
topic. It's also from you.
There you go.
**Diego** 19:54 Damn Right. So, okay, we were discussing this proposal.
For new presses to submit PRs, right?
There's, a recent comment from Aaron, That says the last we chatted about this, current stance we arrived is to not to assign issues at all.
Just to go off comments, because, I think people have a, it has happened before, I mentioned, that, people have requested an issue assigned to them, and they just don't, Okay.
Follow up on that issue, which I think it's a very valid concern.
I just wanted to explain myself a little bit better.
The idea of, requiring… An issue?
To be assigned… Someone?
So that they can open a PR.
is, it's like a critical part of this mechanism.
that, We're trying to implement here to protect us from, PRs opened just by people who are using AI to produce.
A PR or something. The reason why it's the critical part is because, the assignment… Of an issue to someone, is the… the… The thing that finally allows a PR to be created, right?
So, that's why it's important. It's not only, Just, a bureaucratic thing, it, it actually, it's.
It's a part of the mechanism that implements this idea that will help us Protect ourselves from.
these, PRs, right? So… So that's why it's important for this process. And I wanted to explain that a little bit better.
**Aaron Abbott** 22:06 Does anybody remember the context of… that I was trying to share in the comment? I don't know if you remember, Ricardo, or… I almost feel like there was, like, a discussion about this in the… I don't know, maintainer sick or something like that at one point, but I think.
We we could come up with some process, I think just the.
The concern is still valid that if we do assign stuff, people We'll filter the issues list by assigned, and then we had ones which were sitting with assignees who had Gone away for, like, years at a time, so… If we can solve both problems, then that would be that would be good.
**Diego** 22:44 I think, ricardo mentioned that these proposals needs A mechanism that will allow us to unassign issues.
when people have not, Done any work with their assign issues as well.
**Riccardo Magliocchetti** 23:15 Yeah, like last week, I was worried about this as well.
And I asked, like, maybe we need a mechanism that We'll just remove assignment if.
There's no, like, a linked PR in a time frame, like… To like, like we do with the stale PRs, the same for stale assignment, something like that.
**Diego** 23:38 Which is something I think it can be automated as well, right?
**Leighton Chen** 23:44 Yeah, so can people hear me right now?
**Diego** 23:47 Yep.
**Leighton Chen** 23:49 Yeah, so yeah, what Aaron brought up, I think, is pretty legitimate.
So instead of like assigning someone like, can't we just use like a label or something?
Stating that, like, the issue has been triaged and approved.
So it doesn't, like, have the downside of, like.
being stale over time if someone is assigned to it. But like over time, it's not going to be like less relevant, right?
**Diego** 24:17 Oh.
Oh.
I'm I'm I'm not sure if that will will help us with the issue became becoming still still over time.
**Leighton Chen** 24:29 Well.
One of the issues was that, like, we're getting too many PRs before the issue has been identified as actually relevant, or something that we actually want to solve, right?
That's, like, the first When we… because the original topic was, like, we're getting too many PRs, and, like, we identified that not only are the reviews slow, but, like.
the PRs that are coming in are also kind of, like.
too much for approvers and maintainers to handle. So how can we like filter it at the front?
Was one of the top outstanding topics.
So while assignments to someone would be one of the ways that you can address that like, Hey, like.
This, a maintainer or approver has triage this issue and identify that it's like a legitimate issue. So we'll assign someone. It does have the problem of like, you know, going stale, in which, when someone is assigned like.
they might not have time, or like they don't. They don't get to it in a timely manner, whereas if we add a label or something, it's You know, we're just marking that this issue is a legitimate issue without having to worry about, like, the staleness of… of people being assigned to it.
Sorry, Ricardo, you have your hand up.
**Riccardo Magliocchetti** 25:47 Yeah, but, like… Okay.
Regarding your comment… Like, I think that the assignment will solve another problem, but it's the duplicated PRs, maybe?
But, yeah, like… I think we should probably… Like, maybe agree first on the list of issues we want to solve.
Because I think we have a… Like probably like trying to solve different problems.
But yeah, like, I agree that we… We want your… Said later, but.
Yeah, but… Like, we have that problem, but we have an issue that has not been, like, accepted.
Yeah, but you'll still have more problems, I think.
**Leighton Chen** 26:45 Is this the last topic today in the agenda?
Pardon?
**Aaron Abbott** 26:53 And Carlos has to.
**Leighton Chen** 26:56 Okay, yeah, I guess without taking too much time like, maybe we could just like, go through it really quickly, since we have quite a bit of time left and itemize like.
what we're actually talking about in terms of bottlenecks and pain points in the issues and review process.
So I like I.
If everyone's okay with that, like, I identified one of them, which is… Okay.
you know, issues, PRs being created for issues that have not been verified yet.
I can start taking notes, too, if we're okay with this exercise.
**Diego** 27:38 Levon, something I don't understand well is, you mentioned that, PR's being opened for… Issues that we have not agreed.
Yet, it's a problem, but this approach also solves the problem.
**Leighton Chen** 27:59 I'm not listing out solutions right now. I'm kind of responding to what Ricardo was saying by we should itemize the actual issues and pain points before talking about a solution, I guess.
**Diego** 28:14 Okay, okay.
**Riccardo Magliocchetti** 28:16 Yeah, like, I think we have some… And the technician of SPR.
I think we have a bunch of, Issue with everyone.
Share some issues they see.
Like, maybe we can collect, A bit more stuff.
**Leighton Chen** 28:42 Yeah, I think you had a comment above this.
Yeah, right here.
**Diego** 28:49 So… Sorry, guys, if you can scroll down, because… There is a branching of topics that is happening here.
Scroll down, please.
Right, I opened the new… issue.
Because, there wasn't… I opened an original issue that was just about Using AI to help us in the review process.
And that's in… and from that discussion, it branched into this new issue, right? So… Just to clarify that, right, that… Those two things are… Separate topics.
**Leighton Chen** 29:40 Got it.
Yeah, sorry for diverging the conversation. Which one did you want to address?
CLAB, today.
**Diego** 29:50 This one.
**Leighton Chen** 29:53 Is this the the using the AI to to help your Prs.
**Diego** 29:58 No, no.
**Leighton Chen** 29:58 Oh, okay.
**Diego** 29:59 This has nothing to do with AI. This is… something that can be implemented only with GitHub Actions. It is… it is just a proposal for a new process.
Yeah.
The the process. It's very simple.
It requires, first, That an issue is opened, and in that issue we can discuss… It's the topic at hand. And if at the end of the discussion, we agree that it's a valid issue.
Then, we assign this issue to someone.
who would previously appear.
A consequence of this is that any PR that's just opened without any issue gets automatically closed.
At the same time, any PR that It's opened.
And… Even if it's linked to an issue.
gets closed if the author of that PR is not assigned. So, STEP, helps us with Duplicate PRs?
And the first step, helps us.
with, Prs that are opened, Using AI or something, which is, A problem we're facing now.
**Leighton Chen** 31:38 Yeah, I think… I think that totally makes sense. I'm I am. I am more curious about like Aaron's latest comment.
That is a legitimate kind of use case, in my opinion.
And it would be kind of exacerbated with this change.
**Diego** 31:58 I agree. I think that can also be added to the automation, like if an issue gets assigned to someone.
And if, after… I don't know.
A certain amount of time, there is no… Input.
no, no, no, no PR being opened by that person, then that issue gets Unassigned.
To that person, we could also automate it.
**Leighton Chen** 32:35 Yeah, I think I think if if there's a mechanism to handle that, like, I'm okay with this.
Whether it be a label or, like, an automated, like.
X amount of days to get to the to address the Pr.
**Diego** 32:54 I can work on, adding that… Second part… to the automation, that after, I don't know, certain amount of time… I'm just gonna use one week for the moment, we can discuss later.
The actual time that we want to use.
I can add that to the PR.
Linked to the decision.
**Leighton Chen** 33:26 Okay.
Oh, sorry. You heard what?
**Aaron Abbott** 33:29 Yeah, I just wanted to call out one other concern and that's for like editorial PRs and also things which are kind of time sensitive like during releases and whatnot. It would be very frustrating if automation closed these PRs and you had to file issues.
And I don't know if handling the… Special case with, like, a label or something is… gonna create more friction than it would solve. I mean, there's also the possibility to check for people who are, like… I don't know if there's a good way to check for people who are in some kind of allow list or whatever, and… But yeah, I just could see that causing some friction.
Yeah, Ricardo.
**Riccardo Magliocchetti** 34:11 Yeah, like, I was thinking if… Like, I'm not sure this will be, like, the… the first issue that I'll tackle.
For example, like, I think we have, More like longing fruits we can solve.
And we'll, but we require like less work on our side.
Or, like, next friction with the users.
Like, for example, like, the… I'll start by, changing the configuration of the repo to not allowing more than one, PRs open for, For new contributors or something like that.
What would be, like, free for us?
Will not require issue, and that will probably solve the… The stream of user, but, Have some token to burn and just continue to open PRs for, for issue we found.
Like, at least, like, we don't need to explain anything to the others, And we'll solve, like, part of the problem at least.
There you go.
**Diego** 35:33 Right. Yeah, I understand the concern from Aaron that, Sometimes.
I think mostly maintainers, would like to just file, A PR to address, Something that is, immediate and… Non-controversial, right? Something that' whose PRs would not be closed automatically.
So that we can include the maintainers.
Or the approvers, where we think that they are not subject to this restriction.
Am I freezing?
Oh, my.
My Wi-Fi is terrible, I'.
**Aaron Abbott** 36:30 You're my only.
**Diego** 36:31 frozen now.
**Aaron Abbott** 36:32 You are, you're, it kind of buffered your voice, but not exactly. So if you want to.
**Diego** 36:37 Yeah. Do I need to repeat what I said? Did you understand?
**Aaron Abbott** 36:44 I think we got it, but did you have, like, a proposal? I think, Carlos brought up the label in the, Meeting chat here.
**Diego** 36:54 Yeah, we could use a label. I was suggesting that we could tell the automation a list of users that are exempt from this action, right? So if, for example, a maintainer files, An important PR that's gotta be just, quickly merged.
It will not close that PR for maintainers so that maintainers don't need to follow this process.
We could also do that.
**Aaron Abbott** 37:25 Yep. Oh, I'm sorry, Leighton, go ahead.
**Leighton Chen** 37:29 Oh, sorry. Yeah, I prefer a label since… It's more permanent.
Than, like, specific members, which requires additional maintenance.
**Diego** 37:41 Yeah, we could also use a label. I'm not against this idea of having exemptions to this process.
Oh.
Pretty sure we're gonna find use cases for that.
**Aaron Abbott** 38:01 Yeah, I wanted to see, Diego, do you have a… what do you think of Ricardo's proposal to just do the new GitHub feature that lets you limit the number of open PRs for new contributors? We could try that. I think…
**Diego** 38:15 Look, what happens is that.
A new contributor may open 1 PR only.
But we can have… An infinite number of new contributors.
So I… The end result could still be we get 20 PRs.
I think we can do both things.
No, we actually can do both things because, so, so yeah, I think this mechanism is a little bit stronger than that.
**Aaron Abbott** 38:50 Okay, but I just want to make sure we're solving, like, the problem that we're seeing, because I think… there's been a couple cases where it was a lot of… users sending a lot of PRs. I don't know if we had so much the, the other problem, and… like, I… at least for me, I'd rather optimize for people who are, like, handwriting code, or actually spending time with an agent, like, trying to write code and making sure that, You know, their contributions are… seen and, like, valuable versus somebody who's just, you know, spamming, like Ricardo said, tokens to burn on other PRs. So, I just want to make sure we're all solving the same problem and doing it in the simplest way possible.
**Diego** 39:28 Yeah, I also think this proposal also helps with the duplicate PRs.
And, it also helps us.
With, the issue that, right now, even if someone files a PR that's, like.
a PR that involved human effort, someone who's trying to find, to solve Something that they believe is a legitimate issue.
But at the end of the day, the rest of the community may not agree.
So that, it also helps with that situation where someone spent a lot of effort.
into opening a PR, that at the end of the day.
Were ended up being rejected because they skipped.
the… the first part of the process, which is discussing it with somebody else, right? So, I think this, this, this proposal also solves that, that issue, so I think This proposal solves several issues.
Which I think it's also makes, makes it very valuable, I think.
**Aaron Abbott** 40:44 Layton, I just wanna… clarify the limit is for, I think, new contributors only. I think once people have their first PR merged, it would, not count towards that.
**Leighton Chen** 40:59 Yeah, it makes sense. I think my comment applies to new contributors as well.
**Aaron Abbott** 41:07 Yeah, I mean, I don't really, like, have a strong feeling on this, I just… Oh.
I want to make sure we're not creating, like, a lot of bespoke automation that is both hard to maintain and, like, hard for people to understand how to use. So, as long as we're solving the same problems, I'm good with whatever.
**Leighton Chen** 41:26 Yeah, that's true. That.
**Diego** 41:41 Do we, should we… Discuss this, in another meeting, next week?
**Leighton Chen** 41:58 Yeah, we still have the declarative config changes. So like.
Maybe we can go over what Carlos wants to talk about, and then use the remaining time, because I do kind of want to.
not takes too long, Diego. I know you brought this topic up already, like, twice, so…
**Diego** 42:17 No, it's fine. I, I understand that this is a topic, where SRA people have, opinions, and I don't want to… To force this, Process, so that, Because I want everybody to… Have a chance to.
Oh… comment here. And I understand that we have already spent a good chunk of time today discussing this. So I'm fine if we move to the next topic and we I'll continue the discussion of this topic next week.
**carlosalberto** 42:55 Probably, Diego, if you want to make progress on this, you can present an actual summary of changes that you foresee.
I think that… a lot of stuff is being discussed with many options, but something somebody needs to come up with a potential solution, and then we start from there, and we can just discard that completely. This will work.
**Diego** 43:18 All right, I'll work on that and I'll present it next week.
**Leighton Chen** 43:28 Hey, this might be a dumb question, but Carlos, isn't that.
what the proposal that Diego Isn't that what was in the issue in the first place? Like, he already added a proposal, right?
**carlosalberto** 43:42 Yeah, but I would say that first iterating on what is causing this call, review that, update that, try to address some items, like for example, the one that you posted in the chat, like you actually prefer contributors to be able to split PRs.
So how can he solve that part?
**Leighton Chen** 44:05 Oh, okay, I see. I see.
**Diego** 44:09 Yeah, I also would like to address the… The issue that was mentioned, regarding exemptions to this, process which can be implemented with labels or with a list of contributors, and also the issue regarding the time frame for people to do something with their assigned issues.
Which, I can give it a try, and… See how… that can be implemented, and I can present a more complete solution.
next week as well.
**carlosalberto** 44:43 Yeah, oh, by the way, you may remember, but I had mentioned that Trask from Java, he was trying something in private, and then he said that he would be coming back with his results. The idea is that he would try to enable something of AI doing some… pre-checks so people don't have to review every PR and they only, you know, pass on filter. So go and ask him again if you haven't, that could also be something interesting.
Whether he got some… Good answer or not, yes.
**Diego** 45:13 Yeah, that, I mean, I.
Can definitely do that. Just to clarify, that is a separate topic, the renewal of PRs by AI. It's independent from this. This topic branched from that first one.
Sure, just to…
**carlosalberto** 45:32 Yeah, they're related. So at least, you know, like, even though they are separate, I think they are complementary, so to speak. So the outcome of one may affect the other.
**Diego** 45:43 Alright, I'll… I'll have a conversation with Trask. Thank you, Carlos.
**Riccardo Magliocchetti** 46:01 Okay.
So, I'm not sure what's the outcome of this discussion yet, so all of that, let's discuss again next week.
**carlosalberto** 46:11 I only need probably 5 minutes for my session, because probably we will not find some discussion here.
But I would say that from an external observer, if you have more requirements or more concerns, you can pass those ones now or offline to Diego.
So when he's iterating on this updated proposal, he can, you know, get that stuff.
into account.
**Riccardo Magliocchetti** 46:46 Okay, thanks.
And next topic is from you, Carlos.
Nikolaj Cossack.
**carlosalberto** 46:53 Yeah, I would like to, bring the attention to this topic that there are a few competing PRs adding or refactoring stuff around declarative config.
And, I think that probably maintainers should recommend a way to proceed on this one to make the life of the contributors less painful and also to make more effort. So for example, Mike has this big PR for separating the declarative config out of the SDK and into its own package.
But Diego has also this PR for declarative config change for language specific instrumentation properties.
And yeah, I think that probably maintainers should call out or maybe not for your consideration. Let me actually look for the actual PRs that touch on this.
Okay, that's the first one. I will post… I will paste the links here, and then we can add them to the actual agenda for reference. That's the first one. That's the one Mike, It's working for extracting declarative configuration into its own package.
I think there was one that was close, because it was… superseded by what Diego was doing.
Yeah, I think so, yeah, it was I cannot find it.
Yes.
**Diego** 48:31 Wasn't this PR about… Yeah, moving it out of the SDK, and
**carlosalberto** 48:40 Yes.
**Diego** 48:41 I mean, in a separate package. I think we agre.
**carlosalberto** 48:45 Yeah, but the… Actually, wait, was your instrumentation, like… Specific instrumente… sorry, language-specific instrumentation PR merge? I cannot find it.
No, never mind, they found it.
Sorry for that.
**Diego** 49:01 It hasn't been merged yet, if I…
**carlosalberto** 49:04 Stop.
**Diego** 49:05 It's personal.
**carlosalberto** 49:06 This is Diego's, and I think the other one, which was about a slash in the name of the properties. I think it got superseded by this one. It was closed.
**Riccardo Magliocchetti** 49:16 Yes.
**carlosalberto** 49:18 Right. Okay.
Okay, so it's only two PRs instead of three, but still probably that's just for the consideration of the maintainers. I think Mike commented something in his own PR, but yeah, it makes sense to probably decide on which one.
That one, yeah, that comment, correct.
Oh, there was one more, interesting.
**Riccardo Magliocchetti** 49:42 Yeah, I could agree to merge the… Like, Diego won before they moved to the separate package.
And regarding the Diego one, I think… Yeah, like, maybe I'm… I'm worrying too much.
About collision, since we now… apply this normalization here So maybe a check that if the key is already in the… Whatever, Thing is called, but we store it later. Maybe raise an error that there is a collision or something like that.
**Diego** 50:23 Yeah, good point. I… Yeah, that's, Oh yeah, that's a recent comment. Okay, I'll take a look.
**Riccardo Magliocchetti** 50:35 But other than that, it's fine, and it's very helpful. Like, it makes… You know, testing the finger with real code, like, a lot easier.
**Diego** 50:45 Okay.
**carlosalberto** 50:49 Okay.
That's all from my side, yeah. Yeah, it does feel kind of weird that there are some competing PRs, but it seems that you have an agreement now.
Okay, that's all from my side.
**Riccardo Magliocchetti** 51:17 Okay, so we're naming our left.
Do we want to continue the… The discussion, again… or… I have 9 minutes back.
**Diego** 51:40 Anyone else? Updates on my PR.
So… I think it's fine if we give 9 minutes back, because… I can present this PR again next week with the new features that I just mentioned regarding exceptions and Oh.
Timeframe for issues.
**Riccardo Magliocchetti** 52:04 Okay, thanks.
Any last minute topic?
**Aaron Abbott** 52:10 Not to me.
**Riccardo Magliocchetti** 52:13 Okay.
So thank you. Thanks, everyone.
And you have 80 minutes back.
Thank you.
**Leighton Chen** 52:20 Thank you.
**Aaron Abbott** 52:21 I'll.
**Riccardo Magliocchetti** 52:21 Bye bye.
