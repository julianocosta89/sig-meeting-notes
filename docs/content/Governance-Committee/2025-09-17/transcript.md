SIG: Governance Committee
Date: 2025-09-17
Duration: 46 minutes
Zoom Recording URL: https://zoom.us/rec/share/wH7mN57ZYgGD8SRv_hRCrRXUiNGsmrDduthI59c5Pd5qWPcTcCzEM39Lc4r_AXpC.Fqbh31us_hcfqy0A
============================================================

## Zoom Recording Transcript

**Severin Neumann** 00:12 Hello!
**Trask Stalnaker** 00:17 Ayyy.
**Pablo Baeyens** 00:19 Hey!
**Alolita Sharma** 01:32 Hi everyone, good morning.
**Morgan McLean** 01:35 Hey!
**Severin Neumann** 01:36 pay.
**Alolita Sharma** 01:36 Thank you.
**Trask Stalnaker** 01:37 Oh, yeah, yeah.
**Alolita Sharma** 01:46 Do any, any of you recall if we started a deck for our NA?
Should I start one? Because I've started to look at the templates, so… I can definitely Kick it off and, you know, kind of pull in some of the content or framework from… Yeah, that would be great. Meetings, and then we can add to it, share and add to it.
**Morgan McLean** 02:19 By the way, I'm gonna have to drop at the half-pass mark.
**Alolita Sharma** 02:21 Okay, that's fine.
**Severin Neumann** 02:25 See?
then we maybe should talk about the election in the beginning. Do you have it on the agenda already? Maybe let's…
**Alolita Sharma** 02:33 Good idea.
**Severin Neumann** 02:33 no, it's not.
**Morgan McLean** 02:36 It's not there, I need to add it.
**Severin Neumann** 02:37 elect.
Yeah, it's getting… I don't know how to write words anymore.
I'm guessing.
**Morgan McLean** 02:45 Yeah, so I, I took Dan's advice, I made a template for a project for future elections, and then created issue templates for each of the issues that we had previously, minus two that I didn't think were relevant, happy to re-add them.
One was for a question of, like, should we continue to use Helios? I think we're happy with Helios, I wasn't planning on putting that in the template. If people disagree, happy to put it back.
And the other was another one that Dan had pointed out that didn't really need to come up again.
That's there. I then implemented that template for the 2025 election. Nice. I will go enter the election dates once we decide on those. I saw the messages on Slack. I think people are agreeing on the Monday through Wednesday, two weeks prior to KubeCon? Is that…
**Alolita Sharma** 03:34 Yes.
**Morgan McLean** 03:35 That's consistent with what we've done before.
**Dan Gomez Blanco** 03:37 Right now, okay.
**Severin Neumann** 03:38 Yeah.
**Morgan McLean** 03:38 I will enter that, then I will kick off the creation of the Helios poll, and start drafting the blog posts and everything else.
**Alolita Sharma** 03:47 Awesome.
**Juraci Paixão Kröhling** 03:47 So, about Helios, the background for that thing is, we have a very old desire to have ranked votes, ranked voting, for the elections. Like, people who select second position gives less power if they, I don't know rank voting, yeah. But, the solutions that we had… that we had so far have not been good enough. Like, they are not either… We have to host ourselves, and the difficulty there… you might remember, the difficulty there is, if we host ourselves, then we are the ones running the election and being voted at the same time.
**Alolita Sharma** 04:24 Yeah.
**Juraci Paixão Kröhling** 04:24 that's… that's just bad. And, the second thing is, we… so the CNCF does have… like, Kubernetes has a… a platform for voting, but they… they very explicitly, do not want to run our elections, or anyone.
**Morgan McLean** 04:41 selection.
**Juraci Paixão Kröhling** 04:42 other than theirs, right? So, they have a specific SIG for elections, or for the TC board, or whatever they call it.
So, yeah, we don't have…
**Alolita Sharma** 04:52 They have that deep mode-based process, right, Jerassi?
**Juraci Paixão Kröhling** 04:57 I think it is, yeah. And, so we don't have a… we… historically, we haven't had a good open source option that is… that we have available hosted for us, so we would have to host it ourselves.
Let's risk.
**Trask Stalnaker** 05:10 I do think the ranked, voting is a lot less of an issue when you are… are selecting 4 or 5 Yeah. People, because you're already sort of getting that ranked. Like, ranked voting is, like, critical if there's only one winner.
**Morgan McLean** 05:30 Collection of one, yeah.
**Trask Stalnaker** 05:31 But in… I think that mitigates the… I'm not saying we couldn't or shouldn't do it, but I do think that at least mitigates the… Importance of it.
**Morgan McLean** 05:44 Especially when switching to a different platform requires, well, either Kubernetes, which won't do it, or running it ourselves, which, beyond the bias stuff, also just scares me from a, like, security and operations standpoint.
**Juraci Paixão Kröhling** 05:55 Yeah, I mean, if… I think one thing that we typically did in the past, and Dan can confirm it, if that was done last time, is just checking a look at the current ecosystem of coaching software and seeing if that changed.
Like, if the options are still the same as last year, then let's just make the same decision as last year. If there's something very good, that's hosted by an entity that we can trust.
then I think that's, that's something we could consider.
using instead of Helios. Like, Helios is a… suboptimal. We're being recorded, right? Yeah, so it's suboptimal. Like, there are so many UX problems there, like, so many people weren't able, like, didn't cast their votes, and then they saw that… I think they don't even realize that they didn't vote, right?
**Morgan McLean** 06:49 And then it looks like you've casted it, and then you authenticate, and I assume…
**Juraci Paixão Kröhling** 06:53 Yeah.
**Morgan McLean** 06:54 A bunch of people dump out after the casting steps.
**Alolita Sharma** 06:56 Thinking, oh, it worked! Yeah.
**Morgan McLean** 06:58 Not realizing.
**Juraci Paixão Kröhling** 06:59 I've never authenticated. Yeah, your act is really bad, but I think, I mean, yeah, I wouldn't spend too much time on that, it's just, like.
**Morgan McLean** 07:08 I'll spend a bit of time on it.
I'll also re-add that issue to the template about the question of, like, do we want to keep using Helios, and we can revisit that each year.
**Alolita Sharma** 07:17 Sounds good.
**Dan Gomez Blanco** 07:18 two… two things I wanted to mention. First one is, yeah, the issue… the other issue that Morgan mentioned that was removed was that if we required trustees within the GC.
**Morgan McLean** 07:28 Yeah.
**Dan Gomez Blanco** 07:28 We do not. The reason for it is that the only… the only… like, entity that can read the votes is Helios, and not us, so we couldn't really see the votes that… who voted for whom, right?
No, even the person that created the election. The other thing that I wanted to mention is that our scripts that we've got to generate the voter role rely on death stats.
OpenTelemetry, or whatever, the CNCF dev stats.
I think that still works, but I was thinking about this with the new rollout of LFX Insights.
**Alolita Sharma** 08:01 Yeah.
**Dan Gomez Blanco** 08:02 I think that's where they're switching to, Dan.
Right. I'm just thinking, like, if that disappears, and our scripts call the same, let's say, source, data source.
that DevStats is using in that Grafana instance, then… it wouldn't work. So maybe for the next election, we… we need to think of…
**Alolita Sharma** 08:22 Yep. Consource.
**Dan Gomez Blanco** 08:23 For our contributors.
But I think it should still work for now.
**Morgan McLean** 08:30 I think it's still working now, yes, but my sense… I don't know if they've announced anything, but given, like, over the last year they've been hyping up LFX Insights, I kind.
**Alolita Sharma** 08:37 Mmm.
**Morgan McLean** 08:37 That eventually dev stats will disappear.
**Alolita Sharma** 08:39 Yeah, yeah, that's my understanding, Marian.
**Morgan McLean** 08:43 Okay.
Alright, I've got my action items.
**Alolita Sharma** 08:48 Okay, cool.
**Morgan McLean** 08:53 Next is Severin, Community Raps. Yeah.
**Severin Neumann** 08:57 I think I mentioned this on a… on a Slack thread already, that, like, we did this last year on KubeCon North America, so we should do it once again.
**Alolita Sharma** 09:06 Yep.
**Severin Neumann** 09:07 I don't know, I… I think Austin said he can help with the… trophies, or whatever, how you call that. I think maybe somewhere we even have to form from last year, so we could probably recycle that. I can… I can look into that.
Yeah, I just wanted to make sure that we do that, since we just started it last year, so we should…
**Alolita Sharma** 09:29 Yeah, I agree, Severin, and I think… I do think there's a form, that we had… Used last time.
**Dan Gomez Blanco** 09:36 Yeah.
**Severin Neumann** 09:37 Is there anything we want to change?
like, I mean, the only thing, like, one concern, like, I think last year was that not a lot of people participated.
in the voting, or how was the… how was the sentiment, the feeling there? I cannot really remember, since I was not in… North America, or have we been happy with that, or… .
**Dan Gomez Blanco** 10:00 One of the things that I remember and the four… because I, I, I made the slides for the… you know, to present at KubeCon, which I think, you know, was quite nice to have, like, the comments from people. But some of them were, like.
you know, very short comments. And the other one was, like, you know, almost like, some… some long prose, like, you know.
full paragraph on why they voted for this person. So, I don't know if that… if that aspect of, like, why did you vote for this person, if that… You know, if we want to change something there to… to say…
**Severin Neumann** 10:34 Okay, maybe we.
**Alolita Sharma** 10:35 So, like.
**Severin Neumann** 10:35 You know, 100 words, or, like.
**Alolita Sharma** 10:37 Yeah, do a word limit.
**Severin Neumann** 10:38 sweeter-like length or something, yeah, something like that, like…
**Dan Gomez Blanco** 10:42 my limit, yeah.
**Severin Neumann** 10:43 And make it crystal clear that, like, what you write here has no impact on… I think because some people maybe misunderstood that, and like, hey, they should write something, and that's… because I think at the end it was a popularity vote, right?
**Alolita Sharma** 10:57 Yes.
Contribution, yeah.
**Dan Gomez Blanco** 11:00 Maybe we can just change that to, like, if you want to say a few words to them in, sort of, like, you know, to… reward their contributions, say, here, rather than, like.
**Severin Neumann** 11:09 Yeah.
**Dan Gomez Blanco** 11:10 Yeah.
**Severin Neumann** 11:11 Let me see, I think we… I hope that… if not, I can check with Austin, but I guess it's, owned by admin at OpenTelemetry.io, so…
**Dan Gomez Blanco** 11:20 I think…
**Severin Neumann** 11:21 I see…
**Dan Gomez Blanco** 11:23 But if it was Austin, if it was me, that created.
**Severin Neumann** 11:25 I think it was a Google Form, right?
**Dan Gomez Blanco** 11:26 Yeah, it was a Google phone.
**Severin Neumann** 11:28 Yeah.
Yeah, okay, I'm locked out, and on that Chrome account, I have to… book into that. Yeah, I, I will, I will, I will take a,
**Dan Gomez Blanco** 11:42 Let me see…
**Severin Neumann** 11:42 I will take a look into that, and whenever I need some… something from last year, then…
**Dan Gomez Blanco** 11:48 Nice, I got it.
**Severin Neumann** 11:48 He'll follow up on that.
**Dan Gomez Blanco** 11:50 I'll link the, there's a folder in there with, With, the forum and the responses and all that, and the presentation.
**Severin Neumann** 11:57 Okay.
Okay.
Yeah, or I will ping you on Slack then, and we can… figure it out. Because at the end, I think the setup is not a lot, it's just, like, we need some time, and I think… 6 or 8 weeks before…
**Alolita Sharma** 12:11 Yes, everyone, let me know if you need… need… need any help to review or anything.
**Severin Neumann** 12:16 Yeah, yeah, I will, I will share it on the, on the channel.
**Alolita Sharma** 12:18 Okay, okay.
**Severin Neumann** 12:19 Okay, cool.
**Alolita Sharma** 12:20 Awesome, thank you.
**Severin Neumann** 12:24 Yeah, I think the next topic is also mine.
Dan and I are now mods of the OpenTelemetry community on Reddit.
**Alolita Sharma** 12:32 Awesome.
**Severin Neumann** 12:33 I reached out to the original creator of that.
subreddit a few weeks back. I think, Dan, you pinged him as well, and they're like.
he reacted, or they reacted, and said, like, hey, I just created that, and do not even do anything with OpenTelemetry anymore.
We are not, like, pool maintainers, right? I think we cannot add more people. Oh yeah, one very recent change. I created the OpenTelemetry user as well, and that's also a mod now.
So even if Dan or I are not available, the credentials are in… 1Password, so any GC member is technically able to do maintainer, or how you say, mod activities on Reddit. And we own, like, the OpenTelemetry user. I think I used that one already… once already to just post, like, a blog post that we just published this week, so… Yeah, let's see how much Reddit turns into… into a place where people really interact. I mean, with Stack Overflow.
not being net relevant anymore, maybe… maybe it's redded, I don't know.
**Alolita Sharma** 13:42 I think people definitely use Reddit a lot, you know, especially for discussions and commentary.
**Severin Neumann** 13:49 Yeah, but the OpenTelemetry Reddit is still mostly vendors pushing out their content. So there's not a lot of, like, hey, I use this and that OpenTelemetry component, and it does not work. Can someone help me with that, or something like that? But maybe we can work on that. I think the… Decade threaded is fairly active, so maybe we can take some… some inspiration from that.
**Alolita Sharma** 14:12 It's also communicating, right? That we do have the thread for, you know, getting feedback and listening to.
**Severin Neumann** 14:19 Yeah, yeah, exactly. I think we can, like, maybe do some… modern… we just started with that, right? So let's… if anybody has any good ideas, or is, like, a Reddit pro, then… Then inject yourself into that.
**Alolita Sharma** 14:34 Okay.
**Morgan McLean** 14:35 I'm just looking, I've had my Reddit account for 17 years, but I've also never posted or commented.
**Severin Neumann** 14:40 Yeah, I created another Reddit account specifically for that purpose, so…
**Alolita Sharma** 14:46 Oh, good.
**Morgan McLean** 14:50 Yes, Jurassi, literally, yes.
**Juraci Paixão Kröhling** 14:54 I mean, I know the feeling. There's 17 years from.
**Morgan McLean** 15:00 Carly gave it away.
**Juraci Paixão Kröhling** 15:05 Yeah, the question is, Jurassi, can you actually post anything anywhere?
Hmm… But it always gives me the creeps, I don't know.
**Morgan McLean** 15:17 I have one karma after 17 years. Cool. I'm a member of the subreddit. I agree, Severin, like, there's really just some vendor stuff posted there. It'd be cool if it became a bigger part of the community.
**Severin Neumann** 15:28 Let's see how it turns out.
**Morgan McLean** 15:31 Yep.
**Severin Neumann** 15:31 Anyways… Yeah, I think I also put in the donation.
**Juraci Paixão Kröhling** 15:38 Mr. View.
**Severin Neumann** 15:39 I think we have one new one with the Kotlin.
nation.
**Morgan McLean** 15:47 I see communion.
**Dan Gomez Blanco** 15:49 Oh, sorry.
**Severin Neumann** 15:50 Yeah, your keyboard is very loud.
I think we have one more donation that came in with the Cotlin Multi-platform implementation of OpenTelemetry specification.
I think the first step would, like, that we… Make a closer look into that, if we, like, yeah.
What was the process of donations?
Somewhere, quickly.
Help me.
Are you looking for the documentation? Yeah, we will evaluate the proposal to ensure that the donation is aligned.
**Alolita Sharma** 16:42 We… I think, we had documented the process,
**Severin Neumann** 16:48 Yeah, I just looked it up. So, but we have this new proposal, and I think we just need to do that.
and then we can hand it over to the TC for Their due diligence, right?
**Alolita Sharma** 17:03 Yeah, that's right.
**Juraci Paixão Kröhling** 17:05 But I think at least one… Go ahead, Alito.
**Alolita Sharma** 17:09 Oh, no, no, all I was saying is that, maybe everyone can just take a look at it off… offline, and then, Make sure that everybody's commented or said they've looked at it by next week.
**Trask Stalnaker** 17:25 The Kotlin one.
**Severin Neumann** 17:27 Yeah.
**Trask Stalnaker** 17:30 Should, I mean, in the past, we have… oh, okay, so we need to vote, basically.
**Alolita Sharma** 17:36 Yes. On whether to… Whether we want to accept.
**Trask Stalnaker** 17:38 forward.
**Alolita Sharma** 17:39 Yeah.
**Severin Neumann** 17:41 It's not about accepting, it's more about, like, is it in line with the project vision and roadmap, right?
**Alolita Sharma** 17:47 That's right, that's right.
**Dan Gomez Blanco** 17:49 Nothing.
**Severin Neumann** 17:50 So then… Yeah.
**Dan Gomez Blanco** 17:51 I was gonna say, I was asked in terms of, like, about this in terms of timelines, what timelines they can expect.
And I guess, you know, from our side, now, basically, we… you know, if we say that this aligns with mission, vision, and so on, then… I guess that will depend a bit on the bandwidth of a TC to do a review.
**Alolita Sharma** 18:13 That's right, that's right. It gets queued up for the TC, and then a sponsor… a reviewer gets assigned.
**Trask Stalnaker** 18:23 I'm ready to vote.
**Alolita Sharma** 18:26 I know, it's fast. To move.
**Trask Stalnaker** 18:29 to the next step. I mean, I think this one is a pretty… Easy one… If it has, at least… I mean, the… if it has… the people. Staffing.
**Alolita Sharma** 18:44 Yes. Assuming…
**Trask Stalnaker** 18:45 If we assume staffing, then I think this is an easy one, because it's just… Essentially, another language implementation… implementation.
**Severin Neumann** 18:55 I'll… how… oh, sorry, Rossi.
**Juraci Paixão Kröhling** 18:57 Yeah, it was, in line with what Fraske's saying. My point was gonna be that, it should… I mean.
this is an easy one. Like, everybody wants this one. But, exactly because of that, it should be… it has to be easy to find people other than just Embrace to staff this project. So it's not just the staffing from the regional proponent, but staffing for the sick days coming, like, on the long run.
I see 20-plus reactions, only on thumbs up, and I don't know how many on the other one. So it should be easy to find at least, like, a couple of other companies, to be part of it.
Even if… Even if it is just like the previous proposals, where companies would just jump in for the donation proposal and then forget about it. But I'd be happy. I mean, I think it would be a requirement for us to just, you know, have at least a couple of other companies than just embrace.
**Dan Gomez Blanco** 19:55 Right.
**Juraci Paixão Kröhling** 19:55 At this stage. Because, so Severin posted here, that, has a balanced, set of interest contributors and maintainers, so I think this is the very first step.
**Severin Neumann** 20:07 Yeah, mutton has…
**Juraci Paixão Kröhling** 20:09 Yeah.
**Severin Neumann** 20:10 My comment would have been in the same direction, like, we have the DART proposal right now as well, and they also have staffing, but we are blocking them right now because all of them are, like, from the same circle of people. So if we, let's say.
By same measure, then we should do this here as well, and say, like, hey, this is really cool, can we see some second party supporting that effort?
**Juraci Paixão Kröhling** 20:37 I would, I would even say two more, two more companies.
That's what we've typically been kind of asking in the past.
**Dan Gomez Blanco** 20:46 Nice to see.
**Juraci Paixão Kröhling** 20:47 That's what I'll go ahead and do it.
**Dan Gomez Blanco** 20:49 I just wanted to say I agree with that, and that was also communicated to Embrace, so they're aware of that.
And, they've already been, sort of, like, publicizing this in the Android seg call and the client side, you know, to try to get, basically, more folks to… maybe some of those that voted to join.
Yeah, I don't know if there's anything else we can do in terms of, like, You know, help promote this, but, or if they're, you know… If… You know, they're promoting it within current sex, that's probably…
**Alolita Sharma** 21:22 Would it… would it make sense, Dan and others to kind of have a blog post for, you know, key contributors who could come, you know, volunteer to come and join the Cotton?
Project, because…
**Dan Gomez Blanco** 21:39 We've never done a blog post before.
**Alolita Sharma** 21:41 Yeah.
I know.
**Severin Neumann** 21:44 But we could… I mean… We, we could… do that. Like, like, they could ride one, right? It's like, hey, we.
**Alolita Sharma** 21:53 Yeah, yeah.
**Severin Neumann** 21:54 And we could extend that to other donations as well, and we say, like.
So, from my understanding, there's, like.
does this… is this in line with our vision and roadmap? Yes, I think that's answered, right? That's, I think, the very first question. I think the same applies to the… to the… to the… to the Dart slash Flutter donation. Is it in line? Yes, that's answered. But the second question is, like, how can we make this project successful?
And that's something… and there, it says, like, in our own guidelines, we help them to drive that, to make them, like, here, so I'm fine with reaching out to any donation and saying, like, hey, if you come to comms and want to write a blog post.
we are more than happy to push this out and say, like, hey, people, we want to form a new SIG. I think that's a good idea, but we should extend it to all donations.
**Dan Gomez Blanco** 22:46 I agree.
**Alolita Sharma** 22:49 Yeah, agreed, agreed. Because I think it's just, to help, you know, the community form, and more folks who are, you know, aware of the, or interested in language, actually coming and joining the community.
**Juraci Paixão Kröhling** 23:04 So, I, I agree, but with one, one detail, and the detail is the blog post should come from them.
**Alolita Sharma** 23:10 Yes. Yeah, it should not be official project communication.
**Juraci Paixão Kröhling** 23:14 Because I think it is on the people that are gonna run the SIG, to find new maintainers, and to make sure that the SIG is healthy. So, I mean, we should help them in as many things they want or they need, but they should be the ones reaching out and going after people to help them.
**Severin Neumann** 23:35 Yeah, no, I think that that's what we agreed on, right?
**Alolita Sharma** 23:38 I mean, the Embrace team has also been very, very active and contributed to SWIFT, so again, I can definitely.
**Severin Neumann** 23:46 I think the moment we tell them, like, hey, write a blog post, I think I will have one. So, the Embrace folks are, like, very proactive, so I'm not worried about that one.
I think it's a good practice in general to say, like, hey, here's the channels, how you can communicate it, and we will support you on that. But it's your job to do that, right?
Yeah. I mean, we can share it with the maintainers, we can share it, like, in the internal community, and say, like, hey, here's a… but, like, the external communication, they need to… Because they can communicate this better than I could do it, right? I could just copy and paste some stuff from their donation proposal and put it on the website. But yeah.
**Alolita Sharma** 24:26 Yeah.
**Juraci Paixão Kröhling** 24:27 So I suppose that the official comment from the GC is going to be the one that you just said, right? So a comment on the issue there, saying, yes, this aligns with what we want for the future, but it's on you to bring more people in.
**Severin Neumann** 24:41 Does it align on that, like, I mean, can we quickly vote on that?
**Alolita Sharma** 24:45 You can read…
**Juraci Paixão Kröhling** 24:46 Yeah.
**Alolita Sharma** 24:47 We should read the proposal, at least.
**Severin Neumann** 24:51 I think that's the first question, does it align? I think then maybe we vote on that first, and then, like, we can do the second part.
**Dan Gomez Blanco** 24:58 Let's Rask first.
I give you…
**Severin Neumann** 25:00 Oh, yeah.
**Dan Gomez Blanco** 25:01 If not everyone here has read it, then… probably.
**Alolita Sharma** 25:05 Yeah, I haven't read it yet. I'll go through it very quickly. I can do that.
**Trask Stalnaker** 25:11 I was gonna ask a kind of process question. Should we assign a GC member… to, be, like, the… assign them to donation proposals, sort of like the TC does.
We've done that before.
Yeah…
**Alolita Sharma** 25:33 Yeah.
Morgan led the profiling, for example.
**Trask Stalnaker** 25:38 But should we do that more proactively? Because what has happened in the past is, like, donation proposal comes in, and sort of, nobody really owns it, and… for a while, and then they escalate it some… to somebody, and then we get around to assigning and funneling.
**Morgan McLean** 25:57 I think it's a good idea.
**Juraci Paixão Kröhling** 25:59 I think one thing that Severalin did this week, and I think this is one of the reasons for bringing that up today, is we reviewed the donations during the triage meeting this week.
So I think, alternatively to having a liaison for that, I think we could have, the donation proposals as part of the triaging every week. So we take a look and see what is, has there been an update?
I think the thing that I like the most about triaging versus liaison is we don't get dependent on one person. It is… Clearly, like, everybody, and it is part of the process.
**Dan Gomez Blanco** 26:35 Yeah, makes sense.
**Trask Stalnaker** 26:39 good with that. Any way just to not lose track of them, which we tend to do.
**Dan Gomez Blanco** 26:44 Yep, he's.
**Juraci Paixão Kröhling** 26:45 Yep.
**Dan Gomez Blanco** 26:46 to Trask's point.
I think both are valid, right? I think, you know, having that in the triage, and then also having someone assigned that oversees the… You know, as there to support them, let's say.
Like, things like, oh, you know, bringing up to them.
How, you know, go and… you can create a blog post, and things like that.
Following up on conversations, I guess.
**Severin Neumann** 27:13 Point of contact is always good, yeah.
**Alolita Sharma** 27:18 I had a couple of questions, on this, task, specifically from a Java perspective. Again, obviously, you know, Kotlin is, kind of, you know, a… very related to Java. And, and, do you see any kind of… common, libraries and common, you know, features that get built, in Kotlin that could be collaborated on by the JavaSig as well as Kotlin SIG. If… if a Kotlin SIG exists, that's my first question. And second question is, given Kotlin is very, you know, widely used in the Android, you know, world.
how do you see the interaction with the Android community working there, given this is a language SIG we are thinking about right now?
You know, how do you see that interdependency working?
**Trask Stalnaker** 28:25 So I've, I think that those are both… topics, that the TC, review will need to… get into…
**Alolita Sharma** 28:40 Yeah.
**Trask Stalnaker** 28:40 At a very high level, there's… I'm not sure there would be shared library usage, because the… the goal of the Kotlin folks, one of the reasons they want to do this is so that it's a pure Kotlin library, so they can compile it.
**Alolita Sharma** 29:01 Not only Java?
**Trask Stalnaker** 29:04 And then on the Android side, I would… imagine that the Android, like, once there's a solid Kotlin implementation that the Android SIG would probably lock to that.
**Alolita Sharma** 29:23 Sure.
**Trask Stalnaker** 29:24 to that.
I don't want to kind of speak out of turn.
**Alolita Sharma** 29:28 Yeah, I mean, again, these are, I mean, as you said, rightly, there's… it's complicated, right? So… They're big talk, yeah.
**Trask Stalnaker** 29:36 It requires some…
**Alolita Sharma** 29:38 Yeah, because what we don't want to happen is that, you know, again, take away the necessary… I mean, I… it would be nice to add to the thunder of Java rather than, you know, fragment the… community, because there are many Java engineers who love to also write Kotlin. And then the other part is that, you know, again, the essential to have Android adoption in order to Make sure that, the community flourishes in Hotel.
**Dan Gomez Blanco** 30:10 I think… this will probably be more discovery during the due diligence from the TC, but the… at least their initial, approach is to provide two modes, one where, like, you know, there's a Kotlin API.
**Alolita Sharma** 30:25 Yeah.
**Dan Gomez Blanco** 30:25 basically still uses the Java SDK, and the other one is, like, implementing that Kotlin native SDK as well.
**Alolita Sharma** 30:32 Yeah.
**Dan Gomez Blanco** 30:34 M… so far, I don't know, from what I see there, after reading that, Yeah, I would agree with, With the fact that it aligns with… with the… With a vision of hotel.
That would be my… my personal vote, but I think we can postpone that, that vote until everyone's had time to think.
**Alolita Sharma** 30:57 Yeah, yeah, absolutely. I mean, again, these are larger questions in terms of just making sure that we continue to grow the Java community.
Absolutely.
**Trask Stalnaker** 31:11 Do you feel like those quests… do you want any more clarification on those questions before we do the initial GC vote to move forward?
**Alolita Sharma** 31:22 I think, I think, it would be… Good to talk to the current, you know, proposers to see how they work… work through that, because maybe they are just thinking about the technical implementation.
And again, obviously another dimension from a project perspective is to continue to grow our community, right? So, and also have it aligned in these two different key areas.
Because, Kotlin is an interesting, you know, sits an interesting layer.
between the client side, as well as, you know, you can do a lot with it, even in the Java server side.
You know, implementation.
So, again, just having maybe some understanding, and maybe the TC can ask this, is… Just having some understanding of how they plan to address that.
Or have thoughts on it, would be good to know.
**Trask Stalnaker** 32:27 What shouldn't happen?
**Alolita Sharma** 32:27 that they're coming in with a particular purpose, right? And then they're abandoning the deeds.
**Trask Stalnaker** 32:33 Oh, yeah, I thought… I mean, I think we all agree that has to be answered during TC due diligence.
**Alolita Sharma** 32:39 Yeah, yeah.
**Trask Stalnaker** 32:40 The question that I have for this group is, do you… what part of that do you want addressed before we even vote to pass it on to the TC?
**Alolita Sharma** 32:53 I mean, the community aspect is definitely the role of the GC to look at, right? So, understanding how that interaction would play out.
across, you know, technically 3 different communities, is something we should understand a bit more of. It's not a blocker, but on the other hand, it's good to understand how it impacts Hotel as a community.
I mean, I only see positive out of it. It's more that, We should have the same understanding as, you know, the maintainers who are coming in into the Into this, if… if accepted.
**Trask Stalnaker** 33:41 So I guess I'm not quite sure which part you're not clear on.
**Alolita Sharma** 33:46 I'm just, I'm just trying to understand their thinking.
That is the, you know, current proposers in terms of how they plan to grow and sustain the community. That's around the Kotlin SIG, and, you know, what their thoughts are in terms of how they interact or interoperate with the Java SIG, as well as the client-side, you know, Android.
Same.
That's okay.
Definitely.
**Juraci Paixão Kröhling** 34:20 If I may have a follow-up question to you, Lolita, is that, is that something that we need to, that you want an answer right now?
Or…
**Alolita Sharma** 34:29 I can ask it on the… on the issue itself, I can just ask, if that's okay, and then they can just respond to it, and we can just move on.
**Juraci Paixão Kröhling** 34:43 So I think, yeah, I think those are things that, I think Teresk mentioned, that those are things that are definitely going to be addressed during the GC, review.
**Alolita Sharma** 34:51 I mean, does the TC due diligence, I mean, again, I'm just trying to understand myself. It's… does the TC due diligence address the community?
Aspects?
**Trask Stalnaker** 35:07 have traditionally addressed how different projects within OpenTelemetry interact.
**Juraci Paixão Kröhling** 35:14 Like, whether there's a consolidation.
Okay, yeah.
**Alolita Sharma** 35:18 I mean, so I think that that'll be totally addressed then. I mean, I… that's the only question I have, because it's a… it's a very large community. Kotlin in itself is a very large following.
So it's… it's… it's not a… it's not… you know, if it is picked up by Android, especially, and also Green's momentum, there is a lot of positive that comes out of this, right?
But it's also that it has to be helped and managed.
I mean, I just want to raise it. It's not necessarily any blocker or anything.
**Trask Stalnaker** 36:05 No, no, I'm just trying to get to what are the concrete next steps.
Is all, and if you have, if you would like…
**Alolita Sharma** 36:13 Like, clarify.
**Trask Stalnaker** 36:13 Notifications, let's just… let's just write them down and get.
**Alolita Sharma** 36:17 clarifications to your questions. I can just answer or ask on the issue, right?
**Dan Gomez Blanco** 36:23 Yep.
**Trask Stalnaker** 36:23 Yeah, of course.
**Alolita Sharma** 36:25 Yes, I'll just ask on the issue, because again, it's good for them to kind of just provide some understanding of what they are thinking, and then… and then, of course, the TC will dig in. So, all good.
**Trask Stalnaker** 36:42 Thanks.
**Alolita Sharma** 36:42 Thank you, thank you.
**Juraci Paixão Kröhling** 36:45 So, do we want to, take… I mean, it is going to take a.
**Trask Stalnaker** 36:49 Yeah.
**Juraci Paixão Kröhling** 36:50 a week then to, to come back, to this topic, and, it's gonna… and for us to give a definitive word to them. Should we then… comment on the things that Severin mentioned before as well, like, Not the part that we are ready to accept, because that's not… we don't have a vote for that, but The other thing is.
we need… we know already that they need more people. Yeah. Non-embrace folks. Should we want… do we want to comment that already? So that by.
**Severin Neumann** 37:23 I would say yes, because right now, there's only one vote, like, from the donation process, the GC is only doing one vote, right?
So technically, we looked at it and said, like, hey, here's some concerns that we have. We share it with them, and then when they have, like, resolved them.
then we can say, like, okay, this… I think… If we look at it, and I think there's no V2 on, like, hey, this is not in line with our vision and roadmap, right?
**Alolita Sharma** 37:55 Yeah, that's right.
**Severin Neumann** 37:56 But that does not also automatically mean, like, we do that, or that not someone maybe, like… we did not vote on it, but, like, we also do not disagree with it, like, this is, like, how you say it, right? So… so we said, like, hey, this looks like a good proposal.
But here's a few concerns we want you to address, and then we move forward with that. Versus, like, hey, we looked at that, and we block it immediately, and…
**Juraci Paixão Kröhling** 38:20 That's not the case, right?
No, I think we agree on that.
**Alolita Sharma** 38:24 Yeah. Yep.
**Severin Neumann** 38:26 I think… So I think that… yeah, Dan.
**Dan Gomez Blanco** 38:29 I was just gonna say, that's the… so we still have the final say after the due diligence doc is produced.
**Severin Neumann** 38:34 Anyways, yeah.
**Dan Gomez Blanco** 38:35 I think, basically, right now, this vote is, do we want to continue? And, like, and these two things can happen in parallel, TC, you know, due diligence at the same time that, you know, there's more contributors signing up. I don't think…
**Trask Stalnaker** 38:48 That's the one thing that I would like to… that we probably should discuss more, is the… because we have blocked, like, the DART proposal.
on staffing.
We, like, say, we want to see staffing before we move it to due diligence.
**Juraci Paixão Kröhling** 39:06 I think this is, yes, I agree with that, so we should, we should not move forward because of the staffing, but, the, like, is this part of the vision of the project? I would say it is, as long as this X, Y, and Z happen.
like, we agree with the direction, but I'm painting the TC review of the interactions and interoperability with Android and blah blah blah.
But yeah, staffing is definitely something that needs to be committed before we move forward.
**Severin Neumann** 39:42 Okay, I think then it remains, like, that someone picks it up and comments, like, or multiple people can do that. I think, Alolita, you had a few more questions.
**Alolita Sharma** 39:52 Yes, I'm just adding it to the issue 7, so… And maybe someone can comment on the…
**Severin Neumann** 39:58 And let's be positive and tell him, like, hey, this is a great And we want to support you on that.
GC… Has no major objections or something like that.
And we want to guide you through that. And I can later also… I put it on the… we have… comms meeting later today. I will also then discuss with the rest of the SIG about, like, having donation proposal blog posts.
And then I will put a comment on a few of them and say, like, hey.
We want to offer you the opportunity to do a blog post to gather more people around this effort.
And then they can do it or not.
**Dan Gomez Blanco** 40:37 Sounds good.
**Severin Neumann** 40:38 Yeah.
Awesome.
I don't know about the other ones, like, the PHP one, I think TC did their due diligence. There is an ongoing discussion around around, like, C++ and everything, but it's ongoing. I think, the compile time, I think we can close that one, if I understand it correctly.
**Dan Gomez Blanco** 41:06 Yeah, understood.
**Severin Neumann** 41:06 And for OpenLelementary, I think we need CAD, so yeah.
Yep.
**Pablo Baeyens** 41:13 I think… well, I'll let Jersey speak first on that.
**Juraci Paixão Kröhling** 41:17 I was just gonna say that perhaps we can talk more about that, perhaps, asynchronously, because we do have a topic to discuss, and we have only 18 minutes.
**Dan Gomez Blanco** 41:28 Okay.
**Pablo Baeyens** 41:31 Yep, let's do that.
**Dan Gomez Blanco** 41:33 I can… I can create a link if you want.
**Alolita Sharma** 41:36 Alright, Dan. Yeah, see you then.
