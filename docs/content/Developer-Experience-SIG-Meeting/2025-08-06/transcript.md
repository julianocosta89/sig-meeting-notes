SIG: Developer Experience SIG Meeting
Date: 2025-08-06
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:11 Hey! There!
**tristan** 00:13 Hey? Wasn't sure if anybody joined today.
**Juliano Costa | Datadog** 00:17 Yeah, I'm on holidays next week and the following one.
**tristan** 00:20 Okay. Next week.
**Juliano Costa | Datadog** 00:21 Yeah, I thought it would be a nice idea to to join today.
But actually, I don't have any any updates. So I was just texting you, but it's.
**tristan** 00:32 Yeah.
**Juliano Costa | Datadog** 00:32 Maybe it's easier to just join.
**tristan** 00:36 The so I can't. I guess I can check the notes. But I can't remember. If you had some idea for a potential small company or not.
**Juliano Costa | Datadog** 00:48 Yeah. So I reach out to link fuse. I don't know how how small they are like in the top and setup size, but I know that they are a small team.
so I reach out to them. Never heard back, and I also reach out reach out again to to mastodon, saying it would be totally fine if they just reject, but not even the rejection I got. So it's like a it's like applying for a job.
**tristan** 01:19 Okay.
**Juliano Costa | Datadog** 01:21 Sometimes. You'll never hear back from your application. So yeah.
**tristan** 01:27 Perfect.
**Juliano Costa | Datadog** 01:29 Yeah, I like your idea of reaching out the Sig meeting the the end user sync.
**tristan** 01:35 Yes.
**Juliano Costa | Datadog** 01:35 To I. But I'm I'm following the the the Github issue, where we have the the graduation and one of the one of the issues that they are they're facing is that they they need to interview adopters.
Our old tone.
**tristan** 01:57 Not really.
**Juliano Costa | Datadog** 01:58 Yeah, and they reach out to companies. And nobody replied. So like.
**tristan** 02:05 Boy.
**Juliano Costa | Datadog** 02:06 Yeah. Now, looks like someone reach out to the to them after seeing this comment and then, but like, I think they they get some names from from a company list and then reach out to that. Those names, those companies.
And then those companies never replied back. So they updated the the ticket, and then someone that wasn't reached out reached out to the to the Tlc. To kind of hey? I'm here. I can do the interview so looks like they're following up on on that with this company.
So I don't know the criteria of selecting each company or whatever. But yeah.
I know. I I what I'm trying to say is that it. It is a pain to kind of getting people to talk.
**tristan** 02:58 Interesting. Okay.
**Juliano Costa | Datadog** 03:00 I have good contact with South American well, I actually don't don't know where they they are from like the the main. Well, anyways I have a a good contact with a company that is in Brazil. Well, they are from Latin America, but they have, like a a good part of the engineering there, but they are also huge, so like.
**tristan** 03:29 Hmm.
**Juliano Costa | Datadog** 03:30 It's I would say, size of ebay Amazon.
**tristan** 03:35 Oh, really.
**Juliano Costa | Datadog** 03:37 Yeah, so, yeah,
**tristan** 03:39 Hmm.
**Juliano Costa | Datadog** 03:42 I don't think it would.
I don't think it would be different from what we have. I think they produce 6 6 petabytes of.
**tristan** 03:51 Of spends per day. Or let's that had me think not necessarily.
I don't know that kicked in my head that I know a number of people who work on, you know.
contracting job like the Run Company, is to do contracts for other companies to do. You know sites and small applications, and that kicks in my head because one of them, Brazil, is Brazilian, but the that I might by reach through those channels probably somewhat. I mean. Probably number of them are using open telemetry like a new people aren't directly involved in open telemetry work. But the I mean it's early elixir stuff, but the that might be a way to find a small application. That's a good. I'm gonna hang around in that world
**Juliano Costa | Datadog** 04:52 Those will have small deployments.
**tristan** 04:55 That's not a bad idea.
depending on how small we want to go. I mean, I guess we were talking about one collector. So yeah, that'll be that that size.
**Juliano Costa | Datadog** 05:04 Yeah, I mean, for Macedon seems yeah for mustard on. The the interesting thing was that they were deploying one collector, but they also provide the whole setup to not so people.
**tristan** 05:19 Okay.
**Juliano Costa | Datadog** 05:20 They're all instances without the collector.
**tristan** 05:22 Right.
**Juliano Costa | Datadog** 05:23 This would be the interesting part of them. But I would, I would consider, like 100 collectors.
still small.
**tristan** 05:30 Yeah.
**Juliano Costa | Datadog** 05:31 Like, if we compare to the that we have.
**tristan** 05:38 It's yeah. Okay.
I mean, yeah, hopefully, the end user. I was.
definitely, I'm gonna reach out today to the when they wake up the end user sick. But the likely they're gonna be involved with larger companies. But it's possible smaller ones.
I think.
smaller ones to have a number of things to learn from our medium and large. I mean, we could also.
if this keeps taking time. We could also kind of reform it and not do small medium large and call it something else. And just say, it's like collector user stories and put no.
**Juliano Costa | Datadog** 06:22 Yep, what? Yeah.
And then at the end of the the post, we can also invite like, Hey.
**tristan** 06:29 Reach out.
**Juliano Costa | Datadog** 06:30 You have a different story. You want to share your architecture, reach out to us. Yeah.
**tristan** 06:35 That's a good idea. Yeah, yeah. So yeah, maybe we give it.
Give it a bit more time. We can go through the channels we have. And then, yeah, we can restructure, not restructure, but retitle. Essentially.
Whole thing, not calling them medium and large, because yep.
we'll just go with those 2 for now.
Thank you.
I just said.
**Juliano Costa | Datadog** 07:03 No go ahead! Go ahead! Go ahead!
**tristan** 07:06 Well, I was gonna change the subject. So did you have anything more on that.
**Juliano Costa | Datadog** 07:10 Nope! The I just saw.
**tristan** 07:13 That we had a Us meeting last week.
**Juliano Costa | Datadog** 07:18 Okay.
**tristan** 07:19 I opened the notes. I didn't go because we haven't in forever. Nobody was joining, so I just stopped, and I meant to like go through, and, you know, have it removed if nobody was gonna be joining. And and it was 2 people who have. We've never talked to, as far as I know, I mean, I know the 1st guy from Splunk. I know him, but not through developer experience at all.
So I'm gonna reach out to them, to those 2 in the Channel and be like, Oh, sorry about that. And happy to join today. It's interesting, though, that they talked about Apache spark. I'm not sure how what they were discussing there, but that's interesting.
**Juliano Costa | Datadog** 08:01 Nice that they- they joined and updated the the.
**tristan** 08:06 Yeah, updated, it had a discussion.
**Juliano Costa | Datadog** 08:10 That's great!
**tristan** 08:12 Wait, Patrick. Wonder which, Patrick it is because there's like a hundred of pounds.
**Juliano Costa | Datadog** 08:19 Yeah.
**tristan** 08:20 But the that's interesting.
Cool to find out.
**Juliano Costa | Datadog** 08:27 So do you have a company or no companies? You are. You are not working.
**tristan** 08:33 Yeah, I'm not waiting.
**Juliano Costa | Datadog** 08:34 You know right.
**tristan** 08:34 Yeah, last day was Friday, so I'm just hanging out. I'm working on open telemetry. But they and saying at home, I mean, like talking to one company about a potential gig. But I'm not like interviewing around or anything. So taking it easy kind of this.
yeah, I guess nobody else will be joining 9 min after.
Have you started at all on the blog post, or happening dude.
**Juliano Costa | Datadog** 09:47 Just I want to share a side note. So I I'm work on a a talk that I will discuss, spend best practice.
**tristan** 10:02 It.
**Juliano Costa | Datadog** 10:03 And I wanted to to mention Weaver.
So I I went to the to their docs or to their github, and like try to to find my way around. And I was like, Yeah.
guys, the this looks like, hotel 2020, like everything is scattered. And you have like different docs everywhere. And there's like.
there are a lot of assumptions.
so I I actually gave that feedback to them and the they. They were really helpful on the on slack. But yeah, I think every time we start a project.
the committee documenting these steps to kind of do this stuff is really tricky, because the folks that are implementing the the solution. They are super in depth into what they are doing.
and they do not like. They assume a bunch of stuff because yep, for them, it's clear. So yes.
yeah.
**tristan** 11:06 Clear backstory there already.
**Juliano Costa | Datadog** 11:09 Yeah, and
**tristan** 11:12 Weaver's wild, but.
**Juliano Costa | Datadog** 11:14 Yeah, no, I love it now. Now, now that I know how to use, I love it.
**tristan** 11:18 I just learned that it could emit telemetry last week or a week or 2 ago, which is awesome.
based on a schema like I had no idea it was doing stuff like that.
**Juliano Costa | Datadog** 11:32 Yeah, this is pretty cool. Like to test the the Your schema. And how that would look like. So yeah, it's pretty nice.
And also like what I'm saying to my audience is that you can use weaver to enforce semantic like your own semantic conventions, because following hotel semantic conventions is easy, so just go and use it. But most of places have their own attributes, things that are that they they need for for their business, and those are not standardized elsewhere, so they need to kind of standardize internally. And if one team uses one name and another team uses another name, then, like charting that and like alerting and monitoring. That is a mess. So you can use weaver to kind of enforce and put the put weaver on your pipeline. So whenever someone sends a pull request to kind of validate the telemetry that this pull request is generating, and then you can kind of block the Pr. From getting merged because it has a non-compliant attribute.
**tristan** 12:52 Does it have something for that? Or do you have to write your, I mean, does it have like examples of github actions and stuff like that in here.
**Juliano Costa | Datadog** 13:00 It it does have
**tristan** 13:02 And is it? It's checking the actual emitted telemetry, not the instrumentation, I assume.
**Juliano Costa | Datadog** 13:08 So you run. You run a service called Live Chat from Weaver, and then it exposes the port for 3 17. So you send your telemetry, the telemetry from your service to Weaver, and then Weaver gives you a result based on based on your your schema and your definition.
**tristan** 13:33 Nice, alright!
**Juliano Costa | Datadog** 13:35 And I I think it's more powerful than than what I I learned till now. So there is still a couple of stuff that I I can do that. I'm not talking in the talk, and because I haven't learned. But you can kind of create regal which is the no Rego files.
**tristan** 13:58 Yeah, my.
**Juliano Costa | Datadog** 13:59 For policies and stuff. So you can create your own to kind of have different types of validations. So this is.
**tristan** 14:06 Not me.
**Juliano Costa | Datadog** 14:08 Yeah, but I I don't know how that works. i i i only.
**tristan** 14:13 Okay, that's so much.
**Juliano Costa | Datadog** 14:14 Everything that I did. I it was with Yaml and.
That's compliant.
**tristan** 14:20 Have you looked at?
Kind of, related the Ollie Gardens instrumentation score.
**Juliano Costa | Datadog** 14:27 So the thing is that weaver doesn't have it's core.
**tristan** 14:32 Well, I just said.
**Juliano Costa | Datadog** 14:33 3.
**tristan** 14:33 If it's right or wrong, or differs.
**Juliano Costa | Datadog** 14:35 Yeah.
**tristan** 14:36 Good.
**Juliano Costa | Datadog** 14:37 so instrumentation, I'm also mentioning instrumentation score to in the talk like to people to keep an eye on so instrumentation score you would send your telemetry for I don't know X days, and then you would get a score out of that like saying, Hey, this attribute is non compliant.
which what weaver would actually block from from getting merged if you properly define but besides that they also define a couple of other rules like, if you have too many internal spends.
this is, maybe a sign of over instrumenting they have, they have. They have all the the rules in the in the repo, which is.
**tristan** 15:23 Like a pretty cool, linting linting for your instruments at your telemetry.
**Juliano Costa | Datadog** 15:28 Yeah,
**tristan** 15:30 This is nice.
**Juliano Costa | Datadog** 15:37 yeah, but cool down. Another fun fact that. So I don't know if you saw. But there is this.
Oh, come on. I forgot the name.
So Cnf is doing celebrating 10 years.
**tristan** 15:54 And they have.
**Juliano Costa | Datadog** 16:00 I just missed the page.
No, I I will not be able to explain, but you have like they have, like a contribution card or something like that.
Let me see if I can find the Cnc app.
Yeah, there you go this here a little bit better.
and by checking my username here, my github handle. My 1st const- contribution to old Tab was on 2022 on the open telemetry. Airlink.
**tristan** 16:52 Oh, really.
**Juliano Costa | Datadog** 16:53 Yeah, so like it. It was the the thing that added the the column, 4, 4, 4, 3 to the endpoint when sending traces and and metrics. So I was working with hotel before. But I think the 1st issue that I actually opened and actually coming to the Github and doing stuff was this one, if it's, you know.
**tristan** 17:19 That's great.
Oh, I just pulled mine up my 2016 helm.
That's good.
**Juliano Costa | Datadog** 17:30 That that's hilarious.
**tristan** 17:32 Yeah, I guess that's they've been around 10 years. That's 9 years.
**Juliano Costa | Datadog** 17:38 2016. I didn't know how existed like it's 9 years ago.
**tristan** 17:45 Were you in high school or something?
**Juliano Costa | Datadog** 17:49 Well, 10 years ago, I think I was like working with Java, and I had like I wasn't even using it, I think.
But to update the the to update the the jar we connected to the Ftp. And then uploaded the jar and then updated in a in a database in a oracle database like the version, so that every time a user logged in it would check the version in the database. And then, okay, yeah, there is a new version. So then they click, update, and then it would fetch that. Yeah, it it was fun.
I don't miss that.
**tristan** 18:32 Yeah.
**Juliano Costa | Datadog** 18:35 So cool.
**tristan** 18:39 Yeah, very nice.
**Juliano Costa | Datadog** 18:42 It's like I. I went to to Brazil last well, this year in April, and I I gave a talk on motel there, and after the talk I was talking with a a friend, and he was like, Hey.
people are actually not using open telemetry or never heard of it like I was in the countryside. But like still, it's not like a technology that everyone is aware and are using. So it's tricky. I I talk with folks that are 10 years in a in a in a job, and they never created the docker file or container.
**tristan** 19:22 Yeah. It's still the world somewhere.
**Juliano Costa | Datadog** 19:26 Yeah, exactly. So yeah, that's interesting.
But yeah, okay, well, I'll know that I shared all the the fun facts. I'll let you go.
**tristan** 19:41 Alright, cool.
**Juliano Costa | Datadog** 19:41 Wow!
**tristan** 19:42 We got some.
**Juliano Costa | Datadog** 19:43 And see you in 2 weeks.
**tristan** 19:46 2 weeks, alright, cool.
**Juliano Costa | Datadog** 19:47 Yep.
yeah, I I will write the the blog post on Sky scanner. But just after my my holidays, if that's like, I think we still need to figure out what which? What we're gonna do, anyway.
**tristan** 19:59 Exactly. Exactly. There's time.
**Juliano Costa | Datadog** 20:02 Cool.
Okay, then.
**tristan** 20:04 Alright sounds good cheers bye, bye.
