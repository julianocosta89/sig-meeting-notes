SIG: End-User SIG (APAC)
Date: 2026-07-29
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Andrej Kiripolsky** 00:33 Hello, Joe.
**Joe Josue** 00:39 Hi there, hi there.
**Andrej Kiripolsky** 00:50 How are you doing? How is everything?
**Joe Josue** 00:53 I'm good, I'm good. I'm very new to all this, but I'm joining some of the hotel calls just to learn everything I can about telemetry, so I'm just mostly an observer, to be honest.
**Andrej Kiripolsky** 01:08 That's totally fine, that's totally fine, feel free to just… Hang out and watch, and if you have any questions, happy to, happy to answer.
**Joe Josue** 01:16 Appreciate it, thank you.
**Andrej Kiripolsky** 01:18 Where are you based, if I can ask?
**Joe Josue** 01:20 Manila, Philippines.
**Andrej Kiripolsky** 01:22 Philippines. Nice.
**Joe Josue** 01:24 Yeah, yeah.
Are you the lead of the special interest group, or… Sorry, I'm kind of getting familiar left from there.
**Andrej Kiripolsky** 01:35 Yeah, yeah, yeah, I'm a maintainer of Special Interest Group End-User.
And I lead these APEC meetings. I'm based in Europe, in the Czech Republic.
And yeah, but I still have pretty good overlap with APEC, because other.
**Joe Josue** 01:49 Oops.
**Andrej Kiripolsky** 01:50 or… like, somewhere in the… in the North America and stuff, so yeah, their overlap is not.
**Joe Josue** 01:56 Definitely tougher, definitely tougher, for sure.
**Andrej Kiripolsky** 02:00 Yeah, yeah, yeah.
Yeah, so we just kicked this off a couple of… like, 2 months ago, I think, or roughly? Still figuring things out, so… Yeah.
**Joe Josue** 02:10 Is this the end-user one, or just kind of, like, all these community calls is 2 months, or 2 months old?
**Andrej Kiripolsky** 02:15 So, just this particular APEC-specific end-user.
**Joe Josue** 02:20 Oh.
**Andrej Kiripolsky** 02:21 Because other calls are happening for years, I believe. Yeah, I don't know exactly. I started contributing only, like, one and a half year ago.
But I'm pretty sure that… that… so with End-User SIG, I think it's, like, 2 or 3 years, something like that. That one is rather new, but I'm pretty sure that the, like, the… the big ones, like Collector or… or semantic conventions, are around for… for more years.
**Joe Josue** 02:52 Oh, wow.
**Andrej Kiripolsky** 02:53 Yeah.
**Joe Josue** 02:54 I sat in a couple of the semantic con… actually, the last three this week of the semantic conventions, and definitely technically beyond my ability, but it was cool to… Just listen to… kind of like the standards being designed for, I think, 2.0, and then Weaver.
I'm just like, oh, okay, so this is how this stuff happens.
Just like this is how this stuff gets done.
**Andrej Kiripolsky** 03:16 Yeah, yeah, definitely, definitely. It's interesting to join these kind of calls, I think.
Hi, Victoria.
**Victoria Nduka** 03:23 Hi, Andre. Hi, Drew.
**Joe Josue** 03:25 Hello, hello.
**Victoria Nduka** 03:26 Hmm.
Welcome.
**Andrej Kiripolsky** 03:32 So… Have you contributed, Joe, to any other open source project, or this is your first time, like, figuring out.
**Joe Josue** 03:39 Yeah, yeah, I'm not even a… I mean, I took IT 15 years ago, minor in databasing, but I've mostly been kind of like an entrepreneur, so… but I'm very blessed to have my own companies have a couple of exits. I've worked with amazing CPOs.
But, kind of, like, obviously, this… all of this… Agentic stuff has really unlocked on my, you know, I'm completely pilled.
And so one of the things… so I've pseudo… Become kind of like a… I basically have FD'd my own companies now, and all my friends' companies, and so one of my major problems, as I found, is the… So I'm just sharing at this point. Instead of telemetry, meaning that There seems to be a lot of telemetry solutions. I mean, something like this, obviously, obviously telemetry exists, and it's so, so advanced beyond me.
But I was… I've been trying to figure out ways to convert it into business language, like, you know, like, as I talk to CEOs and founders and my own, and the gap I've challenged myself, also, and my companies have deployed to.
Is kind of, translating the telemetry implementation into something a CEO can understand.
And even for myself, like, how… when is an agent actually productive in… in terms of, like, comparable to label. And so that's what I'm trying to figure out. So I'm just going to be doing all the angles I can, and obviously trying to understand telemetry.
At the base level, it's me being in all these calls.
**Andrej Kiripolsky** 05:08 That's awesome. I mean, like, that's a super interesting, problem to be solving, and I think that you're… you are in the right place here, because, like, there are so.
**Joe Josue** 05:16 Too many people.
**Andrej Kiripolsky** 05:17 In this, in this comu… Maybe, no.
this is a good introductory call, but I mean, like, in general, in OpenTelemetry community, there are a lot of people who are really thought leaders about, how telemetry should work, and have deep, deep expertise, so I'm sure that you will find a lot of interesting stuff.
**Joe Josue** 05:37 Appreciate it, thank you, thank you.
**Andrej Kiripolsky** 05:39 Ernest.
**Ernest Tolulope Owojori** 05:43 Hi, hi. Long time.
**Andrej Kiripolsky** 05:46 Yeah, good to see you. It's been a while.
**Ernest Tolulope Owojori** 05:48 Yeah.
I just wanted to see how DAPAC go.
Growth, you know.
**Andrej Kiripolsky** 05:58 Yeah.
**Ernest Tolulope Owojori** 05:59 And also preparing myself to join tomorrow's call.
**Andrej Kiripolsky** 06:02 No, that's good, that's good.
**Ernest Tolulope Owojori** 06:06 Yeah.
**Andrej Kiripolsky** 06:07 So, we realized, but… Sorry, go ahead, Etheria.
**Victoria Nduka** 06:12 Oh, sorry.
the… Your… your full government's name is showing.
So this is the first time I'm seeing your middle name.
**Ernest Tolulope Owojori** 06:22 Yeah, he was asking me to sign up for a jam, like, I'm already late, just join as a guest.
**Victoria Nduka** 06:32 Nice.
**Ernest Tolulope Owojori** 06:35 Andre, you wanted to say something earlier?
**Andrej Kiripolsky** 06:39 Oh, yeah. So, since we started the APAC calls, we realized that they are, like, slightly cannibalizing our… our main call, because, like, some people join the APAC, but they don't then join the main one. Joe, for you, just, just, context.
the… we have, like, regular call happening in, like, more North America-friendly time zone.
**Joe Josue** 07:00 And, it's tomorrow, so it's Thursdays.
**Andrej Kiripolsky** 07:05 late at night for, even for me, it's late at night, so, like, for you, it should be, like, totally, like, 1AM or something.
**Joe Josue** 07:14 I was planning to join as well, I'm just trying to join everything I can this week to just absorb.
Nice. What is sleep in the global world?
**Andrej Kiripolsky** 07:29 Yeah, by the way, we usually take some time at the beginning to just chat and wait until people join. It sometimes takes time for everyone to come, but I think we can slowly get started.
And since we have Joe in the meeting, we can do a quick round of intros. I will start. My name is Andrej Kiripolsky, I am based in the Czech Republic, I am a SIG End-User Maintainer, and I, lead these APEC calls.
And yeah, and my day job is… at Grafana Labs, where I'm a user researcher, so I talk to people about how they use telemetry.
I… am not that technical.
so I'm not the right person to ask, like, how do you set up, I don't know, Kubernetes, hotel daemon set and stuff? Not the kind of question for me, but I… yeah, I can direct you to who would be the right person to ask.
And yeah, I started contributing about a year ago, and what else?
I think it might be about… About it, about me. I have two kids, I have a dog.
I should clean up a bit, because it's… yeah, I was not cleaning up for a while recently. Anyway, victoria, Ernest, who of you want to go next?
**Victoria Nduka** 08:54 So, hi, Joe. Hi, everyone. I'm Victoria Nduka. I am based in… In Lagos, Nigeria.
I… used to be a UX designer.
But I recently transitioned last year to… To the cloud-native space.
So now I work as a tech support intern at Victorian Matrix.
I began contributing to the hotel last year, at about the same time Andre joined the community.
And… now I am an approver for the SIG End-User.
So… yeah, that's it about me.
Ernest…
**Ernest Tolulope Owojori** 09:39 What happens to your day job?
**Victoria Nduka** 09:43 No, I already said that.
**Ernest Tolulope Owojori** 09:47 Okay, I'm in a…
**Victoria Nduka** 09:49 different.
**Ernest Tolulope Owojori** 09:50 Nice to meet you, Joe.
I joined the community late last year with the Lenov Foundation Mentorship, where I design the analysis guide that we expect people to use so that we can have consistent, analytical methods and results. But beyond the hotel, like Andre, I'm not technical in the cloud Nduka space because I have a data background.
And, Data Bargunda also brought me to portal management, which generally I'm not interested in anything, either portal data, that allow me to To use that behavioral research within a digital product.
You know, and some aspect of my poor management is also doing… the BA work, that is guiding requirement, you know. I'm just like that, but there's a thin story to it, which is just trying to understand user behavior changes and all.
Yeah, that's pretty much it. I am married as well, and I'm currently based in Venos in Lithuania. I recently moved here, actually. I used to be based in Nigeria.
And, yeah.
I don't know if to say I'm jobless, because I was not before, but now that I relocated, I'm just looking around. What's new, what can I find?
Yeah, that is it.
**Joe Josue** 11:12 That's awesome so I guess for me, I'm not sure when… Everyone else jumped in. I'll start with Andrej. So, my name's Joe.
I'm based in Manila, I'm married, I have two wonderful daughters, you can see they took over my study. It's very… you can see my background, it's, like, cute paintings in a mini nursery now. And yeah, so I… quick background, I don't… I also don't technically have a day job. I had a couple of humble exits in 2022 and 2023 on my own, kind of, like, frontier tech companies.
I specialize in, kind of, zero to one, so the past 2 years since my my exits, I've mostly been consulting and advisory and doing zero-to-one work with my friends who are founders, private equity who needs to build new departments, so I'm really kind of, like, really into Anything that doesn't exist to making a ton of, like, revenue-generating our business unit, or a department.
Very gusts to be able to kind of, like.
be able to do or build things I kind of like.
And, obviously, I'm here, like I mentioned to Andrej and everything I heard, I… I run now, my consulting has turned into, like, a solo advisory firm, and a lot of it is deploying agents into my own companies, into friends' companies, and the major bottleneck that I've found is, I'm not familiar with telemetry at all, and observability is completely new to me in the past month. I've been reading everything I can, so I found OpenTelemetry, this community, I saw that the calls, they said to join everything, so I committed to joining every call I can this week.
And it's mostly because I… need to translate it for myself into business language. Like, we can install this stuff, but it just doesn't speak.
Bye.
the language that a CEO or a founder or an HR operator might… do for, like, what does an agent do in a company, and so I'm solving for myself.
And so, I'm not a dev, very little technical background, but I'm just learning everything I can for… About it at every level.
**Andrej Kiripolsky** 13:17 Awesome, thank you so much. Thank you all for intros. Quick… a couple of quick, comments about End-User sake. So, what we do is that we help folks get the end-user feedback. Help the other SIG who are focusing on, like, either technical things, or communication, or other stuff. We are helping them get end-user feedback. So we help them collect data through surveys.
We help them run interviews with end users, we run them as live streams. And, also, the last thing, that actually might be, might be interesting for you, Joe, is, that my colleague Dan is leading an effort called Blueprints, and it's about documenting reference architectures and architecture blueprints for OpenTelemetry, about… basically, the idea is how you are supposed to set up OpenTelemetry. What is the best practice?
**Joe Josue** 14:18 So what.
**Andrej Kiripolsky** 14:18 how the hotel should connect with database, how should it work in a Kubernetes environment, and so on. And, as I said, there are two things there.
Blueprint is, like, the general architecture. Reference architecture is specific stuff about, like, what tools do people use and how do they connect them together. So that might be an interesting thing, when you actually want to, like, get this, like, high-level understanding of how things fit,
**Joe Josue** 14:47 That's wonderful.
Is it also part of, like, the scheduled calls within the hotel, or is it separate? Okay, so I'll just look for…
**Andrej Kiripolsky** 14:55 Bread one.
**Joe Josue** 14:55 Thank you.
**Andrej Kiripolsky** 14:56 It's a separate one, this one happens on Mondays, I think every other Monday… I think one will happen just… Yeah, just give me a second… Hmm… Yeah, I guess last week? I don't know.
**Joe Josue** 15:13 Thank you.
**Andrej Kiripolsky** 15:13 August 17th should be… should be the next one.
**Ernest Tolulope Owojori** 15:15 No, no, no. Yeah.
According to my calendar, I can see an August 3 meeting.
I think they do it every week.
**Andrej Kiripolsky** 15:24 Okay, then I probably just removed it from my calendar, or, like, I copied one, I copied.
**Ernest Tolulope Owojori** 15:30 Easy, same.
call. I think he should be seeing it if he checks through his calendar.
I think it's the same, like, it is this same meeting URL.
And, I got automatically signed up for it, just being in the End-User Sea Calendar. So, Evie is already on this call, you should see it. You can check your.
**Joe Josue** 15:50 Okay.
**Ernest Tolulope Owojori** 15:51 Thank you, thank you.
**Joe Josue** 15:52 Go check it out. I'll find the blueprint.
**Andrej Kiripolsky** 15:55 Yeah, yeah. And, yeah, that's about it. And, yeah, this week we don't have a whole lot of attendees, because there is KubeCon Japan happening, and that's, that's somewhere… that's, like, a big event where a lot of folks who join, APEC Meetings went.
Yeah, what we can do today is just to go through our issues real quick, and, yeah, if anyone has updates, then I think then we can… we can wrap up. So, in the agenda, I have… I have two updates.
The first one is… so I have two issues that I was supposed to be working on, but I'm working on some… I have some Corfana Labs stuff, that I was super busy with in the last couple weeks, so I did not progress on… on the… on my issues. I had… we had one survey that's still open. Doof did, that's… So, yeah, Drew did analysis.
Or the first draft of analysis, that was super helpful, but it's waiting for review. So, in case any one of you folks would have free time and would like to check the… check the… Analysts and give him feedback, that's to be very welcome, but… up to you. I will… I hope I will get to it perhaps next week, but yeah, probably not… not anytime soon.
Also, this could… time-wise, it could be good, because Arthur should be back from KubeCon Japan, or at least from Japan. I actually don't know if he goes to KubeCon, so next week, we should start talking about how we present the findings from the survey. And yeah, and I want to ask Yoshi about the Japanese issues that we have opened, but yeah, he's not here, so that's about it. Druf is not here today, so I will ask him, probably, maybe he will join tomorrow's meeting, because he requested a sponsor for For his blog post.
And, yeah.
By the way, where I'm reading these things from, let me show my screen real quick.
We have… So we have an agenda doc that's important, where we try to make notes, so we have all our… all our meetings have notes here. Here are the blueprint notes, and here are the APAC notes that… that we have for today.
And, we also have the… See End-User Board.
And, Yeah, there are issues we have, but I don't think anyone from these folks is on the call except for me, so I guess there… yeah, there will be no updates there.
Victoria, Ernest, do you have anything to share? Not necessarily related to… or, like, primarily related to End-User SIG, but maybe not… It's always… Okay, as well.
**Victoria Nduka** 18:58 I can't… I can't think of anything that I have to share.
**Andrej Kiripolsky** 19:01 Okay, that's fine.
**Ernest Tolulope Owojori** 19:04 I was just going to ask a question on the inside of the Japanese survey we ran.
Are you aware if anyone is trying to… consider the Twitter, or no, you know.
one of the most important things right there was, at least that we think we can follow up in terms of action is, if we want to get Japanese on to engage them online. It's either we find a way to reach them on X, which is formerly Twitter, or we create some other channels that are they actually use.
So I don't know, how can we follow up with that?
needed action. Maybe the government committee, or I don't know.
**Andrej Kiripolsky** 19:52 Yeah, yeah, yeah.
**Ernest Tolulope Owojori** 19:52 Fantastic.
**Andrej Kiripolsky** 19:52 So, regarding X, I'm pretty sure that you saw that there are no plans to open or reopen the X account.
The main reason is that The X is a closed platform, so we… where you… to be able to respond, and to, like, go through the comments, you have to register, and that we do not… do not support that, so we… we stick with… with LinkedIn, Blue Sky, and Masterland.
Having said that, Yes, I… regarding, like, opening other accounts.
on, like, maybe, like, Japanese-specific media, I don't think we progressed with that. But that would be a good question, maybe for next time, where Yoshi is here, or anyone else from Japan, and… because I think, like, the main issue there is that If it's, like, Japanese-specific, we would… I have to… Yeah, like, we might need, like, Japanese translations.
And then there have to be basically a person who takes care of that, because we cannot do it, the way how we do the rest of the socials.
But, yeah, let's maybe bring it to the next meeting and ask Yoshi once he's back.
And regarding, like, other next steps from that survey, I'm not aware, actually, if there are any, but we discussed with Yoshi that we would like to run another round of Epic survey, of Japanese survey. My idea, or, like, the one thing that I would love to do is maybe to extend it.
To other countries as well.
Because the questions are mostly… inter… like, like, reusable for other countries, they are not Japanese-specific… Japan-specific.
So we could just reuse them and open it to… Maybe, like, the whole region of APEC, maybe just a couple more countries to figure out if it makes sense, but let's see. But one thing that… I think Dhruv already also volunteered to work on that survey, but I would love to do it again at the same time, so that means December this year, or November, December, so… We can start preparing for that, but I don't think it makes sense to run it earlier.
**Ernest Tolulope Owojori** 22:10 No problem, I think I agree with that.
**Andrej Kiripolsky** 22:13 Yeah, we have a bunch of other open issues, so if anyone wants to… wants to pick them up, that's… I'm more than welcome, but no pressure. And yeah, I guess that's… that's it about the triage.
And now I will figure out how to… Am I still sharing my screen, or did I stop?
**Joe Josue** 22:34 No more.
**Ernest Tolulope Owojori** 22:35 You stopped.
**Andrej Kiripolsky** 22:36 Okay.
Okay, okay. Cool. So, that's about it.
I mentioned this, I mentioned this, that's just like a… topic for chat, but we can skip it for today. Specifically, I want to talk to Drew about this.
So, yeah.
Folks, this was a quick one. We don't have that much attendance, we don't have folks who picked up issues, so… There's not much to chat about. Does anyone have any other topics, or any general questions about hotel?
**Joe Josue** 23:07 Can I have a explain, like, on 5 question?
**Andrej Kiripolsky** 23:10 Of course, definitely.
**Joe Josue** 23:11 These surveys for end users. So this SIG works on end-user surveys to understand Is it… by End-Us, is there a particular profile? Are these developers who apply Hotel into their apps and products?
Is that generally what that means? Sorry, it's very basic, but… Okay, okay, so it's all… of the open standard. Okay.
**Andrej Kiripolsky** 23:36 Yeah, so it's all the people who use OTL, for whatever reasons. These can be the developers who are instrumenting their applications, these are usually SREs or DevOps engineers who, like, operate the systems, and who mostly are the ones who are looking at the telemetry, and And anyone else, what is the point there is that we don't want to live in a co-chamber where just, like, maintainers give feedback to maintainers.
a lot of maintainers from… from, hotel, or, like, a lot of contributors to hotel, are vendor employees, just to say.
**Joe Josue** 24:12 I am.
**Andrej Kiripolsky** 24:13 And we have a bit different perspective on things. Like, when… if you work on telemetry stuff all day long.
you see it differently than when it's just, like, that small part of your responsibilities, so we want to make sure that we get the end-user perspective and feedback in, and Yeah, so that's, that's kind of the reason.
**Joe Josue** 24:37 Okay, and then, so we mostly oper… SIGL mostly operates by… outreach and kind of, like, mapping out where users might be… it sounds like by territory or country.
Good question?
Getting them involved to… or if they're a user, locate them, get a survey so we get a great sample intel on end-user use of hotel. Is that it?
**Andrej Kiripolsky** 25:01 So… so most of the time, actually, we don't focus on any specific location. We just run, like, a general survey and, like, hope that somebody responds. The Japanese survey that Ernest was mentioning was the first one that was, like, location-specific. The goal there was that, for some reason, I actually don't know why, our… One of the founders, I believe, of hotel, and lead of… SIG communications.
came with this idea that we would like to promote hotel more on Japanese market.
there's… there's perhaps some… that's my understanding, there's some trend towards, like, more presence in Japan.
I don't really know why, why it's, like, why it is happening, but I see it in several tech companies, not, not only in hotel, but also in the vendors. And, yeah, they wanted to understand how… how Japan.
**Joe Josue** 25:57 works.
**Andrej Kiripolsky** 25:58 So, where does the community hang out? What are the channels that they use? How is it with hotel adoption compared to the countries that we usually get feedback from? So… Yeah, but as I said, this was… this was the only survey, and I think… and at the same time, we in general tried to… push for more APAC adoption, because one feedback that we heard is that for the Kubernetes community, this was a big deal, that once Kubernetes become more open to APEC contributors and to APEC market, like, it, grew a lot, so I think that's one of the reasons why we are trying to get more folks from APEC involved. That's why we are running this call as well.
**Joe Josue** 26:45 I'm in the time zone. Okay. Yeah.
**Andrej Kiripolsky** 26:48 Yeah, yeah.
**Joe Josue** 26:49 I just have a couple more questions, because this sounds like the most… the part I'm most interested in, obviously, is trying to use it and convincing friends and business owners to use this as, like, a standard, because if not, I don't know how to… without the standard, it doesn't make any sense to weigh things. So just a couple last questions. So, if I wanted to support, I could look at the to-dos, and then… just see if anything it feels like I can kind of do, and then… I guess, tap into submitting a PR or review, or do I just send a few of these first, because there's not a list, I'm like, oh, at least go through them and… digest, that's the current idea. Let me pass the con to figuring out if it can help, is to check the to-dos and follow all this Kanban board.
**Andrej Kiripolsky** 27:33 Yeah, like, if you want to contribute to OpenTelemetry, that's a way to go. Like, you check the Kanban board, you see what issues are there, and you can pick something up and start working on it.
We can also discuss… whatever else might be interesting for you, or you can come up with your own ideas. If it helps the, like, the general goals of the End-Us SIG or OpenTelemetry, we are happy to promote that. You don't have to just, like, focus on the stuff that are already there. It's more just like a… Easier way how to get started when you might not have any special ideas yet.
**Joe Josue** 28:09 Thank you. So, last question, is there a visualization, a way, or, like, a… I don't know, spreadsheets or database of where the… Participation in end-user surveys exists already.
Like, if I wanted to know how many surveys were done in Asia Pacific, are globally.
**Victoria Nduka** 28:28 Nope.
**Joe Josue** 28:28 All these surveys we're doing, is that somewhere, or is that all in the repo, technically?
**Andrej Kiripolsky** 28:35 Okay, I will show you, I will show you. So, Okay, let me share my screen again.
**Joe Josue** 28:43 Appreciate it, by the way, so I'm just trying to learn as much as I can and figure out as much as I can.
**Andrej Kiripolsky** 28:49 Yeah, yeah, and yeah, we don't have that much agenda for today, so, we can spend the time just answering questions, explaining how it all works, whatever works for you. Thank you.
**Joe Josue** 29:00 That's my last question, I just wanted to get an idea how…
**Andrej Kiripolsky** 29:05 Sure, sure, sure, sure. So, for our sake, we have… Each SIG in, OpenTelemetry has their own repository on GitHub.
**Joe Josue** 29:16 Yep.
**Andrej Kiripolsky** 29:16 Where they document how they work. So, in our case, we store all the survey data here.
**Joe Josue** 29:25 Oh, it's on there, okay.
**Andrej Kiripolsky** 29:27 Yeah, yeah. So, for example, the Japanese survey… oh, wait, no, the Japanese survey is still not here, because I… yeah, my stuff, I didn't… I didn't, Finish the PR. Yeah. I'm very much behind. I'm, like, a year behind on my tasks, unfortunately. I'm so sorry for that. And Yeah, here are the CSVs, for example, the Getting Started survey that we ran a while ago. But, to your question.
We do not collect the location information. So, in general, we try to not collect unnecessary BII, so personally identifiable.
**Joe Josue** 30:02 confirmation.
**Andrej Kiripolsky** 30:03 But, in general, we believe that there is not that much coverage in the APEC region. Maybe… actually, that's… that's, that's good.
I like what you're asking about. Maybe what we can do is that we can include, like, in general, it's not a PII if you say that.
**Joe Josue** 30:22 Regionally…
**Andrej Kiripolsky** 30:24 acre. Yeah, yeah.
**Joe Josue** 30:25 Yeah.
**Andrej Kiripolsky** 30:26 It's, like, so broad.
So we… we can include this, and this could give us a good overview of… or, like, some overview, not a good overview.
**Joe Josue** 30:34 some overview.
**Andrej Kiripolsky** 30:35 Of, where are people based?
So… Oh, add… a region question to our rate template. That's… yeah, that would make sense, because, like, right now we cannot tell, like, how many people are in APEC, but in general… oh, wait, no, we can tell. We ran a… But I actually don't remember where… what was the survey? I think it was Communications one?
a contributor experience.
We had one survey where we asked about location, and yeah, which region do you usually live in?
**Joe Josue** 31:14 Mmm…
**Andrej Kiripolsky** 31:16 And, I think… there is a… there was a blog post for this. I don't know if we… if we covered that particular, like, the region stuff, but… yeah, yeah, here it is. So, 6…
**Joe Josue** 31:31 6.
**Andrej Kiripolsky** 31:31 of contributors, but these are contributors, not end users.
**Joe Josue** 31:34 Not a difference, yeah.
**Andrej Kiripolsky** 31:36 in North America or EMEA. So, vast majority of folks live here, and that's why we also are trying to, like.
push for, like, more friendly, stuff for APEC, and we try to, like, talk about, talk about hotel in APEC region, and yeah, I think there's a lot of room there to, like, evangelize and, and just, like, get more, more participation.
**Joe Josue** 32:03 Okay, alright, that's it, thank you. It's a good start for me. I just need the standard to be everywhere for my own life as well.
**Andrej Kiripolsky** 32:12 Yeah, yeah, sure. If you would… Yeah, if you would be interested in, like, helping us, like, spread the word, or… or come up with some… you have any ideas about how to… how to, get more hotel participation in APEC, we are always happy to get contributions.
**Joe Josue** 32:34 Okay, yeah, I'm definitely interested. Okay, cool, wonderful.
**Andrej Kiripolsky** 32:38 Okay. Yeah.
**Victoria Nduka** 32:40 I wanted to add… There's also… you would also find the… And his, interviews there as well.
In the report. That would now take you to… to the YouTube, the individual interviews that we've had on YouTube.
**Joe Josue** 32:59 Oh, in the repo. Okay, yeah, I think it's just slide earlier. So, individual surveys are all there.
Is that what you… is that what you said? All of the information is there.
**Victoria Nduka** 33:07 Yeah, this one, this one like that.
**Joe Josue** 33:09 Yeah.
Thank you, thank you.
Yeah, okay. I mean, I bookmarked the repo. Thank you.
**Andrej Kiripolsky** 33:17 Yeah, yeah. Also, also, for the interviews, it might be better to just check the… YouTube channel, because I'm not sure if we, like, to what extent we were, like, updating the repo.
this is a community work, right? So a lot of stuff is just, like, done when people have time, and people don't have that much time, often. So, yeah, it can get messy, and it can get outdated, so… Yeah. That happens. That happens. But…
**Joe Josue** 33:43 I'll judge you, I'll judge you.
24.
**Andrej Kiripolsky** 33:46 Yeah, what we want to do, one of the things is that we want to run more, hotel… these sessions, YouTube's live streams, with APEC folks. We ran one so far, and that was, Alibaba.
**Joe Josue** 34:04 Mmm, okay.
**Andrej Kiripolsky** 34:05 Let me find it real quick.
**Joe Josue** 34:11 I think the PR was too high because of the percentage consent here she raised. No, no.
**Andrej Kiripolsky** 34:17 Yeah, yeah, so we ran a hotel in practice session, that's, like, where OpenTelemetry practitioners are talking about how they do open telemetry.
**Joe Josue** 34:27 So that was…
**Andrej Kiripolsky** 34:27 Basically, our only… livestream with anyone in APEC, and we would love to run more of these. So, if you have any thoughts about, like, if you have any companies around you who use OpenTelemetry and would like to talk about how they use it. It can be really just end users, it doesn't have to be hotel experts, we are interested also in, like, folks who are just getting started. But if they would like to talk about how they use OpenTelemnet, we are happy to feature them on our YouTube channel.
Okay, wonderful.
**Joe Josue** 34:57 Fair enough.
**Andrej Kiripolsky** 34:58 Indeed.
**Joe Josue** 34:59 So in fact, I'm trying to find them. That's also why, because when I talk to enterprises here, and some of my colleagues in the region.
I've only maybe had, like, one who talked about open telemetry, so I feel like that's what's lacking. So I'm trying, I want, but it makes it complicated, because there is no standard if there isn't, so I think it needs to be louder here. So I'll do… yeah, I'm very interested to figure out adoption.
Okay.
**Andrej Kiripolsky** 35:23 Cool. Yeah, and one last thing. You mentioned that you're interested in the Agentic stuff, so I think we have a special interest group that is specifically focused on monitoring AI agents.
**Joe Josue** 35:38 Which one?
**Andrej Kiripolsky** 35:40 Yeah, that's a good question. I will try to find out afterwards, and thank you. Are you on a CNCF Slack?
**Joe Josue** 35:48 I am in the CNCF Slack. I joined, just a few days ago, so I don't know… I'm not sure exactly how to navigate the ZNCF Slack, but I'm there.
**Andrej Kiripolsky** 36:00 Okay, yeah, I also don't know how to navigate it, so no worries about it. Alrighty, so… I guess that might be… that might be it. Ernest, Victoria, anything else you wanted to.
**Ernest Tolulope Owojori** 36:13 Yeah, I was going to say that, for the CNCF, you can try to… join the hotel channels. I don't know as many hotel channels as you have, but in most cases, you just do Hash Hotel, then you see quite a couple of them.
Then you can join as many as possible. Then later.
**Joe Josue** 36:31 Thank you.
**Ernest Tolulope Owojori** 36:32 Any ones you want to focus on, you can remove the rest and all.
Yeah.
**Joe Josue** 36:36 Thank you, I found this… I already joined the SIG End-User… Jenna implementation, the general one, I just found Andre, and I just pinged you.
Sure, yeah.
**Andrej Kiripolsky** 36:46 So, we'll go.
**Joe Josue** 36:47 Thank you.
**Andrej Kiripolsky** 36:48 Alrighty.
**Joe Josue** 36:49 Thanks so much.
**Andrej Kiripolsky** 36:50 I guess that might be it for today, so thank you all for joining, hope next time we will have more attendance, and I'm sure next time Yoshi will have a lot of updates, because he will be… he should be recording videos with end users at KubeCon Japan.
So, yeah, I'm super curious about how it goes.
Yeah. But yeah, for today, I guess we can… we can wrap up.
**Joe Josue** 37:16 Thank you guys so much for the time and everything. Thank you so much. I appreciate it.
**Ernest Tolulope Owojori** 37:20 What are they doing?
**Andrej Kiripolsky** 37:21 Bye-bye.
**Victoria Nduka** 37:23 Bye!
