SIG: Collector SIG
Date: 2026-06-24
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Harrison Fritz** 07:27 Alright, Jade, are you here for the collector SIG meeting?
**Jade Guiton** 07:32 Yes, I am.
**Harrison Fritz** 07:36 Cool, me too.
Just wanted to make sure I was in the right spot.
**Evan Bradley** 11:13 Alright, I think the, attendee list is starting to stabilize a little bit. Let's kick it off.
Does anybody have anything that they want to talk about for stability?
**Jade Guiton** 11:39 I was like, but no.
**Evan Bradley** 11:41 Okay, yeah. I just got… I'm just ramping up again from an Eternal project, so… Not sure what's happened. Okay, the next step… There's a, what do you call it? There's an agenda item about Kubernetes multi-tenancy. I'm not sure who introduced it, but go ahead.
**Harrison Fritz** 12:02 That… that was me. This is Harrison. Can everybody hear me?
**Evan Bradley** 12:07 Yep.
**Harrison Fritz** 12:09 Here, I'll turn my camera on. This is my first, time attending one of these, so I appreciate, like, how easy it is to jump in. But anyway, let me give the problem statement, and then I'm just interested in… some advice and maybe, like, direction from this SIG on, like, how can I drive this as effectively as possible, or, like, who I can collaborate with. But the… The problem statement, I can just read it, or I can share my screen, but… Basically, we run a bunch of, like, massive multi-tenant Kubernetes clusters, mainly for machine learning, but we have a ton of different use cases on them.
M… The lack of… decentralized configuration in the OpenTelemetry collector forces platform teams to make some tough compromises, none of which are ideal. And pretty much the three approaches that I'm seeing are You have, platform admins maintaining a huge centralized collector configuration that gets really unwieldy. Some tenants may need sampling on logs, some may be, like, you can't sample any of them. There's a whole bunch of different, like, telemetry requirements that tenants can say, hey, I'm special, I need this.
Way of managing my telemetry, and right now, The first approach is, like, just have… Platform admins do their best to manage that for, like, hundreds or thousands of tenants, which doesn't scale. Or… there's a few other approaches, but basically, I think that gets to, like, the core of the problem is… In, like, diverse multi-tenant environments.
there's no way for a tenant to basically be in charge of their own metrics, logs, and traces.
So I want to stop there, because I can, like, ramble about the details, but is that, like, a clear enough problem statement?
**Jade Guiton** 14:22 This be something to change about the collector, or is this about… Best practices on how to manage a fleet of collectors that are at least partly owned by different tenants.
**Harrison Fritz** 14:35 So, it… It's more… so the existing tools that I think people were using before OpenTelemetry had… basic… like, Prometheus, for example, has the concept of, like, like, pod monitors or service monitors, which means, like, tenant A wants to manage their, like, metrics in a certain way, so they bring their own little configuration to their, like, Kubernetes namespace.
And… Then the centralized, like, collector ingests that, but the… like, from the tenant's perspective, they fully own their telemetry?
And there's already an issue open on the OpenTelemetry operator, which I think is issue number 2 that I linked in the meeting notes.
Like, I'm next to discuss, multi-tenancy, the operator CR proposal. And it seems like that's gotten a bit of traction, but, I'm interested in, like.
this… maybe if anyone else is familiar with this problem and has worked on it, if there's anything I'm missing… could… could they tell me that? And also, like.
how can I… like, is this the right forum to discuss this, and how can I get a little more traction?
on this problem, because I think it's… I think it's more ubiquitous than… we might realize a lot of companies run, like, big Kubernetes clusters, and if they're coming from, like, FluentD or Prometheus scraping, they're… I know, like, we're really missing that… Like, tenant bringing their own configuration, fully in charge of their own telemetry to their application.
**Mikołaj Świątek** 16:32 if I could comment for a second as the author of that operator.
Is true?
I think it's… difficult to define scope the right way for this problem, and that's probably the toughest non-technic… non-directly non-technical part of it. Because, yes, that issue intersects with what you're asking for. I think it might also want to do more than you actually need.
And depending on what exactly you want to do, it becomes more or less complicated to actually accomplish this in the end.
And I… I can get… I think this is partially the right forum for this question, and the other… the other, right forum is the operator thing, which you are, you know, invited, invited to join, and we can talk there as well.
But… Essentially, the problem in this case is that, A, it's hard to define the scope, and the design in general has to be more general than it is for, like, Fluent Debate or for Prometheus, because the auto collector just does more than those applications, or at least Exposes more in a way that, like, tenants might want to configure.
And the other problem is that this is a technical problem which I think we might actually be starting to resolve now, is that, the collector doesn't currently have great facilities to Assemble a monolithic config from pieces, and do it in such a way that the tenants don't affect each other.
In this process, I would say, in the kind of… without going into the weeds of what that actually means, I think that's, like, the biggest technical blocker to actually, like… that would block you from kind of hacking it together, because you can probably hack together some Kubernetes controller that just, like, it takes a bunch of.
random CRs that you put together and sticks that into an auto collector that you've otherwise provisioned. But, for example, if whenever you have to reload that whole config whenever a tenant makes a change, what happens? How do you control how the processing costs of each tenant, right? Do you stick that out into a separate collector, or do you put it in your kind of monolithic gateway collector, and how do you manage that. Like, those are kind of technical problems without clear solutions right now, even if you can kind of handle the control plane aspect of it on your own.
Does that make sense?
**Harrison Fritz** 19:15 Yeah, yeah, that makes sense.
**Mikołaj Świątek** 19:17 And Ivan, I think you are next.
**Evan Bradley** 19:21 Yeah, so, I'm just, like, spitballing here for ideas. I would… Tackle this from a slightly different angle.
I would think about trying to use the load balancing exporter, which uses various mechanisms to determine where to send data at the exporter layer.
If we allow the load balancing exporter to read from, the collector also has extensions, and so these are things that allow interfacing, sometimes with, like, external systems, but they'll do other things too, but they're kind of like plug-ins to the various pipeline components in the collector. So, the way I would think about doing this is… You have your big collector that's ingesting all this data, you've got the attributes on there that have some record of where this data should go, you know, some kind of identifier. You would… Send that to the load balancing exporter, which would then use the… it would basically need to send some part of that data to… the extension, which, you know, reads your tenant, right, and then returns the load balancing exporter, like, this is the URL to send this data to. And then that goes to the tenant-specific collector. Because to what Mikolai said, there's not really a good way to have multi-tenancy, like, within the collector right now, so I.
**Harrison Fritz** 20:39 We're thinking about.
**Evan Bradley** 20:39 trying to look at ways for, basically tackling it with this system diagram that you showed in your issue, where you're sending it to individual tenant-managed collectors, and it's just a manage… or it's a way of.
Finding a way to map from a specific telemetry item to, a downstream collector to send the data to.
If that… I don't… does that sound like it would solve your issue, or…
**Harrison Fritz** 21:05 It's I think I need to look more into the load balancing exporter, but I think the idea of, like, tenants bringing their own collector to each namespace, it's not ideal. And we have a controller that rewrites a routing table to basically do that every time a new tenant onboards.
Like, a tenant will come, they bring their own collector, we have, like, a label on that collector that our controller watches, and then rewrites the routing table in the routing connector to basically send all of the centralized telemetry back to that like… team-specific hotel collector, so kind of like what you were saying, just… and it's not ideal for a few reasons, like, it works, but it… It's running a bunch of, like, little mini collectors.
And we also have to maintain a controller, and it also restarts all the collector, like, the centralized collector pods when that routing configuration is updated, so there's a few reasons why that's tough.
But… yeah.
**Evan Bradley** 22:11 So, this solution with the extension would reach out to an external system to do that mapping. So when that list would be updated, the extension would reach out and then see the updated list. Think like a Redis.
**Harrison Fritz** 22:23 Or something.
**Evan Bradley** 22:23 Just simple key value.
The thing I would… the reason I'm suggesting separate collectors per tenant is that even if we were to get the dynamic, like, routing table updating working, you still have issues, like, how do you determine that, or how do you prevent a specific tenant from using, for example, like, too much memory or CPU or other resources?
That's why I'm thinking that it would be easier to solve this at the control plane layer.
And you could basically… with the system I'm suggesting, I think you could… Essentially rewrite the operator layer you have right now to instead just be, instead of… You would essentially pull the target from it, rather than have the operator bit push the target to the collector, if that makes sense.
**Harrison Fritz** 23:13 Yeah. Yeah, that… that makes sense.
I think, really, the crux of the issue is coming from one paradigm that was, like, really easy to self-service in, like, FluentBit, or Prometheus, or, like, there's a few other tools like Istio, I think Grafana Alloy, they all have these concepts of, like.
namespace telemetry management.
Like, and getting used to that, and having it work well, and then migrating to open telemetry, where we have to like, there's not the exact same paradigm that exists is, like, I think has made, like, adoption and migration difficult. But yeah, I think I'll take a look at that load balancing exporter and do a little more research on that.
**Mikołaj Świątek** 23:57 Does Fluid… does the Fluent bit solution let you, control, like, resource consumption per tenant somehow?
**Harrison Fritz** 24:09 I don't think so.
**Mikołaj Świątek** 24:10 I'm asking out of curiosity, because we keep talking about, like, needing this, but maybe we can… we can try and ship it without that, and kind of just say, you know… We don't solve this problem.
**Harrison Fritz** 24:21 Yeah, I think for the Fluence bit stuff, log scraping… There is actually a lot of heavy processing you can do with like, the fluent CRDs, so I don't know. I haven't seen any way to, like, manage the scaling of, like, the daemon sets through the collector custom resource.
But it is an issue, so… I think I'm coming up on time, and I know… I think somebody else had their hand up, maybe?
**jmacdonald** 24:53 I'd like to speak, I have a lot of context on this… part of this problem, at least, and try and give you a more affirmative answer supporting your concept for tenants in the collector. I'm gonna put a couple links in the chat for reference. About a year ago, I was involved in the middleware extension. The reason I was there in the first place was I wanted rate limiters and resource limiters to be kind of become standard.
the reason I was… the person doing that, I guess, we were… I was, part of the Hotel Arrow project. Phase 1, we built Go Collector components.
the OTel Arrow receiver has a pretty strict memory limiter built into it, and I wanted to try and take that same memory limiter concept and apply it to the collector, which is how I ended up learning about extensions and getting the middleware stuff.
I still believe that we need both rate and memory limiters in… or resource limiters generally in the collector, and I, a year ago, did some preliminary research.
I do want to lean on extensions for this, but I… but it takes a little bit more of design work before I can tell you the whole story. I, So, I looked at the Envoy model, which has a fairly well-developed rate limiter, like a tenant-based rate-limiting infrastructure that is fairly flexible and lets you define the types of tenant architecture that you want in a pretty flexible way.
I have meant to come back to this group, as well as to the OTIL Arrow group, with a more formal and complete design. In fact, I've written it, and I have it pending an internal review before I share it. So, within a couple weeks, I promise to give you a document that proposes how to do tenancy in the OTil Arrow codebase, mostly because that's what my employer wants first, but I was thinking.
deserves to be backported or, like, shared, the same model for both this collector and the Otil Aero project.
And that follows… it does follow the Envoy model quite closely, so you would have a way to describe tenant descriptors, which are based on actions that extract things from context. So receivers would be configured with which tenant descriptor they are responsible for extracting, and then limiter extensions would be able to have a sort of standard way of using those tenant descriptors to create separate limits, or to create separate routing, or to create separate batching, or to create separate whatever. I apologize for not being quite ready for it, but I wanted to share the evidence that I'm working on this, and that I have a plan to come back with a tenant model for the collector.
That is somewhat general. It won't solve all the problems being discussed. I really don't have much to say about the operator or assembling Kubernetes or, you know, CRDs and so on. So there's more to this problem than just what I've described. And I promise I'll come back to this group with something.
Thank you.
**Stuart Buckingham** 27:47 I just, if it's okay, I wanted to just, talk about… I know Harrison, yourself, and I had a few back and forths on the GitHub issues, that, I've proposed a component or two, an extension to the observer framework.
for observing, Kate's CRs. I know that there's existing observers that are based on the receiver creator that are good for, for monitoring in-cluster resources, but with the sort of goal that I've got is to be able to use a similar framework for creating exporters, where customers or, you know, tenants on the cluster might want to define where they're shipping their Telemetry data to, and the most obvious way to store that metadata is as a custom resource.
And so by mirroring the receiver creator framework into a, exporter creator framework, and adding the ability to define those exporters with CRs.
Means that you can write CRs into the cluster and it will auto-discover them and things. I know it's a little bit different to what your end goal is, right? Where you want to define the whole pipeline as in a CR or some dynamic way, whereas this is just extending the, the collector… oh, sorry, the receiver creator, and then adding an exporter creator, and both can use the Kubernetes CRs to define them.
Is that sort of a step in the right direction? I've been looking for support for this project, because it's an internal goal that we've got, and we've been using this, currently, and we want to put it out there to the community. I just wanted to sort of gauge the rest of the room as well, in terms of, like.
is this the right direction? Does this help you achieve what you need to achieve, Harrison? And also, can we try to get this committed upstream?
**Harrison Fritz** 29:53 I think, I think I want to try out your distribution that you've linked of, like, your own collector config, because I think that'll help me understand, like, how much it meets the need.
Z, the reason I was interested in your post is because It seemed like… like, that definition of a new custom resource was close to what I was thinking. You're thinking, like, an exporter creator.
I'm thinking more of, like, what if there was, like, a pipeline creator or something, like, like, bring your receiver processor, exporter, extension connector, like, all of it in one, and… but… yeah. I want to hear what the rest of the group has to say, too.
**Mikołaj Świątek** 30:38 From your description, and I haven't reviewed this in any detail thus far, it sounds a little bit like you're reimplementing an operator inside of a collector.
since you're, like, reacting to CR changes, even though you're not actually mapping it to Kubernetes resources, you are mapping it to something inside the… Collector. And a lot of this just kind of sounds like… A job for the operator.
So, I would encourage both of you who use Stuart and Harrison, to, at the very least, give short descriptions of your use cases in the operator issue, because the main problem of the, from the operator perspective is that it was hard to decide what exactly the scope should be, and what exactly the use cases are that people have for it. So that would help us a lot, at the very least, even though I can't promise you that we're going to have a solution for this quickly, because it's pretty difficult.
From my perspective, I also want to say that there were, like, two hard technical requirements on the collector for this… for the operator to be able to do what we want it to do. One of them is to be able to do config reloading without, you know, bulldozing the whole component graph.
And the other was to be able to isolate pipelines so that if somebody writes a config that's wrong, it doesn't crash the whole collector, which is what can happen right now, and there is only, like… you can't cover the entirety of it with, like.
ahead-of-time static validation. You can absolutely write component configurations which will, like, fail to bind a port at runtime, and the collector will just terminate.
For example.
**Stuart Buckingham** 32:24 That's true.
**Mikołaj Świątek** 32:24 Another thing that we would have to actually have in CollectorCore in order to do this properly, in my view.
**Stuart Buckingham** 32:32 That first hurdle that you mentioned, the dynamic reload, was a hard requirement for us, because we usually run single-homed, collectors, so having any sort of blackout period was going to be a non-starter for us, so that was sort of… a big blocker that lent us away from the, the operator, as well as the existing architecture with, like, service discovery and things that is supported in the collector, sort of.
Gives the indication that dynamic endpoint discovery, and therefore, for the, for the receiver side is, you know, a first-class supported, method, and therefore, why shouldn't the, exporter side also… Have that as a supported method.
**Mikołaj Świątek** 33:22 I think, historically, we just didn't want to mess with exporters in this way.
But this is… but this is changing. For the record, watch out for the other… for something else that's going to be discussed during this very call… during this very meeting, in fact.
Because they're…
**Stuart Buckingham** 33:38 Okay, well…
**Mikołaj Świątek** 33:38 There's development. There's developments.
**Stuart Buckingham** 33:43 Great.
**Harrison Fritz** 33:47 Thanks for the discussion. I'll, I'll plan to join the… the operator… the next operator SIG meeting, too.
And, mikolaj. I think I'm saying your name correctly, correct me if I'm wrong, but…
**Mikołaj Świątek** 33:59 it's fine this way. I'm next, right? Are you good?
**Harrison Fritz** 34:04 Yeah. Yeah, I just… I linked something in the Zoom chat that I'm…
**Mikołaj Świątek** 34:08 Thank you, Mark.
**Harrison Fritz** 34:09 If you haven't seen that project, take a look at it.
**Mikołaj Świątek** 34:13 Yeah, but if they're doing the… they probably touch the collector if they're doing this. Anyway, are you okay with this level of discussion? Can we move on to the next point?
**Harrison Fritz** 34:26 I think so. Thanks, everybody.
**Mikołaj Świątek** 34:28 Alright, so I'm next. I just have a thing.
If you have power in Contrib, or you're a co-owner in Contrib, please look at it.
The gist of it is that if you're using configHDP, And you're instantiating client config, or server config, the struct.
Just by zeroing the struct, you're doing it wrong.
Those structs have defaulted, have default constructors, those default constructors set.
things which matter, and for example, if you happen to… for client, I suppose it matters a little bit less, but for a server, if you're using the config.http server config.
so you're starting the HTTP server in your component, and you just instantiate that, you're disabling HTTP Keep Alive, for example, which is a very unfortunate thing to do.
Especially not knowing that you're doing it. So there's a pull request.
And I am fixing this for mostly selfish reasons. The selfish reason is that we want to stabilize ConfigHCD. To stabilize that, we want to deprecate the current Keep Alive configuration, and we're trying to do it in a way that doesn't break things, and it doesn't break things if you use the default constructors. If you don't, it does break things.
Because the zero values of the fields are different.
After the change. So, there's a pull request. That pull request is, like, plus 3,000 minus 2,000 lines.
Its effect is nothing.
Okay, it doesn't… the net effect of it is zero, the only thing it does is it uses the default constructors, and then sets all the fields to what they used to be. So the effect is zero.
But now, it's explicit what is said, okay? It's explicit that all the components are in there. So right now, it's a draft, because I want to get some… a little bit more, it's really for review, I want to get a little bit more feedback, about actually doing this.
Before we kind of pull the trigger. But this is kind of the… by itself, this doesn't change anything, but I hope that all the co-owners will at least see it eventually, and go, like, well, what are we doing with, you know, with our configuration? Do we have keep lives disabled?
I remember we actually fixed this recently in the health check extension, and were surprised, and at the time, I didn't think to actually audit contrib for the entirety of it.
But, there we go.
That's it. Any, like, questions or comments about this?
**Tyler Helmuth** 37:05 This is great. These exist because we're supposed to use them. So thanks for taking it on. Is there… you're trying to do it as a no-op, right? Where, like, we're, like, using the new value, but nothing changes. Is there any possible way where… To, like, prove that it's a no-op, like, we don't change any tests, and, like, therefore, if all the existing tests passed, then we know this was a true no-op, or is it just… Contrib is unruly, and there's no one-size-fits-all, and… You just had to look at every single component in there.
**Mikołaj Świątek** 37:38 It does change some tests, but it mostly changes the test in the same way that it changes the normal config. Like, it prohibits using, instantiating the structs as zero values in the tests. Otherwise, it doesn't change anything. Like, all the contrib tests pass.
On that pull request?
I don't know what other validation we could do. Like, in principle, this is not a very complicated change. I could… I, I could… I wonder.
I could try to prove that the local code snippet that I'm putting literally everywhere, and I am really not in, like… I really don't have an appetite for trying to make a helper out of this, I'm sorry.
**Tyler Helmuth** 38:24 No, no, we don't need a helper. I mean, the constructor is the helper, the new default is the helper that…
**Mikołaj Świątek** 38:29 Yeah, but I mean, my helper, my helper for the, for the, like, no-op migration, essentially, which is, like, the same… setting the same fields to the same values everywhere, in essence. I don't know if I can validate this, any, any further. It should be.
**Tyler Helmuth** 38:47 Okay.
**Mikołaj Świątek** 38:47 It should be, like, no effect.
**Tyler Helmuth** 38:50 Okay. I think if you're feeling good about the state of it, just take it out of draft and we'll try to look at it closely.
**Mikołaj Świątek** 38:58 Okay.
I want to wait until all the Windows, whatever. I had tests failing on Windows ARM, which I'm pretty sure is not my fault, but we'll see once it succeeds, and I… and since I'm not getting any pushback here, I'm gonna take it out of draft, and we'll see where we land.
**Tyler Helmuth** 39:15 Awesome.
**Pablo Baeyens** 39:18 I guess my only comment, other than thank you for doing this, Chris. Cheers.
Great, and also a lot of work, I assume.
Is if we could get a link to an issue on the to-dos, so that we track somewhere that… We actually fix these things?
**Mikołaj Świątek** 39:40 Yeah, I'm gonna… That would be great.
I'm gonna open a new issue for that, I think, because I created an issue to get the defaults in, but this should be a… this should be, I think, a separate one, which is not about using the default constructors, it's about, like, actually… actually for code owners to actually decide what… how they want their components to Right. Knowingly. Yeah, I can do that, no problem.
**Pablo Baeyens** 40:03 Okay, cool. And thanks again.
**Mikołaj Świątek** 40:11 Yeah, so that was everything. Blake, you're up next.
**Blake Rouse** 40:17 Yeah, mine's gonna be really quick. Mine was just for the first phase of, partial reload, the receivers only. That PR is up for review. I just was trying to… Bring awareness to it in the call.
That's the phase one that was part of the RFC that was merged, so this one focuses only on, the receivers only. So, if anything changes outside of receivers, full reload still occurs, but if it's only for the receivers.
It starts and stops the receivers. This is probably the simplest one.
Because, it's the simplest one, but it does have, like, obviously the extra code in there to see what's changing in the config, so that's kind of new. But when I say it's the simplest one, it's… since receivers are at the start, there's no real, like, hey, I need to worry about, like.
things in front of it, right? Like what we're gonna have with processors or exporters and things like that. So, yep, just trying to bring awareness to it. Please take a look, one, if you're interested, and two, if you're an approver or maintainer, would be great. So, yeah, that's it.
**Mikołaj Świątek** 41:38 Yeah, and it's just…
**Ravishankar Gnanaprakasam** 41:39 Moonlight.
**Mikołaj Świątek** 41:39 Harris, sorry, sorry, just for a moment. For Harris and Stuart, this is what I meant. We actually merged in RFC recently to actually do PowerShell config reloads in the collector, so at least this technical barrier is slowly going away.
And this is, like, the first phase of it, this pull request. So you can check it out if you want to see if it's, if any of it, Well, or at least if the RFC sounds like it would, help you.
**Stuart Buckingham** 42:16 Will do. Thanks.
**Ravishankar Gnanaprakasam** 42:21 Yeah, I think the last one I had is just to… for, PR reviews and merge. So, there are… I mean, like, there's two PRs which, I would really hope we can get it in 1.56, because one is, like, a small, you know, CI improvement in contrab, like, for markdowns.
So, it has a dependency in core, so if someone can take a look on that, you know, and get it by 1.56, we could… Push that.
And the other two, I think we have, reviews, I think it's waiting on code bonus. And one new thing is for the config storage that, we discussed on the last SIG, so I've raised PR for that, and once that is merged, I will, implement the same in the export helper.
So, yeah, just a FYI for people, like, to take a look on that.
Yep, that's… thank you.
**Evan Bradley** 43:47 I'll try to take a look at these today, if I'm able.
Thank you.
**Ravishankar Gnanaprakasam** 43:52 Yeah. Thanks, Evan.
**Evan Bradley** 43:54 Does anybody else have any agenda items? We've reached the end here.
Going once… Alright, see ya.
