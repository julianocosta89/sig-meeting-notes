SIG: Developer Experience SIG (EU)
Date: 2026-10-28
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa (Datadog, Inc)** 00:16 Hello, hello?
Hello, hello?
Hello.
**Johanna Öjeling** 00:47 There, Johanna!
How are you doing?
**Juliano Costa (Datadog, Inc)** 00:53 I'm good, that's good. Yourself?
**Johanna Öjeling** 00:55 Yep, not bad. How was your, vacation?
**Juliano Costa (Datadog, Inc)** 01:01 It was good, yeah, some… Relaxing time, so, yeah.
**Johanna Öjeling** 01:07 Hmm, nice.
**Juliano Costa (Datadog, Inc)** 01:09 We went to a… to a lake in Czech.
Pretty close to our… to our place, actually.
**Johanna Öjeling** 01:16 Okay.
**Juliano Costa (Datadog, Inc)** 01:20 In law school.
**Johanna Öjeling** 01:22 So, are you on leave now?
**Juliano Costa (Datadog, Inc)** 01:25 I'm…
**Johanna Öjeling** 01:27 week, or…
**Juliano Costa (Datadog, Inc)** 01:27 Officially in, what is it called? Garden Leaf.
**So, yeah, Perk (Marcin Stożek) | Elastic Ingest** 01:39 Hey folks, when do you start Juliano?
**Juliano Costa (Datadog, Inc)** 01:42 Hello, hello. In theory, next week.
Monday?
**Perk (Marcin Stożek) | Elastic Ingest** 01:48 Oh, okay.
**Juliano Costa (Datadog, Inc)** 01:49 We still need to… to see if, remote.com has all the legal stuff for Austria. It's a bit,
**Johanna Öjeling** 01:59 Mmm.
**Juliano Costa (Datadog, Inc)** 02:00 complicated, legally speaking, so let's see how that goes. But, in theory, second.
Which, by the way, it's the date of… the… blog post published.
So… I may need to update my affiliation there.
**I haven't done yet, because… still… till 31st, I'm officially employed at Datadog, so… I'm still a Datadog employee, even though I'm on guarding leave, so… Perk (Marcin Stożek) | Elastic Ingest** 02:41 Okay.
**Juliano Costa (Datadog, Inc)** 02:43 But yeah, I'm keeping track of everything, and I have multiple tabs open, and as soon as… 1st of, November starts, I'll… I'll raise a comment then, just fixing my affiliation.
**Perk (Marcin Stożek) | Elastic Ingest** 02:59 3 vehicles.
**Johanna Öjeling** 03:00 update all your upcoming speeches at, like, KimCon, and… Perk (Marcin Stożek) | Elastic Ingest 03:05 Oh, yeah.
**Juliano Costa (Datadog, Inc)** 03:09 Yeah, oh, well, it's part of the job, so, yeah.
How are you all?
I saw the blog, the blog, by the way.
Thanks, Perk. Looks good. Looks good.
**Johanna Öjeling** 03:28 Yeah, it would be great to have that published, so nice work on that one part.
**Perk (Marcin Stożek) | Elastic Ingest** 03:34 Yeah, thank you. Yeah, I added a couple of… Thanks, sir? Oh, I apologize.
Pardoned.
Noise.
I've added a couple of comments, not comments, quotes.
There, so I, I changed it slightly, but then, thankfully, Martin and both Martin and Alex said that it's okay.
So that's good. And then also, thanks for all the comments. By the way, Johanna, I will update the… The blueprints. So I have an issue there for me.
**Johanna Öjeling** 04:02 Oh, yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 04:03 I'll just do it as soon as they come.
**Johanna Öjeling** 04:09 Thank you. Mmm… Nice, and yeah, I actually attended the Blueprint SIG meeting on Monday this week, and so yeah.
they are also kind of aware, and Tiffany was in the meeting there too, who has kind of rescheduled the blog post a bit, and the Blueprints project, they initially, like, they set out to… introduce… For the… to consider the… like, first iteration of the project complete. They set out to have three blueprints and 5 reference implementations, and now Since we have the Adobe Skyscanner and Mastodon, now we'll have Keycloak, and they also got one more reference implementation that will make 5, so they are very happy about that.
**Perk (Marcin Stożek) | Elastic Ingest** 05:05 Oh, very well.
**Johanna Öjeling** 05:07 Yeah, so… and they also saw your issue and know that it's coming, and that it will be kind of a copy of the blog post, more or less.
**Perk (Marcin Stożek) | Elastic Ingest** 05:22 Yeah, just like, I think you guys did for Skyscanner, right?
**Johanna Öjeling** 05:26 Yeah, actually, they did it, so… Perk (Marcin Stożek) | Elastic Ingest 05:29 You see. Yeah, yeah, yeah, so it's even better. So, we are actually, you know, following suit.
**Johanna Öjeling** 05:35 Yeah, and then, But for, like, future reference implementations or interviews, then we can kind of follow their guidelines that they have developed for different kind of sections to include, so I think, upcoming reference implementations will also have that kind of format to, to be consistent.
**Perk (Marcin Stożek) | Elastic Ingest** 06:04 Yeah, that is… that is a good point, that we need to keep that… keep that in mind when we do the interview, also.
**Johanna Öjeling** 06:09 Yeah, exactly.
**Perk (Marcin Stożek) | Elastic Ingest** 06:11 Okay.
**Johanna Öjeling** 06:12 And we have one more blog post coming, which is the Atlassian one.
And that Vidya has been working on.
And, So, she has addressed the feedback and updated the blog post. I have approved it, but I would like to get one more approval or review from the SIG so that she can… hopefully move on to, open a PR soon and, open so much I.O. repo.
**Juliano Costa (Datadog, Inc)** 06:46 This is one of my open tabs. I need to… to go back. I… I had a bit of back and forth with her on Slack.
**Johanna Öjeling** 06:55 Regarding…
**Juliano Costa (Datadog, Inc)** 06:55 Between one of the dashboards, one of the diagrams.
**Johanna Öjeling** 06:59 Oh, that's.
**Juliano Costa (Datadog, Inc)** 07:00 Regarding the… the instrumentation layer. I think the way it was, it looked like a separate thing when it actually runs the instrumentation layers… the instrumentation layer is within the service itself.
But then she… re… rewatched the recording and update it, so I think, we are good. I just need to read through again, sorry.
**Johanna Öjeling** 07:30 Great, yeah, no worries. But cool, done. I know it's… it's being, looked on. Great. Thank you.
**Juliano Costa (Datadog, Inc)** 07:42 Cool. Okay, besides that, do we have anything… anything else, On our plate, like, missing or waiting on us?
**Johanna Öjeling** 07:58 The… Blueprint SIG, I'll mention that again. I brought it up last week, so make you aware, but for your awareness, Juliano, they asked us for feedback, on the reference implementation, template, so I will write down some… some comments on that, issue, and if you have any feedback, given the experience with writing the DevEx blog post, then also please feel free to, write that in the GitHub issue.
**Juliano Costa (Datadog, Inc)** 08:44 Okay.
**Johanna Öjeling** 08:50 And about the meeting time of this meeting, thank you for being flexible. So, I have, like, a recurring team meeting that was scheduled to… yeah, then it collided, but now, found out that this team meeting is being moved, so… like, in two weeks from now, so I think then it's being scheduled from 10 to 11.30, so, so maybe we don't move the meeting time after all, but keep it at 10, then at.
**Perk (Marcin Stożek) | Elastic Ingest** 09:22 Go forward.
**Johanna Öjeling** 09:22 I joined for the first 30 minutes, and usually that's kind of sufficient.
**Perk (Marcin Stożek) | Elastic Ingest** 09:26 It happens. It will happen again. Then Juliano will find out on Monday that he has a meeting.
**Johanna Öjeling** 09:33 The, Perk (Marcin Stożek) | Elastic Ingest 09:35 Oh, we can't hear her. Sorry, you're muted.
**Juliano Costa (Datadog, Inc)** 09:37 I mean, yes, but I don't know what time will my meetings be, but yeah, I'll try to… well, those meetings are already on MicroLender, so I hope I don't have any conflicting meetings.
**Johanna Öjeling** 09:51 Mmm.
**Perk (Marcin Stożek) | Elastic Ingest** 09:52 But also, don't worry, it's, it's life, so let's just move.
**Juliano Costa (Datadog, Inc)** 09:57 So… So, just to be clear, we keep the original time then.
Or…
**Johanna Öjeling** 10:04 Yeah, - and I'll write in the Slack thread, so… Perk (Marcin Stożek) | Elastic Ingest 10:14 Otherwise, I'll…
**Johanna Öjeling** 10:15 Yeah, just to make it clear that, yeah, so it doesn't get moving.
**Juliano Costa (Datadog, Inc)** 10:20 It's weird, because this one is scheduled on our time zone, so it never changes. It is always 10 a.m, because the community demo, the demo SIG is… This week at 4, and next week at 5, because they changed the time.
**Perk (Marcin Stożek) | Elastic Ingest** 10:42 I'm so hot.
**Juliano Costa (Datadog, Inc)** 10:43 neck.
**Johanna Öjeling** 10:44 This, this week.
**Juliano Costa (Datadog, Inc)** 10:44 weekend over there.
**Johanna Öjeling** 10:46 Yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 10:46 Okay.
**Juliano Costa (Datadog, Inc)** 10:47 So, But yeah, as we are good, then, as we are in the… with the EU, then let's skip it.
**Johanna Öjeling** 11:00 Britt, I think it's only… next week that I… Won't be able to attend.
Done, but after that.
**Perk (Marcin Stożek) | Elastic Ingest** 11:12 Hmm. Yeah, okay, okay.
**Johanna Öjeling** 11:15 No, wait, no, actually, it… no, I see now the Meetings scheduled tend to… 11.45, hmm.
Okay, that might change again, so, yeah.
**Juliano Costa (Datadog, Inc)** 11:30 Just let us know.
**Johanna Öjeling** 11:32 Yeah.
Yeah, sorry for any inconvenience, but yeah, let's keep in touch about this.
**Perk (Marcin Stożek) | Elastic Ingest** 11:42 It's okay, it's okay. Next week, I'm going to be here, but in two weeks, I will not be able to join.
Okay.
I have, I, I have one… one topic to, guys, to ask you, before I done with the, with the other stuff, because I wonder… how to… how to find, you know, like, other… other projects that are using OpenBelemmetry, maybe. So, I'm just letting you know, but maybe you have ideas how to reach out to them, but I'm starting to think about how to get those other projects, like Keyclog.
That we're using OpenTelemetry, because we gotta, like, start talking with them, find out whether they are using it.
for real, or is it totally exploratory, and whatnot? And I just wonder… where to find those people? Like, probably I'll just, I don't know, use some AI and, you know… grab through the code, and maybe, I don't know, resend through Windows.
Unless you have maybe some ideas already, and you know that there is a project that is using, and we could start talking with them.
**Juliano Costa (Datadog, Inc)** 12:54 I'm… I'm not… I'm not… okay. I'm not sure how Severin finds all the projects, but he, I don't know if you all know Severin Neumann?
**Perk (Marcin Stożek) | Elastic Ingest** 13:06 Yes?
**Juliano Costa (Datadog, Inc)** 13:07 So he's been publishing on his LinkedIn, some projects using hotel already.
**Perk (Marcin Stożek) | Elastic Ingest** 13:16 Oh, okay, this is what, but…
**Juliano Costa (Datadog, Inc)** 13:18 Yeah, but he's… so, like, he's just sharing how to use Hotel with those projects.
**It would be cool to maybe get the, like, his source, or even just check the videos that he already produced, and then try to reach out to the project… and, Perk (Marcin Stożek) | Elastic Ingest** 13:36 Yeah, exactly.
**Juliano Costa (Datadog, Inc)** 13:38 That would be cool. Like, I think one really cool story that we could try to find and maybe try to bring to the hotel.io is the Claude, story.
Like, they have hotel in it, all the vendors are, making some noise out of it, so it would be cool to bring the… like, the maintainers of the project perspective, like, why they chose OTEL, which is obvious, but, like, if they had any pains, and then explore the developer experience on implementing OTEL, and allowing their users to use OTEL to send data.
I… do… does anyone have any contacts in, traffic?
**Perk (Marcin Stożek) | Elastic Ingest** 14:27 I do not.
Off I'm traveling.
**Johanna Öjeling** 14:29 I don't think so.
**Juliano Costa (Datadog, Inc)** 14:33 I will try to see if they have, like, a… Talk to us.
**Perk (Marcin Stożek) | Elastic Ingest** 14:42 That is definitely something that, people might be interested in.
**Juliano Costa (Datadog, Inc)** 14:47 I think… I think that story would be huge, if we can get them to… To talk about that?
**Perk (Marcin Stożek) | Elastic Ingest** 14:57 Yeah, that's fine.
Okay, but, okay, Anthropic is one thing, but then the other… your other comment about, what Severin posed there, I think that's a good one as well.
Okay, let me see if I can.
**Juliano Costa (Datadog, Inc)** 15:16 Find.
**Perk (Marcin Stożek) | Elastic Ingest** 15:17 Yeah.
**Juliano Costa (Datadog, Inc)** 15:18 September 8th.
So, summary is, No.
Let me see if I can find his videos… So he did one with Claude, one with Open Router.
1… one about Ansible.
Vercels… He… he even did Key Clock.
And, he also has Docker Build and OpenTOFU.
**Perk (Marcin Stożek) | Elastic Ingest** 16:20 Oh, you see, okay. So this is a good, I think, good list of projects to reach out to.
**Johanna Öjeling** 16:28 Where did you find those? Or his…
**Juliano Costa (Datadog, Inc)** 16:30 brochure.
No, share on the… on the… So green… I don't remember.
Shared on the… on the doc.
**Johanna Öjeling** 16:51 Mmm, thank you.
**Juliano Costa (Datadog, Inc)** 17:02 And Severin is super accessible, so we can just ping him on Slack, so…
**Johanna Öjeling** 17:14 That's great. Yeah, that's a good source. Thank you, Juliano.
I wonder if we can also do some kind of outreach over, like, Slack channel, or, in social media, like LinkedIn, or similar to… Try to get in touch with organizations.
**Juliano Costa (Datadog, Inc)** 17:36 Yeah, that would be cool. We could… trying to… two approaches… two approaches. One would be to write a blog post asking for stories?
The other one would just be to reach out to… Comps, hotel comps, and asked them to share, Share a link to our, taurus, like, channel on… on the OpenTelemary channels, so that would.
**Johanna Öjeling** 18:05 Emmy.
**Juliano Costa (Datadog, Inc)** 18:06 Ding, Blue Sky, I don't know if they still have Twitter, or X, or whatever.
Astrodome, so then… People that are following them can join and share.
**Johanna Öjeling** 18:21 Yeah, that's a good idea.
And that reminds me also that the Blueprint SIG will… is planning to post a blog post about like, about the Blueprints project, and, like, there are reference implementations, and also, like, a call for contributors, and that will go out after KubeCon, I believe. So… Maybe we can… Coordinate with that somehow, or… Or… Have a separate post.
Yeah, let's give it some thought.
**Juliano Costa (Datadog, Inc)** 19:03 Cool.
**Perk (Marcin Stożek) | Elastic Ingest** 19:04 Maybe, maybe, guys, maybe you should, we should, write this down, those, ideas for different blog posts that we can do, to have it like a, you know, like a backlog of ideas.
**Johanna Öjeling** 19:14 Come on.
**Perk (Marcin Stożek) | Elastic Ingest** 19:18 You know.
**Johanna Öjeling** 19:20 Yeah, I think that's a good idea.
We can create, maybe a separate tab in our, making notes.
Allowed it… allowed it as a… Bumped up to that blog post.
Pop.
**Perk (Marcin Stożek) | Elastic Ingest** 20:05 Thanks, Johanna.
**Johanna Öjeling** 20:08 Then we can, yeah, capture the ideas there.
Good point. Alright.
Great. Mmm… Anything else we want to?
Discussed today.
**Juliano Costa (Datadog, Inc)** 20:55 Not from my end.
I still need to configure a bunch of stuff.
Cool. Then, we see each other next week. Johanna, let us know if,
**Johanna Öjeling** 21:16 Yeah, how it goes, yeah. Yeah, let's see.
Great.
Yeah, have a good day.
**Perk (Marcin Stożek) | Elastic Ingest** 21:27 Let's see.
**Juliano Costa (Datadog, Inc)** 21:28 Thank you. Bye.
**Perk (Marcin Stożek) | Elastic Ingest** 21:29 Room.
