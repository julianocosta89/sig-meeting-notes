SIG: Contributor Experience SIG
Date: 2026-08-10
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 00:54 Hello.
**Ivan** 01:04 Hello?
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 01:08 How are you?
**Ivan** 01:10 Very good, very good, thank you. You?
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 01:13 Good.
**Amy Super** 01:15 Kayla.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 01:16 Hello!
**Amy Super** 01:23 How is everybody?
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 01:26 You?
**Amy Super** 01:28 Ed.
Oh, I have some people joining.
I think we'll give a few minutes, but one of the things… Let me get our agenda up.
that I had hoped to use today for was to just do, like, a good old-fashioned backlog grooming.
Because a lot of our tickets are really out of date, and it's making it difficult for people who want to be involved with our SIG to, Pick things up and work on them.
Or some of them are, like, really broad, and so, Bogdan had suggested that last time we met, and so, that was what I threw on the agenda for today.
So… also wanted to… oh, maybe I didn't throw it on the agenda. Oh, I put it on next, yes. Okay, it was there, alright. I was like, I swear I wrote that down somewhere.
So I think we'll just give people a chance to join, and then we can jump in, and I'll share my screen and do that, so… Duck.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 02:33 Anyone has also any other topics that they want to figure out?
**Amy Super** 02:36 Obviously.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 02:36 F.
**Amy Super** 02:37 Yeah.
Cool.
And is it Ivan? Ivan or Ivan? How do you pronounce your name?
**Ivan** 02:47 It's Ivan, yes.
**Amy Super** 02:49 Ivan, great.
**Ivan** 02:50 I'm used to both.
**Amy Super** 02:52 Okay, well, it's nice to meet you. I don't know that I've seen you before here, and so thanks for joining us.
**Ivan** 03:00 No, it's, it's the first time.
**Amy Super** 03:03 Thanks. And is it Abhi or Abhi? Am I saying that right?
**Abhi** 03:07 Yes.
**Amy Super** 03:08 Great.
All right, nice to see you as well. So Abhi messaged me, and I said, well, great, you can join our SIG meeting today, because we're going to do backlog grooming.
So, yeah, I don't know if either of you, Abhi or Ivan, want to just, like, say a few words of introduction, if you're interested in that. If you're not, that's okay. If you just want to, like, hang out and attend silently, that's perfectly okay, too.
**Abhi** 03:32 Sure, I can quickly introduce myself.
Myself, Abhi Manu, I go by Abhi. I work for Bloomberg. I have been, involved, with OpenTelemetry project at Bloomberg for a couple of years now, on the observability side for our public cloud and Company level, open telemetry, you know, observatory practices. Right now, I work on security tooling, so we work a lot with security events and login data that nobody clicks. So, focus on that side, but so, like.
Very much interested.
hotel. We had a… Bloomberg cohort with OTL, that's very well.
I've been… heavily involved recently, and I thought I'll continue helping out.
**Amy Super** 04:26 Well, thank you for that. Thanks for joining us. Go ahead, Ivan.
**Ivan** 04:29 Yeah.
Yes, so I'm Ivan. I'm based in Norway, in Oslo, and I work as a tech lead in Landlow, which is a fintech company, for long comparisons.
Quite new, I would say, to OpenTelemetry in general.
But, since we're doing a little bit of migration, being bought by another company, seemed like a good opportunity to… to refactor a little bit our systems, and to start using a little bit more of OpenTelemetry for, observability. So that's how I started, learning a little bit more, in depth, and then… yeah, I found a couple of typos in the website, and wanted to contribute, and that's how I got interested, and I was like, okay, why don't I join and do maybe something more, if it's possible? And, yeah, that's how I ended up here.
**Amy Super** 05:35 Nice.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 05:36 And also, to give a little context, in case you need more information about this group, so yeah, this one started because we did not have, like, a a way to kind of, like, focus on… because we have a lot of contributors, so we do have people that are, like, using Hotel, so we help a lot with documentation on how to use hotel, but not how to contribute to Hotel. So we started this SIG precisely to help out people that wanted to be contributors. We already did, things, like, for example, we didn't have any all the ripples do not have, like, a contributing guide, like, things that are required to be able to do this, so… this group, like, help with that. So, we are basically always trying to get, like, feedback from contributors and see what we can do to help with that experience. So even if, like, both of you, on your own experience, you had an idea, like, something that would make the things better. We're always happy to hear as well, and yeah.
**Ivan** 06:34 Thank you.
**Amy Super** 06:37 Alright, cool. And then just for, maybe a little bit more context on why we're doing backlog grooming today, is that, I think that the SIG was really active.
Up until, I would say, probably, like, the end of 2025, early 2026. And at that point, we started to see some drop-off in participation because some of the maintainers took new roles, didn't have as much time.
And since then, it admittedly has been a bit of, like, fits and starts, where we're, you know, kind of trying to get momentum. But I think one of the things that's a real challenge is that the people who originally kind of built out the backlog for ways that we could improve the Contributor experience, may not necessarily be as active with us as they used to be. And so, I think a lot of us have felt like we've been kind of, like, tiptoeing around the issues, trying to figure out what the right way is to tackle it. And so, you know, open source is sort of, built on people just, you know, actively involving themselves, and so we're all going to actively decide what to do with some of these backlog items together. Some of them maybe we'll keep, some of them maybe need to be split out, some of them maybe don't make sense anymore, and so that's sort of, we're gonna try to make this not painful, but we'll see how far we get, because backlog grooming is always, A little, detailed, so… Any questions on that before I share my screen and we kind of jump in?
Alright, cool. Alright, then let me share, and should be this one… Yeah, okay. And also, let me just drop this link, in the chat, and then that way, anybody who doesn't want to follow along on my screen can follow along there instead.
So, before I just sort of start walking through, those of you who've spent a little bit of time with the backlog, are there any issues in particular that you'd like us to take a look at, kind of first or earlier?
No real burning desires here.
Very cool. Then… let's just start from the top. So, let's look at this one in ready. New Contributor Outreach.
reaching out to new contributors and getting feedback to understand what's difficult. So this was opened in 2024, and since then.
I ran a series of interviews and, shared out those interview findings that sort of did this exact thing. So I… to me, this seems a little bit like a duplicate, but one thing I want to walk through a little bit is that A lot of the things that were in the findings that I had were around, kind of different formats for communication, and people having different learning styles. Some of the approaches in this ticket seemed to take a little bit more of a, like, let's make the tooling do it for us.
And so, you know, some of this work about, like, automating, let's see, you can check author association. If someone's doing their first issue, we can reach them. So this one, again…
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 10:00 in a way, it is already done, because that is the… we do have a survey when you merge your first PR to ask about your experience, and that is already, like, checking if it is the first time and things like that, so that is already… Already exist as well.
**Amy Super** 10:14 Okay, got it. And then there's this sort of, like… thank you, Marylia. There's also, like, this large brainstorming section that… So, we definitely have the Slack channel, and I think that we've tried to manage that. Mentorship program, I think people are engaging in, kind of, more ad hoc.
We do have good first issue. We did the interview… This is all stuff we did during the interview, right? Was, like, find out what people, kind of, people's, reasons for contributing, or, like, what type of contributor they were. And so, my inclination is actually just to close this one, unless anyone sees anything of interest.
Good? Okay.
Alright, let's just go ahead and… oh, where's the button for closing it? I haven't worked on GitHub projects in a long time.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 11:11 It's gonna be at the end.
**Amy Super** 11:12 The bottom, okay.
Oh… There we go. Okay.
Great.
Alright.
Blog posts about new contributor… Research.
I think we decided via Slack that we decided not to do this. Oh, but this is on me to, create a file and add it to the repo. And then Dhruv, I think you had the comment of, like, should we add a section to the community repo that describes these updates?
Can you maybe, explain that a little bit?
More for me, like, what you think we could do there?
**Dhruv Ahuja** 12:02 Okay.
Let me just read it through, because I'm forgetting the context now.
**Amy Super** 12:08 Yeah, I know, it was, like, 2 months ago, so please take your time.
**Dhruv Ahuja** 12:15 Okay, maybe I'll add more… yeah, okay.
Yes, oh, okay, what I meant is that kind of like a changelog where we just, capture the latest, updates that are happening in the community.
**Amy Super** 12:36 What would the scope of that be?
you know, would it be kind of like… is it… are you thinking almost like a full-on, like, release notes for all of OpenTelemetry, or…
**Dhruv Ahuja** 12:50 I was thinking maybe a one-liner, or maybe just a link to the, whatever the update is. For example, if there's the end user, say, doing a blog post on maybe findings, then we capture that as well.
Things like that. So, I hadn't really thought about it too much in advance.
**Amy Super** 13:08 Okay.
**Dhruv Ahuja** 13:09 I should have scoped it better in the issue in the comment itself.
**Amy Super** 13:15 Yeah, it's all good. I think what we could probably do here is create a new issue that splits that out from this notion of the blog post.
And maybe make it, like, an investigate how to do a changelog, because I think that's some of the stuff we would want to decide on, right, is, like, what's the scope? Is it just by SIG? Is it any other kind of, like, major changes?
So I'm going to just leave myself a note to do that, because I'm not going to have you all sit through the torturous experience of having me create new issues.
And then once that's done, I'll close this one.
Any feedback or thoughts on that before I… Move on.
**Dhruv Ahuja** 14:12 Yeah, sounds good to me.
**Amy Super** 14:14 Okay.
Okay.
Update the contributing page at opentelemetry.io.
**Dhruv Ahuja** 14:26 Yeah, I've started working on this one, just going through the blogs and preparing some rough notes.
Before I put out a Google Doc draft.
**Amy Super** 14:35 Okay.
And… Okay, then I think we can move this one to active then, or in progress, whatever we call it.
Okay… Call for participation issues for newcomers.
Also, just so you all know, like, we had, like, really terrible thunderstorms just come through, so, things seem slightly laggy on my end. If I just, like, randomly disappear, please, like, keep going without me, and I'll try to come back.
Okay.
Let's have a place where SIG members can post issues they want resolved and are willing to guide on. We won't assign mentors to search for volunteers, we just make this visible. There could be good first issues from a year ago, but the chances of them getting ready are low.
On the other hand, if a SIG posts an issue they want resolved, a newcomer can contribute knowing it's more likely to get attention.
Let's see… We could kind of collate together all of the good first issues, and then something that gets published.
There's also Up for Grabs already.
So Marylia, I think I'd kind of defer to your knowledge here, since I think you know how this works kind of cross-IG a bit more than I do. How do people find kind of good first issue? Is it on a SIG-by- SIG basis, or do.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 16:01 Yeah, SIG by SIG. No, SIG by SIG. Okay.
**Amy Super** 16:05 And do you think that it is, like, plausible to kind of create a…
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 16:12 So I think right now it can cause more issues than not, because the problem is that as soon as we create, like, a good first issue, the idea when people create this is, like, okay, we can actually have contributors that they can, like, we can train them, like, mentor, but what is happening is that as soon as SIGs are creating good first issue, people are just using AI to grab this and create AI-generated stuff. A lot of slop, a lot of stuff, and they don't really care… a lot of them don't care about, like.
growing in the community, they just want to PR, PR, PR, and expect us to review. So I feel like if we actually create something like this, it would just create more issues to the maintainers, because it would just, like, be the target of, like, AI to say, like, hey, look at this, and you can create now 50 PRs.
So, I think, like, when this is created, like, it was, like, a good idea, but I don't think we should be doing this now.
**Amy Super** 17:11 Okay.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 17:13 I think we should, if people want to get involved, they should go to the SIGs, because a lot of the SIGs, they do have… or an issue, or, like, on their, like, reading machine, like, what are the focus of the current SIG, because a lot of times they want to say, like, okay, we are working on this initiative, so this is a way for them to know that this is, like, the priority stuff.
And they can join the SIGs, but… I don't think we should be doing this… For… yeah, for this issue.
**Amy Super** 17:42 That makes sense. Okay, any objections from the group on that, to keeping this on a SIG by SIG basis?
Okay, so, I'm just gonna say we'll revisit.
If and when we… get, AI… What, slop contributions? Is that rude?
Just say contributions.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 18:43 Usually, I usually say, like, low quality.
**Amy Super** 18:47 Okay.
Yeah, that's much kinder than calling it slop, so, you know, so… Alright.
Okay, how can we run the SIG without requiring everyone to meet synchronously? So this is actually something that I would love to hear feedback on. So when the SIG was originally created, the notion would be that, anybody could look at the backlog, and If, you felt that you wanted to participate on a particular issue, and again, these issues are for the SIG, so now we're not talking about the rest of OpenTelemetry, we're talking about how the SIG runs.
So the idea was that, people would thumbs up or self-assign themselves to issues, and once there was sort of, like, a critical mass of enough people saying, like, yeah, let's work on this issue, that, like, that became the priority, right? So it was sort of, like, almost a voting.
Kind of thing. When we saw the number of people participating in this SIG drop, that stopped being reasonable because, you know, you might just have one person who's like, hey, I can make a quick contribution here to help.
But not enough people would be signing on to that as well. And so, I guess what I'm kind of curious about is, you know, obviously this kind of backlog grooming that we're doing today is a little bit of, like, a hard reset, but going forward, does anyone have ideas, or have you participated in other groups where async prioritization works so that we don't have to have everybody on the call to make it happen?
So, open to hearing ideas here.
**Dhruv Ahuja** 20:36 I think it also depends on the nature of tasks, right? For example, there were a couple of issues that I was able to take up async, or maybe just joining one meeting, getting the context, and then just going one after the other. And as I worked more on it, the more clarity I got.
But that's not always possible, I feel. For example, I picked up issue number 79 just because I wanted something that I could hack away at.
And, async, and it also seemed, like… because the… some of the other issues, for example, creating videos recently, which I believe have been the, more on the higher priority, I felt that they weren't something that I could, possibly do, and do well.
So that is why I had to go down the list to find something that I could work on. So maybe if we could prioritize or create more issues that are smaller in scope, I think that could help.
**Amy Super** 21:35 Yeah, yeah, I definitely agree. I would like to see our backlog be in a state where you know, someone who's not, you know, here every time can read the issue and say, like, and decide whether or not, like, hey, I can pick this up, so I think that's great feedback.
Other thoughts for those of you who are working cross time zones like this?
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 22:00 Because, yeah, this issue occurred initially because we had half of the people that could only come, like.
a good time for, like, Europe and half for, like, West Coast, so we were having a… we actually started this SIG with two meetings, for, like, the two time zones, but we have to keep, like, updating each other, what we were doing, so we were, like, basically trying to figure out a way to sync between those two groups, and how we could do this, like, async. So I think, like, this issue started from that, part.
But I guess it's still valid for, like, new people joining in, because we ended up killing the other one because people started attending the other one, and just kept this one.
**Kayla Reopelle** 22:47 I think another thing that, like, a synchronous meeting provides is also, like, a level of accountability, or just, like, a form of a stand-up, so that everyone can check in and see what we're working on, and so we could look into, like, an asynchronous stand-up type of a check-in if we wanted to.
Have more of a… a non-synchronous… Meeting.
**Amy Super** 23:11 Yeah, there are teams that I work on that do, it's like a Slack bot, right, where everybody just throws their status in, and I wonder if we could look into doing that for the off weeks when we don't meet, right? And just give that a try.
I actually really like that idea, Kayla, especially because I'm staring down my travel schedule, and I'm here now, and I think the next meeting I'll actually be able to attend for this SIG will be, like, September 17th.
So, it's a good time to get some practice like that going. Does anybody want to kind of take on looking into a way to do, like, a scheduled message or some kind of bot in our Slack channel that can ask for status like this?
**Dhruv Ahuja** 24:04 Yeah, I can take it up.
**Amy Super** 24:08 That was you, Dhruv, right? Sorry, I was looking away.
Okay, great, thank you. Okay, so let me just write a couple notes.
Druv, it's your handle, why can't I find you?
**Dhruv Ahuja** 24:44 Am I not accessible here? Okay, I'll…
**Amy Super** 24:48 I think so.
**Dhruv Ahuja** 24:48 God.
I think it dropped.
**Amy Super** 24:51 We can.
**Dhruv Ahuja** 24:52 Yes, sir.
**Amy Super** 24:54 Yeah, can you drop a comment on this one?
**Dhruv Ahuja** 24:56 Yeah, it's number 14, right?
**Amy Super** 24:59 Yes, please.
I think I might be able to… Assign you?
No, I don't see you in here. But yeah, if you can drop a comment, then I can assign this one to you, and we can move it into active.
**Dhruv Ahuja** 25:23 Yes, I just commented there.
**Amy Super** 25:26 Okay, there we go.
There you are.
It's like, I know I've seen you in here. Okay, great.
In this process.
Okay, Contributor experience survey follow-up, project and sub-project priorities.
In the survey, it was found that less than half of maintainers can confidently say they know the priorities of leadership committees.
start with this, we want to identify how priorities are being communicated today, assess the ease of accessing that information, and then decide how to improve.
So I created this one. Marylia, do you have any info or intel for us on kind of how we communicate priorities today, and whether there are any changes happening on that front, since I wrote this a year ago?
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 26:29 You mean, like, in general for this SIG?
**Amy Super** 26:33 So it's basically the survey that we did last year. The maintainer said that they don't confidently know the priorities of the leadership committees.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 26:47 Yeah, so this is where we have, like, some issues. Like, we do have one open right now that is just called, like, Roadmap and stuff like that, so we do post things like that. It's usually always on the community, repo.
And then, on top of that, then each SIG can have their own, like, priorities.
**Amy Super** 27:07 Yeah, I think…
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 27:07 One thing, though…
**Amy Super** 27:08 Project as a whole.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 27:09 Yeah, because one thing that we don't like to do is enforce, like, from a GC side, saying, like, you have to work on this.
**Amy Super** 27:16 Right.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 27:16 Because it's not something we do. Well, like, we do provide guidance, but we do have that issue that is just a general one for all of them.
So I'm not sure if there is much that can be added here, that we can actually do.
But.
**Amy Super** 27:32 Yeah. I mean, I opened this one, so I'm comfortable closing it, just because I know that, like, roadmap stuff is being worked on, so,
**Kayla Reopelle** 27:56 Are you talking about the OpenTelemetry Roadmap project?
Or is there, like, a specific issue in the community repo that has that info?
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 28:05 Yeah, isn't… unless this was a mutual, or… Well, we put it as a PR already.
Yeah, as a PR. So, yeah, it's Postgraduation Roadmap for OpenTelemetry. Let me share…
**Amy Super** 28:36 Yeah, if you can drop me a link in the chat, Marylia, I'll put it in here.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 28:39 Pardon me.
**Amy Super** 28:40 Perfect, thank you.
**Kayla Reopelle** 28:44 Thank you.
**Amy Super** 28:49 Okay, with that then, any objections to closing this issue?
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 28:56 Nope.
**Amy Super** 28:57 Okay, you're out.
Okay.
Sig Meetings.
Okay, in the survey, 82% of contributors found SIG Meetings useful. Meeting attendance correlates to greater knowledge about navigating and contributing, but some dislike the synchronicity, which we have talked about.
Some people are unable to or uncomfortable attending. Meetings shouldn't be required to advance issues. For those who prefer async, meaning-driven decision-making is problematic.
I also noticed this when I started working with the community, that sometimes things were… I, like, I wasn't understanding how to scroll through the spreadsheet to find things.
But since then, we have also changed how recordings get handled, and it looks like we have some issues.
Offer SIGs the ability to schedule messages for when a meeting is happening, have an easier way to visualize a meeting, such as the Kubernetes calendar, and encourage SIGs to welcome and greet newcomers.
So we have sub-issues on this one. I actually feel like this one is pretty straightforward in terms of, like, how to work on it.
of course, I'm saying that because I wrote it, but I don't know how you all feel about the… kind of, like, looking at the sub-issues and whether that seems, you know, like…
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 30:28 I don't know if they have the… calendar is still valid, because we do have the… both from looking at… well, we have several ways, so we have on the community the table that shows the time for each one, we do have a link for the Google Calendar that shows all of them, and we do have the LFX calendar that shows all of them, so we have 3 sources of this data.
**Amy Super** 30:50 Yeah.
Yeah.
Can you list those off for me again, Marylia?
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 30:55 So, the community repo itself?
The Google Calendar.
and the LFX calendar.
**Amy Super** 31:36 Are we good with closing this sub-issue, then?
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 31:41 Yeah, I think so.
**Amy Super** 31:43 Okay.
Okay, alright, so that's one down.
Encourage SIGs to welcome and greet newcomers. So, this is one of the things that… and then allow the ability to schedule messages. So for both of these.
Well, actually, these are a little bit different. So, I think one is providing some… tooling? I'm not quite sure what this is offering. To make it easier… Connect Slack with SIG so you can create a workflow. Oh, so it's a Slack workflow, okay.
So I think what this would take would be kind of, like, reaching out to other SIGs, or maybe we should just start with ourselves and see if it's what the setup process is like before we go offering it to everybody else, because I know that we don't do this.
Any other thoughts on how we might… go ahead, Dhruv.
**Dhruv Ahuja** 32:51 Yeah, I think this workflow would be similar to what's needed for the other task that you just assigned to me.
**Amy Super** 32:58 yeah.
**Dhruv Ahuja** 32:59 Where we can just send a message on schedule saying that, okay, maybe you should report what you have been doing, and similarly, when we do that, we can also experiment with setting the meeting reminder.
**Amy Super** 33:14 Great.
I think… Yeah, I think, Dhruvai.
**Abhi** 33:23 including.
**Amy Super** 33:23 I'm gonna throw another… It's pretty straightforward.
**Abhi** 33:26 forward to add just our ad reminders to Slack channels, so I think we just want to know when we can schedule for the future.
Future meetings, or future… Any of the events that are happening.
I quite…
**Amy Super** 33:42 Hmm.
**Abhi** 33:43 I use it quite often, and it's very effective to, do it async, because I don't have to keep a track.
With, like, announcing a few things in the Slack channel.
So it's,
**Dhruv Ahuja** 33:55 Okay.
**Abhi** 33:55 Pretty straightforward feature.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 33:57 Yeah, the only thing that usually has to be a channel manager that has to do this, so that is the only thing. So I do have access to a lot of them as manager, or with my admin GC account, so that is something that I can… I can do.
So, yeah, because it would be nice to have, like, also the link for the new LFX on it,
**Amy Super** 34:19 Yeah.
Marylia, can I assign you to this one, then? And then, if Dhruv needs help, Dhruv, you can reach out to Marylia if you need a channel manager for your other task.
**Dhruv Ahuja** 34:33 Yeah.
**Amy Super** 34:34 Okay, great.
Okay.
Great, and then encourage SIGs to welcome and greet newcomers. So this was actually one of the interesting findings from the research that I did, was we had some people who joined SIG meetings, and they said that it felt like, You know, walking into a party where they didn't know anyone, where the meetings just sort of, like, instantly jumped into, like, business as usual without kind of, like, looking around for newcomers.
And a couple of ways that this could be fixed is either, in the agenda, having, like, a block for, like, add your name here if you are new, and, you know, or, like, introduce yourself.
I know today, I kind of put Ivan and Abhi, like, on the spot, and said, like, hey, introduce yourself, but that's probably not the friendliest way to do it, because not everybody's really comfortable speaking up immediately.
So I apologize for that, and thank you for being patient while I put you on the spot.
So, I'm curious to hear… I mean, I actually think this is a good reminder for everybody, and so, personally, I think we should keep this on the backlog, but I'm still kind of thinking through, Oh, Dhruv, you've added some context here, some suggestions. Asking newcomers to share their areas of interest, emphasize that communication can happen async, yeah.
Agreed.
So… but I feel like in order to sort of operationalize this more, we might want to have, like, kind of decide on what our concrete suggestions would be.
and then assign someone to sort of do outreach to the rest of the SIGs with this feedback.
So I could see this issue taking that as well.
I'm happy to just leave this one on the backlog, rather than, assign it out, since it has a bit more work needed.
But I guess I'll pause before I do that. Is there… is everybody clear on, kind of, the scope of this one, or do you feel like this needs more context and more, information?
**Dhruv Ahuja** 37:13 annoyed.
**Amy Super** 37:14 If you're quiet.
**Dhruv Ahuja** 37:15 Yeah.
**Amy Super** 37:16 Got it.
**Dhruv Ahuja** 37:16 enough… I think we have enough context here, just my personal experience. I think one problem that might arise here is I… I have reached out to a couple of SIGs in general on different things, and people don't always tend to respond.
So, I think that is also going to be a challenge, where people are maybe just working async and connecting on the call, and not that much active on Slack.
So I think that could also be a challenge when doing the outreach eventually.
**Amy Super** 37:49 Yeah, I mean, like, what it comes down to is we can't really enforce it, so we can reach out to them and say, like, hey, here's a suggestion, based on feedback we heard, and then, it's up to them if they want to incorporate that.
I would like to think that in good faith, they would want to incorporate that, but… Yeah, I think that's just sort of… we have to make our peace with that to a certain extent.
**Dhruv Ahuja** 38:17 Night.
**Amy Super** 38:22 Alright, I'm gonna move on.
Alright, so those are the sub-issues for this one.
Okay,
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 38:35 Yeah, for this one, I just tagged, like, the same, like, Adriana and Luis, in case they look forward to, like, events, because that would not be something for us. So it could be, like, for community managers, if they're looking for something like that, but… so yeah, I just tag them now.
And let's see if they reply or something, but I don't think it's anything from us to do.
**Amy Super** 38:59 Yeah. Yeah, I agree. Let's see what they reply with, because I do agree with you that this is out of the scope of what, this group does, so… Okay.
Create roadmap using project boards.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 39:16 So this one, I'm not sure if it's still, like, because one thing is, like, we did try it out with a couple of different SIGs, if they want to have, like, project boards, and some of them try it for a while and just didn't like, some of them continue. So we do have, like, just a couple of projects that exist, but… it's kind of like we let each SIG decide how they want to, like, organize, so some of them have, like, one issue, the list, all the stuff they've been working on. Some of them just have, like, oh, on the top, But we were looking from, like, the GC side, a way to kind of, like, get a report every time, but we couldn't, right, figure it out the right way, because not all the SIGs wanted to do the same way, so it's hard to align.
But… Again, not something that should be for this group, probably.
Because we were tracking this from the GC level, and we didn't got to a solution that… pleases everybody.
**Amy Super** 40:18 Got it.
I just typed what I was thinking, which was okay, sorry.
Meetings I'm here.
Okay, APAC-friendly SIGs.
Okay, at the moment, special interest meetings follow norms of North America and Europe with regards to meeting times and when the schedule.
If we want to solve this, we need to solve the underlying issues and try a different way. Tried secondary meetings, we know that doesn't work. There's interest in a three-time zone proposal.
So… What I have noticed since this was… Written.
is that some SIGs do have… yeah. There's a kickoff for an APAC meeting for end user experience, for end user SIG.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 42:00 It can happen, yeah, yeah.
**Amy Super** 42:02 And so… I feel like… I mean, I kind of… the way I fall on this one is that, like, it seems very SIG-dependent to me, where, like.
With who is participating?
And how many people there are, right? I mean, I know that we regularly don't meet, just because not everybody is around, we're a smaller group, and so if we also split into time zones, it'll be an even smaller group.
And we previously were split into time zones and stopped doing that, because we didn't have enough people joining on the EMEA-friendly one.
And so this feels to me like another kind of, like, SIG by SIG, Process, unless anybody feels that we should do something higher level than that.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 42:49 No, we would just, like, incurred, like, SIG then, like, hey, just see if you have people on other zones that you should add another one. The problem is that we do want to have at least a maintainer on those calls.
But some SIGs don't have people on those time zones, so you don't want to have a meeting without a single maintainer approver that can actually help with questions and things like that. So… we need to, I guess, one step is get more maintainers on those time zones, and then having those calls there, yeah.
**Abhi** 43:29 Yeah, I've seen the issue of, like, working, SIGs having less number of people in certain regions, similar to what you mentioned, Amy. So it's, I think it's SIG by SIG basis where, some… for some SIGs, it makes Sense to have a meeting in all the three time zones, but for others, it's just… until they start having more presence, it doesn't make sense.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 43:56 Yeah, we're trying to, like, with a few SIGs, getting, like, a group from people from, basically, like.
Asia to get… like, create… we are currently, like, trying to create groups that we can, like, mentor and put it on specific SIGs, so there are, like, some ideas, like, starting around that, but I don't think, yeah, we can do anything for this one, so even we're probably, like.
Closing this issue, because there's no, I think, like, active, like, some concrete that we can actually do it right now.
**Amy Super** 44:48 Any other, comments or feedback on what I wrote here, or to chime in?
God.
Oh, I can't close this issue?
Wonder why.
**Bogdan  Stancu (Adobe Inc.)** 45:10 Meeting the community, bro.
**Amy Super** 45:13 Oh, it is.
Then why is it showing up on our board?
Just gonna… That out of here.
Which is something I just realized, that there are a whole bunch of issues not from our repo showing up on our board.
Huh.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 45:38 Yeah, if you want to copy the text, because I can close things on the community repo.
**Amy Super** 45:42 Yeah, I'll throw it in the chat for you, because I…
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 45:45 No, you can actually just comment.
**Amy Super** 45:48 Oh, I could just comment it, yeah, yeah, yeah.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 45:50 a comment, and then I can close it.
**Amy Super** 45:52 Okay, thank you.
Were we… Tagged in here that… it's showing up, because now I'm worried about our board and whether or not it's set up right.
**Dhruv Ahuja** 46:05 They might…
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 46:06 So this is when the people part of the project, so if you look on the right, Contributor Experience, like, the right column. Like, below the people are assigned, somebody, like, yeah, somebody added to the project there.
**Amy Super** 46:17 added us. I see.
Huh, okay. All right, well, I'll let you tackle that one more, Lily, so… Or close that one.
Okay, whew, 46 minutes. Is everyone still okay? Should we keep going? I know. Backlog grooming is so painful.
Okay, no path would be recognized for your work in SIGs that operate outside of GitHub.
There are multiple SIGs that operate a lot in Google Docs and Slack. This means the work of individual contributors is not tracked in CNCF dev stats.
Which is used for checking who can vote for GC.
TLLDR, if we had some insight into what it would take to bring in more signals.
Marylia, isn't there something being… like, I feel like I… I feel like I saw Jack Berg post something along these lines recently, or semi-recently, of, how to recognize contribution in a way that isn't just dev sets.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 47:30 So, no, I think it's a different perspective. So this is, like.
people that do things outside of GitHub. From that, he's, like, how we can actually recognize even the work that is being done on GitHub, stuff like that. So we want to, like… this is… that one is more, like, how we can give more voice to maintainers, and… That they can, like, shape a little more the whole goal of, like, OpenTelemetry. So yeah, it's a little different, the… the type of… kind of direction? Okay.
**Amy Super** 48:00 I understand.
I have no idea how we would tackle this, I'm just gonna say that. This is one that I've read this issue a few times, and just been like, yeah, I don't know what to do about that.
So, which tells me either that it's outside of our scope, Or… right, because if, like, the main issue that's being ta- or the main problem that's being solved here is, you know, like, voting, basically,
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 48:35 But at the same time, the voting, you can actually request to be added to the list.
**Amy Super** 48:41 Okay.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 48:44 Because that… I know that that happened with quite a few people, that they're like, they, especially, like, end user SIG and stuff like that, you can just send an email to the GC, like, can you add me, because I want to vote. You show the reasons, kind of, like, actually the things that you did help, and then we just add that person.
**Dhruv Ahuja** 49:07 So, on the LFX Insights page, I think this was a recent addition where you can actually see the Slack, collaborative, so it can include Slack collaboration as well.
When counting your total contributions.
Although this, this is not a substitute for the dev stats.
So there's this, toggle on the right side, include collaborations.
**Amy Super** 49:48 Mmm… there it is.
**Dhruv Ahuja** 49:50 Yeah.
**Amy Super** 49:52 I see.
And that is, activities associated with engagement or coordination don't reflect technical German impact. Learn more!
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 50:04 I don't know, we… we are having also some issues, we have, with the data from there, because a lot of people, like, things don't make sense, and we do actually… there isn't even an issue open for that to try and find out, like, if this Data is correct, so… Yay.
**Amy Super** 50:23 Marylia, who's… who's looking at that right now?
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 50:27 There is an issue that Dan opened, I just shared the link for the issue here.
**Amy Super** 51:11 Sorry, I'm not doing fancy formatting today.
So, my take is that… This is being worked on outside of this SIG, and this is outside of our scope.
And so my…
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 51:34 Damn.
**Amy Super** 51:35 My thinking is to close this one.
Because it seems like it's a bigger issue than something that just the SIG could tackle.
Does anyone disagree with that?
Okay.
Okay, I'm gonna pause here.
Because we have a lot more to go, and I actually want to spend maybe our last few minutes talking about what's in progress and what we do want to work on, so I feel like we've mostly talked about what we don't want to work on.
So I also just want to walk through some of the in-progress ones, so that some of those of you who are just joining, can maybe see if there is any of us who are interested in joining in on some of the active issues, Or, if not, that's fine, but just to walk through them.
So, what you will notice is that most of what is open, right now is a parent issue, and it's sub-issues about, kind of, a video series.
And this is… has been squarely, on me, and I haven't gotten through what I should have gotten through by now. But when… one of the biggest takeaways from the user research that I ran when I talked to new contributors was that they felt that there was just, like, a lot of reading.
And they weren't always sure where to go. That kind of bouncing between, Opentelemetry.io and GitHub, and then, you know, they just weren't really sure which of the information really applied to them. And so Marylia and I kind of sat down and created a list of videos that we thought we could put up on a YouTube playlist, and what it remains is basically to actually just, like, make those videos. So certainly, if anyone is interested in participating in any of that, it's just… I mean, literally, they are, like, demos of, like, here's where you go and click, because… frankly, people consume information differently, different people consume information differently, and so some people are… would be much more comfortable getting started just watching someone kind of, like, click the links, rather than reading, all of our documentation.
So any of the ones that say video, that's what we're talking about there.
And I think those are all of the in-progress ones. So, is there anything else that anybody is interested in working on, or tackling, or looking into at this point, until we get a chance to kind of continue grooming out the backlog?
**Abhi** 54:33 Amy, I can help you out with the video ones. I'll read… I'll read through these, because this is my first time attending this meeting, but I'll read through the issue, and then try to understand what… what is needed.
**Amy Super** 54:45 Okay, yeah, that would be amazing, thank you. And then I think we could take, that collab, kind of, like, we can work async on that, because like I said, I won't… I'll be around, but I won't be able to be at this meeting for about a month.
**Abhi** 55:01 I'm also traveling, but I'll try to, like… I'm working, I'm just traveling around, so I'll… async works better.
**Amy Super** 55:09 Perfect. And then Bogdan has also offered up some video editing, help on that front, because he recently got access to some tooling that we had, kind of been struggling with. Some of the open source tooling for video editing is a little, Clumsy, and other stuff is very expensive.
**Bogdan  Stancu (Adobe Inc.)** 55:31 Yeah, I wanted to give an update on that. The answer that I got is that we need… I mean, I would need somebody from the actual Linux Foundation to file, like, a request.
Because the Linux Foundation is the… the non-NGO that, like, we would be able to, to send a license to, so I… we might need to drop that, and I could just use my own, my own license, because I have a whole license, like, a personal one. So, yeah, this is me saying that we want to probably get a license for everybody, but I offer my time and Patience to learn.
**Amy Super** 56:19 Alright.
**Bogdan  Stancu (Adobe Inc.)** 56:20 Video editing and all that. So yeah, I mean… I'll do my best. Just…
**Amy Super** 56:26 Awesome Alright, that is no problem, and definitely appreciate it. I mean, when I looked into it, honestly, I found that for what we would need it for, the built-in editing function on, like, YouTube Studio seemed just fine.
Because the key thing that we are looking for, just, like, to recap a little bit on the tolling choices, is, video editing software that lets us edit the captions, right? So we, you know, for accessibility reasons, we need to make sure that the videos have captions, and a lot of auto-generated captions are, like, pretty bad, especially when people don't have just, like, a basic American or British accent when they're speaking in English.
And so, you want to have the ability to review the captions and just tweak them, the auto-generated ones, which you can do in YouTube Studio, so… Okay, so I think we can take that discussion offline, and then, I'm just cognizant of time here. Yes, it is always hotel. Actually, I had this really funny, I was doing user research for something different, and the participant was telling me how much they like using Google's Looker, you know, like the BI tool.
Only the caption kept saying liquor, like, like they were drinking, and he was like, I love liquor, I love liquor so much. And I was like, whoa, whoa.
Cool. And then I'm thinking that maybe what we can do is, just looking at the rest of the backlog, is maybe just take a couple at a time, and we could just do what we've done today, but maybe async in Slack with a thread, right? Where we drop an issue in.
Maybe we can try that for a couple of them, just to kind of try to get through the rest of this.
But I hope this wasn't horrible for all of you. I definitely appreciate, like, the collective brain trust on this, because it's tricky to try to do this on your own.
I think that's all I have. Does anyone else have comments or feedback or thoughts on next steps and how today's?
Gone.
Okay, then let's call it, let's take a couple minutes before, I'm sure people have more meetings to go to. Deeply appreciate your time, everybody, and see you all on Slack.
**Bogdan  Stancu (Adobe Inc.)** 58:46 Thanks a lot. Bye.
Bye.
