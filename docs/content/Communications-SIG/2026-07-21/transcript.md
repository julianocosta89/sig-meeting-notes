SIG: Communications SIG
Date: 2026-07-21
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Patrice Chalin (Cloud Native Computing Foundation)** 00:20 Vitor! Oh, right, it's your cute puppy!
**Vitor Vasconcellos** 00:25 Oh, yes!
**Patrice Chalin (Cloud Native Computing Foundation)** 00:27 That's it.
**Vitor Vasconcellos** 00:28 And this… There it is.
**Patrice Chalin (Cloud Native Computing Foundation)** 00:32 Yeah! Is it a tickle?
**Vitor Vasconcellos** 00:37 Yeah.
**Patrice Chalin (Cloud Native Computing Foundation)** 00:38 Yeah. I think I might have asked before, but I'd forgotten.
**Vitor Vasconcellos** 00:42 Yeah, no.
**Patrice Chalin (Cloud Native Computing Foundation)** 00:44 Hi, everybody.
**Vitor Vasconcellos** 00:44 One of them. Imma.
**Patrice Chalin (Cloud Native Computing Foundation)** 00:46 Oh, one of them.
**Imma Valls (Raintank, Inc. – Grafana Labs)** 00:48 Oh, God.
**Patrice Chalin (Cloud Native Computing Foundation)** 00:49 Oh, hello.
**Vitor Vasconcellos** 00:50 Amen, amen.
**Patrice Chalin (Cloud Native Computing Foundation)** 00:52 Hey, Deanna?
**Diana Todea** 00:54 Oh, good afternoon, or good morning.
**Patrice Chalin (Cloud Native Computing Foundation)** 00:57 Hello, hello.
Exactly noon for me. I'm right in the middle.
**Vitor Vasconcellos** 01:07 still getting used it. I think this is the first… no, not the first, the second… second meeting I'm joining.
And by… by the afternoon, it was… it used to be in the morning for me, so…
**Patrice Chalin (Cloud Native Computing Foundation)** 01:24 I guess you must be accustomed to your new time zone by now.
**Vitor Vasconcellos** 01:28 Yeah… It was hard at first, but… It's better now.
**Patrice Chalin (Cloud Native Computing Foundation)** 01:35 Good.
**Diana Todea** 01:44 So, I'm guessing with the new changes to the platform, we lost also the agenda links?
Right.
I don't see…
**Patrice Chalin (Cloud Native Computing Foundation)** 01:58 I can repost here… I didn't go to the original invite, so I don't know whether there's still a link.
Todd did you, or Severin?
**Severin Neumann (Bronto)** 02:13 Sorry?
**Diana Todea** 02:14 Oh, okay, I see it, sorry, I see it. Agenda, cool.
**Patrice Chalin (Cloud Native Computing Foundation)** 02:18 All good.
Hi, everybody.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 02:20 I just joined at the other call to see if anyone was there by accident, no one was there, so I came here.
**Severin Neumann (Bronto)** 02:26 Okay, and I mean, we have 6 people, so it looks good, right? So…
**Patrice Chalin (Cloud Native Computing Foundation)** 02:31 Yeah.
But, well done. Thank you, Marylia.
Nice green screen.
**Severin Neumann (Bronto)** 02:37 Yeah, yeah, I'm just doing some video recordings, so as I set up this whole… stuff here, right? I even have one of those slides I can now… Hopefully turn off, because it starts to get annoying.
Yeah.
Yeah.
It was funny, because I tried to attach this to my ceil… to… to my ceiling, and then, like, the first thing I did is, like.
creating a big hole in it, because, like, I used the wrong equipment, right? So, yeah.
Yeah, a little bit of work to do here. Anyways… Yeah, are we missing anyone? I think Fabrizio said he's not going to join us, so… I think we can get started, and I'm happy to have you all here. I know that, like, last time.
Deanna, I think you said, like, you were here, like, there were only, like, two peoples attending?
So it's good to know that, like, this time, we are a little bit… On, on… On a bigger list.
So yeah, let me, let me, let me, let me share… the meeting agenda, and then we can get started, I guess. If there's anything missing on this agenda.
Please, add it, so let me see… I share that thing here, you can see it, hopefully.
Yeah, cool.
Yeah, first of all, I'm excited that this transition to the new Zoom meeting worked. So, yeah, let's see how this goes.
Forward, I mean, it's, There's some differences we will recognize, especially around the recording. So for our day-to-day business, this is probably not making a huge difference. Okay, cool. So let's get started, maybe. Vitor, you have… a topic that I think I don't… cannot open the Slack link here, but maybe you can just give us a rundown on it?
**Vitor Vasconcellos** 04:45 Alright, yeah, that's actually one of the… One of the topics we've been discussing a lot over the past month.
It's actually related to the… To the… to the changes across… Lookouts.
with… Yeah, how can I say? There's this… this gray area where… Which… on which… With changes, we can consider, like.
Scope it changes, or we can… considered… how can I say, essential changes to, like, a link fix, or… or things that we could spend across multiple locales, and there's a discussion that was originally raised by Yoshin last week.
And… I was just finishing reading the proposal that Patrice share it.
And Yeah, I think we can… we can go over it, and… Hmm. Oh, yeah.
**Severin Neumann (Bronto)** 05:59 Yeah.
**Vitor Vasconcellos** 05:59 I was just finishing, so I was just wondering if, Patrice want also to give some overview on the proposal?
**Patrice Chalin (Cloud Native Computing Foundation)** 06:13 Sure.
essentially, The proposal is to remove the gray area, and to restrict multi-loccale changes.
To be done only to either allow the build to pass or checks to pass, which usually means link checking.
And, for about a month now, we've adapted the link checker so that it ignores drifted pages, so we don't have to worry about drifted pages anymore. So the number of PRs where we actually have to have multiple locales is going to be less and less.
**Severin Neumann (Bronto)** 06:56 Okay.
**Patrice Chalin (Cloud Native Computing Foundation)** 06:56 And my suggestion would be to limit it only to those two cases. Either the build is broken, you just can't submit a PR without touching another locale.
Or, same thing, there's a check failing. Well, a check failing means link checking not formatting, or something like that.
In another locale. And there's a footnote… there's a note there that says that, by the way, maintainers might be able to do… might be doing cross-local infrastructure broad changes, and those don't address, are not in scope, because what we're seeing here is we don't want any semantic changes. Anything that changes the meaning or the way that a user can interpret the content, that includes code or configuration or whatever, to be, multi-local.
or a PR.
That's the gist of it.
**Severin Neumann (Bronto)** 07:49 Okay.
Okay.
So we go from, like, very strict, like, hey, never touch it, to, like, hey, there's some corner cases that we learned over time.
Should work that way, and then beyond that, it's still like, yeah, do not… Touch it until, like, someone reviews it from a localization team.
Or have multiple PRs, right?
**Patrice Chalin (Cloud Native Computing Foundation)** 08:11 Correct. And what's nice is that there's no ambiguity here, we can test it.
**Severin Neumann (Bronto)** 08:15 Okay.
**Patrice Chalin (Cloud Native Computing Foundation)** 08:16 a PR, if you remove the non-English changes, or you set Remove any of the… multi-local changes, then the PR breaks, essentially.
**Severin Neumann (Bronto)** 08:27 Yeah.
**Patrice Chalin (Cloud Native Computing Foundation)** 08:27 So that's our unambiguous mechanical test. We're not going to do that, I don't think we need to set that up, but that's our criteria.
**Severin Neumann (Bronto)** 08:36 Okay.
**Patrice Chalin (Cloud Native Computing Foundation)** 08:36 I mean, that's the suggested criteria.
How does that sound?
**Severin Neumann (Bronto)** 08:43 I mean, it works for me, but we have a few localization approvers and maintainers here, so I'm curious to hear your opinion.
**Diana Todea** 08:52 So, be honest, I mean, when we receive that workflow, it's, like, sometimes it's not very clear what we need to approve upon, like, what's the actual content from our side.
It's just, like, sometimes it's just, like, a bunch of commits. We are looking through those, and we are, like, trying to see exactly what's… where's that relevant chunk of… You know, content that we need to check for our own language.
And sometimes these PRs, for example, they don't really have that part, right? So it's maybe, like.
I don't know, PR that makes a few changes, but there's not really a translation per se, right?
So sometimes it's really difficult to identify that part for which we are responsible for reviewing. And I think this is, like, what's confusing. I don't know, I'm assuming, at least for the others, when they receive the… the PR also, sometimes the maintainer, obviously. Meanwhile, a maintainer, approves it, so it can come late at night due to time zone.
And in the meantime, you know, that PR was already approved and merged, but we didn't approve it from our side as, you know, approvers for that specific localization. So maybe we can clarify a bit these ambiguities.
**Patrice Chalin (Cloud Native Computing Foundation)** 10:25 I see that as a… Distinct topic and an artifact of the way we set up code ownership.
Maybe what could help clarify for you is that if you see the label CI slash INFRA, And if it's coming from a maintainer, That will usually… that may be merged Ahead of your approval, and it may not require a locale's team's approval. It's, again, there… it falls in that note where it said if there may be infrastructure changes that are multi-local.
And for that, we don't want to wait for every locale to come back, because some have very few team members, and it would take too long to wait. And that's why there's… there's no… we don't wait. And the main… hint there is the label CI slash INFRA, so hopefully that can help. For others, there should not be any other situations. Well, this is what we're clarifying and discussing here. There should be no other PRs that do that, that would put you in a state where you're confused, why are these changes Happening.
in my lookout, or… Does that make sense?
**Diana Todea** 11:43 Yeah, no, that's perfectly clear. Yeah, and I think, I mean, after a couple of these PRs, yeah, that was the intuition, you know, that something is happening there, some type of work in that sense. And obviously, you know, it was already emerged, or it was already approved by another maintainer, so that's totally fine, but we lacked some sort of, like, context around it.
But right now, it's very, very clear. So, yeah, that's fine with me, at least, yeah.
**Patrice Chalin (Cloud Native Computing Foundation)** 12:12 Good. Thanks.
By the way, because of code ownership, we cannot remove the required, locale, approvals.
even as an admin, I can't… remove it, so… Anyone else?
**Severin Neumann (Bronto)** 12:35 But if we have some documentation on that, and I think that's why we need that feedback, right? So, we know, okay, this is confusing for localization maintainers and approvers, but because, like.
There's always this situation that, like.
we get in each other's way, so to speak, right? So, if this makes sense. So, yeah, Deanna, I think it's really helpful if you share, like, hey, this is confusing for us, this is our experience.
And it's really helping a lot.
No, I think I'm more than happy to move forward with that, like, I mean, everything we make more clear and more streamlined, the better.
Yeah.
**Patrice Chalin (Cloud Native Computing Foundation)** 13:23 So the PR is still in draft. Once, I'm done with some final polish, I'll remove the draft status and then ask for… Final approval, and you can go through the… Do a final review there if… if you'd like.
**Severin Neumann (Bronto)** 13:41 Okay, cool. Yeah, so action item for everybody is to take a look into that specific PR, it's… What number is it? I just had it open.
10,930. When did we cross the 10,000? That's right.
**Patrice Chalin (Cloud Native Computing Foundation)** 13:55 I know.
**Severin Neumann (Bronto)** 13:57 Yeah, amazing.
Cool. I think we keep the conversation going on localizations, and I think, Deanna, your question is semi-related to that, and maybe I created a little bit of confusion here also. So let me, let me say this.
And I hope it clarifies a few things. I think that… or one goal from the get-go when we did the localizations is that over time.
We want to give localizations teams more and more own responsibility of what you're doing, right? And the thing is, like, right now, and we see this with Korea and localization, for example, we're just bootstrapping them.
there will always be a phase where, like, docs maintainers will stay in the loop, right? I mean, if they come to our page and say, like.
Hey, we want to do a localization into this and that language, but nobody who proposes that is even part of our project.
then we have to shepherd them through that, right? So step one is, like, see how far they get, and then make them members, and then make them approvers, and eventually maybe even maintainers, and this is maybe a separate topic. But I think the moment we have a good group of approvers.
my feeling now is, like, we can hand this over to everybody and to say, like, hey, you can now add approvers yourself, right? I mean, you don't need me, or Patrice, or Vitor, or Marylia, or any other comms maintainer to… to agree on that, right? I mean, we can give you maintainer permissions on the… On the… on this thing, so you can self-manage the approvers. The next step is maintainers, right? And we have done an experiment, I think a year ago, with adding Portuguese and Japanese maintainers.
That experiment failed, but we never rolled back those permissions, and I think what we now have now is that, like, with this auto-merge feature, and Patrice and Vitor, I think you can speak more to that.
We are testing that out.
**Imma Valls (Raintank, Inc. – Grafana Labs)** 15:58 On that…
**Severin Neumann (Bronto)** 16:00 Yeah, yeah, exactly.
**Imma Valls (Raintank, Inc. – Grafana Labs)** 16:02 On that, we have a problem, it's not working for us, so… when you are an approver in Spanish, we try to auto-merge, and it says that we don't have permission, so…
**Severin Neumann (Bronto)** 16:12 Exactly.
**Imma Valls (Raintank, Inc. – Grafana Labs)** 16:13 I don't know.
**Severin Neumann (Bronto)** 16:14 Yeah, because you don't have a maintainer group yet, right? So this discussion that we now need to do is to think about, like, hey.
What other localizations are ready to have certain people made maintainers, right? I think that's just the stuff that's missing. But before that, Patrice and Vitor, I'm just curious how good that auto merge feature works, right? But sorry, I did not want to interrupt you, so please go on.
Imma.
**Imma Valls (Raintank, Inc. – Grafana Labs)** 16:43 No, I was thinking that maybe there's no need to be maintainers if an approver can use AutoMarts.
But I don't know if that breaks the whole OpenTelemetry documentation.
But that's what my thinking was, so we don't need so many levels.
**Patrice Chalin (Cloud Native Computing Foundation)** 16:59 I… I… we do have the two levels in place.
For a reason, and that there's, like, a maturity… There are criteria per level, and like any open source project, there are different levels with different levels of responsibility, and graduation from one level to another is obtained over time through demonstration of contributions to the project. So I think the levels make sense.
To answer Severin in terms of your question, I think auto-merging is working well, and we've had I'm not sure which aspect of the trial you said didn't quite work out, but right now, with the auto-merge and having the maintainer group for the Japanese locale?
has given them full autonomy, and you've noticed that because there's so many Japanese translation PRs coming in, right?
So I think… I think it is working, and it is allowing that team to be autonomous, now that they have a… a maintainer.
group, and… We are in the beginning with some of the other locales, so it's normal for… Other locales to not necessarily have maintainers yet, but as the team matures and continues to contribute, then we're at this point, and we've had this discussion in Slack. It's time to start assessing Could potentially be promoted.
**Severin Neumann (Bronto)** 18:34 Exactly. Yeah, no, that was the thing, like, I wanted to have a little bit… the experiment I was referring to was, like, a year ago, where we gave maintainers, localization maintainers, full permissions on the repository. Right. And they could not only merge localization PRs, but any PRs, and it was not feeling like… I mean, technically, I would laugh that, like, I, as a non-localization maintainer, cannot even merge your work, right? So technically, that would even be better, but, like, it's not possible right now, but, like, having a little bit of net separation to say, like, hey.
You work off your stuff, and then, like, you have this, this, this, this, how you say, like, additional responsibility. So, so, but, but, but to get back to, to the original answer, so… Question. So, so I think there's, there's, there's one answer. So one answer is definitely We need to look into Spanish, Romanian, what are the other ones that are really mature right now?
I think even French, so there's a few localizations beyond Japanese and Portuguese that we maybe just need to look into and make a decision like, okay, you're doing this now for a year or something like that, so maybe we need a soft criteria where we say, like, hey.
if people are doing this for this and that period of time, and have done their PRs and reviews, and we have the feeling like everything is in a mature state, then we can make people maintainers, and my understanding is with that, you can Almost work independently, right?
Until then, yeah, I think what we need is… is a better way to… That you can get ahold of us and say, like, hey, we have done our homework, all that's missing is a maintainer to… To… to merge that PR, and… and I think the… the place for that… I mean, the one thing is, like, and I want to look into this later, is the pull request dashboard, right? I mean, that should help with… a little bit with that. But… but the other thing is, of course, we have the… how is it called? OTel Docs localization.
General, with an S or without an S, I'm not sure.
ping us there, and don't wait one or two weeks, right? I mean, the moment you're ready.
just say, like, hey, I need a maintainer to merge that.
I mean… The other maintainers, maybe you disagree with me on that, but, like.
I think that's one of the cases where I would be totally fine if you just drop us a message.
almost immediately, and say, like, hey, here's a… or maybe do it once every week, and say, like, here's the list of Spanish localization PRs that need a… a comms maintainer to merge, or whatever, right? So, but I really don't want you to be stuck for more than a week. Let's maybe put it that way. So, two weeks is way too much.
**Patrice Chalin (Cloud Native Computing Foundation)** 21:28 I agree in terms of… timeline, I might suggest that, There not be a ping per message, because we already have.
**Severin Neumann (Bronto)** 21:37 Yeah.
**Patrice Chalin (Cloud Native Computing Foundation)** 21:38 overload of notifications from GitHub.
I think… A few… in the maintainer team, there have been people moving around and moving and whatnot on vacation, and so… We have lost, track of locale PRs where we just needed to come in and approve We can pick up the ball again, and make sure… there are no unreasonable delays, but certainly if there are unreasonable delays, then… then let us know in that channel. It makes sense.
Imma, did you want to add something?
**Imma Valls (Raintank, Inc. – Grafana Labs)** 22:24 No, no, that's all set for me. I wanted to know also what was okay to premium. We didn't want to ping you immediately, like, hey, we need this match.
prefer… I think it's a good idea to just have all the… we have, for example, now two peers, but they are reviewed, we can send them. If in a week no one has got to them, we'll send them on the channel. That's perfect.
**Patrice Chalin (Cloud Native Computing Foundation)** 22:45 Thank you.
**Severin Neumann (Bronto)** 22:46 Yeah, and as I said, I think at the end of the meeting, we should quickly look into this dashboard here. I think it should also help us a little bit on that, right? That we say, like, hey.
This is waiting on reviewers, and we see, like, hey, nobody looked into that.
And I suspect there's probably some… you see here's some Japanese, here's some… here's, for example, a Spanish one, and we see, like, hey, nobody has taken care of that.
So, so hopefully we can, we can assist you with that.
I said, semi… semi-related to that, it's like, Deanna, what, what you asked here, and… and… and Imma, I think I… I said I… I put this on your plate without a lot of… Without a lot of context, and we really don't need To discuss this out here, but what we would need is, like.
the Spanish maintainers to look into that, and then say, like, hey.
Yep, we want you to be added to this group of approvers, and I think and I hope you have the permissions to that.
No, you don't, so let me add.
Changed his… I don't know.
**Imma Valls (Raintank, Inc. – Grafana Labs)** 23:55 Actually, that would be the next step? How do we do that?
**Severin Neumann (Bronto)** 23:59 Yeah, so you are now… so you and Carol and Pablo, and I think Pablo said at some point he wants to be removed.
**Imma Valls (Raintank, Inc. – Grafana Labs)** 24:07 Inc.
**Severin Neumann (Bronto)** 24:08 But you're now able to add additional approvers, right? So you and Carol And whenever you add someone to this group, also give them that permission, because really, we want you to self-sustain those groups, right? We really don't want to be the bottleneck here. And if you ever have the feeling like… and this is also like, Deanna, I don't know if I gave you the permissions for the Romanian approvers already to self-manage on that.
If this is necessary, then just let us know. I think, most of the localization groups are… are… are experienced enough to manage that themselves. I'm not sure if we would do this for all of them from the get-go, right, if we now have a new group.
Coming up, and we have to think, like, hey, we want them to be approvers, but maybe not yet self-select, but that's one of the… maybe we have to lay out this journey a little bit clearer on, like, how do we get from No localization at all, up to, like, hey, you now have maintainers.
and you just do your stuff, right? And are just very autonomous on that, so that's maybe a homework that we need to work on.
**Patrice Chalin (Cloud Native Computing Foundation)** 25:16 I have a separate PR in flight that talks about, somewhat related topic to localization, graduation, so we can maybe have a discussion around that PR.
**Severin Neumann (Bronto)** 25:27 Yeah, no, that's, that's, that's really cool. If you, if you… do you have to PR by hand, at hand, or is it…
**Patrice Chalin (Cloud Native Computing Foundation)** 25:33 I do. It's… it draft status. I'll drop it in the, the notes.
Yeah, we can talk about it.
Later, offline.
**Severin Neumann (Bronto)** 25:50 Yeah.
Okay, now let's, let's… maybe everybody can, can take a look into that.
Patrice, you have two FYI topics, so maybe you can want to speak about it real quick?
**Patrice Chalin (Cloud Native Computing Foundation)** 26:02 Well, they are just… you earlier today asked about, an announcement for QCOD Japan. I'm working on that. I… the reason I'm bringing it up here is I think you also were wondering whether we should have a blog post or not. Was that it, or is the announcement enough?
Well, I guess we'll start with the announcement, and then you.
**Severin Neumann (Bronto)** 26:28 You can comment.
**Patrice Chalin (Cloud Native Computing Foundation)** 26:29 comment on that PR, whether you want a blog post or not, but that'll be more work.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 26:34 In the past, we did a few blog posts just sharing, like, what are the talks related to OpenTelemetry. So, is that included on your announcement, or…
**Patrice Chalin (Cloud Native Computing Foundation)** 26:44 No.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 26:45 Okay.
**Patrice Chalin (Cloud Native Computing Foundation)** 26:45 The announcement is just the banner on the front page for now.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 26:48 Okay.
**Patrice Chalin (Cloud Native Computing Foundation)** 26:48 We have all been separated the two, because reviewing a blog post is much.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 26:52 Yeah.
**Patrice Chalin (Cloud Native Computing Foundation)** 26:53 involved, and then… yeah.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 26:55 So I think it might be worth the blog post just to have, like, the list of, like, hotel talks, like we did in the past.
**Patrice Chalin (Cloud Native Computing Foundation)** 27:02 Then we need somebody to own that.
Crickets.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 27:08 Yeah, I'm crazy.
**Severin Neumann (Bronto)** 27:09 Maybe you're raising your hand if I volunteer.
**Leandro Caracciolo** 27:14 Patrice, if you need some help on social media assets, or illustration for the event, or something like that, I'm available.
**Patrice Chalin (Cloud Native Computing Foundation)** 27:23 Got it. Thank you.
**Reese Lee** 27:26 For the Japanese blog… KubeCon blog post, you just need someone to, like, get a list of the OpenTelemetry-related talks.
**Patrice Chalin (Cloud Native Computing Foundation)** 27:38 I can do that. Yeah, and I… I think we have a script in place somewhere that somebody… but, I mean, if you… a friend of your… any friendly AI agent can certainly get a list.
But I think there's a script somewhere. I don't know where it is, though. We'd have to look at a past, I'd have to dig through, but thank you for offering.
**Reese Lee** 28:02 Other problems.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 28:03 Yeah, to give an example, here's the, like, the blog post that we did for, like.
the KipCon U. You see, like, the blog itself doesn't have, like.
Anything that you need to create on your own, it's just, like, Hey, this is coming!
These are the things. So that would be the equivalent blog post.
**Reese Lee** 28:24 Yeah.
**Severin Neumann (Bronto)** 28:26 Yeah, I think Last time, I'm not sure who it was, but I think you can even, even ask an LLM to maybe work on that, and then just pull down.
the content for it, but… but yeah, having it would be really cool, especially since we have that… that keynote, by Tad, and Alolita, so that would be really cool to highlight that, even in a blog post.
Yeah.
**Reese Lee** 28:54 Yeah, I will get that in… That's awesome.
**Patrice Chalin (Cloud Native Computing Foundation)** 29:00 We'll see.
**Severin Neumann (Bronto)** 29:01 More blog posts, but yeah, I mean, let's go for it.
Cool.
then, yeah, we'll wait for that, and then, Patrice, you have another… or anything else on the KubeCon thing, on the event?
Nope.
So…
**Patrice Chalin (Cloud Native Computing Foundation)** 29:22 The next point was just to say that today landed some PRs related to a switch of link checker. So this is just to say we've got a faster link checker now. You do have to install it locally, it's a separate step, but it's a step forward. If you have any issues, ping me on Slack or in the, Tom's channel, and I will look into it. But so far, it's been smooth sailing. We've been using it for a couple of weeks in parallel with the old checker.
That's it for me.
**Severin Neumann (Bronto)** 30:01 I mean, the next one is also your top one.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 30:03 Yeah, I was gonna say, you were also next.
**Patrice Chalin (Cloud Native Computing Foundation)** 30:05 Oh, no, that was the link you were asking, and I didn't know where to put it, so…
**Severin Neumann (Bronto)** 30:11 Okay, yeah, everybody did take some time looking into that.
**Patrice Chalin (Cloud Native Computing Foundation)** 30:16 After the draft status is removed, it's still working.
**Severin Neumann (Bronto)** 30:18 Okay. Okay, cool.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 30:21 So next one is actually, mine. So yeah, for those… If you don't know, we have, like, a survey that is when a person is not a member, and they got a BRT merge.
That is coming from the, like, consumer experience SIG that we want to see the experience, so I'm trying, like, from time to time, share the responses. So the last time I shared here was, like, 6 months ago, so I'm trying to keep that cadence. So for this past 6 months, so we got 41 people that reply, the average are 4.8.
The… yeah, the majority of people gave, like, a 5 score, and we had a couple of… force, and… one… like, 1, 2, and 1-3 kind of thing. That was the majority. So the pros was a lot of people, very positive experiencing, like, people are respectful, kind, they like the responsiveness of the reviews, clear explanation when they ask for stuff, so it was in general really good, like, people were really happy, so… First of all, I want to say congratulations to everyone that has been working a lot, because that calls like this very welcoming, like, people.
For things that people mention for improvement.
there are things that we don't really, like, control, like, for example, the CLA was saying, like, oh, I want, like.
my address and stuff like that, like, why do I have to provide my address if I want to fix a typo kind of thing? So it's not something we can do much about it, but I'm bringing up just anyway. The… so a lot of things were related to, like.
tooling? Well, let me actually… one first, that is just, like, a person had… one mentioned, like, I had a draft PR, but I had questions, but I didn't know if I should, like.
open the PR to get reviews, or leave it there, and already, like, tag people, so it was, like, trying to understand the protocol, but a lot of them were related, like, to the tooling, because I had a few comments that were, like.
I am not a dev person, but I want to help with, like, docs.
So they say, like, can we create, like, a guidance for somebody that is not a developer? Because they're like, I don't know what a Zoom module is, and I have to, like, sometimes fix this, like.
I don't know what that is, so they were like, can we have, like, a very basic, like, okay, if you just want to help with the documentation, like, I think, like, if we review, that's fine, but if they want to create their own, like.
Or it could be even related to localization. They were just asking if there is a way to have, like, a guidance of, like, some basic stuff for non-developers, more like tech writers that can help out. And yeah, that was pretty much it from the comments.
**Severin Neumann (Bronto)** 33:01 That's great.
**Patrice Chalin (Cloud Native Computing Foundation)** 33:03 Yeah, thank you so much.
**Severin Neumann (Bronto)** 33:04 Yeah, yeah, yeah, I… I was thinking about the survey the other day, and it was like, hey, we never look into those numbers, so thank you.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 33:11 Oh, no, I look at it almost every week, and I check, so when there is, like, when there is enough, I share, because I don't want to, like… as soon as someone, like, merged, I share so you kind of know who it was, so I try to A little, like, but with the time, like, there are a few SIGs that have, like, 4 answers, and I have, like, Collector Country that had, like, 76 replies, so it is also, like, changed a lot by SIG, so, yeah.
**Severin Neumann (Bronto)** 33:38 How many these days with the server, like, how many SIGs are using it today?
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 33:43 So we have, like, this one, JavaScript, Java, Collector, and CollectorConstrip.
**Severin Neumann (Bronto)** 33:53 Okay, maybe we need to be promoted a little bit?
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 33:56 Yeah, I was thinking, because one thing that I did is, like, I put it on the share workflow.
**Severin Neumann (Bronto)** 34:01 Yeah.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 34:01 now is easy for people to use. The only thing that I need to actually manually update the form itself.
to actually have… oh, also .NET, and just to have the option to select their repo, but I'm planning on, like, actually adding two more repos, just, like, I can do this, like, on my own, and then people can, like, approve the PR or not, but yeah. It's similar to the… also the… The shared workflow about, like, first time.
a person that shows that message, like, hey, this is a CLA, or, like, don't use AI.
like, follow, like, the policy, so I'm also adding that one to a few repos.
**Severin Neumann (Bronto)** 34:41 Okay, cool.
So, first of all, I think on the ECCLA, I saw something that someone said, like, they want to change that, that you only need the email address or something like that, so… Maybe I'm mistaken on that, but yeah, I mean, that has been a complaint since probably the inception of the project, so that's… but I think, yeah, I totally see the problem with the… we are one of the few sub-projects that are really geared towards non-developers, or more geared towards non-developers than other projects, but with the submodules. I mean, we have a bunch of workflows that help with that.
But yeah, maybe, maybe we can… I don't know, maybe we can get creative around that, so… I wonder if we should turn that a little bit into issues, and then have it at least locked away outside of the… of the Google Doc, so that we maybe at least have a, like, hey, this is what people are reporting. But Patrice, I see you're raising your hand, so…
**Patrice Chalin (Cloud Native Computing Foundation)** 35:50 There are two types of complexity. There's essential, which we can't get rid of, and non-essential, which we can.
the path, I think, for simple contributions is to use GitHub, the GitHub interface.
And just, you change a typo, you submit a patch.
And then use the slash fix command.
And so what we could do as a step in the direction of helping, drive-by contributors and whatnot could be to add support for slash help.
Which I think we might have an issue open already.
**Severin Neumann (Bronto)** 36:26 could…
**Patrice Chalin (Cloud Native Computing Foundation)** 36:27 help. But in terms of I think we are trying to make local dev contributor experience as smooth as possible. And, But the fact that we're using submodules, which I might be able to get rid of, could help, but it's still… there's a part of the complexity of pulling in fragments in… submodules from other places that we can't get rid of, and I'm not sure we can make it simpler.
Other than… I know even Reese submits big PRs from a patch, And just using the web interface, which is probably the simplest way to do things.
And I would guide… drive-by contributors or simple typo fixed contributors to use that. Would that help?
Does that make sense?
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 37:21 Yeah, I was gonna say, like, we can add those things, like, to the… we have, like, the contributor file, right? Like, how you wanna, like, contribute. So we can have, like, a session for, like, tips, like, on how to contribute. So you have, like, oh, if it is, like, a simple thing, follow this. If you need to run.
this is the basic thing you should know about, like, Super Mario. Just run this command to update, kind of thing. So we'll have, like, I was thinking just updating our own contributing guides to have… Makes sense. Yeah.
**Patrice Chalin (Cloud Native Computing Foundation)** 37:53 Deanna?
**Diana Todea** 37:55 Yeah, no, I mean, it relates to what you and Marylia already said, basically, I don't know, probably besides the guides.
have, like, a glossary, what does it mean? Because sometimes, maybe it's not even that they want specific sub-modules to be gone, or fixed, or whatever. It's just, like, what it is that, right? So, what does it do? What's that about, right? So it's just that curiosity.
And sometimes, even for devs, it's a bit hard to understand until, you know, they go once, twice, three times through the process, and then obviously it's clear.
So yeah, like a glossary, or even, like, a, maybe extrapolating, like, a video, I don't know. So that will be there, and everybody can look at, you know, besides running webinars or something like that.
Yeah, we can get creative, I think.
**Severin Neumann (Bronto)** 38:52 Yeah, I mean… Interesting. I mean, one thing, of course, we could do, but of course, we would need someone to staff that, is something like a… I don't know, monthly… call where people can jump on and can get additional help, or something like that. I mean, the other thing is, like, we have our contribution documentation, and I think it is very… detailed, and then gives away a lot of information, but at some point, it's maybe a little bit too detailed. So, like, balancing that is always, like, the big challenge that we're facing, right? I mean, at the end, what people maybe sometimes would need is something like, hey, they open this up with whatever IDE they're using, and the IDE can tell them, like, hey.
you need to update your submodules, you need to do X, Y, and Z, so… but it's like… Making things really, really complicated.
And I think we have chatted about this for years now, but yeah, I think we improved a lot as well, right? I mean, at least that we have some… something like a fixed submodules command is already, like, I think.
a big improvement, but yeah, I mean, I'm always open to review any suggestions to make things better, but yeah.
I said, maybe, Marylia, we can take some of them and put them into issues, and then keep the conversation going.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 40:10 Yeah, I can open the issues for all those.
**Severin Neumann (Bronto)** 40:13 Yeah, appreciated.
Cool, anything else on the survey beyond that, like, we did a great job here?
Okay, Deanna, I think we… we partially addressed your issue, but, like, I think you had another question about the… the… the localization meeting, so… so yeah, we can quickly talk about that.
**Diana Todea** 40:36 Yeah, sure, yeah, it's just a quick one, so, because obviously you're running, you know, with the changes on the platform.
So like I said, at the moment, I'm gonna discuss with the Romanian localization exactly if we can commit a specific I don't know, date and week, that's a problem with us, because everybody's working, and they're like, nobody can commit to an exact weekend. So far, we've made it only for the date and the hour, but not which week of the month.
So, yeah, it… would that pose a problem? So, in case that… This is not happening, so we cannot do this on the new platform. We need to select a specific week, and even if we miss it, then we just miss it.
**Severin Neumann (Bronto)** 41:21 I mean, if it's really only about a week, right, and if you say, like, hey, we meet, I don't know, on Tuesday at 6pm, whatever, let me… Take that as an example.
then I can schedule you a meeting that happens every week on that day.
I actually can also keep it out of the public Linux Foundation calendar, and we can put in a note that says something like, hey.
This is not happening every week, so come to the… Romanian channel and then ask people. The only thing I cannot do right now is give you some kind of ad hoc meeting that you can do whenever you want, right? So that's, like, that's what we could do with our own Zoom. We could create a room and just give it to people and say, like.
run it whenever you want to, so that Linux Foundation platform thingy is requiring us to say, like, hey, this meeting is happening every week at that day, at that time, and I cannot just say, like, yeah, whatever you want to do. So, if you can really say, like, hey, we want to have this Open every week on this day, on this hour, then we can run for it.
just to add that, like, we got the feedback, of course, from Linux Foundation, like, hey, you could give people access and they can do their own meetings, but as you know, like, this brings us back into a governance problem, because, like.
who gets access, who doesn't get access. Right now, we keep it simple and say, like, sure, GC is just managing this for everybody.
But the moment we say, like, hey, every maintainer, every approver has access to that, we have, like.
Correct me if I'm wrong, like, almost 200 people having access to it.
That's not scaling, so I… I would… sure, we could talk about that in a community issue and see how it scales from there, but if you have that solution for me, then, and say, like, hey, we want to meet same day, same hour, but not sure about the week.
Yeah, let's… let's put this into the calendar, and we can… we can work off that.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 43:27 I can give an example, like, when we did, like, the Portuguese one, we had on the calendar for, like, every week, but we didn't do it every week. We were, like, on the channel, we would say, like, do we actually have topics for today? And people were like, no, I cannot attend. Okay, so nobody joined, but the meeting was there in case we needed, so… Yeah.
**Diana Todea** 43:47 Yeah, perfect. Yeah, I think we will do it like that, and don't worry about the… setting up meetings, it's fine the way it is.
It's just, like, more, like, I think we'll do it recurrently every week at a specific hour, and that's it. I think the only ask was, to be publicly visible in case we want to… Revisit the videos, so if somebody wants to go and check the recordings.
Definitely, we want to have that, so if that is possible, then it's great.
**Severin Neumann (Bronto)** 44:20 The recordings are not yet sorted, is my understanding, right? So we will have recordings, but we have not yet figured out 100% how to… so we preferred our existing pipeline, right? We prefer to have them not public on YouTube.
But,
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 44:37 So, right now, they are available, like, on the calendar, like, if you go to the LFX calendar, and you go to… if you go to the one that, like, oh, this one already happened, if you click it, it's gonna show the link for the recording.
What is not happening right now is that we have, like, the spreadsheet that pulls the link for all of them. That is the part that is not working for the new ZO accounts.
But if you go to the calendar itself, let me show the… like, this here… this one, so for example, if you, like, look right now, the ones that already passed is gonna be on gray, and then if you click on them, it's gonna have the link for, like, the… you can see, like, share, whatever is the recording. So it is available, yeah.
**Severin Neumann (Bronto)** 45:23 Okay, okay, that's good to know. Okay, cool. So then, you know, just let me know, like, hey, we want to meet that week, that time, and then we can set it up for you the way that you're, like, flexible on the specific date.
I think the worst case that could happen is that someone shows up in the wrong week and is surprised that nobody's in a meeting, but I think you have a good relationship with everybody that's right now part of the Romanian localization, so… Yeah. No, cool.
**Diana Todea** 45:49 Perfect, sounds good. Thank you.
**Severin Neumann (Bronto)** 45:52 Awesome.
I'm happy that we have another 15 minutes remaining.
So that gives us a little bit of time to… click into the pull request dashboard. I don't know, anybody already spent some time on that? Like, I haven't… open from time to time, but didn't really get to rug off it. So, I don't know, anybody wants to comment on it, or sell, like, if any, any existing experience with it already?
**Patrice Chalin (Cloud Native Computing Foundation)** 46:25 I haven't worked with a dashboard, but I have noticed the comments that appear on PRs to say what the status is and what next steps are, and I think that's… that's brilliant, I think.
**Severin Neumann (Bronto)** 46:40 Yeah, I really like, like, that part here, like, I see already, like, I have a little bit of homework to do, so… Yeah, so I think the idea is a little bit to have a central place that allows us to… see a little bit quicker, like, like… so we all know that, like, GitHub notifications are just, like, useless, right? I mean, I'm not sure what your experience is, like, I have… a workflow that works for me, but especially those kinds of things of, like… I tell people, like, here's my review, and then, like, maybe I forget about it for, like, 2 weeks.
then I'm just, like, not able to come back to it, so it's really helpful to see how, like, hey, there's even things, like, that are open for a really, really long time. So I think one thing we definitely can look at is making sure that we maybe get a… kind of… SLA for that here that we say, okay, there's just nothing waiting for reviewers more than, let's say.
38 days. Maybe less than that, so if we… so actually, I'm quite excited that, like, the most of them are, like, below 14 days, and then, like, really quickly, like, we have really good numbers on that.
So, so yeah, I think, like, this, this is, like, hopefully a place that, that we can work off.
We don't have to start with it today, but I think in the future, what we also can do is, like, if we have a little bit of time in this meeting, maybe we can find a way to Go through them, and then maybe do even a little bit backlogs.
scrubbing. But yeah,
**Patrice Chalin (Cloud Native Computing Foundation)** 48:23 One idea could be, a lightweight version of what they do in Kubernetes, which is to have a PR Wrangler.
assigned for… A month.
Or whatever, a week, or two.
**Severin Neumann (Bronto)** 48:39 Yeah.
**Patrice Chalin (Cloud Native Computing Foundation)** 48:40 Just somebody who's named, and that… while they're drinking morning tea or morning coffee, goes through the 100 and whatever day-old PRs and figures out what to do. But it requires… it requires time and investment to figure… figure out and track down people and things like that. But if we have an assigned role and we rotate through it, then that can help.
**Severin Neumann (Bronto)** 49:03 Yeah, I think that's something we can also… I mean, we now have… A good group of maintainers and people that can help with that.
So, so yeah, maybe that's something we should, we should think about and talk about. Did we maybe find… among maintainers, and maybe also the triager group, right? I mean, we have a bunch of triagers, and I think maybe it's a little bit of a guidance problem. Maybe we can talk about something like that, that we have a maintainer and triage assigned every week, or every, what do you say, like, two weeks, and then say, like, hey, it's now your job to keep an eye on that.
So, yeah.
I said, I mean, technically we could go over it, but I would right now not be sad if I can save myself 10 minutes to go back to the family.
So, yeah.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 50:03 Or bring the family, and we all reveal together.
**Severin Neumann (Bronto)** 50:07 Yeah.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 50:07 I won't.
**Severin Neumann (Bronto)** 50:10 We can do this the moment we have a German localization, and they're maybe happy to help with that, but, like, beyond that, this is not a family adventure yet.
Awesome! No, I think this is, like, really good, and I think to echo something that Patrice said in between the meeting, like, I mean, a lot of the maintainers are right now for whatever reasons, a little bit impacted on their availability and on their attention. At least for me, it's getting better now that I'm back in my new thing with Bronto.
So, so yeah, I really hope to, to follow up with a lot of things, so, yeah, just keep patient with us, and like… I mean, yeah, today was a successful meeting, so yeah, thank you, everybody, and speak to you in two weeks.
**Patrice Chalin (Cloud Native Computing Foundation)** 51:02 One question before we go.
It could be just for maintainers or for everybody, but it's regarding, taking our own medicine, and having our own collector. Vitor, do you want to take this offline, or do we want to talk about it during this meeting?
**Vitor Vasconcellos** 51:21 Yeah, we can take this offline. Actually, there's just one thing that I wanted to… To start out, before we start provisioning the components is where this is gonna live.
We have the admin repo, and we currently have our .io repo.
I kind of like the… the idea of having the… the configs.
as public files.
So… My idea was to… Mix, to merge both.
Both ideas and have a separate repo.
Where the… AIC configs relevant, so we don't mix the… Documentation repo with some infrastructure management, but… Yeah, I have this… there's a PR that I raised… Earlier today? Earlier this week.
Which, I haven't merged it yet, and if someone wants to leave some thoughts on it.
We can also discuss… async, or… Oh… Whatever works, also.
So let me share this with you.
**Patrice Chalin (Cloud Native Computing Foundation)** 52:45 I was gonna say if you could share the PR.
I, agree with the preference you just stated.
I just wanted to maybe step back and reframe the… To me, the goal was to take our own medicine, and whether it becomes, Infrastructure as code, or not, We can just… Whether there are any config files or not, we can have A collector collects some data and shows it through some dashboard.
which I think is less than… doing… IAC.
That was the only comment I wanted to make here and get your feedback on.
**Vitor Vasconcellos** 53:31 Oh, right, yeah, okay,
**Patrice Chalin (Cloud Native Computing Foundation)** 53:36 And we can take it offline as well.
**Vitor Vasconcellos** 53:38 Yeah.
Definitely, definitely. Yeah, I was thinking more of… How… how we can… Make sure not, to… to also show the people how we are setting up the environment, but the idea is to make everything fully available for everyone, from the dashboards to the Oh.
We created it, and how we are… Configure.
**Patrice Chalin (Cloud Native Computing Foundation)** 54:07 I agree with that objective. I think it's… it's a good… Yep, I agree with that objective.
**Vitor Vasconcellos** 54:17 And, yeah, and the AIC was basically the… how we can make it easy to… For us to… to maintain.
Without needing to… everyone having access to… To… to the… To the account, or having… Yeah.
Too many permissions, but… Yeah, anyway, there's the pull request, and… I also… Invite everyone to leave some feedback.
**Severin Neumann (Bronto)** 54:52 Yeah, that's very cool.
**Patrice Chalin (Cloud Native Computing Foundation)** 54:54 Thank you.
**Severin Neumann (Bronto)** 54:57 Awesome.
I need to drop now, so if you need to discuss anything else, but… talk to you soon.
**Patrice Chalin (Cloud Native Computing Foundation)** 55:08 Bye, everybody.
**Diana Todea** 55:09 Bye.
**Vitor Vasconcellos** 55:10 Thanks.
**Sophia Solomon (Elastic)** 55:10 Hey, everyone.
**Leandro Caracciolo** 55:11 Oh, thanks.
