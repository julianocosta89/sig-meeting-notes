SIG: End-User SIG
Date: 2026-09-10
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Andrej Kiripolsky** 00:26 Hello?
**Mateen Ali Anjum** 00:30 Hi, Andre. It's Mateen. How are you doing?
**Andrej Kiripolsky** 00:34 Hi, Mateen, nice… nice to meet you. Yeah, all good, all good, how are you?
**Mateen Ali Anjum** 00:38 I'm good as well.
**Andrej Kiripolsky** 00:40 Yeah, glad to… glad to see you here.
It's their first time joining the meeting?
**Mateen Ali Anjum** 00:45 Yeah, yeah, it's my first time. I joined the Slack channel last month, and yeah, I talked to Victoria about an anomaly detector check that I was working on, and she said, just join the meeting, show us what you have built, and we might share it with the community. So yeah, here I am.
**Andrej Kiripolsky** 01:04 Oh, wonderful. Glad to hear you.
Hi, Karimot.
It's your first meeting here as well, right?
**Karimot Isiaka** 01:11 Yeah.
Hi, everyone.
**Mateen Ali Anjum** 01:15 Hi.
**Andrej Kiripolsky** 01:17 Oh, hello.
Welcome.
**Karimot Isiaka** 01:20 Thank you.
**Andrej Kiripolsky** 01:22 Yeah, yeah, yeah.
Yeah, so we can do intros later, when everyone joins.
But… Yeah, Karimot was doing some great job on Ecosystem Explorer.
project within OpenTelemetry, so that's a tool to, like, somehow organize the metadata about different ecosystems, so… Yeah, I invited her to join us here as well, in our site.
**Mateen Ali Anjum** 01:52 Good to know.
**Andrej Kiripolsky** 01:56 Hello, Dhruv! Yeah, so this is how it looks usually in the beginning, so people are, like, slowly… Joining it.
Joining, yeah, so… We can give you that.
A few more minutes.
Mateen, where are you based?
**Mateen Ali Anjum** 02:12 I'm in Toronto, Ontario, in Canada.
How about yourself?
**Andrej Kiripolsky** 02:16 I'm in the Czech Republic, in Europe.
**Mateen Ali Anjum** 02:19 Nice. Yeah, we have KubeCon this time in Prague.
**Andrej Kiripolsky** 02:25 Wait, really?
**Mateen Ali Anjum** 02:26 Yeah, that's what I read. Is it coupon or open source summit?
**Andrej Kiripolsky** 02:31 OpenSource Summit is in Prague in one month, but I didn't know about Google. Like, I don't think… I didn't know it… I think it was in Spain, it was announced to be in Spain.
But I might be wrong.
**Mateen Ali Anjum** 02:42 And I featured block.
Yeah, sorry, I meant the Open Source Summit, not KubeCon.
**Andrej Kiripolsky** 02:51 Are you joined?
**Mateen Ali Anjum** 02:52 No, I went to the Open Source Summit here in North America, in Minneapolis, in May. I was a speaker there, but yeah. Yeah.
**Andrej Kiripolsky** 03:01 I'm going actually, like, since it's so close, I would feel a little embarrassed not to go, so… Yeah, I'll be there. Just as a boot staff for my company, and just hang out.
Okay, Lord.
**Mateen Ali Anjum** 03:16 Nice.
**Andrej Kiripolsky** 03:18 Yeah.
Alrighty, so yeah, let's, like, let's give them one more minute, and hopefully, hopefully someone will… Join us, some more folks.
I think we can get started, even though… Yeah, nobody will join. So… Once again, welcome, everyone. Usually there is a bigger… there's a bigger group, but apparently it will be… it will be just us today.
Yeah, as I mentioned, maybe we can do a quick round of intros before continuing to… to the… topics that we have for today. So my name is Andrej, I'm a user researcher at Grafana Labs, and I'm a maintainer here at SIG End-User of OpenTelemetry.
And I take care mostly of surveys that we run.
And, yeah, that's kind of… that's kind of it. I, Wondering what else can I share? I have two kids, and I have a dog.
It's a tiny, like, German Spitz. It's one of those, like, very furry dogs. And Yeah, that's, that's kind of it on me.
I'm wondering… maybe, Dhruv, do you want to go next? You are the old-timer here in SIG End-Us, or, like, experienced SIG contributor now?
**Dhruv Ahuja** 05:52 Well, feels good to hear that. So, hey folks, I'm Dhruv. I'm from India, and I work for Cygnos, which is an observability startup. So, I got started with the OpenTelemetry community about 3 months back, I believe, I think around June.
So… And yeah, End-User SIG was one of the first SIGs that… whose call I joined, I liked, and then I thought, okay, why bother trying other places, because I like it here.
So I've since then stuck to it.
And… Yeah, I've recently participated in the OpenTelemetry and Promethe Center Operability Survey, so which was the major thing that I've done.
So, yeah, and validation of that is Andre now calling me an old-timer.
So… Yeah.
And we have a blog post that is supposed to come out soon, so once that is out, I'll be applying for my membership, because I want to show this one milestone under my belt before I do that.
So yeah, that's basically it. I've come here recently, I'm trying to be active, and just trying to learn and contribute.
Yep.
**Mateen Ali Anjum** 07:13 Good to know, good to know. I can… maybe I can go next now. So yeah, I'm Mateen. I'm a site reliability engineer. I'm basically a contractor with Apple, and I've been extensively working on site reliability Automation. I'm involved in many, tags, like with operational resilience and initiatives, like site reliability Automation.
I'm also an active contributor on OpenTelemetry CPP, with Mark and Doug. So, yeah, that's, I'm based in Toronto, Ontario. I have two girls as well, and I don't have a dog, but yeah, I'm looking for one nowadays.
Yeah, that's… that's me.
Karimot, you wanna go next?
**Karimot Isiaka** 07:57 Yes.
Nice to meet you all. My name is Karimot Isiaka. I'm based in Lagos, Nigeria.
I, I think I would describe myself as… Okay, I was a mentee at the recently… would I say at the most recent LFX mentorship round, And I… contributed to the project, the OpenTelemetry Ecosystem Explorer. I did some user research work and information architecture work.
and Andrej… was one of my… is one of my mentors, I wouldn't say was, is one of my mentors, and yeah, I'm so excited to be here, and hopefully become an active contributor to the End-User SIG community. Thank you.
**Andrej Kiripolsky** 08:53 Yeah, wonderful. Thank you, everyone.
So, we have a couple of topics on our agenda. Maybe we could go through them first, before, Mateen will tell us more about, about, his topic. I just checked, our contributor's channel, and I think Dan and Victoria will be joining as well, so I think it would be, like, since you discussed this with Victoria, I think it would be great, and and I think it would be also awesome to have Dan around, because he was an SRE before, so he might… he might have some, like, the technical understanding of things that might be… important for this discussion. So let me go first about the contributor Slack channel.
Last time, during our last meeting.
we discussed that in the main, OpenTelemetry Sq End-User channel, we have 1,000 people, or, like, more than 1,000, and we use it for two things at the same time. So one thing is, as a place for any end users to come to us and share their feedback or ask questions. And also, we use it for discussions between contributors.
That can be just something like, give me feedback on PR, or, sorry, I will be 5 minutes late for our meeting, or something like this.
So, these two things feel very different, and we discussed it might be a good idea to have a separate channel for contributors, just so they also… they feel a little… more comfortable.
chatting over… over Slack, because, like, you don't want to… you don't want to ping 1,000 people, with these kind of, like, random things every time. So we created a new one, channel OTLCAN user contributors, And, that's just an announcement for this.
So, yeah, I guess, like, in case you would like to, be aware of what kind of stuff are we discussing as contributors? Feel free to jump in there, but otherwise, I think it's, like, for most of the people, it will be just fine to stick with the regular OTLSIQ end-user channel.
And yeah, I hoped for, like, a little more attendance from the usual contributors, so I wanted to just, like, double-check with everyone that they're okay with, yeah, the way how I create the channel and the description and everything, but yeah. I guess, like, for today, it will be… it will be kinda… kinda… it, so yeah, just… just FYI.
And I will probably open it again next time. And the second thing that I want to talk about is the survey that Dhruv already mentioned briefly.
So… I opened a PR.
in… Let me open it here… I opened the PR in, Opentelemetry.io, that's our website.
where also the documentation lives, the blog posts live, and, like, a lot of other… Content. So, yeah, we would like to share the findings from our… from our report, from our survey.
As a blog post, and yeah, I just, again, wanted to mention it to everyone, that it's open for reviews, and if anyone is willing to give a review, I would be very… or, like, we all will… would appreciate it.
Huge thanks to Dhruv for, like, very quickly reviewing it.
I incorporated all your feedback, Dhruv. I hope everything is alright now, especially this… this thing about, image is being a little broken. I'll have to check in the… in the preview.
But maybe just a quick question.
Do you know, Dhruv, does the preview that you linked update with the… Yeah, it does update, so…
**Dhruv Ahuja** 13:00 Yes, so I got the preview link from, so, there are a bunch of checks that run, correct, as we push commits. So, there is one called Netlify Preview Deploy, something like that, and the check itself just points to the link itself.
And it updates as we push. So if you scroll a bit below, you'll see something like deploy something from Netly 5.
Okay. Deploy Preview.
**Andrej Kiripolsky** 13:28 Oh, yeah, I see, I see, wonderful. Yeah, yeah, yeah. So… But as I… as I checked here, the… the charts are not overflowing, so I think it should be… should be all right now.
**Dhruv Ahuja** 13:41 Yes, it is fine for me as well now.
**Andrej Kiripolsky** 13:45 Okay, wonderful. So, yeah, once again, thanks for the review.
I asked all our co-authors for review, I, like, Arthur reviewed, Anna did not, but I think she's… she's aware. And, yeah, now I will… I will request review from… from our SIG colleagues, so from Dan, Adriana.
Reece, Victoria, or Sophia, and once they accomplish their review, we should be ready to ask review from the docs contributors, and then we should be ready to publish. So yeah, there are a few more steps in the process, but we should be… we should be done soon. Dhruv, just a quick question.
Hold on, actually, I can just ask you for… re-review now, since I incorporated your stuff.
And, yeah, just give me a thumbs up if everything is alright, and if not, just… Please just share.
share any other feedback you might have. So yeah, I asked you for your review here.
And it's…
**Dhruv Ahuja** 14:48 I'll check and let you know in, yeah, today itself.
So I'll approve it on the GitHub, and I'll send a message in our contributor's channel, so we can start putting that to positive use as well, and get people active.
**Andrej Kiripolsky** 15:03 I'm sorry, I didn't catch the second part of this.
**Dhruv Ahuja** 15:06 I… yes, I said I'll, respond accordingly on the GitHub PR itself, and also put a message in our new contributor's channel, so we can also start getting some activity there, just regarding this.
**Andrej Kiripolsky** 15:20 Yeah, that sounds good, that sounds good, yeah. This is our own tiny little channel where, so yeah, feel free to post there, as often as… as… Excuse me.
And yeah, we have… we have two more topics, from Victoria, I guess, and so one is from Victoria about the assets, and… One is, about the… about the Oakland practice session by Mateen, but yeah.
Folks are still not here, so let me… let me just quickly ping them.
Every minute, okay.
Okay.
Yeah, let's give them some more time. It happens sometimes that, you know.
This is a voluntary free-time activity for many of us, so… Occasionally people just have another… other… other responsibilities to take care of.
So, yeah.
Let's give them a couple more minutes. Mateen, can you tell us a bit more about your… Your work, it sounds exciting. Especially, I think, like, since yesterday, we all are thinking about Apple, like, we were all thinking a lot about Apple since the… Oh, yeah. What kind of stuff do you… do you do there, and Yeah, if you can talk about it, it's just very.
**Mateen Ali Anjum** 17:55 Yes, so I am on the software development experience team over there, and we take care of all the SDLC that happens in Apple. That includes Artifactory, CICD management, uptime of the developer tools that they are using. So, we have almost 21 verticals that we own inside Apple.
And we use a bunch of observability tools as well, almost all the industry players. Mainly, they have, Splunk for visibility, but OpenTelemetry and OTL SDKs are, you know, implemented everywhere, and they're using that for metrics, logs, traces, everything. And basically, one of this all came through a project that I was working on, so my project was, to test if anomaly detectors actually work. You know, with anomaly detectors, we just turn them on. Victoria's here. Do we… should I? Hi, Victoria.
So yeah, so we turn on the detectors, and we don't know, we choose a detector based on the F1 score, and we decide that this is the best one, and then we put them in.
But is it really working on your incidents and telemetry that you are giving it to? So, the main goal was to check it, and when I checked, I got different results, and that is why I wanted to bring this too.
the community to see if they can run this check that I've created on their OpenTelemetry data, and see what they find, and let me know, if it works for them, if it doesn't work for them, what word their findings are. I also wrote in a paper, a journal article, a research paper on this exact topic, where I tested 8 different detectors, so… and all 8 of them gave me, unexpected results, so… That's also out there, yeah.
**Andrej Kiripolsky** 19:44 That's something.
Yeah, sorry, I didn't mean to do any spoilers before folks join.
Yeah, hi, Victoria. Yeah, we were, we just literally just started. I was just asking about how… how, how is it, working with Apple, especially, recently, after all the announcements, but yeah, Mateen mentioned that he's not on those, on those teams, but… Yeah.
Little different, little different stuff.
**Dhruv Ahuja** 20:15 But can you still provide us with some, like, discount coupon for the new Fold?
**Mateen Ali Anjum** 20:21 Because of the show.
**Dhruv Ahuja** 20:23 Happy meeting.
**Mateen Ali Anjum** 20:25 Only if you're in Canada.
**Andrej Kiripolsky** 20:30 Yeah, yeah.
But that's super cool to hear that you use OpenTelemetry for everything.
**Mateen Ali Anjum** 20:36 Yeah.
**Andrej Kiripolsky** 20:37 like, in Apple, I… I mean… what we learned in the Prometheus survey is that like, smaller companies are quicker to adopt open telemetry. Perhaps they are, like, more agile, like, less people involved, less of a legacy code, so it's interesting to hear that in, like, such a giant company.
**Mateen Ali Anjum** 20:58 Same with Apple, because there's so many services, but, like, I can tell you, like, Apple Maps and Apple CarPlay, they use OpenTelemetry, but a lot of legacy is also still there, so if there's a service that is on Prometheus, they would rather not change it, but when new services or new verticals are being created, they are preferring hotel, yeah.
**Andrej Kiripolsky** 21:18 Got it, got it, got it. Yeah, by the way, and victoria, we were… we are also waiting for Dan, because he mentioned that he will join.
**Victoria Nduka** 21:25 Where?
**Andrej Kiripolsky** 21:26 Okay, so I wanted to give…
**Victoria Nduka** 21:28 Oh, good.
**Andrej Kiripolsky** 21:28 Sometime.
But… but yeah, it's… it's been a while, so maybe… maybe… Maybe we can… Get started? I don't know.
with Mateen's topic, I think you, you already, Lori mentioned it.
so… And I know that you folks discussed it over Slack, so yeah, I will leave it to you to continue the discussion.
**Victoria Nduka** 21:58 Oh, okay, I thought that was what she was talking about before I joined.
So I, like, I wanted to bring it to… I saw his message, and I felt I had to leave a response, so it's not like somebody dropped a message, I'm just ignored, and everybody ignored it.
**Mateen Ali Anjum** 22:12 Yeah.
**Victoria Nduka** 22:13 And I thought to bring it to the meeting where everyone, like, where we could all, Where he could have a better opportunity to explain what the study is about, and exactly what it is he… He wants… The community to do for him, or what he wants to do.
With the community, then we can weigh it and decide.
**Mateen Ali Anjum** 22:37 Sure.
So yeah, I'll just give you a bit of a background, Victoria, on the stuff that I already talked about and what I am asking here. So basically, as I said that I was doing a study, okay, so I'm Mateen, I'm a contributor, hotel member on OpenTelemetry.
and collector Contrep, and I'm also part of the initiative for Site Reliability Automation. So, this topic came out when I was doing a research on anomaly detectors. People turn on anomaly detection and have no way to tell whether it's working on the data or not. And a broken anomaly detector looks exactly like a working one, like, you cannot differentiate between the two of them. There's no crash, no errors.
everything's green. So, I have an example where an isolation force processor and contrep gave every span nearly the same score. It shipped, like, almost 220 days for… before anybody noticed that it wasn't working. And a user reported, and a fix landed, like, 140 days later, and found that the contamination rate, setting did nothing either.
So, I created this check, which basically came out of a study I ran on 8 detectors over OTL tracers, metrics, and logs, and I created a testbed with EKs with Fort injections in them. And the reason is simple, like, F1 moves with how often those anomalies happen. So a detector that flags everything, scores well on anomalies, it's quite common.
So, the check that I've created, it pulls, basically what it does is that it's all open source, it's vendor neutral, there's nothing, it's all written by me, solely, no else, nobody else has… done that. So, what that detector does is that it checks if the anomaly detector is actually working. So, all I want from the community is, basically, I'm looking for two or three operators to run this detector on their, you know, telemetry data, where they have a CSV. They don't need to do anything, they just need a CSV of their incident windows and alerts or scores.
And under 2 seconds, they can, you know, see if it's working or not.
**Victoria Nduka** 24:46 Okay.
**Mateen Ali Anjum** 24:47 Yeah.
**Andrej Kiripolsky** 24:47 Okay.
And, So, this is something you want to promote to the whole community, or you are searching for, like, a small number of Of testers who can give it a try.
Initially.
**Mateen Ali Anjum** 25:01 Yeah, initially, I just want a small number of testers who can try and see if it is useful, and then if it's useful and it brings useful results, then definitely we can, you know, promote it to the community and, you know, it can go out, and… because this is, like, the new thing, like, everybody has started implementing anomaly detectors. In the past one year, I've noticed major vendors have started, and automatically it's enabled. Like, with Datadog, they automatically enable anomaly detection, but whether if it's working or not, nobody knows. So, I think it's useful for the wider community as well.
**Andrej Kiripolsky** 25:38 Got it, got it. So… I think that would be… it would be a good idea to post it, like, if you are just looking for volunteers, I think what might make sense is to post to that channel with 1,000 people in there, and perhaps you will find some folks who are willing to give it a try. If that doesn't work, we are happy to help you find some more people. We have, we have other channels as well. We have, we have Reddit, that, other folks are, are, I think.
Yeah, Dan here, who just joined. He's a Reddit moderator for OpenTelemetry, so we can post there, and I think if you are searching… if you are looking for just a handful of people, I think that could be good enough. And then, what Victoria mentioned to you in the thread.
That, like, once you would like to Report your findings, or, like, share it more broadly with the whole community?
And ideally, if it's, like, a little more mature, I think then hotel in practice would be… would be a great…
**Mateen Ali Anjum** 26:52 venue.
**Andrej Kiripolsky** 26:53 format, yeah, or venue for it, because that's… that's basically a livestream, that is being recorded and is being published on YouTube, and Jam.
then that way, it's… I think it's a good format to share these kind of things, especially, as you said, that you already wrote, a paper about it, I think that might be a little more… Easy to consume.
Yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 27:20 I joined late, but is the… is the… was the discussion about, is it a Tulin, particular tooling that, that we… So, if you can summarize it, Mateen.
**Mateen Ali Anjum** 27:29 Sure.
Sure, Dan. So, basically, you know, there's been a trend where everybody's enabling anomaly detectors, but do those anomaly detectors work or not? Nobody knows. So, I wrote a check where, what it does is it gets a CSV of your incidents and your alerts, and it matches if the anomaly detector is actually working or not. It's, simple as that. So I tried 8 different anomaly detection techniques.
and found out that F1 scores don't mean anything. Like, today, if we wanted to enable an anomaly detector, we would look at the F1 score and see if it works for us. But not every detector works for everybody. So, it's about choosing the right anomaly detector, and this check basically helps, yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 28:13 Okay, yeah, I guess I would say that… Apart from what was mentioned here, there is an… in the… OpenTelemetry, so on Reddit, there is a… I think it's every Friday, a blog post that, you know, not a Reddit post where people can share their tooling. So one of the problems that we had on the Reddit, subreddit, is that we, it became a little bit more… a little bit like, you know, everyone's sharing their tool, and with AI, basically, everyone's building tools, right? Yeah. So it just became a little bit, like, too much of that. So now there is, every Friday, I think, and tomorrow's Friday, so that's a good point.
every Friday there is a post where you can add your own stuff, basically. Like, you know, that would be one thing. There is already… there's also a… I would… I guess, discouraged from using the general OpenTelemetry channel in Slack.
For stuff like that, but there is an OTEL-Ecosystem.
Okay. Where, like, people share, like… tooling around OTEL, right? There are only 100 people in it, but people do share stuff there. If you were to share in the OpenTelemetry general channel.
**Mateen Ali Anjum** 29:30 Sure.
**Dan Gomez Blanco (New Relic, Inc.)** 29:30 yeah, you'll probably get shouted out by someone. But but yeah, if you share the hotel ecosystem, and End-Us, I mean, I'm… If it's related to OpenTelemetry, I don't see a problem with that.
Yeah. Man.
**Andrej Kiripolsky** 29:45 Dan, do you think the hotel SIG End-User channel with 1,000 people would work for this, or that's also not the right one?
**Dan Gomez Blanco (New Relic, Inc.)** 29:54 So what are we asking them to do?
**Mateen Ali Anjum** 29:58 So, all that they need to do is run the tool, it's a script, basically, which runs on their CSV and reports the results if their anomaly detector is working or not. And honestly, like, I'm not promoting this tool, like, it's just for research purposes, because I wrote a research article already, and I'm enrolled in a.
**Dan Gomez Blanco (New Relic, Inc.)** 30:15 my…
**Mateen Ali Anjum** 30:15 So…
**Dan Gomez Blanco (New Relic, Inc.)** 30:16 My… yeah, so I guess my concern… concern on… I mean, not… not… not a concern, but, like, the, the boundary of… where the boundary of OpenTelemetry sits as a project, right? OpenTelemetry is normally more… I guess, involved with the instrumentation side.
We, you know, we don't provide a backend, right? So… there is… a CNCF observability tank that is more general, where, like, maybe that is potentially a… a way… You know, if you wanted to have, like.
the CNCF observability tag. Back to that, there is… there is as well… let's see if it's there in CNCF… There is an observability… Signal… SIG observability? No, it… there is a… there used to be a tag.
I think it's Tank Operational Resilience, I believe.
**Mateen Ali Anjum** 31:15 Yeah, I'm already part of it, and I'm… I'm involved in a couple of initiatives with DAGOR.
**Dan Gomez Blanco (New Relic, Inc.)** 31:22 Oh, cool, awesome. So, I mean, what I'm… what I'm saying is, From the perspective of hotel, some people may ask, what… how is hotel?
Involved in this, right?
That's… that would be the honest… Question that they may ask.
Right. So, okay, you know, incident data.
hotel… Does not have an incident data… does not have an incident in semantic conventions, for starters.
**Mateen Ali Anjum** 31:47 Here.
**Dan Gomez Blanco (New Relic, Inc.)** 31:48 So, while it is a cool idea.
Hotel does not provide any type of, like, anomaly detection either.
**Mateen Ali Anjum** 31:58 Yep.
**Dan Gomez Blanco (New Relic, Inc.)** 31:59 So… I mean, I'm okay from the perspective of, like.
sharing it in the ecosystem perspective.
**Mateen Ali Anjum** 32:06 Yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 32:08 But… I don't know.
**Mateen Ali Anjum** 32:10 Or does it only run on, yeah?
**Dan Gomez Blanco (New Relic, Inc.)** 32:12 I don't know if this is in the scope of OpenTelemetry, you know what I mean?
**Mateen Ali Anjum** 32:16 Okay.
**Dan Gomez Blanco (New Relic, Inc.)** 32:18 So the hotel ecosystem, great. I mean, that's a good… that's a good spot for it, because it ultimately is all related to observability.
Reddit? Yeah, go for it.
**Mateen Ali Anjum** 32:29 Okay.
**Dan Gomez Blanco (New Relic, Inc.)** 32:30 but the hotel channels, I think you might get… certain views on it, being like, yeah, hotel does not do anomaly detection, does not do incident management.
There is a link, which is observability, but is the observability, or the operational rating is, sorry, operational…
**Mateen Ali Anjum** 32:48 Resilient.
**Dan Gomez Blanco (New Relic, Inc.)** 32:49 Brazilians, tag a bit… a better home for it.
Okay. That would be my view on it.
**Mateen Ali Anjum** 32:56 Okay.
Sounds good. Yeah, I'll, I'll DM you, like, do… is there a way to… is there a process for Reddit post, or do I just post it from my user ID?
**Dan Gomez Blanco (New Relic, Inc.)** 33:07 Yeah, you can post a phone user ID, yeah.
**Mateen Ali Anjum** 33:11 Okay, sounds good.
**Andrej Kiripolsky** 33:14 Right.
**Dan Gomez Blanco (New Relic, Inc.)** 33:15 I'm genuinely, genuinely interested in this, though. So, please do share.
Okay.
**Andrej Kiripolsky** 33:23 Yeah, in that case, what I mentioned about the… The hotel in practice, that's probably… that's probably not relevant, based on what you're saying, right?
**Dan Gomez Blanco (New Relic, Inc.)** 33:32 Yeah, I think it would be… because what we want to see with OTEL is, like, how was Hotel… How did OTEL help with that? And I guess, you know, you could say, well, the data is there, but, like.
how are you using OpenTelemity? Like, the old tooling practice bit is, like, are you using OpenTelemony tooling?
for it, and I guess, you know, in this case, you'll probably be getting the CSV from different vendors, right? Or different backends.
**Mateen Ali Anjum** 33:54 Yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 33:55 And so, again, you know, this is another element where, like, we need to be really careful in OpenTelemetry with comparing vendors. So if you're gonna say, oh, you know, this anomaly detection over here worked better than that one… It's a can of worms.
Yeah. But I'm, I'm, yeah, I'm interested in that, though.
But I think, yeah, OTL ecosystem, Reddit, Tag Operational Resilience, that sounds like more of a better home for it.
**Mateen Ali Anjum** 34:21 Okay.
**Andrej Kiripolsky** 34:29 Fighting.
Mateen, is there anything else? Any… or is… is there… are the next steps clear for you?
**Mateen Ali Anjum** 34:36 No, I guess that's good. What I'll do is I'll put a post up on the subreddit for Friday to… for people to see, and I'll reach out on the general channel to see if I gain some volunteers there.
Yep.
**Andrej Kiripolsky** 34:53 Awesome.
**Mateen Ali Anjum** 34:54 Thank you.
**Andrej Kiripolsky** 34:55 Awesome, awesome, awesome.
Cool.
And I think that Victoria had one more, has one more.
topic in the agenda? So, Victoria, do you want to…
**Victoria Nduka** 35:08 Yeah, I was going to ask, like, if that had already been discussed.
So, how this came up was… Pussy.
was looking for… he was… he asked for… that's… that was… that's our last authentic practice speaker.
He wanted some… the, SIG End-User logo to add to these slides.
for the presentation, and I know Rhys is the one who does all of the designs, or most of the designs.
So, Alec… I, I thought to check on, OEM.
if I could see… some of those assets there, and I did see a PR.
That is the… you read me, or a folder.
A linked folder.
Meetings.
Well, it appears… We started uploading, like.
started uploading the assets, but I didn't get around to actually uploading the assets. So, we just have a folder named Assets, and it read me, but no assets.
So I thought to bring that up, maybe… We could pick up.
Oh, really good.
**Dan Gomez Blanco (New Relic, Inc.)** 36:19 Yeah, okay, I see what you mean.
Yet.
I actually did, this is related… this is maybe, I don't know, We can race it with Reeves, I think if she can share anything there.
Yeah. Do you want to tag her into the… we're in the contributor's channel? Like, I think that's… Pulled.
**Victoria Nduka** 36:38 Yeah, yeah, I'll deducts was that one?
**Dan Gomez Blanco (New Relic, Inc.)** 36:42 I want to comment on that.
Related to the KubeCon Japan video.
I am not, you know, because we talked about, like, editing the videos, and if Reese, or… I don't know who did it before.
I'm not a video editing person. I did one, like, two months ago, and it took me so long, I was like, oh god.
It's not my thing. I edited one video, and it took me, like, 3 weeks to edit a video, but yeah. So, if someone else, you know, has any skills on video editing, then, yeah.
If you have the resources, yeah.
**Andrej Kiripolsky** 37:17 Yeah, I responded, I think, in the issue there, that Sophia volunteered to do it, the editing, so I think that's also what Yoshi is waiting for. Or, like, that's the next step, basically, for the KubeCon Japan.
**Dan Gomez Blanco (New Relic, Inc.)** 37:32 Nice.
**Andrej Kiripolsky** 37:33 I also don't have video editing skills, so… Totally understand.
Alrighty.
**Victoria Nduka** 37:42 Oh, and, Andrej, I have a… I have a post on Buffer.
Nice.
**Andrej Kiripolsky** 37:50 Yeah, yeah, yeah, I didn't get the notification, or I didn't notice it, so let me… Let me… I will approve after the decision.
**Victoria Nduka** 37:57 No problem. Like, I usually reached out to Jenna for this, but I saw that she was out of office, and then I reached out to Rhys, and then I noticed that Reece later on had an emergency, and she didn't respond, so…
**Andrej Kiripolsky** 38:07 Okay.
**Victoria Nduka** 38:08 Okay.
**Andrej Kiripolsky** 38:10 Yeah, I will respond, I will… I will approve.
**Victoria Nduka** 38:12 Yeah.
I might just… I might just have to change the published dates.
**Andrej Kiripolsky** 38:22 Is there anything else we want to discuss today?
**Victoria Nduka** 38:26 your opinion.
**Dan Gomez Blanco (New Relic, Inc.)** 38:26 or something, if that's okay. I've, so, as you may remember, I didn't ask this topic, I didn't put this topic in the agenda, by the way, but I will.
Tool.
Last year, We… we merged some changes to… to make… To have a sub, a subheading.
or a footer, basically, on every issue across OpenTelemetry. That basically prompts people to say, well, if you want to help prioritize this issue, leave a thumbs up, right? The whole idea was, like, improve Community participation, some of the issues, and then, you know, for the, for the, the, Actual maintainers who understand what the priority for the community is.
I was thinking that, Yeah, we could be using that in a better way, so let me share my screen.
This is a… I only ran it yesterday once, but Yeah, so basically I built a script.
That will… Generate a report.
It's a fairly… fairly simple script. But it will generate… it will go through all the repos.
An hotel.
and then generate a report. The idea was to… I guess this is my… Thoughts at the moment.
Is, put it… start to generate these reports, let's say, on the first day of the month, or the last day of the month, or something like that.
that takes a look at the last month, and it says, okay, what are the most… What are the 10 most popular open issues?
Across open telemetry, like, what are the most voted ones that are currently open, basically?
What are the, So 3 things, basically. What are the most, Popular issues that are open? What are the most popular issues that were… Open in the last 30 days, and maybe some of them were closed already.
And then what are the most… the 10 most liked issues, the 10 most popular issues?
Closed in the last 30 days.
So this is… this could be good material for us to do… I don't know, an hotel, me, or… Something like that? Like… a session on it, or maybe, like, a WhatsApp hotel.
If we see something here that pops up.
That is, like… I mean, some of them are very specific, right? But imagine that you're… we're closing something to… I don't know, to provide support for… For a new… ecosystem, right? And then that gets closed.
Then, it'll be interesting to catch it here.
That was closed, and then have it as, like… In the news, right?
That's one thing. And then for each of the repos, the same thing, right? So each of the repos would have the… The 5 most popular issues, the 5 most liked issues, and the open and close.
Question here is, like, do you think this… And, you know, you can be honest. Do you think this would be useful for you, or for the end users?
I mean.
**Andrej Kiripolsky** 41:50 I think.
**Dan Gomez Blanco (New Relic, Inc.)** 41:50 time to build it, thanks to Claude.
**Andrej Kiripolsky** 41:52 I think it could be useful.
This… but one thing that, that, like, immediately… or, like, two things. First, I think… I'm not sure if, like, monthly is a good idea, but, Because, like, I don't think things move that quickly.
Or at least in our six things, that quickly, really.
But that's just a… that's just a detail.
Another thing is, if it's a SIG End-User thing, Because… I think that when you mentioned WhatsApp Hotel, I think this is something that Adriana, Rhys.
And that, other community manager, unfortunately, I've never… I've never met her. I think this is what they are doing, and I… but I might be wrong. I might be wrong.
**Dan Gomez Blanco (New Relic, Inc.)** 42:39 No, no, they are doing that. So I guess, you know, from the perspective of the end user.
Seeing the… the things that were delivered that were, like.
Is this an end-user thing, or is it more of a contributor experience thing? As in, like, maybe this would be more useful for maintainers than for end-users, perhaps.
**Andrej Kiripolsky** 43:01 Yeah, well, at least contributors, not end users, probably, but the contributors, for sure.
**Dan Gomez Blanco (New Relic, Inc.)** 43:07 Yeah, for contributors, like, you know, for… yeah, maybe not maintainers, but… yeah, people that are… Looking at… Yeah, okay, that's a good point.
**Andrej Kiripolsky** 43:18 I'm just, honestly, like, whenever I see a, like, yeah.
That's… those scripts that we… or the… the… Oh my god, what's the name of it? Like, a dependency bot that is in our repo, because of the… Yeah, because of the renovate script that is in our repo, just because of that single, like, YouTube script that we have there, and it keeps opening issues, and it's just one issue, it's, like, it's much better than it was, but… Yeah, I think it just adds a lot of… Good.
**Dan Gomez Blanco (New Relic, Inc.)** 43:57 Oh, maintenance, yeah, I guess.
**Andrej Kiripolsky** 43:59 and technical complexity into the repo that was originally just really text-based, and there was nothing else there. So I'm just wondering if SIG End-User Repo is the right one for this type of stuff. But it's just… yeah, I'm not, like, against it, if you feel like that's… it should belong there, but… Yeah.
That's fine.
**Dan Gomez Blanco (New Relic, Inc.)** 44:22 I guess, you know, the question is, yeah.
If it's more useful for end users. And maintaining it, like… I mean, it's… fairly… I don't know. It is a bit of a pain having to merge the PRs, but… But I'm more concerned about, like, this being something that adds.
more toil to this group, right? If we don't see that as useful for end users.
That's… that's the thing.
**Dhruv Ahuja** 44:50 I think…
**Andrej Kiripolsky** 44:51 Rocus.
**Dhruv Ahuja** 44:52 Yeah, I think maybe starting off, it would be useful for the contributors, because I remember reading about a couple of concerns being raised around the gap between a small number of people contributing major amounts of code across all OTL repos, so maybe something like this can help, Around that perspective first, before we start focusing on the end users, because I think end users might still want to see more progress made towards the actual implementations for the SDKs, or a feature that they are looking at, or semantic conventions.
**Dan Gomez Blanco (New Relic, Inc.)** 45:27 End-Us, yeah, I guess what you're saying is, like, end users just care, or if they do, they care about their own stuff, right?
**Dhruv Ahuja** 45:33 Yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 45:34 about… yeah, Casey, what do you mean?
Let's prioritize. Yep, makes sense.
**Andrej Kiripolsky** 45:42 And, yeah, maybe we should think first about, like, what would be the… what… like, how would we report it? Like, how would… how would it be presented to people? As you mentioned, like, it could be in the… in the livestream, it could be some kind of newsletter, or something like that.
**Dan Gomez Blanco (New Relic, Inc.)** 45:56 I think…
**Andrej Kiripolsky** 45:56 I think, based on that, we could, choose the right place.
**Dan Gomez Blanco (New Relic, Inc.)** 46:00 Yeah, so the way I was thinking is, like, this would be, you know, a report that's generated automatically, I don't know, every… Every month or so, and then only 4 basically goes in there.
We can have a look at it, if we want to get more information as a… as End-Us, sorry, I mean, as the end-user's sake, so we can say, alright, oh, actually, there's… This… this thing that had a lot of end users.
Voting for it, because all these votes will… the majority will come from End-Us.
has been merged. So, if this has been merged, does it mean that we need to do something like a… an O'Tell Me session with perhaps the… some of the people that commented on that issue, or that originally opened the issue. Do we want to do any type of content around it?
Because it is solving the end-user's problems, which is… what I think sometimes there is a… to your point, Dhruv, as well, is that sometimes there's not… Always the thing in hotel, where, like, we're not focusing on the problems that the end users want to solve.
So if we are able to… To sort of, like, tie it back in to the end-user solving the problem.
be a good thing. However, like, I get your point. I think it's… it's probably more useful for… Contributors at the moment.
And I think if we were to generate it, perhaps.
another repo, like the contributor experience one, or something like that.
Maybe a… a better… A better home for this.
**Andrej Kiripolsky** 47:40 could it live, perhaps, on the website, on opentelemetry.io? Since you mentioned that it would be, like, regularly… it should run regularly, and it should be, like, one place where we would go and… and check the results. Maybe it could be somewhere… somewhere there, and So everyone has access to it, because I think it would be a pity if… if it's something that… that we know where it lives, but other… and we would kind of act as gatekeepers for that. Like, if it's… if it's information that can be relevant for… for everyone in the… in the community, and especially the contributors, I think it might be… might, Be helpful if it's integrated with some of the tooling that everyone is already using, or some of the places that everyone is familiar with.
**Dan Gomez Blanco (New Relic, Inc.)** 48:23 Yeah, imagine, like, for example, like a quarterly blog post, or something like that, right? That does a bit of… Churning over that, maybe in the website.
Maybe not a news section on the website, but maybe, like, a quarterly blog post that says, hey, these were the… almost automatically generated. That says, this is… these are the… It could be automatic, completely automatically generated. An automatically generated blog post that says.
These are the most, voted issues.
I can race it with the comms, SIG, is what they think.
**Andrej Kiripolsky** 48:58 Yeah, that's probably… that probably makes sense. Like, I really… I think it's a little far away from what I'm usually doing, so I don't think I have a good opinion on this.
**Dhruv Ahuja** 49:11 Yeah, I had, proposed something similar in the, Contributor Experian SIG some time back, where, I had proposed that maybe a changelog or a latest update kind of section somewhere in the documentation or the contributing section for people that are interested in contributing, but if it's something that impacts the end user as well, maybe it can be a more prominent section. And rather than a blog post.
maybe individual line items there would make more sense, do you think? With individual issues or PRs linked. For example, let's say that a roadmap was decided, or something. Like, I remember there was a roadmap, the post-graduation roadmap, so something like that could be a prominent entry there, with a couple of key discussion points linked. Maybe we could just use AI for the analysis, because a blog post then would require more nuance and more I believe human intervention to deliver value to the end user.
**Dan Gomez Blanco (New Relic, Inc.)** 50:11 Yeah, I see.
Okay, cool, that's good feedback. I will think about it, and keep you posted. Yep.
Makes sense.
**Andrej Kiripolsky** 50:23 Alright.
**Dan Gomez Blanco (New Relic, Inc.)** 50:24 Alright.
**Andrej Kiripolsky** 50:25 Anything else that we can discuss before, or shall we… shall we wrap up?
Yeah, I think we can wrap up then. All right, it was great seeing you all.
**Dan Gomez Blanco (New Relic, Inc.)** 50:36 Good seeing you. Bye.
**Andrej Kiripolsky** 50:37 Alright.
