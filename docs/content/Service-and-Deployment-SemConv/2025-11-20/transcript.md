SIG: Service and Deployment SemConv
Date: 2025-11-20
Duration: 46 minutes
============================================================

## Zoom Recording Transcript

**Janhvi** 02:51 Hey, everyone.
**Josh Suereth** 02:54 So…
I'm just gonna make this note before I kick the bot, but there's no OpenTelemetry policy around note takers. We actually have every meeting recorded.
we have notes that you can read, and so, we do not want, like, additional people just signing in as note-takers with AI, because we already provide that as a service to the community. So you can check our community repo for that, and apologies, Andrew, but I'm gonna kick off your note-taker.
Actually, I can't do that just yet. Let me… let me find someone on the GC who can help.
But yeah, that's… that's the OpenTelemetry policy.
Okay.
**Janhvi** 04:22 Cool.
**Josh Suereth** 04:24 Oh, Trask is on, maybe Trask can do it. Trask, do you mind booting the note taker?
**Trask Stalnaker** 04:28 Yeah, I'll do that, and I'll even chat the, there is a community…
Section on how to do it, but they are super annoying, and it's annoying every time.
I've given up… I gave up on a couple of the meetings and just…
That is, like, every time. But yes, since I'm not driving, I can do this in the background.
**Janhvi** 04:50 Okay, cool.
**Josh Suereth** 04:51 John, do you want to run the meeting and present the notes?
**Janhvi** 04:54 Yep.
Okay.
One sec.
**Josh Suereth** 04:59 Yes, sorry for that.
**Janhvi** 05:02 Hope you can see my screen.
**Trask Stalnaker** 05:07 Guests.
**Janhvi** 05:14 I think… should we get started, or do you want to wait for a minute or two? I know how usually he joins the call. Maybe let's give one more minute, and then we can get started.
Feel free to add the agenda, meanwhile.
**Josh Suereth** 05:29 I hope you don't mind, I threw all of the active PRs… I didn't pull issues, but I threw active PRs that were tagged against this.
**Janhvi** 05:37 SIG.
**Josh Suereth** 05:38 Into the… into the agenda item, and then I…
finally followed up on my PR, sorry it took so long, with, like, responding to comments and things.
**Janhvi** 05:47 Thanks for doing that.
Okay, I think we can probably get started. Let's maybe go through the active PRs, and then we can see if there are any more agendas, or any more topics to discuss.
Josh, first one is your PR. Do you want to quickly talk about it?
**Josh Suereth** 06:28 Yeah, so we had, we had a bunch of discussions about this before, but effectively this splits, the service namespace into 3 pieces.
Those 3 pieces are the namespace.
the service itself, and then the instance of the service, with, like, a bunch of descriptions. And there were a bunch of themes to the comments that we got,
one is a bit easier, which is just making the descriptions be precise. Like, let's make sure that the description is well-formed. Yeah, if you look at files changed, there's a service markdown file that we can render that would probably be the best one to look at.
Oh, you were showing the PR, I mean in the PR. I can, I can do that too if you want, but…
**Janhvi** 07:14 Sorry, my screen just froze, I don't know, just one second.
Yeah. I need to update my laptop. Josh, meanwhile, do you mind sharing your screen? I'll figure this out.
**Josh Suereth** 07:26 Sure. Hopefully I don't have too many tabs open.
Oh, you have to stop sharing your screen before I can, sorry.
**Janhvi** 07:36 Yup, go ahead.
**Josh Suereth** 07:38 Okay.
I mean, I… I… okay.
I literally can't until your screen is not shared, for some reason.
**Janhvi** 07:47 Yeah, I think, sorry, there's some lag on my end. I think I've stopped the sharing now.
**Josh Suereth** 07:52 No, no worries. Okay, yeah, so if we look at… let's do resource service. This is the new file that has, I think.
most of the discussion of things. So, yeah, this is where we're trying to get the three descriptions. So, a service namespace is an entire system of components designed for end users or other applications to leverage.
A service is one of the logical, distinct components that make up an application. This, by the way, is when we ask, like, ChatGPT or Gemini about what a service in OpenTelemetry is. It consistently used the word application.
which is the second contentious point of this PR. But, Yoshi and, Yao
brought this up, and kind of… I went with their suggestions of just using the word application here.
Anyway, it's a logical, distinct components that make up an application, typically running as a bundle of instances that run the same container image for load balancing. Now, this is… this we can cut. Like, Trask, you actually wanted to remove that section, and then others proposed, like, changes, so I took the proposed changes, but didn't cut it from the definition.
So that would be actually discussion number one.
Of, of that.
whether or not… let's start with service, because I think this is an easier definition.
Do we think that this caveat here is too limiting, or… and should we cut it, or should we leave it?
**Trask Stalnaker** 09:26 I don't recall what my concern was now, but it looks good to me at the moment. I will… I will look…
check out the, my previous PR comment on the change, but it looks good.
**Josh Suereth** 09:40 I can play devil's advocate on my own proposal, which is, this is very Kubernetes-specific, right? So if you're talking about, like, an old-school VM, right.
it would be, actually, instead of typically running as a bundle of instances that run the same container image, that could be, like, for a Java application, it'd be running the same jar across a set of, you know.
Tomcat instances or something, like… but…
So, we could change typically to, for example,
I do think this example helps reinforce what it is, though. Like, I think we need something.
Which is why I left it.
**Trask Stalnaker** 10:25 Oh, I see. It was previously typically running as a separate process or microservice. Yeah, yeah. No, I don't have any… my, objection to the prior was just, like.
**Josh Suereth** 10:40 It didn't.
**Trask Stalnaker** 10:42 Yeah, it didn't seem to add anything to me.
**Josh Suereth** 10:45 Gotcha.
**Trask Stalnaker** 10:46 And also process… oh, yes, I see, I had pulled out the word process, making me think of service instance, like, then if it's a separate process, then for each of my separate processes, I have a service name, or something like that.
**Josh Suereth** 11:02 Yeah, no objection to the…
**Trask Stalnaker** 11:04 New.
wording.
**Josh Suereth** 11:07 Okay.
And then the last one is service instance, which is a distinct instance of a service component, for example, a specific Kubernetes container that is part of a Kubernetes deployment which offers a service.
this one… this one uses for example, instead of typically, so I actually…
I would like to change this to be, for example, instead of typically. Yeah.
**Trask Stalnaker** 11:29 I agree.
**Josh Suereth** 11:30 Alright.
Let me… Oh, men?
Let me switch my…
Visual Studio Code. I'll make the change right now, and then push it after the meeting.
If everyone's okay with that…
Okay, other concerns with these three defines… like, I think this, honestly, this is the most important of the PRs, these three definitions.
**Janhvi** 12:05 Josh, I have a question orthogonal to this one, right? Once we submit the PR, so this is going to be in the development state, right? Then we'll have to work towards stabilizing, let's say the namespace and the instance thing, is that correct? That would be the next step?
And for that, we need a prototype for this.
Or, given this is already being used a lot, we can skip the prototype.
**Josh Suereth** 12:33 I think… I think we can provide, I actually already have a prototype where I had service instance in Java. So we could… I could revive that one. I don't think it's actually hard to do.
The reality is, like, for entity relationships right now, there isn't, like, that hasn't landed fully in OpenTelemetry, so, like, you have to use one of the entity prototypes to do that.
**Janhvi** 13:00 Hmm.
**Josh Suereth** 13:00 This is really just how we're gonna bundle the attributes, so we're gonna treat… like, we're gonna stabilize… we can independently stabilize service from service instance, for example.
And if you look at service today, right, service instance ID is not stable, but service is stable.
Which causes awkwardness.
**Janhvi** 13:22 Yeah, because that's the main entity, right? So, we're saying the entity is stable, but one of the attributes is still not stable.
**Josh Suereth** 13:28 Yeah.
So, I think there's, like…
**Trask Stalnaker** 13:31 No stable entities, because entities aren't stable, but those…
**Josh Suereth** 13:35 There's stable attributes, yes.
**Trask Stalnaker** 13:36 After things are stable.
**Josh Suereth** 13:38 Right. What this does is it actually gives us the ability where, like, the service entity, all of its attributes are stable, kind of immediately.
Once this is done.
**Janhvi** 13:48 Got it.
**Josh Suereth** 13:51 I think it lets me update some policy things as well.
Okay. The other thing that, that we, we kind of mentioned was service namespace versus application.
The furthest I went there is just use the word application here, because I think it makes sense to people. It's like, what is used in Kubernetes, it's what is used,
in ChatGPT and Gemini, when you talk about, like, a system of services,
But I did not actually make it be service names. Service namespace is still namespace. It is not, like, application.
where an application would have a service. I am comfortable with this, because I think this isn't a one-way door. I think if we decided to have application as an entity that is composed of services and other things, like mobile application, that kind of thing, we can still walk down that path.
just fine. Like, there's nothing preventing us from doing that.
So I don't think it's a one-way door where we have to make a decision about application and the use of application. I think it's fine to leave it here. It's defined to call this thing service namespace, and if we ever wanted to have a, application be modeled as something called application.
We can do that on top of this, and it's totally fine.
**Kartik** 15:11 Can an application map to a service.namespace, or are we leaving it sort of open to interpretation, Josh?
**Josh Suereth** 15:18 Right now, I think what we are suggesting as service namespace would be an application. So if you want to define… if you want to define something that is a composition of services, you would use application for that, like…
I don't have the bug, but there was someone who was asking about
when to call a service a service, and when, like, what to put in service name. So they had this thing where they wanted, like, a service role, and a service, like, pool, all this kind of stuff, where what we're gonna suggest in the future is instead of
instead of having a service be an application, you would define a service namespace that is the application name, and then under it, you'd have multiple services. Like, that's… that's gonna be our suggestion going forward.
**Kartik** 16:03 Okay.
**Josh Suereth** 16:04 me not remembering that bug is actually not helping us here. John V, do you remember where… where's our Git… our project? Is it…
It's just called, service and namespace, right? Yeah.
**Janhvi** 16:17 So…
**Josh Suereth** 16:17 Because I think it's on their… Let's see… service…
Yeah, okay. So it, like, the one that was interesting was… I think this one here.
This was someone who was confused about, you know, instances of a service can be grouped into pools, so you could have a canary in default.
Oh, this is where we wanted to do environment name, I believe, was what pool was, right?
**Janhvi** 16:48 Yeah, this is more like a deployment kind of a thing, right, that they're talking about?
**Josh Suereth** 16:52 Yeah, that was deployment. There was another one that was… Locality Deployment Data Center…
Oh, this here.
This was the one that was confusing. So they were talking about, with applications running cloud and scaling elastically, host name becomes highly variable, service name times host name is awkward.
And they were talking about having, like, a purpose.
And then we kind of walk through what this could look like, and I think this is where we're basically saying.
Use service name, also use hostname, and use a namespace if you need to kind of, like, group these things meaningfully.
As opposed to adding purpose of database applic… so what they were saying is, I have a, you know, I have a service called, you know, Credit Card Checkout.
and they wanted to have a role that says this is the database part, and a role that says this is the load balancer, a role that says this is the compute, you know? What we're saying is, no, your service would be, like, checkout database, and your namespace would be, like, checkout application, or whatever.
**Trask Stalnaker** 18:09 There was also, this one.
Which is closed now, but… I think it's…
**Josh Suereth** 18:20 Service type and service distro. Oh, yeah, this one here.
This is interesting, because this one gets more into remote control, if I recall correctly.
**Trask Stalnaker** 18:46 Yeah.
**Josh Suereth** 18:48 Like, this is the interaction between service and op-amp.
Which,
I think, going forward, what we want to see is,
They would actually use, maybe a collector-specific convention for that if they need it.
Submit engine exposedervice.name is set to API Gateway.
Yeah, this is… this is the difference of,
I'm making an API gateway, and it happens to be implemented as NGINX. How do I know it's NGINX? That's what they wanted to type it for.
**Trask Stalnaker** 19:29 Yeah.
**Josh Suereth** 19:33 Yeah.
**Trask Stalnaker** 19:35 Now, this…
**Josh Suereth** 19:36 database.
Cuz…
**Trask Stalnaker** 19:40 They went in a different direction.
**Josh Suereth** 19:42 Gotcha.
Okay.
Go.
**Janhvi** 19:54 Cool.
**Josh Suereth** 19:55 So coming back… To this…
Do we have any other major concerns here?
Oh, for context, this is now not a draft, this is an approvable PR. So, like, this is mergeable at this point.
**Trask Stalnaker** 20:17 Cool, I will.
**Josh Suereth** 20:18 re-review it.
**Janhvi** 20:21 Okay.
**Josh Suereth** 20:27 So, yeah, and I was traveling…
**Janhvi** 20:33 Quick question for PRs like this, what is the, approval process? Like, we'll need somebody to approve from this SIG, and then it goes to the committee, and we get approvals there. That's the normal process in this one as well?
**Josh Suereth** 20:48 Yep, so… and we don't have a SIG group created for, like, SIG approvers yet, which I think you saw in… will see in the other PR.
But yeah, effectively, once folks in the SIG approve, so that would be, like, folks in this meeting, this could be Yao, this could be Yoshi, once we get approvals from the SIG, and we feel like the SIG has approved it.
So I'd say about two of us, at least.
Then we… it goes to a new queue for the semantic invention maintainers to look at, for just checking on the SIG. Since we're a new SIG, we don't have, like, full approval status, so they'll make sure that we understand the semantic invention rules. You have Trask and I here, so…
Hopefully, we're helping you make sure you understand the semantic entry rules. And then that, once that approval goes through, then it gets merged.
So, it's a two-phaser, yeah. The SIG, then the overall maintainers, then Merge.
**Janhvi** 21:37 So should we create a group for this SIG as well?
**Josh Suereth** 21:42 We should, yeah. The idea should be, it should be folks who show sound judgment in understanding the goals and the, like, scope of the SIG would be in that approvers list.
**Janhvi** 21:55 Okay, got it, okay.
**Josh Suereth** 21:56 Yep.
**Janhvi** 21:58 I can probably take that, yeah, I can, check with you and Trask, and then we can add the folks.
That we feel a good way.
**Josh Suereth** 22:06 Yeah, I think technically Trask would be doing some, or no, I could do it too, the, Terraform proposal to make a group, right?
I think I can do that now.
**Trask Stalnaker** 22:17 You can, but I also… Don't mind doing it.
**Josh Suereth** 22:22 Okay.
I need to learn how to submit the PRs at some point, but yeah. Cool.
Was there anything else? Those were the, kind of, the two main themes in this that I saw, by the way, for this PR, in terms of things to discuss. This is, like, Yao's example of,
You know, calling things service name, calling things application.
But I don't remember… Yoshi had a few comments that we…
addressed… yeah. I think that's it.
**Janhvi** 22:55 Yeah, I met Joshi in one of the last SIG meetings during the APAC time, he was good with the high-level proposal.
**Josh Suereth** 23:02 Cool.
Awesome.
**Janhvi** 23:07 Yeah.
**Josh Suereth** 23:08 Should we go to the next one?
**Janhvi** 23:10 Yep.
**Josh Suereth** 23:16 So this is service criticality.
The one thing I want to call out on this one is, the build was failing.
And I think there's… there's a few things to fix the build. But I actually approved this one immediately.
Personally, I didn't see anything out of line here. Let me go to…
Is this gonna be the best way to view it?
Yep. It adds a new service criticality, which is in development.
This would be on the service.
And it has critical, high, medium, and low as an enum.
And then… It's based on operational importance. Like, the description seemed fine.
And about how you could, you know, use this to understand sampling rates, or optimizing the cost of that service, and use it to kind of filter things in and out if you need to downstream.
And then it has this definition here.
Is this readable, by the way? Am I zoomed in enough?
**Janhvi** 24:25 Yep.
**Josh Suereth** 24:26 Yup.
**Janhvi** 24:26 We can, we can eat it.
I think, Josh, one of the questions… so we discussed this PR last time. One of the questions that came up was, if this attribute is already standardized in Kubernetes or not, or if this is more like a user-driven attribute, and if it is a user-driven attribute, is this the right place to add it or not?
I checked out Kubernetes, I don't think there is a related attribute, specifically for, like, criticality or tier.
It could be, like, a user-driven thing, but at least from observability and cloud perspective, I do think it makes sense, because, you know, if there are incidents happening and you want to see, hey, how bad the incident is, you can do that if you have, like, if you have a standardization like this in place.
**Josh Suereth** 25:11 Yeah, I would agree with that. When I've seen people do criticality.
Before, it's usually, like, a custom thing.
**Janhvi** 25:21 Yep.
**Trask Stalnaker** 25:24 How would we get prototypes… for this.
**Josh Suereth** 25:31 Oh, like, where's our source of truth for getting the criticality?
**Trask Stalnaker** 25:36 Yeah, anything to… basically, how do we… Show that this is… Useful, being used… Our general bar of…
You know, having instrumentation pour it.
**Josh Suereth** 25:55 Yeah, I'll give you a straw man that I think would be something that could be a really good prototype of this. So, effectively, we,
Update the hotel demo?
So, we inject criticality We have n variables in the, Docker Cades config.
We, update collector… Components… to… high, low…
what do we call it? Criticality pipelines.
That automatically are… needed based on…
the existence of this attribute. So basically, what we have seen, and what we… like, I know this from talking to some of our clients, is we talk about having a collector pipeline.
Where you have two collector pipelines, one for high criticality things, and one for lower priority things. And, like, if you use the memory limiter in the collector, right, you know that the memory limiter, when you hit a memory limit, will drop things.
So what you do is you actually have a high criticality that's less likely to drop things, or doesn't even use the memory limiter, because you're saying, I want this to kind of fuck up as much memory as possible. Use the memory limiter on the other one, so if the first one starts to take up a lot of space, you start dropping data from the other
things, because you're using criticality, right? So we could actually have a demo of that, of, cool, let's write data with criticality into a collector, let's have two pipelines, one where the high criticality stuff is, like, forced to go through, basically, and the low criticality stuff might get dropped if the high criticality stuff takes over.
Or, or bloats.
And kind of show what that looks like. And I think we can do that in the operator.
sorry, in… with the, the demo, the OpenTelemetry demo, we could make a patch to that that just…
Injects these via… A human writing it.
Because that demonstrates, if you read the description of what this.
**Janhvi** 28:02 is meant to do in the PR, I think that fits perfectly.
**Trask Stalnaker** 28:06 Yeah, I like that. It's just some kind of end-to-end…
Prototype, showing it's… how it, yeah, works.
**Josh Suereth** 28:18 Yeah.
**Janhvi** 28:20 Josh, can you add, like, a link to the hotel demo? I don't think I have a lot of context on it, I'll probably go through it offline, just to understand what the flow looks like today, and how this would work with criticality.
**Josh Suereth** 28:33 Sure.
I'll put a link right here.
**Janhvi** 28:38 Thank you.
**Josh Suereth** 28:46 Yeah, so basically we're demonstrating the use of service criticality. The thing that we still don't have is, like, what's the source of truth for it? Like, where does it get pulled from?
So I think if we… like, there's a second piece of investigation we should have of…
Update OTL demo… To show… oh, man, my typing, come on.
To show usage.
And then, we should probably have a,
Can we find sources of truth?
This inflammation from… That's where I think, John V, if you…
I think you had a demo that was… that you showed me internally that was doing something like this, right? Where we have… people might have a, like, a tag that they've annotated things, and we can look it up and pull it in?
**Janhvi** 29:35 Yeah, I think what we tried to do was, in case of VMs, we tried to, like, locally run the VMs, and then we were adding some custom attributes to it, and we made changes to the detector so that the detector could look into those attributes and fetch that. We could do something like that with the criticality attribute.
**Josh Suereth** 29:55 Right, I think the key here is we want where people already have a criticality attribute, which…
Which I think… I think that they are using that for criticality, right?
**Janhvi** 30:08 I don't know if you already, like… in case of VMs, I don't think we have this attribute already present, right?
**Josh Suereth** 30:16 Okay.
**Janhvi** 30:17 Yeah.
**Josh Suereth** 30:19 I don't remember. Go ahead, Troy.
**Trask Stalnaker** 30:21 Look for prior public… prior art, basically, of… I mean, if we think that this is, you know, useful enough, important enough to be adding, there should be some, you know, we should be able to point to some public prior art of…
Other systems using this.
And I think that gets to the question of the source of truth, like, for mapping…
Kinda like, if you're in…
if there was something like this in Kubernetes already, this is where we would map it from, if some other external system.
Or external… schema.
**Josh Suereth** 31:04 Yeah, this is, this is… so, so, the…
The thing I'm mentioning is a public thing where you can actually tag VMs on Google Cloud, and people will tag… like, there's a blog article I found where someone was showing how to, like, tag all of our stuff with criticality, and then leverage it in automation.
But, again, the problem is, it's not like everything is a convention. It's not like there's a known… and that's why… that's why we want to have a convention. That's okay.
**Trask Stalnaker** 31:31 Yeah, yeah, that's okay if we…
Can just point to other prior art of conventions in this, covering this.
Just to kind of show…
**Janhvi** 31:43 That it's… it's a…
**Trask Stalnaker** 31:44 It is… Broad enough, like, we're not just inventing something new here.
That hasn't been proven out.
**Janhvi** 31:54 Sounds good. I think, Josh, you can assign the TI to me. I'll try to figure it out, I'll look around and see what is already present, and if we can have some end-to-end thing working on this.
Plus, I think we have Bhagtiar as well, who's the one who raised this issue, and he was willing to help with whatever is required in prototyping, so I'll see if he can get help, or if he already knows of some use cases for that.
**Josh Suereth** 32:18 Yeah, the other thing I'll say is this criticality thing, I know it's used a lot in security.
Yeah. So, I think a lot of where you see people tagging it is, like, where the observability security boundary is.
**Janhvi** 32:35 Yep.
**Josh Suereth** 32:39 alright.
**Trask Stalnaker** 32:41 It reminds me a little… I mean, there's some overlap, though, with the audit logging proposal.
This is, like, a lightweight version of… of that proposal.
**Josh Suereth** 32:54 Right, right. Well, that's another, another dimension to this, like, having multiple pipelines of.
**Janhvi** 33:01 You might have a different.
**Josh Suereth** 33:03 Pipeline for audit logs that are guaranteed
That has more guarantees than, like, regular logs, where, you know, you're more willing to drop regular logs, but you don't really want to drop audit logs ever.
Unless your system is actively crashing, in which case, you know, you can't do anything.
Alright, cool.
So, we have, we have AIs here. This hotel demo thing, I'm…
Do I have time for that? If we can't find anyone else who wants to sign up to help out here, I might be able to pick that up. Otherwise, we should see if someone can.
And John, you and I can talk about it offline, or we can talk about it in the chat space as well. Yeah. If anyone not in this meeting is interested, yeah.
**Janhvi** 33:49 Yeah, I think I'm sure Bhagtar would be interested. I'll literally sping on the group and see if he is, if not, even we can pick it up, should be fine.
**Josh Suereth** 33:58 Awesome.
Okay, and then here's another new one. This one went through some discussions in the main semantic invention.
meaning, and I think we talked about it a little bit… I talked to Michelle a little bit in,
at QCon.
But this is basically the notion of having
moving peer.service.name to be service.peer.name. So it would be actually the purview of this group's ownership to understand peer communication of services.
So, basically, the TLDR is,
And I think there's already some comments on here. Where is the…
Under Service Attributes, we have a new attribute that is kind of raw.
This is not part of resource, this is not part of entity, this is just a…
attribute that you can use to communicate about a peer. So, if I have a trace that I'm… where I'm, like, have a client library talking from my service to another service, I can annotate that span.
or an event, to say, this is about communication to a peer, and I know their name. Like, I know that my, you know, web server is talking to a credit card authorization server.
And so the peer would be the credit card authorization service, and I would be the, like, web application service or something, right?
By the way, all my examples are shopping, because the last time I did any real application like that, it was a shopping-based thing.
So, apologies if it's, like, too heavy on that. Okay.
And this would, this would include both name and namespace. The idea behind the .peer thing is…
These are attributes about service, and peer is how we talk about the thing we're communicating to. There is a convention from HTTP
and net to use peer, when we're talking about, like, I wanna, you know, record metrics about A talking to B, there's, like, a peer IP address.
**Trask Stalnaker** 36:14 It's net… it's network peer and network local.
**Josh Suereth** 36:19 Network peer and network local, got it, yeah. So if I… if the network is communicating to something, it uses .peer.address, as opposed to the local address. So, I think we have… we have,
We have convention around this. I think this is entirely reasonable. The only thing I'm unhappy about with this has nothing to do with this SIG, and has everything to do with semantic conventions, which is we don't have a way to just bundle raw attributes and say these are applicable in any span.
So it's just awkwardly placed where this lives.
Other than that, I think this is…
**Trask Stalnaker** 36:54 Similar to, like, the thread name.
Problem.
**Josh Suereth** 36:58 It's the same… exact same as the threatening problem, yeah.
Yeah, but otherwise, I had no problems with this. I think there's some cleanup to do in here where the, the deprecation…
Not the usage of it.
Yeah, like, this just needs to go to the other… the other side.
No, actually, I think this one's fine.
yeah.
And any other thoughts here we need to discuss?
**Trask Stalnaker** 37:40 Just the breaking nature.
of it, and… I mean, not that that…
Should stop us from doing it, but just… What?
Should we… do we need to do any communication?
Around it.
**Josh Suereth** 38:05 Interestingly, I think Service Peer is technically used by our Jaeger spec?
Not Jaeger, Zipkin spec.
**Trask Stalnaker** 38:16 peer.service.
**Josh Suereth** 38:17 peer.service is used by the Zipkin spec, but I don't… I don't know…
how… how much OpenTelemetry itself uses this, so it's more like a convention that people were using independently of OpenTelemetry.
That's my understanding from Michelle as well.
Like, the thing that provides that is not an OpenTelemetry open source component, it's something else that's doing that work.
**Trask Stalnaker** 38:43 So, in Java, we support it, via config. Basically, you can supply a config map of these addresses.
Or host names mapped to this peer service.
And I know that, the LightStep was using that heavily, so I think a lot of LightStep customers…
And Michelli, mentioned that even, also, the light, that that's where he's seeing it, is people migrating who are coming from LightStep.
**Josh Suereth** 39:20 Okay.
So, yeah, we do need to do a communication around this, then. So, I think we should ask Michelle
about that. I… the question would be, do we need to have a general service stabilization
migration A to B thing, or do we want one specific to peer namespace?
**Trask Stalnaker** 39:45 Do we have any other… breaking…
We're not really proposing any other breaking things in service.
I think… I mean, we could bundle it with Service Instance… Stability.
**Josh Suereth** 40:06 Yeah, but…
That one… that one, I don't think that… I don't know if that will be breaking if we roll that out. Like, I think we can roll that out without breaking.
So I feel like we should just have… we can ask Michelle to run this independently.
Because I think… I also think the components are completely different. Like, the things that interact with Service Peer
are gonna be totally different than everything that interacts with service.x.
**Trask Stalnaker** 40:33 Yeah, so how do we get, I guess,
what I… the advice… I would want to give the same advice, like.
That we've done for other SEMCOM
breaking SUMCOM, which is… although we didn't do it for environment name, where we say, don't…
take this until we stabilize it. So, like, how…
How soon do we think that we can… What do…
what are the steps to stabilization for this, I guess?
Because I don't mind, in general, breaking if we're breaking to a stable thing. It's the braking from unstable to unstable.
**Josh Suereth** 41:16 like.
**Trask Stalnaker** 41:17 The environment name that cause more…
**Josh Suereth** 41:21 Well, this is… this goes into, like, what do we need to be comfortable with this…
to stabilize. I, I…
what do we want to see? The Java implementation you suggest, that's an example of something we'd want to make sure there's a prototype of that.
Rick?
**Trask Stalnaker** 41:37 Yeah, we don't… I don't think we do namespace.
I think that's just pure.service as the only one that we…
Is there even a peer… is there even a namespace today? I don't think so.
**Josh Suereth** 41:49 There is… there's not… if I remember right, there might be, but I… I think…
if there was, it was added late, and I don't know if it's used, but I think it's fair for us to ask Michelle to drive, like, as part of this drive, to, like, do those steps. Do you know what I mean?
So, like, let's just give him the list of what we want to see happen and let him run through them. But before we accept that PR, let's make sure he's aware of the, like, things that need to happen to finish.
Before we can mark it stable. Because I think his goal… his goal is to get it stable. Originally, he wanted to stabilize the previous name, and we said, no, we've got it here to continue to exist. So, his goal is stability, so let's just…
Carve out the path of what that looks like.
I'm looking at model from here right now, yeah.
**Trask Stalnaker** 42:40 I don't think we have peer service name, we only have peer service.
**Josh Suereth** 42:47 Yeah, it's so weird, right?
Peer service is the only peer thing today.
Okay, we're almost out of time, so, let's… Trask, do you want to outline what we need to see happen, and work with Michelle on that?
**Trask Stalnaker** 43:04 Sure.
**Josh Suereth** 43:05 To happen to stabilize this image here.
Committed to the foreign connection. Okay, cool.
Alright.
So, next is… do you want to take this one away, John V? The request for Asian-friendly tour?
**Janhvi** 43:27 added this one. I think the Asia-friendly slot that we have, it's not very friendly to a lot of regions. I've added this here so that I can get, preferences from people. I'll add it to the Slack channel as well. Once we have the voting, I think I'll need…
Trask, can you all's help to change the invite? So I'm helping you once I get the preferences from everyone.
**Josh Suereth** 43:51 Okay.
**Janhvi** 43:53 But I think this one slot probably is fine, right? With you guys, I've not heard, like, in general, any complaints for this time slot.
**Josh Suereth** 44:00 No, this slot's fine, and now that it's offset from the, the entities and the, profiling one, I'm good.
**Janhvi** 44:09 Okay.
**Trask Stalnaker** 44:10 Yeah, I have a every other week.
At this time also, so this works great for me.
**Janhvi** 44:17 Okay, perfect.
**Josh Suereth** 44:19 And one of these, if I'm… depending on what time you pick, if there's one I can join where I might… sometimes I join APAC-friendly ones with a whiskey, and just see what you guys are talking about. But I don't… one of these is a little… little awkward for me. Anyway, we'll see.
**Janhvi** 44:37 Sounds good. Yeah, feel free to add your suggestion as well, if this is a common slot, we'd love to work on that.
**Josh Suereth** 44:42 It needs to be APAC friendly, that's… that's the key, yeah.
**Janhvi** 44:47 agreed.
**Josh Suereth** 44:49 Alright.
Issue triage next steps. We have AIs. Is there anything… is there anything we need to talk about that wasn't… I think we had a good, lively discussion with active PRs. Is there anything not in the PRs that we want to talk about, or, like, need to make progress on?
**Janhvi** 45:05 I think maybe something for next time, we should start talking about the deployment side of things as well. We wanted to stabilize that and see if, you know, the naming, the definitions look fine, so we can talk about that next week, maybe.
**Josh Suereth** 45:20 Yeah.
Yeah, I think we should keep asking this question repeatedly, of like, what do we need to be comfortable stabilizing something? So, yeah.
Cool. Do you want to put together a, like a, a one-pager, if you will, or like a…
in the, you know in the notes how I put, like, here's the arguments against, service name? Just a, hey, what are the considerations we should think about for stabilizing deployment?
**Janhvi** 45:49 Yeah, yeah, I can do that.
**Josh Suereth** 45:51 Awesome. Yeah, and it doesn't have to be hard, it can just be, like, in the notes, so we have, like, what's our major theme that we want to talk through?
**Janhvi** 45:59 Right. Yeah, I think I'll try to send it in Slack as well before we meet next time, so that everyone can, you know, read, add comments, and then once we meet next week, we can discuss.
**Josh Suereth** 46:08 Sounds great. Awesome. Thanks, everybody.
**Janhvi** 46:12 Thanks, everyone.
**Trask Stalnaker** 46:12 Yeah.
**Janhvi** 46:13 Bye.
**Trask Stalnaker** 46:14 Cheers.
