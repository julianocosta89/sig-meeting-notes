SIG: Community Demo App SIG
Date: 2025-07-02
Duration: 26 minutes
Zoom Recording URL: https://zoom.us/rec/share/pP-ihrTxJqxxdbM-cOUlGrOyhSkgG_o18j05N7zmSxfF9Pq1fESaCOr6741VN9p1.G70HduNAhjFTr294
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:34 Hello! Hello!
**Ani ( Opensearch )** 00:38 Hello! Hey! There! How are you?
**Juliano Costa | Datadog** 00:40 I'm good. How are you?
**Ani ( Opensearch )** 00:41 Good morning. I have multiple conflicts today. I might stay for some time, but might need to drop.
**Juliano Costa | Datadog** 00:50 Yeah, no worries. I just Ju, just one thing that I want to to to ask you. Have you seen the the message that I tagged you. I was trying to add you and.
**Ani ( Opensearch )** 01:04 Yes, I need to add, do the hotel approval thing. Yes, this week I'll wrap it up.
yes.
**Juliano Costa | Datadog** 01:16 Awesome.
**Ani ( Opensearch )** 01:17 Thank you for that.
Everyone. Yeah, that's true.
**Juliano Costa | Datadog** 01:23 Hello!
**Alessio** 01:24 Hey! How are you?
**Juliano Costa | Datadog** 01:27 Understood.
**Alessio** 01:28 Actually.
**Juliano Costa | Datadog** 01:29 Yeah, it's a pleasure awesome. Yeah, I I love seeing Brazilians around. So.
**Alessio** 01:34 Actually, I'm not.
**Juliano Costa | Datadog** 01:35 You're not. Oh, wait!
**Alessio** 01:38 I'm Italian.
**Juliano Costa | Datadog** 01:39 Okay, maybe I misjudged you on the by the name. No. But I confused you with someone that open a issue recently. Yeah, okay, yeah.
**Alessio** 01:50 Okay, no no worries.
**Juliano Costa | Datadog** 01:51 That's right.
**Alessio** 01:52 Don't worry, don't worry. I see you've got plenty of tattoos, actually. So it's something that.
**Juliano Costa | Datadog** 01:58 It's awesome and yeah, cool. Well, well, I think it's your 1st time joining the this. This thing right?
**Alessio** 02:06 Yeah, it's actually my 1st time I actually like I started like I knew open telemetry for from like since ages, basically. But I never like leverage that in in like very deeply.
especially from the you know, from the receiver point of view, like usually you just collect of internal imagery things, and you send them over to tool tools like Datadog, for example. And instead, now I'm working at Suzy at the in the observability team. And so I wanted to learn. Actually, like I get my as dirty.
And basically the the 1st thing that I noticed when I when I read like the news. The blogs and the stuff like that was that you deprecated the elixir service. But you were interested in bringing some elixir back and been like an alchemist in the past. And I still.
I'm I'm very fond of elixir, actually. So yeah, I I'm that guy actually, that asked you.
**Juliano Costa | Datadog** 03:13 Yeah, we've we've been looking for you. Awesome.
**Alessio** 03:16 Lately.
**Juliano Costa | Datadog** 03:17 Well, I don't. I don't think we have many folks with elixir or airline experience.
**Alessio** 03:26 Okay. I've nothing.
**Juliano Costa | Datadog** 03:27 Worldwide. It's not just in this city.
**Alessio** 03:31 Okay.
**Juliano Costa | Datadog** 03:32 Yeah.
**Alessio** 03:33 Cool.
**Juliano Costa | Datadog** 03:34 So I I think we briefly discussed in the.
**Alessio** 03:39 Yeah, in the channel.
**Juliano Costa | Datadog** 03:40 In the channel already. Yeah, let me just bring that back.
Hey, Pierre? Hey, Roger?
Hello! Hello!
**Alessio** 03:47 Okay.
Hi, everybody.
**Juliano Costa | Datadog** 03:51 So I think that the the main concern here is adding an extra service.
And That that was the 1st suggestion from Pierre, and I was like, come on, Pierre, you are the the 1st one that we would have had the Gym service.
**Pierre Tessier** 04:12 Can we replace one then? But, like my, my sense is just, hang it off of Casco.
**Juliano Costa | Datadog** 04:18 Well, this is the easiest way to plug and unplug things.
So I would say, if we do not have any other choice. Yes, but I was checking the the architecture.
and we have so we have checkout and product catalog. Both are in go, and I feel that in the future. We may need to showcase, auto instrumentation and manual instrumentation.
**Alessio** 04:53 Okay.
**Juliano Costa | Datadog** 04:53 The alto instrumentation is not there yet.
so maybe we could replace one, and whenever all the instrumentation comes, we think about it.
**Ani ( Opensearch )** 05:03 On Saturday would be my last.
**Pierre Tessier** 05:04 I just want to call out the history of elixir with the optometry demo, and why? It's not in the demo today.
And that reason why was lack of elixir talent on the demo sick team and back. Then we had it as a feature flag service. And so it was.
you know it was called almost all the time, and the lack of any skill set there meant that a critical component of the demo was highly at risk, and it. It often caused us pain. And eventually we just said, Let's rip it out and replace it with open feature, because open feature built like flag. D something that we could use.
**Alessio** 05:44 Yeah.
**Pierre Tessier** 05:45 So we ripped it out, and and that's my hesitation on saying, Let's put elixir to replace like product catalog, for example.
because it's called so often.
**Juliano Costa | Datadog** 05:56 Yeah, it is.
**Pierre Tessier** 05:57 I would care less if, like we did like quote or shipping.
The product catalog is called everywhere.
That's my only hesitation.
**Juliano Costa | Datadog** 06:06 But you, you actually gave me a nice idea up here. What about replacing the flag? Dui?
Yeah, I know it.
**Alessio** 06:15 Another time.
**Pierre Tessier** 06:16 That would be amazing. I would be all for that.
**Juliano Costa | Datadog** 06:19 Because now.
**Pierre Tessier** 06:20 Do that in elixir.
**Juliano Costa | Datadog** 06:21 We don't rely on on the on the flag Dui anymore. So if it if the Ui crashes, all the services will work fine with, because they they query the the flags from flag, d yeah, from from flag d exactly.
Deflect the ui.
**Pierre Tessier** 06:38 Ui currently is not instrumented either for what it's worth.
**Juliano Costa | Datadog** 06:41 It is, it is, it is.
But you need to navigate to slash feature, and then you get traces from from it.
**Alessio** 06:51 Okay.
**Juliano Costa | Datadog** 06:52 So, yeah, yeah, so it it would be a nice like.
**Alessio** 06:58 Starting point for you. Okay.
**Juliano Costa | Datadog** 07:03 It's it's funny, because we removed yeah, it like.
But then, yeah, but.
**Alessio** 07:11 Yeah.
**Juliano Costa | Datadog** 07:11 It's like.
**Alessio** 07:12 I actually asked you like for for that specific reason, because actually like you, you just remove that. And now you wanna like, bring it back, basically. But yeah.
**Pierre Tessier** 07:23 Well, because if Flag D is a part of the critical path.
the ui was not, and back. Then, when when we had it in elixir. We use Phoenix to build a ui.
and then we we had all the Api calls still in there as well. So it is interesting because we're keeping the critical thing being its own self and and the ui in this case here, it just modifies a Json file. If I'm mistaken, that's all it does.
and and it just rewrites and resaves it, and then Flag D picks up, changes to that Json file and works with it. For what it's worth flag. The Ui does it do ice.
I know. Actually, yeah, I take all that back. Yeah. So yes, that would be it. That would be its use. Case.
**Alessio** 08:09 Okay. Cool.
Go with that.
**Pierre Tessier** 08:13 And I don't hate this at all.
Giuliano. In fact, I love the idea by Dui being rewritten in elixir is a fantastic idea.
Because you're right. Why do we want a vercel flavor and a next Js opentelometry like, like, we're just getting too many flavors of Js instrumentation at this point.
**Alessio** 08:32 Oh, my God!
**Pierre Tessier** 08:32 Right.
**Alessio** 08:33 Right.
**Pierre Tessier** 08:34 We have the act native as well, for the mobile tier, like like we've got Js instrumented 12 different ways in here, and we probably not that many, but we. We don't need that level of repetition, repetition almost.
**Alessio** 08:49 Yeah, thank you. Very.
Cool thanks, everybody like.
**Pierre Tessier** 08:54 Yeah, if you want to try going navigating the feature, you'll see. It's a very simple Ui, it reads so A. Json file. It just renders it. I don't care if the new ui looks the same or not.
Capability wise. All we really care about super simple interface where you click on a flag and easily change it from on or off.
There are some flags that support a set of numbers as well, so we'd have to be able to support that and the ability to input those those separate numbers. I think right now it's all just dropdown but that would be, that's all we need.
**Alessio** 09:28 Cool. Thanks. Yeah. It looks feasible. By the way, you know, like.
**Juliano Costa | Datadog** 09:34 Awesome. Yeah, I'm excited.
**Pierre Tessier** 09:37 Yeah, okay.
**Alessio** 09:37 Actually.
**Juliano Costa | Datadog** 09:39 Oh, we we actually need to start thinking about releasing a new version. So I think we we can wait for that.
**Alessio** 09:48 Okay.
**Pierre Tessier** 09:49 Yeah, how long?
**Juliano Costa | Datadog** 09:49 No pressure.
**Pierre Tessier** 09:50 Just just so. We have a sense here. How long would you think it would take to to deliver like a draft Pr, or something like that. That's functional in this area.
**Alessio** 10:00 I really don't know like today. But yeah, I don't know what's your timeline for the month, because maybe.
**Pierre Tessier** 10:07 We don't have one.
**Alessio** 10:08 One I don't know, because maybe like it takes one month, and because I have the jobs and and all that, all the other stuff.
and I could convince my manager like Suzy, has a very excellent posture about that. Like I'm a principal engineer, I can. I'm going to do an upstream contribution and open telemetry. I need some time. And so, yeah, I can set up some time in the working hours. But like we, we have a lot of stuff on our plate. And and this is observability team. So yeah.
I feel like, I, I don't wanna be like the the person that comes to my team and like, Hey, I'm going away for 2 weeks to to build something upstream.
It's okay.
**Pierre Tessier** 10:57 Think, generally speaking, with with.
I think. Look, we're all developers here. We've all we've all written code in our lives.
The syntax of Erling really throws a lot of us off, I think, is is probably, but we could eventually get it figured out. It's just. It's hard for us. It's not. It's not natural, like, we could look at Js code like, Oh, yeah, that's what's wrong with it, or or go code.
**Alessio** 11:20 Yeah, no, no, actually, actually, I'm very proficient at elixir. Like, I, I built an elixir system at Susie until like 7 months ago. So yeah, that's the it. The the elixir part would be the least the least difficult part. The the only thing is like I I really.
I don't know how much time I have right now, but I can for sure deliver results.
**Juliano Costa | Datadog** 11:46 Awesome.
No, the question wasn't too much to to put a pressure on you. So actually, maybe we could go and release a new version. Because, if we take a look at the unreleased change log, it's
**Alessio** 12:03 A lot of stuff. Yeah.
**Juliano Costa | Datadog** 12:04 A lot of things, and then, whenever a new service lands, we we can ship a new one.
**Alessio** 12:10 Yeah, sure I can. I can just like do a draft pr and keep that updated like on by like from my fork, right okay, cool.
**Pierre Tessier** 12:21 Yeah, and just make sure your fork is your personal fork, not a company fork. So it's
**Alessio** 12:25 No, no, no, yeah.
**Pierre Tessier** 12:26 We could, we could merge from Maine against it, that's all.
**Alessio** 12:30 Sure!
Perfect thanks.
**Juliano Costa | Datadog** 12:35 Thank you.
**Pierre Tessier** 12:38 That's awesome. Now I'm excited about that. And yeah.
Julia, did you take these notes in the meeting, Doc?
**Juliano Costa | Datadog** 12:48 No.
**Pierre Tessier** 12:49 We should do that.
**Juliano Costa | Datadog** 12:50 Should do that. Yeah.
**Alessio** 12:52 Yeah. Actually, the the way I like stepped on this is because we have 2 demo environments for observability. One is the auto environment. And I don't know if we actually have one public, because I saw you also showcase like public environments. But with the like, the the demo deployed publicly.
and the other one is like a bespoke demo that we that we energe over time. It's very legacy.
and I just wanted to to give contributions to the auto demo. And I saw like.
there's this elixir service we would like. And I was like, Oh, okay.
**Juliano Costa | Datadog** 13:40 Cool, cool, cool.
I think we have also something from from Jonathan. Jonathan. Did you have the chance to to take a look at that. I I think you, replied the comment. Right? But you I I saw that to take a look.
**Jonathan Munz** 13:58 Yeah, I saw the comment. I haven't had a chance to take a look yet. I think it should be a pretty small change. I just needed to get back.
get everything like set up and running again.
**Juliano Costa | Datadog** 14:07 Wish I had.
**Jonathan Munz** 14:08 And in a little bit. But yes, that's still on my radar to to take a look at.
**Juliano Costa | Datadog** 14:13 Cool and I think Shana, you you got approved as member. So I I'll open up here.
**Shenoy Pratik** 14:24 So much for the support.
Yeah, no worries.
**Juliano Costa | Datadog** 14:29 I let let me check one thing here on the on the notes.
Yeah, I I most probably will open up here to add you as as approver on the demo.
So then you just need to.
I think you don't need to do anything. But yeah.
**Pierre Tessier** 14:56 No, we just need to merge it. We're good.
**Juliano Costa | Datadog** 14:58 Yeah, okay, cool. And Roger, you have all the permissions. Right, I think you already immersed stuff. So very good.
awesome.
Cool, okay, do we have anything pending? I think the last week was busy. But the the Prs were flowing through. So yeah, I think we have the dopper thing that we need to decide.
I I worked a bit on it, but it's really difficult to to make it work. So I I I actually will try to get a meeting with Henrik, and we go together through the through his Pr. And and see what what is going on there.
**Pierre Tessier** 16:01 I mean, we have this duplicate spam thing.
It's actually 2 spans with span kind server that show up in the front end that Cedric Diesel mentioned.
It makes sense like we. We should not have that.
I think what's happening is the Htp. Instrumentation is saying, hey, I'm getting a request in span server span kind server, and Nextjs is saying, Hey, I got a request coming in. Spend that kind server and they're both right, but they both can't be right at the same time.
Or it's not for proper semantics, should we? And and the information capture on each fan is different.
So I think you know, we should probably make a decision. Do we want to disable Http, Http, in auto instrumentation on the front end, and just depend on nextjs auto instrumentation?
Or do we want to do something in the collector where we changed span kind to internal for the next js, where it's in that path.
**Juliano Costa | Datadog** 17:19 I will give the question back to you. If we were using auto instrumentation.
both instrumentation would be added right.
**Pierre Tessier** 17:31 Yes, and it would both be set to server.
**Juliano Costa | Datadog** 17:33 So we would need to on the auto instrumentation configuration disable. One of them.
Yeah.
**Pierre Tessier** 17:40 Or in the collect, but the the span attributes collected by each one are different. And there's I could see that being useful on on either case.
**Juliano Costa | Datadog** 17:56 What a what do you think about maybe raising this to the Js. Sig.
and see what they think, because.
honestly, I don't know if that should happen.
I know that they are different instrumentation libraries. But I guess one is relying on the other. No.
but they are totally different. And then.
**Pierre Tessier** 18:27 But it it like.
Can you use nextjs without an Http.
**Juliano Costa | Datadog** 18:33 Exactly.
**Pierre Tessier** 18:33 Javascript, right.
**Juliano Costa | Datadog** 18:35 That that's the that's the point. So like Nextjs should capture everything that it should be captures and then surprise it, or I don't know.
because having 2 server is wrong. 2 servers.
**Pierre Tessier** 18:54 Okay, so let's just say, we're not gonna do anything for now pending outcome from what the js sig thinks, we should do.
Yeah, I think next year I should change their stuff to not be server, I guess.
**Juliano Costa | Datadog** 19:15 I, I remember from my previous employer that I will not say the name, but that when you when you have like.
When you define instrumentation, they require a specific order of declaration, otherwise the instrumentation wouldn't work.
**Alessio** 19:40 Conflicted.
**Juliano Costa | Datadog** 19:42 Yeah, something like that.
So like, I think this the the 1st Instrumentation library should be I I don't remember. But like Http. And then the second one, whatever other was, because the second one was relying on the Http instrumentation.
So I don't know if this is the same for Nextjs.
**Pierre Tessier** 20:12 Next Gen. Still has a bug where they're still adding.
I car. Now, the Urls to span names.
I'm gonna I'm gonna assume we need to get Nextjs instrumentation cleaned up.
and there's probably a greater need and push for that at this point, and maybe we should go back to the jsig and saying, Hey, can you like clean this up? Because it's it's it's out of its back, and it's breaking things, and it's causing pain.
**Juliano Costa | Datadog** 20:42 Yep.
**Pierre Tessier** 20:44 Right? Because without if you, if you have nextjs auto instrumentation and you have a span metrics connector, which is a common configuration, you will break your Prometheus.
which is also a common configuration.
Okay?
Well, let's take a note that then we should go to the Sig. Js team.
Anybody at your company works on 6 as Juliano.
**Juliano Costa | Datadog** 21:13 I don't think so, but I know Mark from from yeah. Then a trace.
**Alessio** 21:24 Can't you just yell at them like on the slack.
**Juliano Costa | Datadog** 21:29 Hey? Yes.
yeah, we can, but and most probably they, they will say, Hey, you are welcome to contribute it.
**Alessio** 21:36 Oh, okay.
**Juliano Costa | Datadog** 21:39 Yeah, I I they did the a lot of rework on the SDK 2 dot. O, so I know that they they've been busy. And now there is the browser seat also being started, so that will also divide like developers into.
So I don't know if they have.
Well, I don't think they are splitting. They are just creating a new Sig focused on on browser instrumentation.
What I was. What I meant is actually that.
**Alessio** 22:19 The Js developers that were working on one may now focus on the other, and then the the workforce on the sync reduces.
**Juliano Costa | Datadog** 22:28 So.
**Pierre Tessier** 22:32 Okay, is our efforts for the Js, I think we're loosely part of the Js honeycomb, but we're pretty heavy on the new web, Sig, though.
but I'll see if I could just bug Jamie on our side. I think she may be able to like. Help me usher this with some additional urgency, but I will see or or tell me how to navigate it to netsake.
Okay.
Alessia, just for tracking. Did you say you were part of seuss.
**Alessio** 23:06 Exactly.
**Pierre Tessier** 23:08 Okay. Thank you.
**Alessio** 23:10 Yeah.
**Pierre Tessier** 23:14 Yeah, Julia, I think we're better shape now, and we got in.
We're adding an approver. We got a maintainer. We're we're adding humans which I think we needed.
**Juliano Costa | Datadog** 23:30 Yup!
**Pierre Tessier** 23:31 Okay.
**Juliano Costa | Datadog** 23:32 Yeah, okay, any anything else? I don't. I don't think we have any any pending stuff. I'm open. Just so. So you all know I'm opening a Pr that adds the nginx metrics receiver to the collector, and also adding a dashboard in Grafana. But yeah, not being that like like, not a big change. Just the new.
**Pierre Tessier** 24:00 Does that mean? We need to open up a port on a services or to capture this data.
**Juliano Costa | Datadog** 24:06 No, we have. We already have nginx service, that is the where's my Pr. Oh, too many tabs.
**Pierre Tessier** 24:15 Does? Does nginx just expose them on a standard port?
**Juliano Costa | Datadog** 24:20 I just had to configure the as soon as I find it I'll let you know.
**Pierre Tessier** 24:25 Sure. Okay, I'm thinking Kubernetes is really where I'm thinking of, because then we have to do some fancy stuff to add the port there as well.
**Juliano Costa | Datadog** 24:32 Yeah, no, no, no need to. No need to to open a port.
It's just an extra configuration that I add to the to to the.
**Pierre Tessier** 24:47 Your next call.
**Juliano Costa | Datadog** 24:48 Provider. Yep. So I just had a new location slash status.
and then the the nginx receiver queries that so perfect we we will need to change the the yamo files. But just adding extra environment variables.
Yeah, this. This is easy, I think.
Oh, cool. Okay.
**Pierre Tessier** 25:20 Amazing.
**Juliano Costa | Datadog** 25:21 Then.
Well, have a great rest of week, and enjoy your holiday, Pierre, now that you celebrate 4th of July.
**Pierre Tessier** 25:32 I? Well, no, I actually I celebrated yesterday, July 1st Canada day. I I got to, and I had to send a couple of messages out to a few people as well, saying, I'm not doing July, 4th celebration, my family. We actually have plans to do a big thing. The town was throwing a big event.
So we we did that, and it was it was fun, although I'm now realizing on Friday none of my coworkers are going to be around, so I will be working lonely.
It'd be great.
**Juliano Costa | Datadog** 25:56 It. It's good to have calm, base.
**Pierre Tessier** 26:00 Yes, yes, I could get some documentation done.
**Juliano Costa | Datadog** 26:06 Awesome.
**Pierre Tessier** 26:07 Thanks, everybody.
**Juliano Costa | Datadog** 26:07 See you all, bye.
**Alessio** 26:11 Bye.
