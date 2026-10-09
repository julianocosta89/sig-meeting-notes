SIG: End-User SIG
Date: 2026-10-08
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Julia Furst Morgado (Dash0)** 00:22 Hello?
**Daniel Rolles** 00:27 Hi there.
**Julia Furst Morgado (Dash0)** 00:29 How are you? Nice meeting you.
**Daniel Rolles** 00:31 Nice to meet you!
Yulia?
**Julia Furst Morgado (Dash0)** 00:34 Yes, Julia.
**Daniel Rolles** 00:36 Here they are.
**Julia Furst Morgado (Dash0)** 00:37 First time, first time joining this call. Have you, have you joined a lot of, of these calls?
**Daniel Rolles** 00:42 No, it's my first time as well.
**Julia Furst Morgado (Dash0)** 00:44 Oh, okay. Let's see.
**Daniel Rolles** 00:49 Let's see, let's see who turns up.
**Julia Furst Morgado (Dash0)** 00:51 Exactly. Yeah. Usually I think there is either a maintainer from the the project or someone from the governance committee that joins. I don't know.
**Daniel Rolles** 01:04 Have you…
**Julia Furst Morgado (Dash0)** 01:06 Are you an end-user?
**Daniel Rolles** 01:08 Yeah, yes.
Yeah, and potentially contributor, so the reason why we're joining the call today is,
**Julia Furst Morgado (Dash0)** 01:15 Awesome!
**Daniel Rolles** 01:16 is we've just raised, some issues and potential RFCs in the, semantic convention.
In the repo. So, yeah, we've been doing some work previously with the Open Lineage community. So, from a data observability perspective, not a software and infrastructure observability perspective. So, yeah, we've, just raised, a… piece of work with them.
With the OpenEdge, with OpenTelemetry, and with…
**Julia Furst Morgado (Dash0)** 01:48 Yeah.
**Daniel Rolles** 01:49 with MCP.
**Julia Furst Morgado (Dash0)** 01:50 Cool, cool. Yeah, no, I'm not… I'm not an end-user, I'm a contributor as well. I contribute a lot to the documentation, so the SIG comms, the communication.
But, I'm always curious to know about the other SIGs, so I'm trying to join calls from other SIGs, and today I decided, oh, I have some free time, let me, let me join this call. So yeah, but nice meeting you.
**Daniel Rolles** 02:21 Nice to meet you as well.
**Julia Furst Morgado (Dash0)** 02:23 Hi, Dan.
**Dan Gomez Blanco** 02:25 Hello.
**Julia Furst Morgado (Dash0)** 02:25 Hi, everyone.
**Daniel Rolles** 02:30 Hello, Dan.
**Dan Gomez Blanco** 02:32 How's it going, Daniel?
Okay.
**Daniel Rolles** 02:33 Alright, how are you?
**Dan Gomez Blanco** 02:35 Good, good, good.
Yeah, just like… It's just meeting after meeting today. Yeah, and also, like, had to talk in all of them, so, like, you know, throat… my throat is, like, suffering.
**Daniel Rolles** 02:48 They're not the usual join and turn your camera off and just hope that you don't get asked a question.
**Dan Gomez Blanco** 02:53 Yeah, and send your agents to do things, what you're like, on the background.
Yeah.
Cool, cool, cool. Let me just bring up the agenda.
**Ernest Owojori** 03:40 Hello, everyone. Just confirm my mic is working.
**Sophia Solomon** 03:46 Hey, everybody!
**Ernest Owojori** 03:49 Sophia.
**Dan Gomez Blanco** 03:52 I'm gonna try to add whoever is here on this call.
By the way, I'll post the notes here in the chat.
Yeah, so if you have any, Any topics that you would like to add to the agenda, feel free to add them.
**Daniel Rolles** 05:10 Dan, if you're okay, at this juncture, probably just… unfortunately, I can't stay the full meeting, but I just wanted to flag to the community an issue we've just raised on semantic conventions, and I thought it was worthwhile for the end-user community.
And probably just in this meeting, if you're okay, again, only for gender allows, because I realize it's a last-minute addition, but just wanted to flag that we'd raised the work we've been doing in the bearing node lab, etc.
But again, only if it's okay. I don't want to gate crash. This is my first SIG meeting. So only if that's okay.
**Dan Gomez Blanco** 05:46 Yeah, absolutely. If you have a time limit as well, just go ahead and… I'll add you to the agenda at the top. Yeah, so… Can you, yeah, drive us through it and then we can.
**Daniel Rolles** 06:00 Yeah, sure.
Yeah, and let me just give you a thumbnail. Unfortunately, I've had to… I can only give it 30 minutes, well, next 20 minutes or so, and I'm on a network that I haven't got proper access, so you'll have to excuse me. I would bring my… share my screen and show everybody what's in the lab, etc.
Let me just back up and introduce myself, because I'm conscious this is my first meeting. Dan, you and I have met before, but let me just, let me introduce myself to everybody. So, hi everybody, Dan Rolles.
Founder and CEO of BearingNode.
We Bering Note is a data analytics and AI consulting firm based out of London.
Unfortunately, as you can see from the grey hair, I've been at this a while, grey hair and grey beard.
I, I've been at this 30 years. Started my career in a real estate investments business, back in the 90s. Again, showing how old I am. But for the last 20 years, I've been working with financial services, northern and southern hemisphere, doing consulting for chief data and analytics officers and, and risk teams and data teams inside banks, insurers, asset managers, etc.
We have been working with the Open Lineage community, for about the last 24 months, 18 months, really trying to work on data observability. And, as Dan will know, I've attended many, many of an event on software and infrastructure observability, i.e. OpenTelemetry.
And we've been looking for the intersections, and working with the community on the intersections between those two.
Over the last… over summer, we've launched the Bering Node Lab, which you can find on GitHub, and there's some posts also about it on our… on our blog.
And the first work stream within that lab we've landed is something called… we're calling MCP Lineage. So what we've tried to do is we've actually tried to show lineage both on a infrastructure and service observability perspective, the calls, and align ourselves to trace and span IDs, and parent trace IDs.
But also make sure that where the MCP is reaching to a governed data set, and the scenario we've built is around a Postgres instance, so a governed Postgres instance, and we've actually built a fictitious business called ObsInsure to model a commercial insurer.
To try and make the use case as real as possible.
We've actually showed how you can adjust the MCP engine.
within a SQL MCP call on how you can log that call out to a governed dataset. What we've published is a number of artifacts, and again, I'd share my screen if I was able to, and illustrate those artifacts, but there's a number of artifacts that are probably helpful from a call chain perspective about how to go down that call chain, and how do we log those events, and for the respective elements of observability, starting with the MCP. So we've now logged today, we've logged issues in each of the standards.
bodies. We've logged in MCP, we've logged in OpenTelemetry, and we've updated the issue's been open since, April. We've logged with the, and presented last week to the Technical Steering Committee of the Open Lineage about how to… how to approach that.
what we're… specifically ask, and again, Dan, if you're okay, I might come back next fortnight, or indeed at the Semantic Conventions meeting, I think, which is on Tuesday, and present more in detail, if that's appropriate, but specifically about how to correlate between the span and trace ID and the run ID, or more particularly the lineage run event within the Open Lineage Convention.
**Dan Gomez Blanco** 09:57 What you're trying to build, if I get this correctly, is, like, which I think it's… first time I hear it, but it's awesome to hear, is how, I guess, OpenTelemetry and OpenLineage can start to connect the… the… the… the trace, or the… the trace pairing ship to the… to the lineage from… from data… data sets, right?
**Daniel Rolles** 10:19 Yeah, correct. I'd even take a… that's exactly right, and to build on it, what we've tried to do is show traceability all the way through the MCP protocol. I think you've spotted it straight away, the use case and the scenario and the reference implementation we've built. So anybody can… it's all up there on the lab. You can… all the test cases are there, all the data's there, you can literally pick it up and run with it.
is we've actually started with the MCP call, because what we're trying to highlight is that whether an agent's operating on behalf of a human being, or indeed autonomously.
Assuming it calls via that MCP, the fact that it's touching a governed data set is actually a governable event, right? So we're differentiating between the data observability requirement, i.e. what event happened.
from the software and infra-observability requirement, which is in the OTEL's purview, to make sure that we segment those two capabilities, and one goes off the reference implementation we built is Jaeger, so we've tried to use all open source software wherever possible, so we've used Jaeger For the OpenTelemetry call, we've used Marques, which is an open source, open lineage collector.
On that side, plus one of the open source MCP, implementations for Postgres, and we've used Postgres as the backend. Again, all open source, specifically to make sure that anybody can replicate what we've done.
That's awesome. So, yeah, I just wanted to… sorry, it's… you're exactly right. I just wanted to build on it, Dan, because we… the whole point we're making is it must go back to the… back to the call originally. There is a gap currently that we've flagged in the issue that we actually think we need to capture the actor as well.
But what we are flagging is currently we can correlate open OTEL call, sorry, span and trace.
with the open lineage event. However, tracing back to the actor requires a rebuild, and we've created a… what's called a bow… we're calling a bow tie, where we've Shown the capture of the event, and the analytics on the right-hand side of that artifact.
**Dan Gomez Blanco** 12:28 Nice.
Yeah. I mean, like, we can I mean, the best place to discuss that will definitely be the semantic conventions SIG meeting. The Gen AI one.
If you have an issue raised there, definitely, definitely do that. I think there is one thing that we could definitely help here with, from the end-user SIG as well as the SEMCOMP, because there's two aspects.
is that if you're able to share, I know that, you know, you were saying, like, you know, you can share the… you can't share the screen right now, but if you're on the CNCF Slack.
And if you can share, there is an OTel end-user SIG or OTel SIG end-user.
**Daniel Rolles** 13:05 Yeah, I posted there today.
**Dan Gomez Blanco** 13:07 I've not seen it, but yeah, so, like, if we can all… maybe, like, you know, what I would like to… I'll give it… try to give it some… yeah. See if, if other users are… Because chances is that someone.
Either is already doing something similar or that they're having the same problem and the same challenge. Right. So I would like to get more in users.
Having a view, having a look at that, and seeing… And that can bring up some of, more feedback for the… for the semantic convention's sake, right? I don't know if this is what… currently one of our… I guess… I guess not, one of the areas that they're focusing on.
I don't know about the issue in particular, if you're like, you know, the one that you're sharing, if that's already in the roadmap or not, but Yeah, I guess…
**Daniel Rolles** 13:57 We've done from our analysis. Yeah, there's some related ones open already. And we've tried to in our issue, we've tagged those, and saying it does look like we're pulling in the same direction on semantic conventions. We met with one of the team that sits on there at a conference last month.
And we flagged that this is what we were potentially coming back with, and everybody went, yeah, that's the right thing to do. Now, whether it lands exactly the right way, etc.
What's exciting about them, about what you just said, is we're having the same conversation over in the Open Lineage community as well. Some of the vendors over there, Jacob from IBM, is interested because his clients are hitting exactly the same challenges, and we're seeing if we can get a coalition of the willing together.
to actually give this some R&D from an end-user perspective.
**Dan Gomez Blanco** 14:44 Nice. Yeah, absolutely. Cool. Well, thanks for sharing, and I think,
**Daniel Rolles** 14:51 Welcome. Thank you for giving me a couple of minutes completely on spec and in my first meeting.
**Dan Gomez Blanco** 14:56 Anyone that's watching the recording of this, because all these are recorded, you can find the material on the CNCF Slack.
Cool. So I guess, you know, it'll be… if you have any updates, but I will ask if you have any updates after going to the Semantic Convention SIG, to the Gen AI SIG, sorry.
And.
If you can drop them there, or link them there, that would be great.
**Daniel Rolles** 15:19 Yeah, will do.
**Dan Gomez Blanco** 15:21 And, yeah.
Let's see how that…
**Daniel Rolles** 15:24 Thank you.
**Dan Gomez Blanco** 15:24 How that goes.
**Daniel Rolles** 15:26 Thank you very much.
**Dan Gomez Blanco** 15:27 Thanks, Katie.
**Daniel Rolles** 15:28 Thank you. Thank you for letting me go, Crash. Greatly appreciate it, Dan. Thank you.
**Dan Gomez Blanco** 15:32 No problem, thanks.
**Daniel Rolles** 15:34 Jeez.
**Dan Gomez Blanco** 15:34 Okay, moving on to the next topic, which I wanted to share, which is, this is going to be a short one, but the I spoke to the… so I started speaking to some of the people that shared reference implementations.
And Adobe are initially, yeah, they're happy to go and do an OTelMe session. So… Yeah, if Well, I have not created the issue yet.
But I will create it, we'll have to… don't know when the target is.
I don't know at the moment how we are doing in terms of, like, planned sessions for OTELME.
**Victoria Nduka** 16:14 Like we have we have tons, not tons, but we have a couple of sessions lined up. I think we have four more.
So. You can do that. You can present issue.
We will get to it.
Cool.
**Sophia Solomon** 16:30 Have you submitted through the Google Doc at all?
Dan.
**Dan Gomez Blanco** 16:35 No, I would…
**Sophia Solomon** 16:36 perform.
**Dan Gomez Blanco** 16:36 I have not, the Google form, yeah, I have not done that. I did have a chat with.
with Adriana about that, because I think that the form is her form, I think, although, you know, we can all see the responses.
Because now that we've got issues.
or issue templates in the SIG and user.
I don't know if we actually… I mean, the forum used to use it. I don't know what other people's opinions is, if we just ask users to create Maybe the issue template needs some… I don't know, modifications, but…
**Sophia Solomon** 17:09 Yeah, I've been working on the issue template. Sorry, I don't… go ahead, Victoria.
**Victoria Nduka** 17:15 Yeah, like, what I wanted to say was… I don't remember exactly why Adriana created a form.
I think we're getting a couple of requests on Slack.
It's Gather all the requests in a form.
And then process them one after the other. But now that we have the… Detailed issue, templates.
I think it's better we just use BitTorrent instead of… having, like, copying whatever it is that is in the form on the GitHub issue template. We are using the GitHub issue template as the guide for facilitating or for running the entire process. So let's just keep it in the middle.
**Dan Gomez Blanco** 17:57 Yeah, I mean, if we just… That just seems like, in a way, an unnecessary step, but if we do.
**Victoria Nduka** 18:02 I'm.
**Dan Gomez Blanco** 18:03 Hotel Me propose. It says propose a new episode of Hotel Me. Right. And I don't know what we call.
Right, it seems to be already aimed at the… Yeah.
The tasks… Can be completed as part of a… okay, so… Feel free to… okay, so if you're an end-user, and this hat's the label, cool.
So, if I were to go here and click on this… Okay, we've got 3.
**Victoria Nduka** 18:35 And.
**Dan Gomez Blanco** 18:36 In the pipeline, yep.
**Victoria Nduka** 18:38 Yeah.
**Dan Gomez Blanco** 18:39 Is that… is that… is that… does that match the…
**Sophia Solomon** 18:42 Yeah, we're concluding the one from Diana that we'll do next week. So just.
3.
**Dan Gomez Blanco** 18:50 Oh, sorry, Diana, that's not.
**Victoria Nduka** 18:52 Diana's is Diana's is hotel in practice.
**Dan Gomez Blanco** 18:55 Oh, that's what we do in practice. Yeah, okay.
**Victoria Nduka** 18:57 Yes.
**Dan Gomez Blanco** 18:58 Hotel and practice.
Okay, this one.
No, sorry.
**Sophia Solomon** 19:04 Are you submitting for hotel meetings?
**Dan Gomez Blanco** 19:07 Yeah, so that would be for Otelmi, the…
**Sophia Solomon** 19:10 Wolbachem.
**Dan Gomez Blanco** 19:11 Yeah, the other one, the one with Adobe.
Would anyone?
1, 2… Drive the hotel me, otherwise, you know, I… I don't know what my bandwidth would be in the next few months, but if someone was to drive it, like, with, you know, if I were to create an issue… I don't know if we've got people.
**Victoria Nduka** 19:33 basically.
**Dan Gomez Blanco** 19:34 these already. This one seems to have been here for a long time.
By the way.
**Victoria Nduka** 19:39 Oh boy.
**Dan Gomez Blanco** 19:40 With Max.
The one with Michele, actually this one.
We need to follow up on this.
Because.
**Victoria Nduka** 19:52 Okay.
**Dan Gomez Blanco** 19:53 Kelly said initially, let's do a no, well, I did say to me, Kelly, let's do a no tell me session to talk about the instrument.
Packaging SIG.
And the work that he's doing.
And then we said… Let's do a WhatsApp hotel.
So I'm not sure if we still need to do that with Michele, if he wants to do that, or if, yeah.
**Julia Furst Morgado (Dash0)** 20:16 Yeah, I think he did already a WhatsApp hotel with Luis and Adriana.
**Dan Gomez Blanco** 20:22 Yeah.
So maybe we don't need to do this one, and then we've got this one that was opened fairly recently.
Miss Kabishka is.
Yeah, we can follow up on these. I mean, OTEL Meet and OTEL in practice is not like… it would be good to have One of each, rather than everything being hotel in practice, but… It doesn't need to be.
**Victoria Nduka** 20:47 Yeah.
**Dan Gomez Blanco** 20:50 Right.
Moving on, I think I'll… what I'll do is I'll add the issue that I guess, you know, we talked about.
And down below the issue, For this, and then what we said is, like, We… We can just tell people.
To open the issue directly.
And not.
Use.
Adriana.
Just tagging Adriana, I'm not sure if she'll see it, but was he?
And.
Sophia.
Oh, yeah. Yeah.
**Sophia Solomon** 21:39 you're.
**Dan Gomez Blanco** 21:39 Thanks.
**Sophia Solomon** 21:41 Yeah, no. I just wanted to alert everybody to the OTEL in Practice session next week that we're having with Diana. Victoria will be hosting, and I'll be leading the Q&A. So, yeah, October 13th, the time… I need this specific time.
Oh.
Victoria, do you know the specific time?
**Victoria Nduka** 22:06 I know that it's 5pm my time, but I don't know what's…
**Sophia Solomon** 22:11 Okay.
**Victoria Nduka** 22:12 you.
**Dan Gomez Blanco** 22:13 Cool.
**Sophia Solomon** 22:14 Diana, I don't know your name.
**Dan Gomez Blanco** 22:16 And we have it on the, yeah, we have it on the OpenTelemetry Live.
**Sophia Solomon** 22:20 Yes. Oh, yes, it'll be 9, 9 PT, 18 CET.
A.
Cool.
I think that's for Central Time, America, that's 11 a.m. for me.
So yeah, please join. We'd love to have you guys. And the next thing that I wanted to mention was that, yeah, I'll be attending KubeCon NA.
2026 this year. I don't know who else is attending. I know it was kind of small last time we, like, all… oh yeah? Oh!
**Dan Gomez Blanco** 22:58 I'll be there, I'll be there.
**Sophia Solomon** 22:59 Okay, sick, sick. I'll be there.
**Julia Furst Morgado (Dash0)** 23:01 They are as well.
**Sophia Solomon** 23:03 Oh, incredible. I know you guys have both already been tapped, though, for Humans of Otel, which makes me sad, because I would love to talk to you again, but, we are looking for more people, so if anyone knows anyone else that is attending.
You Dan or you Julia, please let me know. And yeah, we're, we're setting it up to kind of do it in the more informal style, that they did at Q.
**Victoria Nduka** 23:29 can't.
**Sophia Solomon** 23:29 this year. So yeah, please just let me know. Awesome. Cool.
**Dan Gomez Blanco** 23:33 Yeah, let's try to look for… New faces, right, as well.
**Sophia Solomon** 23:37 Yes.
**Dan Gomez Blanco** 23:39 I mean, it's Julie and I probably have been on on it too much. Yes.
**Sophia Solomon** 23:45 No, absolutely. I'm asking if you guys know anybody, because I know you guys have already been to… we can't.
**Dan Gomez Blanco** 23:50 Yeah.
**Julia Furst Morgado (Dash0)** 23:51 I'll think about it, I'll see who I know is going, and I'll let you know.
**Sophia Solomon** 23:56 Thank you so much.
**Julia Furst Morgado (Dash0)** 23:57 you.
**Sophia Solomon** 23:58 That's all.
**Dan Gomez Blanco** 23:59 Nice, All right, Dhruv.
**Dhruv Ahuja** 24:06 Yep, so Dan, the OTel Native blog is finally live, so…
**Dan Gomez Blanco** 24:12 Oh, is it published? Finally. Yay.
**Dhruv Ahuja** 24:15 Finally.
**Dan Gomez Blanco** 24:16 Nice.
**Dhruv Ahuja** 24:17 Thanks a lot for your patience and support.
**Dan Gomez Blanco** 24:20 Good. No, it's a good blog post. I think I'll… Oh, yeah, I repost, I think, Yeah, thanks for writing it. It's,
**Dhruv Ahuja** 24:28 Yep.
Yeah, and I think now… so it took time, but I'm really happy with the shape it's taken with yours and Severin's feedback, so I think it really is, like, I guess… Like I think it's worth reading now compared to earlier actually.
**Dan Gomez Blanco** 24:45 Nice. Feel free to share it with, within the end-user SIG as well, and then in the channel.
One of the things that I'm personally telling End-users.
Is that when they speak to another.
vendor, like, as in, like, as a SaaS, right? As a SaaS provider. that the end-user should be the ones asking for that native hotel support, right?
So, yeah, I think your blog does a good job at explaining to them why.
So, awesome.
**Dhruv Ahuja** 25:22 Thanks.
**Dan Gomez Blanco** 25:25 And Ernest.
**Ernest Owojori** 25:29 My update is more or less like I'm just informing everyone.
the post-March survey that Andrea shared with me a couple of weeks or months ago.
I finally was able to work on it, and presented to the contributor experienced SIG on their last meeting.
And based on the insights that we saw, then Hami asked a question to Dive deeper, to dig deeper into the work, which includes us trying to see.
Why do we see in the survey that There are a lot of people complaining about, the time they're making us.
takes to… review their work, or even manage a PR. Some instances where it is just a simple one-line edit, and it takes 3 months.
just because a single individual that was supposed to approve it is probably not available. So we wanted to now see how large the problem is by fetching the repository activity, which I think I'm currently doing.
I spent like.
A large part of my day-to-day has been on that.
Even right now, I'm still working on it. So, if I was able to find something interesting.
I'm going to, report that again to the contributors again at large, record a video according to the MISA recommendation, so that everyone could Get the extent of what we find.
And that's because I do not want to write a blog post for this.
**Dan Gomez Blanco** 27:11 That's good. Good stuff.
The analysis on GitHub is actually quite interesting. I think I was looking at, I presented a couple of SIG meetings ago, but, but I've not been… I've not had the bandwidth to go and speak to the… either the comms SIG or the contributor experience SIG.
Or keeping it here in the end-user sake. Is that type of, analysis over GitHub issues.
Which is something that I think could be valuable.
I was having a look at the work that we did last year to ask users to use thumbs-up reactions and issues to prioritize.
To help prioritize issues, and then start to see what are the highest priority ones that were Not open or the one has.
The most voted issues that are.
Open, or that were open in the last week, or that were closed in the last week, which also signals that something important happened.
So, yeah, I'll be… if you have anything… That you want to share.
In terms of, like, doing that type of Work. Let me know. I think I'll… I might be.
**Ernest Owojori** 28:23 Yes.
**Dan Gomez Blanco** 28:23 Something as well.
**Ernest Owojori** 28:24 Yeah, sure, sure. Anything around mining repositories is largely my research interest.
So I'm more than happy to keep doing that within this space.
**Dan Gomez Blanco** 28:34 Nice.
**Ernest Owojori** 28:35 So if there is a block of work, I'm more than happy to add it to my roadmap, like I would like to see.
**Dan Gomez Blanco** 28:43 Nice.
Cool.
I think that's all the topics for today. And that's.
Yeah, that's all. One thing that I wanted to raise is the… if you scroll down a little bit, you can see in that, in the notes, you can see OTEL Blueprints.
We are… we do want to close this out by… KubeCon. So, yeah, we are going through the last blueprint at the moment.
And then there would be… I know that the DevEx SIG are working on two more.
Reference implementations that will be shared soon.
Don't know how soon, but I'm just following up with them on that.
So yeah. And I say closing is not like the end of blueprints. It's almost like the start of it. But we're closing the bootstrapping of the project. We are then now continuing to work as part of End-User SIG with Tiffany and Lukasz as Yeah, my co-approvers.
And, we'll be asking for… More end-users to give us reference implementations.
And give us, Yeah!
more blueprints. In fact, reference implementations is something that I wanted to bring up as a… I think I brought it up last week, but… No, I think I did that in the blueprints.
in the Blueprints meeting.
There is a list if you go to the OpenTelemetry website.
Let me share my screen.
There is a list of, adopters here.
End-user… no.
What is it?
Community?
So, an ecosystem… Yeah, ecosystem.
So the whole ecosystem part, you will see these, like, you know, the ecosystem lists are frozen.
The ComSec reached out and said, we've got all these adopters, some of them have blog posts, some of them have CNCF case studies, and so on.
That use the the US hotel We want to get rid of this.
And then focus on moving them to blueprints and reference implementation. So, if we could ask those… start to ask those folks that, you know, this is something that we're doing from the… From the blueprints, let's say subgroup.
But at some point, we'll, you know… Anyone, anyone that knows anyone in that, in that, in that list of adopters could do that. Ask them to raise a reference implementation.
for their work if they want to, and then they will be listed as adopters. Otherwise, from the perspective of the comms sake, there is not really… they don't see a lot of value in having just a list of adopters here.
Without much, you know… much more information, right? So… That's it. That's the only thing that I wanted to raise, that hopefully in the future we'll see more reference implementations with adopters.
Going away.
Cool. Awesome.
**Victoria Nduka** 32:12 I wanted to ask.
**Dan Gomez Blanco** 32:13 yeah.
**Victoria Nduka** 32:14 Like, now that I have you… I have a couple of posts on Buffer that I need someone to approve. It's related to Diana's session, alternate practice session. I made six posts. I think three of them got approved and published.
But 3 are still pending, and I'm hoping you could help me out.
If you have access to Buffer.
**Dan Gomez Blanco** 32:33 Sorry, to approve the,
**Victoria Nduka** 32:36 Social media posts for Diana's.
**Dan Gomez Blanco** 32:39 Right, okay.
**Victoria Nduka** 32:40 practice session.
**Dan Gomez Blanco** 32:41 Yeah, yeah, send them to me on Slack, and I'll be… I think I've got permissions to approve, so I'll go and have a look.
**Victoria Nduka** 32:51 Awesome.
**Dan Gomez Blanco** 32:52 Thanks.
Gustav.
Any other topics?
All right.
Alright, catch you later. See you, bye-bye.
**Dhruv Ahuja** 33:09 Bye-bye.
**Ernest Owojori** 33:10 Bye, everyone.
**Sophia Solomon** 33:12 Bye, everyone.
