SIG: Governance Committee
Date: 2026-06-10
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Armin (Dynatrace) 00:00:21 Hey, good morning.
Austin Parker 00:00:24 Yo…
Morgan McLean 00:00:25 Hello?
Trask Stalnaker 00:00:40 Hello!
Austin Parker 00:00:42 Howdy, howdy.
Morgan McLean 00:00:57 Austin, do you have an outdoor fan on your patio?
Austin Parker 00:01:01 I do.
Morgan McLean 00:01:02 That's very cool.
Austin Parker 00:01:06 Helps keep the bugs down a little bit.
Morgan McLean 00:01:08 Yeah, makes sense.
Austin Parker 00:01:16 Oh, you can see the flexion.
Morgan McLean 00:01:18 Yup.
Alolita Sharma 00:01:19 That's… that's how we can tell, Austin.
Reiley 00:01:37 Long one.
Tigran Najaryan 00:01:43 Hey, everyone.
Alolita Sharma 00:01:46 Hi, Tigran. Long time.
Tigran Najaryan 00:01:50 Hey.
Alolita Sharma 00:01:51 Thank you.
Jack Berg 00:02:15 No items in the agenda.
Trask Stalnaker 00:02:19 Yeah, I was just creating the new log entry, but yes, it is empty.
Marylia Gutierrez 00:02:45 Well, I can think of one. Actually, Trask, you brought it up this a while back, but I don't know if you discussed it with the GCs yet. The idea of having… because the GCs, we have the liaison channels.
Not all of them include the TC responsible for that sick, so we're thinking if the… Is sponsor the name? Yeah, the TC sponsor should be also on the liaison channel.
Tigran Najaryan 00:03:16 You kept it secret from us.
Juraci Paixão Kröhling 00:03:22 We were hoping super intentional.
Alolita Sharma 00:03:26 What advice?
Jack Berg 00:03:26 Yeah, exactly.
Alolita Sharma 00:03:27 Only discussed last week.
Jack Berg 00:03:32 What if the maintainers have an issue with their TC sponsor?
Alolita Sharma 00:03:38 Well, well, it's a whole separate…
Trask Stalnaker 00:03:40 escalate.
Marylia Gutierrez 00:03:43 Yeah. I do always, like, on my messages, say, like, if you have a issue, because there's always, like, a generic, like, if there is something you want to bring, you can bring it up. If there is something more, like, private or stuff, feel free to just DM me directly.
Trask Stalnaker 00:04:07 Yeah, I think it would be great to have the, TC books on all of those.
Check-ins, just for visibility.
Armin (Dynatrace) 00:04:18 Yeah, sounds good. I only found out about the existence of those GC liaison channels for the 6 where I'm at it, because of being a maintainer rather than the TC.
So I think it makes sense to have us there as well.
Trask Stalnaker 00:04:33 You also found out about it because, Relia has been bugging us all to create them and do our job.
Marylia Gutierrez 00:04:42 Which, by the way, I'm still waiting for people on this call to read to fill that note, so please do that.
I actually… okay, I'm gonna share that file with the TC as well, because now you know the… all the ones that do exist, so if you should be in one, you should bug your GC for, like, why you didn't create as well.
Juraci Paixão Kröhling 00:05:04 is we should change also the community README file to include the TC liaisons, because I tried to include the TC liaisons on the channels, but I found that they are not listed there.
They're only listed for the spec SIGs, not for the cross-cutting SIGs, for instance. So I don't know where the TC… sponsors for… Things like… I think it…
Alolita Sharma 00:05:29 This might be a good thing to walk through that list with the TC, actually, first, and then… go through Marillia's, list of the channels.
Marylia Gutierrez 00:05:41 So, actually, the thing that Pablo was working on was really helpful with that, because I… Yeah, yeah, that was the place that I grabbed from. So, if the file that I created, I actually added a column for TC Sponsor, so all you see, liaison, TC Sponsor.
are on that column. The ones that don't have is because they, well, did not exist on the… gonna share the file here on the channel again. But yeah, they should be there. If you see something that is wrong, then, yeah.
Let me know, because then it has to be fixed on the file, the link that Pablo just shared.
Alolita Sharma 00:06:44 So, Marilla, this is the, file that gets updated now, right? Because for the new SIGs and… The new, updates.
Marylia Gutierrez 00:06:57 What do you mean?
Alolita Sharma 00:06:59 There is, you know, when we create new SIGs, or we set them up.
This is the YAML file, right? Instead of the… sigs.yaml.
That used to be there.
Marylia Gutierrez 00:07:12 I mean, the Workstream link that…
Alolita Sharma 00:07:14 Yes, yes, yeah, yeah.
Marylia Gutierrez 00:07:17 Well, I guess Pablo can confirm.
Alolita Sharma 00:07:20 Pablo, is that the case?
Because I don't see sigs.yaml anymore, right?
Pablo Baeyens 00:07:25 Right, workstreams.yaml replaces sotyaml.
Alolita Sharma 00:07:28 Okay, okay. Because I don't think that's very clear, even in the instructions, to create and set up new SIGs.
Pablo Baeyens 00:07:38 Try to replace old references to 6.yaml, to work streams.yaml.
Alolita Sharma 00:07:42 Yeah, okay.
Pablo Baeyens 00:07:44 Maybe there was no reference to 60 YAML in the first place.
Alolita Sharma 00:07:47 No, there was, actually.
Marylia Gutierrez 00:07:55 Yeah, just for the stock, then if you'll agree, at least. I'll be adding the For the ones that I haven't added already, the TCs to the channel, and I hope you all do the same as well.
Trask Stalnaker 00:08:21 Ludmilla!
Shall we talk about open inference donation?
Liudmila Molkova 00:08:27 Yeah, let's talk about open infrared donation.
Should I present?
Give me a sec… Okay, yeah.
Open inference, folks, send the issue to donate their instrumentation code. They are not donating semantic conventions, we don't need anything but instrumentations, and we're going to use these instrumentations to seed our, Python repo for sure, and depending on other languages and, whatever rules and, their impressions they have.
They can make use of this code as a reference.
So this is code only. We are not going to keep the repo, we are not going to use this code in OpenTelemetry instrumentations directly. We will port it to whatever we want, and it's the GenAI SIG Work power to do this. It's not a rise.
We had the discussion this week, I have the due diligence document here, with some steps of how we absorb this change, at least in Python, and probably in other languages as well.
The SIG is supportive of doing this, and it's important for us to get the instrumentation coverage and Hopefully, reduce fragmentation in the ecosystem because of all those different instrumentations out there.
it seems that, it's approved on the GC side, and I'm still not completely sure what the process we should follow here, or if we should consider it.
done by now, but I think we should, talk about it a little bit.
Trask Stalnaker 00:10:29 So, we didn't vote on it in… or did we? I brought it… I raised it in the GC whether we needed to, given that it was… just being handled by CLA, By a PR as CLA within the SIG.
But it's probably worth… Voting.
To move it forward, going through the normal process as well.
Pablo Baeyens 00:11:02 Yeah, I mean, we did discuss it on a GC.
Alolita Sharma 00:11:05 Yeah.
Pablo Baeyens 00:11:06 with Quorum, so… I never think that as being approved.
Alolita Sharma 00:11:10 Yes, yes, and it was discussed in detail. So, and those of us, you know, again, on the Gen AI seg, there's been a lot of public, support for it.
So… It's been pretty vetted out from the Sega also.
Pablo Baeyens 00:11:27 from the TC side, there's a thread, from May 29th, where My understanding with what was said there is that we didn't need anything from the TC.
-Oh.
Trask Stalnaker 00:11:44 Yeah, it sounded like there was… that was my understanding from that thread as well, or at least that was my proposal in the thread.
But it sounded like there was still a desire from last week's TC meeting to do the due diligence.
Lyudmila, is that… that's… I assume that's why you did the due diligence?
Liudmila Molkova 00:12:06 Yeah, I think it's, it's good to have it documented and have, The TC, take a look. Do people want a review?
TC Fellows.
Tigran Najaryan 00:12:21 We trust you.
Alolita Sharma 00:12:25 I use a TC.
Jack Berg 00:12:27 Do the due diligence, because I don't want you to have wasted your time. Like, I will read this, but I do also trust you.
Alolita Sharma 00:12:34 It has actually been quite, quite, quite well vetted out.
Sorry, I was disappearing.
Trask Stalnaker 00:12:41 Dude.
So I want to, just in the TC channel, Have a vote later.
today or tomorrow, and because we do have the, we did get the PR yesterday from Arise, into the donation, the temporary donation repo.
Alolita Sharma 00:13:02 Good, good.
Tigran Najaryan 00:13:05 Yeah, we can do that, but… Yeah, but…
Armin (Dynatrace) 00:13:08 And trust me, let me… Absolutely.
Tigran Najaryan 00:13:10 the due diligence, it's fine, right? You make the call.
Armin (Dynatrace) 00:13:17 And Trask, you've reached out to the CNCF Legal, via service desk, right? And… with the CLA running on the PR that we are just looking at, or we're just looking at earlier, that's all settled then, nothing extra.
Liudmila Molkova 00:13:35 Awesome, then, I'll post a quick what on the TC channel today, right after this call, and… It sounds like there is a support, and… but let's just do the formal vote, and if we have no objections by the end of my day today… I… I'll… We'll proceed with donation. How does it sound?
Awesome.
Cool, that's…
Trask Stalnaker 00:14:08 This… this is, I think a good template for us for certain kinds of donations going forwards, of… doing it through the CLA.
When it's, like, donating already, open source stuff, that's kind of what I had reached out to the… when I was discussing with the CNCF, because it's kind of… frustrating every time we have a donation to go back and be like, okay, can we get legal involved? Like, how do we do this? Every time we're always, like, reinventing, rediscovering how to do these steps.
And I think as long as it can go through the CLA, a PR CLA into, like, a… and we can always do a temporary repo like that, that that's a good path for us in the future to simplify things.
some things.
Armin (Dynatrace) 00:15:12 as long as the PR is coming from someone who's employed with the IP and trademark owner, I think we can trust that whatever they certify with the CLA bot is fine. If it would be coming from someone else, then we'd still need to have our own Layer of diligence around that.
Alolita Sharma 00:15:35 I think typically an explicit, call-out is done for just the license, and the donation CLA, agreement.
Acceptance.
So, Trask, is that something that they have added in the PR, or… Just a couple of lines, in terms of… You know, publicly stating that they're handing the… Handing off this piece of code, actually.
Trask Stalnaker 00:16:05 Yes, the links are right there if you want to check.
Alolita Sharma 00:16:09 Okay.
No, no, I mean, usually that's what we do, so…
Trask Stalnaker 00:16:13 Yeah, it is. It's very clearly… Stated in both the community issue and in the PR.
Armin (Dynatrace) 00:16:24 I think the community issue also serves as paper trail. I remember us going some extra miles with Elastic back in the days, where we asked for some higher up there to make a public blog post or something like that on the topic. But there it was about the roadmaps converging on the long run, which is not the case here.
Alolita Sharma 00:16:47 Yeah, I think, I think, Armin, that was a bit more complex.
Pablo Baeyens 00:16:53 I think what's missing here is an explicit acknowledgement of the marketing guidelines, or at least I haven't.
Alolita Sharma 00:16:59 Yeah, I couldn't see it.
At least in the, issue.
Pablo Baeyens 00:17:03 And I feel like that's separate from the CLIE legal aspect, it's more like.
Alolita Sharma 00:17:07 Yes, yes.
Pablo Baeyens 00:17:09 Would be nice.
Alolita Sharma 00:17:10 Yeah.
Trask Stalnaker 00:17:10 Okay, I can ask for that.
Liudmila Molkova 00:17:36 Let me hit since Riley is next.
Reiley 00:17:39 Yeah, so just sharing a link, I… I've seen, like, people trying to define Gen AI-related formats or semantic conventions or something in between in other places, and I suggest that we… we probably should do a proactive, like, reach out to them.
It'll be bad if, for example, OpenTelemetry and semantic convention, then there's a W3C or RFC or some standard that's totally different from what OpenTelemetry is doing. I know, like, trying to align people is hard, but having a conversation is always, like, better than a late discovery.
So, just hi-fi.
Trask Stalnaker 00:18:20 Riley, do you know what, is there a foundation… A group… working group or foundation behind this?
I… That's all.
Reiley 00:18:30 I don't have the…
Austin Parker 00:18:32 It's just an idea.
Drift, draft…
Alolita Sharma 00:18:35 Yeah, it's…
Trask Stalnaker 00:18:35 It looked like just a single…
Austin Parker 00:18:38 It's a guy.
Trask Stalnaker 00:18:39 That's all.
Reiley 00:18:39 Yeah.
Yeah, it seems to me… a single… a single contributor from a company trying to push for something. It'll be great if we can align the effort. Anyway, so my point is, like, there are many standard bodies, and I expect AI is called, people might, like.
it doesn't mean, like, they just want to invent their own thing. Maybe they didn't even know OpenTelemetry, they didn't know semantic conventions, so it's, like, good to just, like, spread the information, let people just understand.
Austin Parker 00:19:12 Yeah, I mean, we… Agentsign.dev?
Also.
Alolita Sharma 00:19:25 there is a task group. I think, Pablo, you're already connected there, on the AAIF. I think they're also starting to discuss, some of the…
Austin Parker 00:19:36 Oh, boy.
Alolita Sharma 00:19:37 availability.
Pablo Baeyens 00:19:38 I can ask you more of this.
Alolita Sharma 00:19:41 Yeah.
Austin Parker 00:19:42 I got a coach.
Trask Stalnaker 00:19:42 to that meeting, as a laya.
Alolita Sharma 00:19:45 Okay, okay, friend.
Trask Stalnaker 00:19:46 telemetry.
Alolita Sharma 00:19:47 Okay, okay, awesome.
Austin Parker 00:19:48 I… I would not overdose.
Trask Stalnaker 00:19:51 That's a legit… that's like a legit foundation that is, you know, they have working group and meetings. They have a lot of people who attend the meetings, actually, so I do think that's an important one for us to… Stay close with.
Austin Parker 00:20:10 That is a very… clawed website.
Alolita Sharma 00:20:14 Yes.
It's like, Claude may have generated this completely.
Austin Parker 00:20:22 I'm fairly… I strongly suspect that Claude generated every…
Alolita Sharma 00:20:27 Wood.
Austin Parker 00:20:27 in… This entire thing.
I mean, I can speak, and just, like, as an aside, like… I've had pretty poor luck in… Well, the bigger… the bigger challenge, actually, is… There's the… Agentic AI Foundation? Is that the name of it? It's the new Linux foundation?
Trask Stalnaker 00:21:04 Hell up.
Alolita Sharma 00:21:04 The EIF, yeah.
Austin Parker 00:21:06 Right, well, so they have a observability working group, that is members only, so it's literally pay-to-play. So…
Trask Stalnaker 00:21:16 They let us… they let us join as OpenTelemetry.
Austin Parker 00:21:21 Yeah, but, like, that, to me, is…
Trask Stalnaker 00:21:24 Oh, in general, yes, as a non-.
Austin Parker 00:21:26 In general, it's a slightly more concerning.
Trask Stalnaker 00:21:29 Closed.
Alolita Sharma 00:21:30 It's not open source at that point.
Austin Parker 00:21:33 I mean, it's a slightly more… like, that feels like where Anthropic, at least, is putting their pennies. Yep. So…
Morgan McLean 00:21:43 Sort of reminiscent of Standard's bodies, like, 20 years ago.
Alolita Sharma 00:21:47 Yes.
Austin Parker 00:21:48 Everything old is new, again.
Trask Stalnaker 00:21:50 race for… race to create AI standards bodies.
Alolita Sharma 00:21:54 Exactly.
Austin Parker 00:21:59 Was that Sable to do it for us?
Why don't we just put Fable in charge of… well, put Mytho's in charge of the standards, buds.
Trask Stalnaker 00:22:20 Shall we move on?
Alolita Sharma 00:22:23 So what's the action item on this specific… Follow up, who's following up?
Rask will be not that?
Trask Stalnaker 00:22:34 Not me.
Alolita Sharma 00:22:35 Okay, no, no, I didn't say you. It's like…
Trask Stalnaker 00:22:38 I'm following up with a… I already attend two other AI working group, foundational meetings.
Liudmila Molkova 00:22:50 wait, AI Agent Foundation Austin was talking about, and which is the second one?
Trask Stalnaker 00:22:55 COSI, the Coalition for Secure AI.
Liudmila Molkova 00:23:00 Okay.
I… I can reach out to this person, but I… to be fair, I don't think the… like, I can tell them, okay, hi, we've seen you, we have GenAI working group here.
But I… I don't think they are, in any position to compete with ASB, or that it's a serious competition, because we have 10 other much more serious competitors in the space.
Alolita Sharma 00:23:24 Yeah. Yeah.
Trask Stalnaker 00:23:28 If this… I mean, you know, we could check back and, you know, keep an eye on it. If it gets… if they create a working group around it, or there's, you know, more… some interest forms around it, then definitely, you know, we would… It would be worth… Engagement.
Liudmila Molkova 00:23:51 Awesome.
Jack Berg 00:23:57 Alright, next topic.
That's mine.
Alright, so, at the last joint GCTC meeting, I brought up, you know, the issue of incentivizing… incentivizing maintainership.
I'm not gonna recount all that, but I opened an issue to follow up with that, and there's, like, a parent issue that describes, like, the overall goal.
You know, let's… let's create more incentives for maintainers, because they carry a lot of load for the project, and we want to encourage the types of things that they do. And there's a bunch of child issues, about specific suggestions on how we can provide those incentives.
And, the parent issue, which is like, hey, this is a problem, let's do something about it, has gotten a lot of support.
And you know, it's a month later, I think we should do something about it. So, I don't propose that we do everything all at once, or anything like that. Maybe just start with one thing and see where that takes us.
I have a pet issue of mine, or, like, a pet proposal of mine, which is, you know, I want to channel the, the ideas and the priorities of maintainers into some sort of published artifact.
Because, you know, as we all know, this isn't a company, we don't have a hierarchy, we can't demand that maintainers do things. We operate on, like, you know, distributed consensus, and we share ideas, and those ideas encourage people to do different things. And, you know, so, like, what does a roadmap mean in the context of that type of organization? I think the closest thing to a roadmap is just, like.
Like, some sort of collection, expressing what maintainers intend to do.
like, a sort of heat map of the things maintainers intend to, like, focus on, and that's kind of what I would want to produce.
We did this exercise at Hotel Unplugged earlier this year, where Austin and Ted helped organize this, where, you know, there's, like, kind of a multi-phase thing. It was the first, like, hey, let's collect topics.
And, you know, people collected a bunch of topics, open-ended, and then maybe there's, like, a little bit of grooming that grouped them together, and then there was, like, a voting period. And, you know, the result of that was just, like, a sort of prioritized list of the things that people think are important in the project.
We could do something like that, as just, like, a simple first step, and do it on some sort of periodic basis.
once a year, twice a year, or whatever cadence we choose. But, that's what I was thinking, and yeah, if anybody else has any suggestions they think would be a good first step at this, or just, like, disagrees that we should do this, I want to hear about it.
Pablo Baeyens 00:26:44 I think I shared to link I shared in the Zoom chat before, but yeah, I like how Rust, as a project, does that with the project goals.
I think we could take inspiration from them.
Jack Berg 00:26:56 How do they channel those goals, Pablo? Like, how do they source them?
Pablo Baeyens 00:27:02 So, I think… somebody has to propose it, and be, like, the champion, and then the… their teams, which would be, like, our SIGs, need to accept it, and… Probably not.
Some name on it.
In our case, could be a different thing, but I like the… the fact that there's… somebody that doesn't necessarily need to be somebody from the SIG that is saying, like, I want to do this, and then the project says… or the different SIG say, like, yes, I have resources to help you drive this, to, like, review your PRs, too.
Look at your design proposals.
Jack Berg 00:27:49 I like the artifact that comes out of this. It's something that's consumable for people interested in the project, it has names attached to it, it has you know, lists of projects where you can go read more details, a lot of good things, but, you know, Pablo, you have this PR open that was trying to do something simple, like adding the TC liaisons, or the TC sponsors to work streams that were missing.
And that's been open for a while. And that's just, like, the reality of how we operate. Like, doing things that requires consensus on issues and PRs, we're not good at that. It takes too long. And so I think if we want to do something in this project that channels the input from maintainers, it has to be sufficiently lightweight, or else it won't happen.
Alolita Sharma 00:28:32 Yeah, I agree with that.
Pablo Baeyens 00:28:34 Is there anything about this process that you think it's, like, too… too process heavy?
Jack Berg 00:28:40 the Rust thing, I think somebody would have to, like, actually take the onus to propose those projects, to make a description, to review those descriptions, to, like, you know, collect potential owners, and then to review and merge those things. So, I do think that that is process-heavy compared to something like a survey.
Pablo Baeyens 00:29:05 I guess my problem with this survey is that it does not necessarily reflect what we are going to work on, just what people would want us to work on.
Unfortunately, those are… those tend to be different things, I would say.
Jack Berg 00:29:23 I think the survey does actually channel what we are going to work on, because if you restrict it to maintainers, and they're the ones that are, you know, suggesting the ideas and voting on them, I think it's the closest we can get to, like, what will actually get done. Now, whether that's what end users want us to work on is, like, a different thing.
I don't think that that would actually channel what end users want us to work on, at least not very accurately.
Tigran Najaryan 00:29:47 We don't have a mechanism to force maintainers to work on something they don't want to work on.
Alolita Sharma 00:29:53 done.
Tigran Najaryan 00:29:53 Presumably. That's how it works today, right? So if maintainers think this is what they are going to work on, that's what happens.
they are not going to vote differently from that, right? They vote on what they think will be… they will be working on.
So, I don't see any kind of contradiction here. It's not like they are voting with one mindset and going and working on something else with a different mindset.
Alolita Sharma 00:30:21 Yep.
Pablo Baeyens 00:30:21 To put an example, I… I want to work in Collector 1.0, I think that's important. The project also wants to work on profiling, and so I have to dedicate some resources on, like, reviewing PR support and profiling support to the collector.
So, in some sense, the thing I want to work on is not the same as the thing that I end up working on, to some extent, because I end up dedicating resources for profiling. And I think profiling is a, like.
great project, I'm not, saying anything bad about it, it's just, like, there's… people come with things that they want to work on, and I end up investing resources on reviewing or supporting them, and it's not necessarily what I personally want to work on.
Jack Berg 00:31:02 But people act in their own self-interest, and while, like, I do things because I wear, like, a TC hat, or a maintainer of this hat.
that I don't think of as a priority for myself. It's my responsibility to go review, like, the work that somebody else proposes in the areas I'm a maintainer for. I'm disproportionately, like, indexed my time and effort towards the things I do care about.
And I think that that would be reflected in a vote, and I think, like, Pablo, like, you care about profiling, but maybe it's not your top priority. Your top priority might be Collector 1.0. I hope that that would be reflected in, like, how you voted in such a thing. And I hope that if enough people feel like you do, Pablo, that, you know, that would manifest in the, you know, the results showing that Collector. 1.0 is, like, is a high priority.
Pablo Baeyens 00:31:54 It is a high priority, for example, on the unplug thing. I don't see how that has… compared it into the thing that we're actually working on. Sorry, I'm, I don't know, I… I feel like the survey exercise is good. I just don't feel like it's a good predictor of what we will end up working on. But.
Alolita Sharma 00:32:15 Yeah, I mean, that's a fair point, Pablo, because, typically, I mean, in the large SIGs especially, maintainers do talk and, you know, figure out what's the most urgent Areas that are kind of burning priorities, and… figure out what they want to work on, right? But so there is discussion amongst the maintainers themselves on a SIG.
Are you saying that that doesn't necessarily help prioritize?
like, you said, you know, there were two competing priorities, and yes, totally understand Bond. And, profiling is a good example, but, You know, there could be 3 priorities that the maintainers decide on, then… And then kind of drive.
Pablo Baeyens 00:33:03 If water feels like this is something worth trying, I feel like it's worth trying. I just… Yeah, I'm skeptical about it, and I wanted to voice it, but it's not necessarily something that… I don't want to block this because of that. Maybe I do want to track that we actually end up doing what we built on.
Jack Berg 00:33:22 Yeah, it's definitely not perfect, but, like, what I'll say is that we've done roadmapping exercises in the past, and the roadmapping exercises have been, like, the GC and sometimes TC get together in a room and, like, write some things down on a piece of paper, then publish a blog post, and that's worse.
Yeah. Like, whatever down… whatever issues, and like… this type of process has, like, you know, just restricting the… it from the framing of the GC and TC, that's a more closed body, it's less representative of what people will actually be working on.
Alolita Sharma 00:33:57 Yeah.
Pablo Baeyens 00:34:01 I totally agree that it's an improvement with respect to that, yeah.
Alolita Sharma 00:34:05 Yep.
Austin Parker 00:34:06 One question… And I think this is… Just a thought, I guess.
Do we want to encourage SIGs to… Well, let me rephrase this.
I feel like we kind of go back and forth as a project on how much control, really. We want to seed to individual SIGs in terms of, like, roadmap and direction.
And it feels like what we're kind of talking around is the idea, perhaps, that the pendulum has gone too far towards centralization, where the GC and TC are… trying to set this overall project direction, and, you know, it's either not working, or people aren't happy with it, or something, and we want to move more towards let SIGs kind of control what they're gonna do.
I guess first question, is that… do you feel like that's an accurate characterization of the tension we're trying to solve here?
Jack Berg 00:35:22 The problem I'm trying to solve is that maintainers are load-bearing in the project, and they don't… there's not enough of them, and they don't get enough reward for the job that… and the responsibilities that they have.
And so, that's… that's it. I'm not trying to, like… I think, like, you know, the issue isn't about centralization, the issue is about, like.
Creating more of a reward structure for maintainers such that more people want to do it.
And, like, you know, if I can solve two problems at one time, the other problem being, like, hey, can we get roadmaps a little bit more representative of where the key players in the community are actually thinking are important? Then that's great, too. But that's, like, I think, like, secondary to the main thing I'm trying to solve, which is, like, more maintainers equals good.
Austin Parker 00:36:14 Okay, I, I mean, I… I think they are maybe more related than we're saying, though, right? Like… Obviously, nobody wants, you know, being… I don't think people feel great about the idea that, like.
oh, I now have a second job, or an unpaid job, or something where I get to go and do what other people tell me to do, versus I'm a maintainer, and I actually have control over what I'm doing.
Like… some of the reward structure we're talking about here is simply to give people more control. Is that… like, I'm not opposed to this, I'm just trying to… Accurately characterize the trade-offs.
Jack Berg 00:37:00 Yeah, I think give maintainers more control. Like, I'm in favor of that, on the whole. Like… the centralization, I think, is reaching breaking points.
you know, and I have some examples of that, like security advisories with the uptick because of LLMs. Like, you know, previously it was maybe okay for the TC to be sort of a backstop that was the primary, you know, you know, point of communication on all these advisories. It's just not working anymore. There's too many. The volume's too high. And so we need to delegate to maintainers more. We need to give them more of a seat at the table and channel Their, their feedback more.
Alolita Sharma 00:37:38 Agreed, agreed, and that will continue to grow. That is the backlog.
Austin Parker 00:37:42 Huh?
Alolita Sharma 00:37:43 That we are getting.
Austin Parker 00:37:44 Sure, yeah, and so just to, yeah, just to say, like, I'm in favor of giving maintainers more control.
And, like, making, like, letting… Take it.
I'm in favor of this, I think that we… I think the thing that would need to… I think the flip side of this is going to be that we, the people on this call, will have less ability to… like, the mechanisms that we will have to encourage certain outcomes will be more limited. It'll basically be what we can drive through either A the spec, or B, like.
more direct kind of initiatives. Things like donations, things like…
Jack Berg 00:38:37 projects, proposals.
Austin Parker 00:38:39 Project proposals, but also things like… Convincing other people to come into the project to work on things.
Right? Like, if we think something is a very big priority, then our answer, you know, instead of saying, oh, we need to convince maintainers that this is their biggest priority, it might wind up being, we need to go… Convince other people to come in and make it their biggest priority.
Which is not, you know, again, no moral judgment, or there's not a moral valence, it is just a difference.
Jack Berg 00:39:12 I think that's not really documented right now, that the GC has that sort of, responsibility to, like.
or privilege to go and state what the project priorities are? Is that the case? Like, we talk a lot about soft power, soft influence. That's always the way that we've had to work.
Alolita Sharma 00:39:34 Yeah.
Jack Berg 00:39:34 It's getting a little bit softer when the GC isn't the ones publishing a blog post with the project priorities.
Austin Parker 00:39:47 I… go, but I just… I think that there's maybe one of… maybe that's a thing where it's like.
the way… work as it is versus work as it ought to be. I think the GC… I think, like, if Ted was here, he would probably… have a stronger statement around, like, the role of the GC in setting project priorities.
Alolita Sharma 00:40:09 I think, I think, Jack, sorry, Jurassi, I just wanted to conclude one sentence, then please go ahead. Jack, to the point that Austin is making, again, you know, in a… maybe an unwritten way, what the GC has kind of tried to do is shepherd the roadmap and the project, Feature priority, if you will, based on the community proposals, as well as other input that is published, right, on the project.
But… and the TC is kind of the technical experts, you know, who have shepherded, you know, that process also in, you know, kind of an good faith way. But I think that, to your point, I think you're calling out that, hey, you know, how do we communicate that to maintainers? How do they be part of that process?
How do they also feel?
Incentivized to be part of that larger… discussion. Is that… is that also one of the goals you're trying to achieve?
Jack Berg 00:41:14 I think that ends up being a repercussion of it, and to be fair to Austin and this point in general, so I'm about to share a link in the chat, and it is, it is part of the GC's charter to find the roadmap, so…
Alolita Sharma 00:41:27 Right, right.
Jack Berg 00:41:28 It's officially… I was saying that it was, like, implicit, it's not implicit, it is explicit. So this is, like, a softening of that.
Alolita Sharma 00:41:37 Yeah, yeah, okay.
Juraci Paixão Kröhling 00:41:38 I mean, that…
Alolita Sharma 00:41:39 Everybody's good.
Juraci Paixão Kröhling 00:41:40 That part of the… yeah, that part of the charter might be… reminiscent of the bootstrapping of the GC, so perhaps it is not accurate anymore, and if we think it should not be GC, then we can definitely remove that.
But, my… I had something else in mind, actually, so… Jack, you, you raised… a point back then, like, 10 minutes ago or so.
on the incentives for maintainers, why they… what are they doing?
Or what… what are… What is there for them to gain from the contributions and so on?
Do we know that? I mean, do we have… do we know what moves them?
I have a couple of stories, but most of them are… People are being paid by their employers to work on something, and they work on whatever their employers tell them to do, not what the GC tells, or not what the projects priorities are. Like, people are moved from SIGs, from one to another, because the company decided to move them, not because they are moving.
I have a feeling that we can talk a lot about creating incentives to the maintainers and to developers or contributors in general, but if their employers tell them to do something else, they're just going to do something else.
Is the survey that you want to do, that you want to create, covering that part, or is it covering what they think they should be doing?
Jack Berg 00:43:06 So I agree with you. I don't think we have firm data on this, and probably maintainers are motivated by different things, and we just have anecdotes. Like, what I… what my anecdotes tell me is, like, maintainer burnout.
And so, like.
you know, and you hit it at the nail on the head. Most maintainers in a project like this, like, are employed by somebody, and that employer is essentially sponsoring them to go do work that is, like, somewhat aligned with what that employer wants, and maybe somewhat aligned with the community.
And, you know, I want to find a reason for employers to sponsor more maintainers.
And so, like, if you have an answer for that, a suggestion for that, on, like, what might incentivize an employer to sponsor a maintainer, like, that would be great. I want to hear that, and I want to do that.
Juraci Paixão Kröhling 00:43:58 Yeah, I think we kind of touched on that on the last time that we discussed it, and I think there are a few things that we can be doing to make it more enticing for companies. Like, why do they care? They care about having badges to show at KubeCons that they are contributors to open telemetry. We know that they care about that part.
Like, I…
Morgan McLean 00:44:20 I care a little bit about that dress. I don't think that's the main motivation.
Alolita Sharma 00:44:23 Yes, I…
Juraci Paixão Kröhling 00:44:24 It's not. It's not, but if… I think, if we have ways of recognizing those contributions, if we have ways of saying.
Like, those companies, they really are the hotel friends. Like, things like that. Like, if that's what makes companies move, then I think that's where we should be going. And the point is more general, that it might not be… As hard as it is to say this, but it might not be to please the maintainers, it might be to work with the people paying them to work on the project.
And, and one way to soften The focus on vendors is, how about we can have we focus a little bit more… we usually see, perhaps, on attracting, making a hotel more… more enticing to end users. Like, let's talk to the Bloombergs, let's talk to the Ebays, and so on. Like, what would make them invest?
In employing people to work in a hotel.
like Adobe, and so on and so forth.
Right, so let's make their work also more… recognized. Often, they are the end users working on the projects, they are working on the problems that they have on a daily basis. They have an interest in working on that.
I think that could be one way of… to go there. Not necessarily… Of course, recognizing maintainers.
But, if they move, if the companies tell them to move, then… Let's have a different focus, perhaps.
Jack Berg 00:45:51 If we're going to care about these end users, these large end users, I want it to be about, like, how can we encourage them to become maintainers? So what would they want in a maintainer role, like, besides the responsibilities of maintainer? Like, what privileges would help incentivize that? So, ideas open. I have this, like, you know, this pet, you know, proposal of mine, but, you know, I want to do something as, like, a starting point, and I don't think.
Morgan McLean 00:46:17 Are there…
Jack Berg 00:46:18 thing. Go ahead, Marty.
Morgan McLean 00:46:19 Are there any open source projects that have successfully done that?
Like, I'm asking legitimately, I don't think.
Alolita Sharma 00:46:26 What?
Morgan McLean 00:46:26 I think the answer's no, but I don't know enough.
Alolita Sharma 00:46:27 What's your question there, Mark?
Morgan McLean 00:46:29 Are there any examples of open source projects where end users have been, like, contributing a lot back.
Alolita Sharma 00:46:35 Yes, Cortex. Cortex is completely… has maintainers with end users, from end users. I mean, and that includes us as Apple also.
Morgan McLean 00:46:46 I want to look at what they do. Yeah, okay, great. That's encouraging.
Juraci Paixão Kröhling 00:46:50 Yeah, I mean, Prometheus was born out of end users solving their own issues, right?
But, I think what… I have a pet project as well, and that is, a few years ago, I proposed having a stable seat at the GC for end users. I don't think that's a solution, but if we want more end user involvement, I think we have to hear more of their voices as well, and invite them to the table, not only making theories about them. But, that said.
That's all that I have to say.
Liudmila Molkova 00:47:22 Yeah, I think that… Vote in the roadmap is something that should incentivize at least some of the employers, because the common concerns is that vendors want to move certain features forward, and through their employees who are maintainers, they will have more control over project roadmap and schedule.
Because currently, you can invest a lot in open telemetry, but it will not… nothing is guaranteed to happen. And of course, it will not be a guarantee that… but it will introduce more bias into the process.
Austin Parker 00:48:01 I do want to point out that the things that we have just said are in opposition to Jack's point, because… If we say, oh, the way we think we can help maintain… prevent maintainer burnout, and to encourage people to maintainers, to give maintainers more control, that is in opposition to… big end users get a seat at the table to determine the roadmap, right? Like, this is the core tension. We… We are not… Yeah, the th… So… to, like, Jurassi's point of, like, oh, well, we just need to give end users… we need to go give end users to see the table, we need to go to Adobe and say, like, what do you need, Adobe? And Adobe comes back and gives us a laundry list of things that span 14 different sigs.
like… That is in opposition to, hey, maintainers get to set their roadmap, and it is inviolate, right?
Like, if we are going to…
Jack Berg 00:49:05 I heard… I heard Jirassi's proposal was something different. I heard Jirassi's proposal as if, like, hey, you're an end user, you want to influence what this project does. The way that you achieve that influence is by you know, engaging the project as, like, a maintainer, such that, you know, you now are participating in it, and thus you can influence the project's direction through these mechanisms.
Austin Parker 00:49:26 Yes.
Jack Berg 00:49:27 increased version was a GC slot.
Austin Parker 00:49:30 But, but the point is, is that… when you're not… because we're talking about two different things. Influencing the project and influencing the SIG are two different things.
Alolita Sharma 00:49:39 Yeah.
Austin Parker 00:49:40 The place that you could influence the project is by having someone on the TC, or having a spec maintainer, right? Like, if you really want to make wide project changes, the places to do that is not by becoming a collector maintainer.
Jack Berg 00:49:55 It can be if, if we have this voting process, and collector maintainers can express what they want to see at the project level. That's like elevating individual SIG maintainers to be able to have influence outside of that individual SIG.
Austin Parker 00:50:09 Right, and that… Kind of gets us back to the point of… you know, Tegrin's point earlier of… What, you know, Like, yes, some maintainers might be really interested in… you know, cross-seigs up, but some might not. Like, what… why should the JavaSig get a vote on what the collector does?
That's all you said.
Jack Berg 00:50:39 This is just not… it's just a… it's just a way to express what people think is valuable.
Austin Parker 00:50:44 So, I just want to throw out another idea here, which is that One other thing that we, you know, another way to think about this is that if the problem… if a problem is that maintainers don't feel… like, if it feels… like, one thing I've heard from maintainers, some maintainers at Honeycomb at least, is they get very discouraged because they've been working in the pro… you know, they've been in JavaScript or Collector or whatever.
And some of them are very happy just doing what they're doing, but some of them would like to have more project-wide influence, to your point. Like, they feel like, like, oh, I've been a maintainer or whatever in this SIG for quite some time, and I am… there's a ceiling, right? Like, there's nothing above that.
There's nothing above… been a JS maintainer for 4 years, or whatever. So one other… one thing that we could consider is, like, okay.
like, what is that next step? What is the next step on the ladder for maintainers? Because right now, it's effectively, like, we've said a lot of things over the past, like, spec maintainer, or, like, ShadowTC, or whatever, but, like, maybe the answer really is to say, like, okay.
what if the TC is just, like, all of the, you know, senior maintainers from every SIG? And then it's kind of like… and then they're the ones that's at the roadmap. And so if you want influence, you want to… have control over what the project does. You become a senior maintainer, and now you are part of the group that makes those sort of, like.
Being project-wide calls.
Jack Berg 00:52:25 Again, you can't make the call because it's not top-down.
Like, all your…
Austin Parker 00:52:30 But it wouldn't be top-down, it would be…
Jack Berg 00:52:32 maintainers actually want to work on. Like, I want…
Austin Parker 00:52:35 But I'm…
Jack Berg 00:52:37 Okay.
Austin Parker 00:52:38 That's what I'm saying, we make that decision be made of a group of maintainers from each SIG.
That when you are a senior maintainer, you are now at this level where you are making those project-wide calls.
Jack Berg 00:52:50 So you want to differentiate between maintainer and senior maintainer, and then, like, say senior maintainers have, like, the ability to vote on project priorities?
Austin Parker 00:52:59 Sure.
Jack Berg 00:53:00 Okay.
Austin Parker 00:53:02 I mean, it's like a, you know, it's like, it gives you another rung in the ladder, it gives you something to work towards.
I would like to think that… People that have been a maintainer for 4 or 5 years or whatever are probably, you know.
Have that level of, like, cross-project, Insight that they would be good at, you know, evaluating the trade-offs or whatever.
Anyway, I've talked a bunch, And I'm not saying, like, we have to do it my way, I'm saying, you know, here is an idea, rightly.
Reiley 00:53:36 Yeah, I have a clarification question. What's the goal? I can imagine it's either one of the following, or maybe a combination of some of them. It could be, like, we want to, like, let the maintainers feel they're more value, so, like, a lot of maintainers are struggling. They worry about, hey.
Like, why am I still, like, doing all this work? Maybe I should step down, or my employers are not giving me enough support. Like, I have the paid job, I probably need to step down. So that's one worry. Another worry is we're seeing some sick, like sick security.
We don't even have… I'm the only maintainer there. I want to, like, recruit more maintainers, but people always say, like, right, as long as you hold the security bar for us, we're fine. Like, we'd rather see you doing the heavy lifting work, so that could be one thing.
The other thing could be, we have a lot of people who want to be maintainers, but they don't even feel there's enough reason for them to get support from their employer, so there could be many of this. What are we trying to do? Maybe, like, if you look at the SIGs, some of the SIGs will say.
like, we're overstaffed, we have… we have too many maintainers, we just want to have less maintainers, because the decision-making, all the things become, like, super inefficient. So… so do we… do we really understand what's the problem, and… And if we want to solve the current problem for the existing maintainers, we probably can do some, like, informal survey, asking the maintainers, hey, like, what's the reason you become a maintainer, and do you see any potential problem, like, within a year, you might step down from the maintainer? If the answer is yes, then what can we do to keep you as a maintainer? And what can we do to encourage You to stay as a maintainer for a longer time.
Or if it's about, do we want to encourage more people who are not maintainers to become maintainers, then we can do a survey asking for people, like, if you're the aspirational maintainer, you want to become a maintainer, then what's the barrier that's preventing you from becoming a maintainer? It could be your employer told you.
I don't need you to be a maintainer, it's just additional work. Like, I'm happy if you just be a approver or something. If that's the case, we can see, like, how to fix the problem. I feel like the conversation here at least I don't understand what's the problem we're trying to solve.
Jack Berg 00:55:50 So, the contributor experience SIG has probably… you know, has survey results that somewhat answer those questions. Maybe not directly, but maybe there's insights in those results that we can go back on to, you know, help identify the problems with more data, rather than just, like, you know, anecdotes that we all hold in our heads.
And yeah, I don't know what those would show.
Reiley 00:56:16 Yeah, one fake question might be, like, we ask the maintainers, if there's anything we can do to put something shiny on your resume, then I would assume all the maintainers would say, yeah, let's do it. But once they do it.
What… what the community would get.
The existing maintainers will feel happier, and people who are not maintainer, they might have more motivation to become maintainer.
if that's, like… if that's the problem we want to solve, then we have an answer, but I'm not sure if that's the problem we want to solve.
Okay, I'm, I'm done, huh?
Marylia Gutierrez 00:56:57 I want to reply later with the contributor experience question. So, we do put surveys from time to time, but we do have an issue that we don't have a lot of people that reply, so we try to actually… okay, interviewing people to actually understand their experience, like, what they want to do, how they want to, like, grow in their career and stuff like that. But what ended up happening was a lot of them that understood, like.
oh, I'm here because you're gonna teach me how to contribute. So, like, half of the calls were, like.
Not helpful, because they thought that we were doing, like, a workshop on how to be a contributor, which was not the case.
But yeah, we are… we work on stuff to help the contributor experience, but the only people that actually reply to us are very people that, like, I want to start, not the actual maintainers and stuff like that, so it's hard to get their perspective as well.
Jack Berg 00:57:51 So, no good data for maintainers, and, like.
Marylia Gutierrez 00:57:53 For maintainer of that.
Jack Berg 00:57:54 And the class of contributors that we'd be interested in encouraging more of here.
Pablo Baeyens 00:57:58 I think for maintainers, the best data we have is the one I just linked, the big survey we did of intruder experience, but we don't have anything that is very… Specific clips.
Alolita Sharma 00:58:13 I think one way to get better… sorry, Jurassi, if I can just… add to what Marillia was saying. One way, again, Marillia, to get more specific, you know, all maintainers to provide for your feedback, or most maintainers to provide feedback on these surveys could be that the GC sponsors could actually work with them to get them to do the… respond to the survey, like, handhold that process.
Go ahead, Jurassi.
Juraci Paixão Kröhling 00:58:47 So I think I'll go back to Jack's main point, like, I'm not quite sure yet if we… that we understand the motivations of those people.
So I'd like to ask, like.
Y's and whys until we get to the main… to the main… Thread, like, the main problem that… that… That we are trying to get people to contribute more, like… Why do they contribute, and what are their incentives?
I think, as GC, and as the leadership of the project, so GCGC here.
What I would suggest as a concrete action item is you see people go there and talk to the people that you're a liaison for.
And ask them, no need for a survey. Like, try to get from them why do they care.
Why are they here? What motivates them?
those are only stories that… that's not a full survey, but I think that helps already whenever we have the next discussion on this topic, so that we have stories also to tell.
And then we stop guessing things.
Would that help, Jack?
Carlos Alberto Cortez 00:59:53 We haven't talked away.
Jack Berg 00:59:55 We're at the time.
Carlos Alberto Cortez 00:59:56 that Sean Marciniak also mentioned that in the issue that Jack created, that we should go and talk to vendors directly, try to get some ideas, and that's a good starting point.
Jack Berg 01:00:09 Alright, let's continue this conversation asynchronously.
That was good.
Alolita Sharma 01:00:14 Thank you, yeah.
Armin (Dynatrace) 01:00:15 Bye. Bye.
Alolita Sharma 01:00:16 Bye, everyone.
