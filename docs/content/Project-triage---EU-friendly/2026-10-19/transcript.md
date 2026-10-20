SIG: Project triage - EU-friendly
Date: 2026-10-19
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Robert Pająk (Splunk Inc.)** 07:42 Hello, hello, sorry for being late.
**Pablo Baeyens (Datadog)** 07:46 Hey, no worries. I think Severin is joining, yeah, here he is.
**Robert Pająk (Splunk Inc.)** 07:53 Well, hey.
**Severin Neumann (Bronto)** 07:54 there.
**Robert Pająk (Splunk Inc.)** 07:54 It's funny.
**Severin Neumann (Bronto)** 07:57 Sorry for being late.
**Robert Pająk (Splunk Inc.)** 07:59 Same, I just changed 40 seconds ago.
**Severin Neumann (Bronto)** 08:01 Okay, no worries.
**Robert Pająk (Splunk Inc.)** 08:03 And…
**Severin Neumann (Bronto)** 08:04 Did you… did you do anything already, or…
**Pablo Baeyens (Datadog)** 08:07 No, he joined, like, 30 seconds before you, so… Okay.
**Severin Neumann (Bronto)** 08:10 Okay.
Oh… Should I share my screen, as always?
**Pablo Baeyens (Datadog)** 08:17 Troop!
**Severin Neumann (Bronto)** 08:18 Let me see, let me see, let me see… you can see that?
**Pablo Baeyens (Datadog)** 08:24 Yes.
**Severin Neumann (Bronto)** 08:29 Happened to my noise?
Add hotel metric, exporter max batch size, environment variable for pertick Exporting metric reader.
Is this… Okay, that's,
**Pablo Baeyens (Datadog)** 09:09 This one already has a PR open with some people.
**Severin Neumann (Bronto)** 09:12 It does not mean that it was, like, accepted, right?
**Pablo Baeyens (Datadog)** 09:16 Yeah, there's some people from the TC giving support, or…
**Severin Neumann (Bronto)** 09:21 Oh, okay, yeah, yeah, yeah.
**Pablo Baeyens (Datadog)** 09:22 Cool.
I don't know.
**Severin Neumann (Bronto)** 09:36 Okay…
**Robert Pająk (Splunk Inc.)** 09:37 Yeah, I think it can be treasures accepted.
**Severin Neumann (Bronto)** 09:40 So I tag it as accepted and make… David D.
Sponsor, because he approved it, so… Or should we just accept it?
**Robert Pająk (Splunk Inc.)** 09:52 Just accept it.
**Pablo Baeyens (Datadog)** 09:54 DM.
**Severin Neumann (Bronto)** 09:58 Based on red.
R, and existing trunnels.
Cool.
Next one.
recommend exporter time bounds across… Robert, it's yours, so tell me how I should triage it. Is it accepted already?
I mean, you have created a PR.
**Robert Pająk (Splunk Inc.)** 10:33 I do not… it was a week ago. I honestly do not remember. I know that I had two similar issues.
**Severin Neumann (Bronto)** 10:39 Yeah.
**Robert Pająk (Splunk Inc.)** 10:39 I… this one, yeah. I… this…
**Severin Neumann (Bronto)** 10:43 Except that…
**Robert Pająk (Splunk Inc.)** 10:44 Yeah.
**Severin Neumann (Bronto)** 10:49 Ready?
Done.
Cool.
**Robert Pająk (Splunk Inc.)** 10:56 You can assign me, if you want, also, to the issue.
**Severin Neumann (Bronto)** 10:59 Really not sure.
Assigned comfort.
That's the PR, right? And then here, SBOM format for OpenTelemetry… Okay, okay, okay.
Seems like there's community.
discussion going on, so I put it that way.
And… Leave it like that.
And then… Huh.
Oh.
We're getting better and better.
14.
Okay.
change default trace ID format to be similar to AWS X-Ray.
Wow.
**Robert Pająk (Splunk Inc.)** 12:11 This is the issue that we recently…
**Severin Neumann (Bronto)** 12:13 Huh?
**Robert Pająk (Splunk Inc.)** 12:14 This is the issue of these tables, right? That you, I think, recently pinged on TCGC.
**Severin Neumann (Bronto)** 12:21 Did I?
**Robert Pająk (Splunk Inc.)** 12:23 I mean that the sailboat conflicts with the follow-up.
That you get this triage follow-up.
**Severin Neumann (Bronto)** 12:30 Oh, yeah, but I think that was fixed, but of course, after that, Lutmila, I think,
**Robert Pająk (Splunk Inc.)** 12:49 Yep.
You're right, this is old. We just not got to it last time.
**Severin Neumann (Bronto)** 13:05 So, I removed it.
triage labels, and I close it as…
**Robert Pająk (Splunk Inc.)** 13:14 Boy.
**Severin Neumann (Bronto)** 13:19 Additional specification around OTLP exporter retry requirements.
Also, just closing it as stale.
**Robert Pająk (Splunk Inc.)** 13:31 Yeah, also, if I remember correctly, this is very not… explicit what we should do. Like, I agree that the retro requirements are not well defined.
But at the same time, the implementations are doing differently, so I think it's just worth closing. If someone just, you know, finds a problem, then, like, personally, I just quit EPR if I find some unclarity.
And I think that having this, you know, meta, meta issue does not really improve anything.
**Severin Neumann (Bronto)** 14:04 Okay, so should I close it like that, or with an.
**Robert Pająk (Splunk Inc.)** 14:07 Yeah, that's stale. No, just, just stale.
It doesn't give any benefit having tokens.
**Severin Neumann (Bronto)** 14:12 Okay.
Return type of callbacks functions for asynchronous instruments… Okay…
**Robert Pająk (Splunk Inc.)** 14:33 Was there any… Response from anyone besides you and the author?
**Severin Neumann (Bronto)** 14:39 No.
Yes, in the past, but, like, it stalled, I closed it, and he said, like, hey, not cool, and they said, like, hey, can you… Did you have any chance to discuss this within… Let's back muting, or… I just built C-Logan, and I will ping him a few times, and if he's not…
**Robert Pająk (Splunk Inc.)** 15:11 But is it the author? I'm not sure if it's the author that you picked.
**Severin Neumann (Bronto)** 15:15 It is.
**Robert Pająk (Splunk Inc.)** 15:16 Okay, Zelto, okay.
**Severin Neumann (Bronto)** 15:17 Yeah, and he was not happy with,
**Robert Pająk (Splunk Inc.)** 15:20 Oh, dude.
**Severin Neumann (Bronto)** 15:21 Diego's Auto Review.
Yeah. I trusted, like, hey, if you…
**Robert Pająk (Splunk Inc.)** 15:39 Because…
**Severin Neumann (Bronto)** 15:39 Yep, logged on.
Path-through text map propagator…
**Pablo Baeyens (Datadog)** 15:49 This is from 2021, maybe?
**Severin Neumann (Bronto)** 15:52 It's like, old, old.
**Pablo Baeyens (Datadog)** 15:56 Maybe we should just… Close it.
**Robert Pająk (Splunk Inc.)** 16:02 If I remember correctly, this issue… I think it is indeed important. And I'm not sure if there's not any… some precedence that some Sikhs implemented them already.
Let me…
**Severin Neumann (Bronto)** 16:17 Alright.
**Robert Pająk (Splunk Inc.)** 16:18 just, send it, I don't know, our private lead to me on Slack or to our channel, and I will think about how to proceed with this.
**Severin Neumann (Bronto)** 16:28 I, I just shared in the EU…
**Robert Pająk (Splunk Inc.)** 16:31 Yeah, I will think about it more.
**Severin Neumann (Bronto)** 16:34 But I removed a follow-up for now, so if you don't do anything about it in two weeks, we will talk about it again.
**Robert Pająk (Splunk Inc.)** 16:42 Sure, I will try to do it in Cabot today.
**Severin Neumann (Bronto)** 16:46 Inheritable attributes.
Could still be useful.
Okay.
Does not seem to be a contributor.
Apprentice issue, and it's a member…
**Robert Pająk (Splunk Inc.)** 17:09 I agree with Josh, so that I will not work on it. Like, Josh suggested that he would prefer to expand on the baggage specification for this use case, and I agree with that.
Yeah, I agree.
**Severin Neumann (Bronto)** 17:22 So I find it very beneficial if attributes could be inheritable, meaning that any such elementary parents may ever…
**Robert Pająk (Splunk Inc.)** 17:37 Yeah.
Indeed. Seriously, theoretically, the collector could do it, some processor in the collector would make it. I don't think there's a reason to do it across all languages.
**Severin Neumann (Bronto)** 17:50 So, what should we… I was just…
**Robert Pająk (Splunk Inc.)** 17:53 close it as… I'll just close it as not accepted, or something like that.
**Severin Neumann (Bronto)** 17:58 Or should I give it to you, and, like, this is maybe something, like, the TC should…
**Robert Pająk (Splunk Inc.)** 18:03 I can do it on my own.
**Severin Neumann (Bronto)** 18:04 Yeah.
Yeah, okay. But I removed the triage label again, and then you can…
**Robert Pająk (Splunk Inc.)** 18:13 Okay.
**Severin Neumann (Bronto)** 18:14 Take a look.
**Robert Pająk (Splunk Inc.)** 18:16 This is an old issue.
**Severin Neumann (Bronto)** 18:17 For margin of terms?
**Robert Pająk (Splunk Inc.)** 18:27 Is that most stilet?
**Severin Neumann (Bronto)** 18:31 Okay, what was this about? Does BAC use different ways to mention Turk?
They're using backtakes for terms like, okay…
**Robert Pająk (Splunk Inc.)** 18:43 I just make a joke, because I know that you don't want to work with it, but it's a perfect thing for the docs team. So…
**Severin Neumann (Bronto)** 18:52 I mean, at the end, it's a copy editing issue, yeah, yeah.
**Robert Pająk (Splunk Inc.)** 18:55 Yes.
**Severin Neumann (Bronto)** 18:56 But the question is if we, like, tag… like, like, tag the person and say, like, hey, this is something you can… Should we allow them to open a PR for it and run.
**Robert Pająk (Splunk Inc.)** 19:08 Yes!
**Severin Neumann (Bronto)** 19:09 Yeah.
**Robert Pająk (Splunk Inc.)** 19:10 Yes, I think there's, you know, making something more clear and better, I'm not against. You can keep it open.
**Pablo Baeyens (Datadog)** 19:18 And do you think we should put it as, like, a SIG issue for the comms SIG?
**Severin Neumann (Bronto)** 19:22 No, that's not something, like, like, we're not, you're not.
**Robert Pająk (Splunk Inc.)** 19:24 goes with Lonzo.
**Severin Neumann (Bronto)** 19:25 but for copy…
**Robert Pająk (Splunk Inc.)** 19:26 But that's all.
**Severin Neumann (Bronto)** 19:26 I'm absolutely against that. That's not the… It's not ours.
**Robert Pająk (Splunk Inc.)** 19:32 It's about the consistency of the spec, that, you know, one logs is formatted like that, in metrics like that, then in one document you have capitals lower, which is… it's just a mess.
**Pablo Baeyens (Datadog)** 19:43 I mean, you do own the style guide, so that's… that was my argument, but I guess you don't own the… enforcement of the style guide.
**Severin Neumann (Bronto)** 19:51 The style guide is for the documentation, and this back is always, like.
Above the documentation, so they would need to…
**Pablo Baeyens (Datadog)** 19:59 verb.
**Severin Neumann (Bronto)** 20:01 So we said, like, we give their website a style guide, but I don't think the spec ever did that, so…
**Robert Pająk (Splunk Inc.)** 20:09 this.
**Severin Neumann (Bronto)** 20:09 Yeah, I mean, you could,
**Robert Pająk (Splunk Inc.)** 20:12 You can, you can… if you want, you can share the style guide here, because, to be honest, I… probably I…
**Severin Neumann (Bronto)** 20:19 Our style guide is fairly… we use the Google and the Kubernetes… so we use the Kubernetes one, which inherits from the Google one.
And here's a list of things that we do on top of it, which is mainly also for doc-specific, but I think the important part for you is, like, follow those two, and then here's some words that we define how to be written. Nice. Everything else is, like… I mean, if you like, we could have… we could… I could open an issue for that and link back to that one.
Or we could… How do you want to have that?
**Robert Pająk (Splunk Inc.)** 21:00 you can just drop a, you know, link here, I just do not want to waste a lot of your time just creating the issue and nobody will.
**Severin Neumann (Bronto)** 21:06 No, it's linked already, here.
**Robert Pająk (Splunk Inc.)** 21:08 That's good. Okay, there's nothing to do on your side, unless you want to work on it, but I will say.
**Severin Neumann (Bronto)** 21:15 Yeah.
**Robert Pająk (Splunk Inc.)** 21:15 Worst of your time.
**Severin Neumann (Bronto)** 21:17 Should I… should I tell them, like, hey, if you're open to help, please do, and, like, raise a PR, or…
**Robert Pająk (Splunk Inc.)** 21:22 Yes, yes, yeah.
**Severin Neumann (Bronto)** 21:24 So, should I accept it, then?
**Robert Pająk (Splunk Inc.)** 21:26 I accept… I accept it.
**Severin Neumann (Bronto)** 21:28 Yeah, you accept it. You're the sponsor.
**Robert Pająk (Splunk Inc.)** 21:31 I can… oh, no, I can… yes, I can be the sponsor. I'm me speaking very often. I can be the sponsor, and I will then…
**Severin Neumann (Bronto)** 21:39 Let me.
**Robert Pająk (Splunk Inc.)** 21:39 Right.
**Severin Neumann (Bronto)** 21:39 I make it without a… I make it without a sponsor.
Wasn't there copy editing or editorial? That's the right one.
What just happened?
Why did… why did everything get removed? That was not mine.
**Robert Pająk (Splunk Inc.)** 21:59 I don't know. I don't know.
**Severin Neumann (Bronto)** 22:01 That was not what I wanted.
**Robert Pająk (Splunk Inc.)** 22:09 I accepted.
**Severin Neumann (Bronto)** 22:14 Okay.
If you're open to help here, please go ahead and place ours.
Excess Consistencies.
Okay. The other one is triage… considered to use custom MIME types.
Any… Thoughts on that?
**Robert Pająk (Splunk Inc.)** 23:24 Closing a sale.
**Severin Neumann (Bronto)** 23:26 Do I still have my message? No.
As not planned, close with comment. Ta-da!
Make it possible to automatically list all specification requirements.
**Robert Pająk (Splunk Inc.)** 23:48 Jesus.
**Severin Neumann (Bronto)** 23:53 You said, like, keep it open?
Define resource reporting for Sipkin. I don't think that…
**Robert Pająk (Splunk Inc.)** 24:14 I think Zipkin is deprecated.
Maybe even removed, I'm not really sure. Maybe it's even removed from this pack.
**Severin Neumann (Bronto)** 24:25 Yeah, it's removed, I think, already. Provide a way for knowing when a context is made current.
Closing at a stale, or…
**Robert Pająk (Splunk Inc.)** 24:42 Yep.
**Pablo Baeyens (Datadog)** 24:42 Yeah.
**Robert Pająk (Splunk Inc.)** 24:46 This is also language specific.
**Severin Neumann (Bronto)** 24:50 Propagation exceptions and span events.
Stale.
**Robert Pająk (Splunk Inc.)** 24:56 Yes.
**Severin Neumann (Bronto)** 24:59 I will not get into any… discussions about… span event, so…
**Robert Pająk (Splunk Inc.)** 25:04 Yes, and exceptions, thanks.
**Severin Neumann (Bronto)** 25:09 Non-immediate and non-causal link.
Between spans…
**Robert Pająk (Splunk Inc.)** 25:16 Oh, Jesus.
**Severin Neumann (Bronto)** 25:23 Okay.
Yeah, but this is also, like, stale, right?
**Robert Pająk (Splunk Inc.)** 25:36 Extremely mistaken.
**Severin Neumann (Bronto)** 25:48 Standardize on exclusion functionality for HTTP instrumentations.
**Robert Pająk (Splunk Inc.)** 25:56 Hell.
**Severin Neumann (Bronto)** 26:03 Bail.
**Robert Pająk (Splunk Inc.)** 26:05 If… Yeah.
**Severin Neumann (Bronto)** 26:09 Making tracing SDK metrics aware.
What?
**Robert Pająk (Splunk Inc.)** 26:15 That's… You can close it as stale, but my guess is that it's about self-observability that CJ is already working on.
Kind of probably already solved.
**Severin Neumann (Bronto)** 26:29 Yeah.
I mean, that's… right, so, so that's, like, yeah.
**Robert Pająk (Splunk Inc.)** 26:36 Who's joining here?
**Severin Neumann (Bronto)** 26:37 Just give me a second… marks… let me see if this is, like… I think we're done.
**Robert Pająk (Splunk Inc.)** 26:46 We have… Hello, hello!
**Severin Neumann (Bronto)** 26:49 Oh, no, no, oh, I forgot to, to unlabel… oh, yeah, yeah, yeah, label… Removing debt.
Triage labels from those.
Follow-up, I think, is enough if I remove them.
Hey Jurassi, we're almost done, so…
**Pablo Baeyens (Datadog)** 27:11 Just like you did on removal.
**Juraci Paixão Kröhling (OllyGarden Inc)** 27:12 That's why I joined now.
**Severin Neumann (Bronto)** 27:14 Yeah, so we have nothing to…
**Pablo Baeyens (Datadog)** 27:16 Sweet.
**Severin Neumann (Bronto)** 27:16 us.
I think we hadn't had that for a while now.
**Juraci Paixão Kröhling (OllyGarden Inc)** 27:23 I think we did a good wave a couple of weeks ago.
on the whoops.
**Severin Neumann (Bronto)** 27:30 I mean, we can, of course, always remove that one until, like, about, like, really old issues. Oh, no!
I think everything is triaged. It's like… A biggie.
Is it like I removed… I removed the date filter?
**Robert Pająk (Splunk Inc.)** 27:46 Yeah?
Awesome.
**Pablo Baeyens (Datadog)** 27:51 Nice.
**Juraci Paixão Kröhling (OllyGarden Inc)** 27:58 Label, London, yeah.
**Severin Neumann (Bronto)** 28:01 I'm just wondering if there's a typo in, like, in the… The bookmark?
Or was it just me that I… no, I typed something while at it. Okay, okay, okay, okay, okay.
**Robert Pająk (Splunk Inc.)** 28:16 Updated.
**Severin Neumann (Bronto)** 28:18 But the up… yeah, okay, that could be that I screwed something up here. But again, like, it looks like we are… Yeah, curse.
Even without the updated, we are good.
**Juraci Paixão Kröhling (OllyGarden Inc)** 28:29 Nice.
**Severin Neumann (Bronto)** 28:31 It's a new one. Everything triaged, giving everybody back half an hour.
**Robert Pająk (Splunk Inc.)** 28:36 I have a question. Sorry.
**Pablo Baeyens (Datadog)** 28:40 No questions allowed.
**Robert Pająk (Splunk Inc.)** 28:42 maybe it's more like a homework, so I just want to ask you, do you have any thoughts on the follow-up regarding the Maintainer Summit?
Do you have any proposals for the project meeting? Who of you want… want to join, will join? You know, KubeConU wants to be on Sunday, etc?
And do we want to do anything?
**Severin Neumann (Bronto)** 29:08 Yeah, because it's on Sunday, and I will not… most likely not travel there. Maybe short notice, but I'm… But I think, like, I think we did the Prometheus hotel one, right? So I think that was very… and I also thought, like, the general, like, hotel get-together thing, I mean, nothing will come out of that, let's be honest, right? But, like, giving the people the feeling, like, hey, we are once in a room together and have a little bit of time of.
**Robert Pająk (Splunk Inc.)** 29:33 That's what I thought, even to have the opportunity to be together in one room.
**Severin Neumann (Bronto)** 29:38 Exactly. So, so, so even there, like, even if we…
**Robert Pająk (Splunk Inc.)** 29:43 Yeah.
Yeah, we'll set up.
**Pablo Baeyens (Datadog)** 29:49 I propose the Prometheus one, I'm fine with anything, honestly, I just… thing… We need to have a list of the people that will… Own it, but otherwise… If we want to do something different, I'm alone.
**Robert Pająk (Splunk Inc.)** 30:04 So, Mr. Re… So you want to repeat the Prometheus one? Because I have not heard the initial sentence.
**Pablo Baeyens (Datadog)** 30:11 Oh, sorry, yeah, yeah, yeah, like, that's what I was proposing, but I'm…
**Robert Pająk (Splunk Inc.)** 30:14 Okay.
**Pablo Baeyens (Datadog)** 30:15 with anything else. I think it's good that we explore other formats, especially because since it's a very short time slot, maybe We have to find a different format.
**Robert Pająk (Splunk Inc.)** 30:31 The one thing which I personally, but it's only my opinion, with this Prometheus one that we had, that we had these silos conversations.
that we didn't, like, talk everything together, and I'm not sure what was the outcome of this one. Like, compared to the previous ones, where we are sitting all together.
And sometimes it was just, I don't know, Austin or Morgan talking, you know, and we were just discussing stuff together as one big, unorganized team, as usual.
**Pablo Baeyens (Datadog)** 31:04 I honestly prefer the smaller conversations because, like, I feel it gets to a point where it's too many people talking at the same time, but… yeah.
I, I do think…
**Robert Pająk (Splunk Inc.)** 31:16 when you.
**Pablo Baeyens (Datadog)** 31:17 It was very short, and the outcome was… Well, we have this Google Doc, we share that, but… there was not a lot of follow-up, honestly, and I don't know. That's something that I think we should improve on. The… Like, we're not going to decide anything in 35 minutes, but maybe we can… more things into issues, or somewhere other than a Google Doc that is going to be more red.
**Juraci Paixão Kröhling (OllyGarden Inc)** 31:46 We had a maintainer session, a maintainer… a meeting, project meeting during Maintainer Summit in Atlanta, I think it was. I felt like that was quite… quite good. I mean, way better than the Prometheus one that we had in Amsterdam this year.
I would… like, if anything, I would frame or use that one from Atlanta as a… as a… As the standard, like, as the format.
So…
**Robert Pająk (Splunk Inc.)** 32:17 Unless I was there, how was it working? Because I do not remember, and I was there.
**Juraci Paixão Kröhling (OllyGarden Inc)** 32:23 So, there were… there were some tables, the GC was also there, most of the GC. We had a few topics to discuss. I remember library discussions with, with, Tigran as well, like, we made quite a good comments on… on community health needs, how do we assess that, the state of PRs, and so on.
I feel like the discussion in general was good.
And people… and even we got people from outside of the community to join in asking us questions.
people from adjacent projects in the CNCF, so maintainers of other projects. So I feel like that is…
**Robert Pająk (Splunk Inc.)** 33:08 Yo!
It was more healthy, it was more interactive.
**Juraci Paixão Kröhling (OllyGarden Inc)** 33:12 It was a… yeah, exactly. So it was less of… less… less… it was more like a team building, from my perspective, than a… a proper, like, let's… Because, you know, follow-ups are not… they're never going to be followed up on. I remember, like, Hotel Unplugged, so many things were discussed, and my impression that… I'm not day-to-day anymore in the project, so perhaps my assessment is unfair, but my impression is not much was followed up on. Like, so many discussions happened,
**Pablo Baeyens (Datadog)** 33:45 But I think that is a problem of the format, like…
**Juraci Paixão Kröhling (OllyGarden Inc)** 33:49 Yeah.
**Pablo Baeyens (Datadog)** 33:49 We could have followed up on things if we wanted to, we just didn't have anybody that was, like.
**Severin Neumann (Bronto)** 33:54 Doing the world.
**Pablo Baeyens (Datadog)** 33:55 Make sure it will slow up.
**Robert Pająk (Splunk Inc.)** 33:57 Exactly. I'm on the other camp.
We are in the open source project.
And not everyone is possible to be there, and I do not think it will be effective to make any decisions and make any real planning on such meetings. I think it will be elsewhere.
**Severin Neumann (Bronto)** 34:15 That's what I said, or I think shared also in last week at the meeting. I think the important part about this meeting is really to get people into a room, so they have, like, they see each other in person, they are able to interact with each other in person, and maybe two people or three people agree on, like, hey.
Looks like we in this language and that language have the same problem, let's talk about it post this event. But what I always like about those ProChank get-togethers is really more like, hey, finally I see people in person, or I get…
**Robert Pająk (Splunk Inc.)** 34:50 This is the main reason I go to these conferences.
**Juraci Paixão Kröhling (OllyGarden Inc)** 34:53 Yes, you were there, you were there, Robert. Like, you and Severin were there. Like, I can see you in the picture here, yeah.
**Severin Neumann (Bronto)** 34:58 Yeah, exactly.
**Juraci Paixão Kröhling (OllyGarden Inc)** 34:59 Yeah, so I think we're all aligned. Like, I think the reason for not following up is exactly, like, there's so many people outside… from the community, not here. They should know and be part of the discussion, so there's no point in having a discussion up to the end or making decisions here without those people. So, that's why I think it is way better to have a… team-building kind of exercise, or something like that? Like, Let's have a high-bandwidth discussion, things that we would not want to do in a recorded session, or anything like that, instead of, let's get something done.
We're not gonna get something done.
**Pablo Baeyens (Datadog)** 35:47 Doop.
Who's going to propose what, and own what?
I guess that's my question, because I feel like that's fine, but who's going to do it?
**Juraci Paixão Kröhling (OllyGarden Inc)** 36:02 I'm so over-committed at the moment, I cannot just open my mouth anymore to suggest anything.
**Robert Pająk (Splunk Inc.)** 36:10 I can do it just right on the thread, if you like this, I just want to have any, you know, asynchronous feedback in the channel, if you think that's a good way. Diana also has written to me that she can also help me.
in moderating this, so I could already have some people, or I saw that Alolita also has written that she can help with the moderation, so I think there'll be people there anyway, so I can propose it even myself. I just want to make… I just want to make sure that I'm not, you know, stealing some idea, and yeah.
let's just make it happen that we'll have opportunity to be in one room, and just not miss, you know, this opportunity. Even if it will be 10 people of us, or whoever. Juraci plan to be on the KubeCon as anyway?
You?
**Juraci Paixão Kröhling (OllyGarden Inc)** 36:58 What is that? What is the question?
**Robert Pająk (Splunk Inc.)** 36:59 You plan to be on the… on the…
**Juraci Paixão Kröhling (OllyGarden Inc)** 37:01 Yeah, yeah, I was, yes, I was just looking at my calendar. I'm getting there on Saturday at 9pm, which is…
**Robert Pająk (Splunk Inc.)** 37:10 Thursday night, I'm so excited.
**Juraci Paixão Kröhling (OllyGarden Inc)** 37:12 Yeah, which is 4PM our time here in Europe, so… I don't know the state that I'm gonna be when I get there, but I'll try to be there on Sunday by the Maintenance Summit.
**Robert Pająk (Splunk Inc.)** 37:25 I will talk to you all.
**Juraci Paixão Kröhling (OllyGarden Inc)** 37:26 What is that?
**Robert Pająk (Splunk Inc.)** 37:27 I will take you a pillow.
**Juraci Paixão Kröhling (OllyGarden Inc)** 37:29 No, I'll be there, I'll be there.
I'll be there, probably… I mean, if it is the very first session of the morning, then I might not be there, but if it is closer to noon or afternoon, I'll be there, yeah.
**Robert Pająk (Splunk Inc.)** 37:46 Awesome.
**Pablo Baeyens (Datadog)** 37:53 Should we post on, like, auto maintainers, or somewhere to find people?
**Robert Pająk (Splunk Inc.)** 38:00 Yes, it would be awesome. Do you want Pablo just to write it down? I can, you know, I can organize the follow-ups. I just want to be sure that I'm not acting as myself and telling, oh, other people said that they agree, because it won't be fair.
**Juraci Paixão Kröhling (OllyGarden Inc)** 38:13 No, yeah, just tag me there. If you write there, tag me, and I can just react and say, yes, I'll be there.
**Robert Pająk (Splunk Inc.)** 38:20 Okay, so I can just put and tag all three of you, and yeah.
**Juraci Paixão Kröhling (OllyGarden Inc)** 38:24 I think… Yeah. Yeah.
**Pablo Baeyens (Datadog)** 38:26 Yep.
**Severin Neumann (Bronto)** 38:28 Okay.
**Robert Pająk (Splunk Inc.)** 38:32 Okay.
**Juraci Paixão Kröhling (OllyGarden Inc)** 38:36 That's it. Cool. So… See y'all soon.
**Severin Neumann (Bronto)** 38:40 See you, bye-bye.
**Robert Pająk (Splunk Inc.)** 38:41 Bye.
**Pablo Baeyens (Datadog)** 38:42 Bye.
