SIG: Kubernetes Operator SIG
Date: 2026-07-02
Duration: 145 minutes
============================================================

## Zoom Recording Transcript

Harrison Fritz 00:02:24 How's it going?
Mikołaj Świątek 00:02:26 Hello, good… I don't know, good morning? Or is it afternoon?
Harrison Fritz 00:02:32 It is morning for me, I'm in San Francisco.
Yeah.
Mikołaj Świątek 00:02:40 Whoa, Jacob, what is this, what is this new, this new look, this new vibe?
jea 00:02:47 I remembered.
Mikołaj Świątek 00:02:47 Just…
jea 00:02:49 I'm on vacation, so…
Mikołaj Świątek 00:02:51 Are you sure you want to be in this meeting?
jea 00:02:54 Yeah, I'm happy to be.
Mikołaj Świątek 00:02:59 Alright, the little, little GIF.
Our stragglers a little bit more time.
jea 00:03:07 Michael, I have a really dumb question for you.
Mikołaj Świątek 00:03:09 Oh, no.
jea 00:03:11 Unrelated to anything that we do.
Mikołaj Świątek 00:03:13 Okay.
jea 00:03:16 Do you have a secret, Relationship to the famous tennis player who shares your last name?
Mikołaj Świątek 00:03:24 No.
jea 00:03:25 Okay. I'm gonna do the last question.
Mikołaj Świątek 00:03:29 Surprisingly few, but I am happy she exists, because now there's a normalized spelling of my surname, so sometimes when I, like, check into a hotel, I don't have to give them my ID so they can understand what to put in there.
They now know. But no, no, there's actually, like, a second line of my surname living in my hometown of 40,000 people that is completely unrelated to me, so it's, like, not, not such an uncommon surname.
jea 00:04:01 But it's… yeah, but it's not super common, right?
Mikołaj Świątek 00:04:04 No, no, it's not super common, but it was, like, it's also not super uncommon. As it turns out, I was surprised to… I can give you… I can also give you, like, a bonus fact about my name and surname.
Usually, you can kind of translate my name and surname together as Santa Claus.
jea 00:04:25 Really?
Mikołaj Świątek 00:04:28 Yes, because my name literally means Nicholas, as in the name of the saint, and you can kind of translate my surname as meaning saintly, something like that.
jea 00:04:40 Wow. That's… Right, right.
Mikołaj Świątek 00:04:43 Kindergarten was awful.
I still… I still carry scars from that time.
jea 00:04:50 Yeah.
Oh my god.
Mikołaj Świątek 00:04:53 Alright, let's actually… let's get started. Like, if Pavel wants to be late more than 3 minutes, then he can catch up in his own.
Right, so, Harrison, thank you, thank you for making it here.
Harrison Fritz 00:05:09 Yeah.
Mikołaj Świątek 00:05:10 That you… that you managed?
Jacob, we are… we are unearthing the distributed configuration problem.
Harrison Fritz 00:05:22 Yes, I don't know if that's a good or bad thing, but for… yeah, thanks for… thanks for running these meetings.
So… I think we already talked about this, at least, like, some of us in the collector SIG, but… If you look at the agenda, I've linked two issues, one that I opened, and it references a bunch of other issues that kind of touch on, like, some sort of distributed configuration.
But, just for people who aren't familiar with the issue, We run a bunch of large Kubernetes clusters with thousands of tenants, and the tenants we don't know in advance.
So, coming from stuff like Prometheus operator and, different, like, fluent operators.
There's the concept of, like, kind of a distributed configuration, where tenants can bring their own custom resource.
Applied in their namespace, and have full control over their, their telemetry, so for fluent logs, for Prometheus operator metrics.
And we've recently migrated all of these clusters to a fully OTEL approach, and we're really missing that, like, self-service ability for our tenants to be able to have control over like, the processing and exporting of their telemetry, so that's the problem. I'm taking a crack at, at, putting together, like, a vague design, and I, But I just wanted to, like, start the discussion in this SIG, because it's my first time joining, and see if anyone else is, like, interested in this issue.
Or maybe knows something I don't.
I guess the last thing I'll say before I, like, turn it over for open discussion is the… the… let me see if I can share my screen. I'm just taking some… Notes… Oh, I'm not gonna be able to share, because I forgot to update my permissions, but if you… If you click on… this link that's in the agenda, I'll put it in the Zoom chat. I'm just basically doing, like… like, some notes, a rough draft design doc on… Trying to break down this, like, what the problem is.
And, suggest some solutions. So… I think the Prometheus operator and the fluent operator and that kind of paradigm is pretty established, but I know, like, they… those operators are much more narrowly focused than Like, the hotel operator, so… The devil's in the details with these kind of, like, implementations, so, Yeah, I don't know if anyone has any thoughts, or… That's… that's the… That's my rant.
jea 00:08:22 Yeah, we can, miguel, you want to start?
First off, thank you for joining. This is, like, great to read through this document. Clearly, you've, like, thought a ton about this, which is great.
there are a lot of challenges with OTEL, not just because it's more broad in focus, but the general model makes this a lot more challenging in a push-based world, right?
That model doesn't lend itself well to how service discovery works for logging and, like, Prometheus metrics, right? Because in a pull-based world, you can simply just have a subscriber.
Right? Yeah. And that subscriber then… gets added to the actual, like, centralized collection pipeline pretty easily, right?
Harrison Fritz 00:09:18 Exactly.
jea 00:09:18 actually tell… and then because it's pull-based, you're just telling the centralized thing, hey, go look here.
Right.
Harrison Fritz 00:09:24 Yeah, and just to clarify, like, when you say pull-based, like, Prometheus is, like, a pull-based system where we're scraping stuff. People are pushing telemetry via the hotel SDKs or, like, auto-instrumentation to a collector.
jea 00:09:38 Exactly.
Harrison Fritz 00:09:38 Hotel, like, so for logs, like, and logging is probably the most, like.
Complex case that, like, we run into this, because we're scraping logs off of a file on the node.
using the file log receiver, and that, to me, is kind of like… that's a pull-based approach. We have these legacy log implementations that are never gonna get… well, maybe not never, but there's no plans to convert them to, like, a push-based OTEL system.
So that's, like, that whole, like, scrape the file system is probably the top-of-mind use case for this multi-tenancy, because we're… that's… we're coming directly from, like, a fluent, paradigm, which… Yeah, I mentioned before, and moving to hotel where we don't have the, like, multi-tenancy self-service.
jea 00:10:28 Yeah, so that is where I think… so we had a conversation about this, like, 2 years ago, maybe, and there was a group that came to us from a company called Axiflow. Do you remember this, Mikolai, when that guy came by from… Yep. They run something called Logging Operator. You're familiar already.
Harrison Fritz 00:10:45 the telemetry op… the telemetry controller and logging operator, yeah, I've looked at both of those, and I've… I have issues on… I mentioned it in, like, when, and it… anyway, yeah, I'm super familiar with those. They're trying to solve… the multi-tenancy problem, but that I have some qualms about adopting their project, because they use a special distribution of the collector.
And it is… they don't have all the bells and whistles of open telemetry, so I think I need to be sold on some of their design choices more. And also, there's only 4 contributors to the repo, so…
jea 00:11:22 Not suggesting that you should go with them, more suggesting that, their model for doing multi-tenancy is one that we've thought about, but in our initial sort of read of it, thought it was both too narrowly focused and also a little bit overly complicated.
Yeah, and so… I think that… were we to, like, do this again, I think it's important that we have a clear idea of Like, the problems that we're attempting to solve.
Like, I don't think we should reinvent, service monitors and pod monitors. Like, those exist, we already use them in the operator ecosystem. I think it does make sense to have, logging done in a… to allow for the multi-tenancy case.
Tracing is a little bit more challenging, but we're sort of already looking at that with… the work that Pavel's doing with the next version for, instrumentation.
for, like, auto-intermentation and injection.
So I think it makes sense for us to have a better logging story. So I think if we were to focus on… A distributed config for… The file log receiver.
That… that narrow focus would probably make a ton of sense to do. I think where it gets challenging is trying to layer on more… functionality. And so… Miguel, I'm gonna say one more thing, and then I'll pass to you.
So there's a, OTEP that I just wrote that just got merged in this past week that is interested in doing dynamic configuration and sort of the management centralized management of… Things like transform and filter rules.
Which would allow for a much better multi-tenancy story for, like, internal to the processor layer, which today is really challenging to do any remote configuration for.
I'll post that in here, and we can talk about that a bit later, but I think that focusing on the receiver side Strong story there will be super valuable.
Nikolai, I'll pass to you.
Mikołaj Świątek 00:13:42 Right, so… To me, again, the difficult part of this whole problem is to… Define what exactly the scope of it is.
Historically, the distributing… distributed configuration issue that I originally filed.
Suppered a little bit from this division.
Where… Part of it pulled in the direction of Let's… let's help… let's help platform teams by allowing them to delegate some of the ability to configure collectors in some way to their… to the teams, to the tenants, however you want to call them. These are slightly different use cases, whether you have, like, tenants Which you don't know and have more control over, versus, versus, like, teams on a platform, which you have some… some control over. But it kind of… it is… these are kind of convergent use cases.
And the other way it was pulling was… let's try to make the operator more batteries included. Like, let's be more opinionated about what we're doing. And these things are… unfortunately, there is a little bit of convergence between these as well. So that was… that was kind of a… problem for us, that these were… these were, like, the two things that we wanted to do broadly, but… and it looked like the solution had some amount of overlap, but we couldn't properly scope what it is exactly that we needed to do, which is why we always tried to ask for use cases from people. We didn't get that many, unfortunately.
But it would be much easier if we had, like… your idea helps a lot, because it's, like, it's specific. It's specific about what exactly our… what exactly your problems are, and… and what you want to do.
I have, I have only now, only now, so I have only really skimmed it, but I did read the document that you linked.
And I think… yeah, I think that… like, a lot of the problem… let me tell you what architecturally, I think is the biggest problem and the biggest decision in solving this problem.
now, not in terms of the API that is exposed externally, but in terms of the internal architecture of the thing. The problem of the internal architecture of the thing, relative to something like the Fluent bit solution or the Prometheus solution, is that those have well-defined topologies. Like, the architectures are well-defined. You have a single Prometheus, maybe it's… or maybe multiple Prometheuses with different, you know, areas assigned to them, but you have a Prometheus. It has a certain amount of So, monitors assigned to it, it gets them, it does service discovery, it takes the targets, It scrapes.
And that's it. It's just a single thing. Similarly, when you have FluentBit, you're only really collecting logs from a node, right? And that's the only thing you have running in the system, and everything that you can configure in those Fluent Bits is, like, scoped to this.
To this deployment.
method. Whereas with the auto collector, oh, you know, we have some things running as a domain set on the node, we have something running as a deployment, this is our cluster collector, and then we have some gateway that might do some processing and ship some stuff somewhere, you know. What happens if we want Prometheus metrics with the target allocator? That also has 3 different deployment methods. So, and realistically, you can only really do two things, right? You can either let your users control this in some way, or you can just say.
We have an architecture, everything that happens needs to fit into that architecture in some way.
An example of an architecture is what is done by default in… there's a Helm chart, I don't know if you're aware of, it's called OpenTelemetry CubeStack.
And that contract, by default, basically says, there's a daemon set collector, it collects everything that's local to the nodes, there's a cluster collector, it collects things which are global to the cluster, there's a gateway. They both ship to the gateway, gateway ships somewhere else. That's it. And… It might… my idea for how to proceed with this from the start was something like.
Take this architecture, we just… accept things that can fit into this architecture, which I think is almost everything, if you do it the right way, and then we… whatever we let be configured or set, has to be… has to explicitly fit into one of these pieces, and then everything else becomes much simpler. Does that make sense?
Harrison Fritz 00:18:35 Yeah, that makes sense. I think I… So, my thought on the, like, the specific custom resource… Like, that users would be interacting with would be, like, it would have to have some way of being, like, aware Of the architecture, but, you know, like, you could basically say, like, okay, user, define a pipeline, so user defines a receiver, processor, exporter, and then you have, like, another field that says which like, collector do you want to inject this pipeline into? And… and then… and I'm still fleshing out the details, but then you'd have, like, the operator basically just merge all of these separate configs into a gigantic, like, just single collector config at the end of the day.
But those are… yeah, I see what you're saying, like, there's… it's a way more complex, like, problem than, like, for OTEL than it is for these, like, more narrowly scoped operators.
I tried to… break down this problem, and I know I said I'm coming up on time, so, like, I can, you know, cut me off if I don't know what else is on the agenda.
I tried to, like… this is talking to Claude, so anything that I… I have an appendix here, which is, like, Claude's design, and then I'm slowly moving it into, like, you know, editing it into, like, the one above, but, like, there's a few different problems that I think we can tackle to try to, like, like, scope this better.
one… so this is, like, what should the custom resource be that the tenant, like, interacts with? So that's… that's one.
The other one is, like, how do those custom resources get, like, merged or ingested, like, at the end of the day, into, like, the actual daemon set or deployment or sidecar container, like, as a config map, I guess, or secret? Like, I know Prometheus compiles everything into a secret and mounts it like that.
And then there is, like, the restart problem, which I think we talked about a little bit. Like, if we have thousands of tenants constantly applying these new configurations.
we would just have, like, let's say, like, a daemon set continuously rolling, like, every single time, so… so there's a few different, like, problems that I think we can… we can break it down into, and this is my attempt to… I think I'm sharing my screen, right?
Mikołaj Świątek 00:21:10 Yeah, yeah, we can…
Harrison Fritz 00:21:11 Okay, good. That would be… but anyway, so I think I'm going to continue to try to just, like.
push this design forward, and I think it'll, like… I need to… maybe this weekend, or whenever I have time, I'll build my own, like.
I'll try to actually start doing some of the implementation, just to, like, try out some stuff, And then I can come to the… The next meeting with, like, a more concrete example that we can look at.
Mikołaj Świątek 00:21:40 Yeah, I want to… something that kind of jumps out to me, looking at this… sorry, Jacob, I'll… you're next, okay? I can see that you're ready to go as well. So, something that jumps out to me from this document… from this document is that Yeah, it's kind of a list of problems, but those problems fall, like, under different… categories in here. Like, the category of what does the tenant interact with, and what do they get to set exactly, and what is the structure of what they get to set, I think is a very… is a pretty diff… the most difficult problem in this, honestly, defining that. But this is, like, an API problem.
Right?
Harrison Fritz 00:22:21 Yeah.
Mikołaj Świątek 00:22:22 The problem of… Collector restarts are not performant enough.
is a technical problem inside the collector. Like, that is not… you know, these things, in some way, are independent. You have to sell a bulk of them to get the solution that you want at the end of it, but you don't have to… they don't… they aren't coupled in any way. And in fact, as I think you now know, at least the… the, the configuration reloading problem is being solved in CollectorCore. Whether that will still be performant enough for all use cases remains to be seen, but, like, soonish, that should be merged, and… and you'll be able to, like, flip a feature gate on and at least get some level of reloading.
Or… or there's, like, a full implementation of this as well, as a pull request.
Jacob.
Yeah, yeah, yeah, I can, in a moment. You can also find it. There's an RFC in the collector.
Repository for this, describing the… what's gonna happen.
But that's one of my observations, is that technical problems to be solved in the collector. Another problem, technical problem to be solved in the collector, for which there is no solution on the way right now, but it still needs to be solved for this to work at all, in my opinion, is to be able to, not terminate on config errors, because chances are, whatever you put in your CRD will not be sufficient to guarantee that the collector will actually run it without crashing. The only proper way to know if a collector will run something is to actually try running it.
And… Yeah, so there needs to be a feature, which probably wouldn't be such a complicated feature, but there needs to be a feature in the auto collector to actually say a flag, to be able to say, if this pipeline fails, just continue, everything else needs to run, right? And this also ties into the reporting, status reporting problem. Like, realistically, if somebody writes invalid configuration, what you want to be able to do is to say, hey, you wrote… in this CRD, in this custom resource, you wrote the configuration. Here is the error the collector spat out for your thing, right? But there needs to be some way of collecting that status, reflecting it, maybe you have to interact with the status reporting framework, maybe with OPAMP, even, right? This is… this is also something that needs to be solved. But again, this is also a technical problem. The API problems and the architectural problems are kind of orthogonal to it, in a way.
Right.
And… This is just… a thought I had, I remember having, and this has lived in my head for a while, but the way I always thought about this… and this was from a platform perspective, it wasn't necessarily from, like, you know, we're running tenants who are customers of… about whom we don't necessarily know a lot.
In, in our, in our large cluster. But my idea at the time was basically, that… You would have some notion of a source of data.
I'm intentionally not using the collector terminology of receiver, processor, and exporter to differentiate between these concepts. So you have some notion of a source of data. The source of data would be something like container logs.
These are container logs, and this would be attached to a daemon set collector, to some daemon set collector, by you as a platform admin, and you would expose that as a resource.
to other users of the cluster. So they wouldn't get to write their own file log receiver.
receiver configuration, because honestly, that sounds really difficult to scope.
Like, it sounds really difficult to scope writing your own, like, unrestricted hotel collector configurations without, like.
breaking every possible security boundary that should exist in this system. So I think it would need to be something in that respect, where you have something that's called a source, which is really a receiver that is already guaranteed to run in the right architectural context, in the right deployment.
plus maybe some processors, if you want to have them in there as part of that abstraction. And then the… your user says, I want data from here, which is… which has this and this shape, right? There's some way for them to tell what… to say what they want from it. I don't know if this is enough to actually properly isolate tenants, but I think this is a more realistic way of trying to do this without having to contend with you know, we just let the user write their own component configurations and their own pipelines, and then try to fit that together, you know, into a reasonable whole. But that's just an idea I have. It's not very well developed, so I don't… also don't want you to, to be… to… to be too primed by it. Sorry, I've talked a lot. Jacob, you're…
jea 00:27:52 Yeah, so a couple thoughts. I do think that what Mikolai just said is what I would also echo, in that I would not recommend trying to do a full pipeline configuration. I think… from a user perspective, given that you're trying to give this to, like, you know, a team, a user, not necessarily, like, an SRE or an ops person, you want to make it, like, really well constrained, right? Like, the tenant should be a constrained thing, where the boundary is really well set.
Otherwise, the scope of this just continues to expand, as Nikolai said, for, like, security, but also, like, configuration merging gets really tough.
the more that you try to do this. A good example of this is that, let's say you want to, again, if you want full receiver configuration, two different users define the same OTLP receiver configuration on the same port.
Right? That would be an invalid configuration, because they're running on the same port.
Right? But you then need to do something to deduplicate them, and then split the pipeline for the processors that they both want to run in that pipeline, right? That's a really, like, technical and difficult thing, and then you have to have validation logic it just… you see what I mean? Like, it grows that scope really, really far. And so I think Focusing on, like, log source, and that only configures a set within the file log receiver is going to be a lot simpler to do, and I think a thing that is much easier to experiment with than any of those other cases.
The other thing… have you already looked at the, the receiver creator pattern?
Harrison Fritz 00:29:36 Yeah, I have.
jea 00:29:39 Were you able to, like, make that work with a multi-tenant environment, or was that not enough?
Harrison Fritz 00:29:44 It's not something that I actually, like, tried to implement, but I did… I did look at it, and I think the… the receivers are probably the least… the one I'm the least concerned about. It's more about, like, processing and exporting.
like… But yeah, I've been… there's another issue open to extend that also for, like, exporter creator as well.
but, yeah, maybe I need to take another look at that, but I don't think that would fully… solve our issue. Like, if I could type fast enough, and tenants could communicate what they needed fast enough, I could… I could just sit at my computer all day and maintain this config as, like, and pretend the daemon sets and deployments don't restart. So I'm just looking for, like, something to automate that. But these are great examples, like.
that I will think more about, like, so yeah, thank you.
jea 00:30:40 Yeah, and all that's to say, like, this is something that I think everybody in the sort of collector ecosystem, or maintainers, like, thinks of a lot, and cares a lot about, and, like, we want to see done.
There have been a lot of attempts to do this over the past, like, 5 years. Like, I… I led a team 3 years ago where we dedicated 2 years trying to solve this exact problem, and failed. Frankly.
Harrison Fritz 00:31:06 Oh, man.
I should just… I should just give up now.
jea 00:31:10 I… no, I don't think you should. The lesson learned is that you need to scope it very small.
So that… to exactly the use case that you have, because otherwise the… the scope expands. It, like… Uncontrollably and infinitely, and is going to make everything really, really complicated.
I'm fat.
the…
Harrison Fritz 00:31:33 Gotcha.
jea 00:31:34 Okay.
Harrison Fritz 00:31:34 Okay, that's…
jea 00:31:35 Glad I mentioned.
Reporting status is something that started very, like, targeted in scope, because we wanted to replace the broken help check extension.
And then turned into, like, a two-year project.
Great.
Mikołaj Świątek 00:31:47 Which is now reason… it's now in reasonable shape, so that didn't fail, right?
jea 00:31:53 No, that didn't fail, that was worthwhile.
Mikołaj Świątek 00:31:56 Aside from the fact that a lot of components don't do enough of it, it works well.
jea 00:32:01 It does, yeah. It is in there. More of just using that as an example of, like, if you want this in a reasonable time frame, like, we are all… I mean, I'm speaking for all of WE maintainers in this SIG, but it's like, we're all definitely interested in having this within our Within the, like, CRDs that we offer. And, like, we're usually a pretty vast Group to get things out.
As opposed to the collector, which is going through a lot more stability and is less likely to do something of broad scope.
So… in that sense, like, if you could figure out a well-scoped way to make this work within the operator ecosystem and the collector ecosystem, I think that that's something that we could definitely, like, look into, and would be a lot more likely to be able to add in.
I think, yeah, do some thinking on it and some, like, research on it. Go through the whole corpus of issues that we've talked about.
And come back maybe for our next SIG, and we can, like, discuss further there. I'd also definitely check out the policy work that I'm doing right now, because that is really aiming to solve the processor part of this in a way that does not currently exist in the OTL ecosystem, which has, like, dynamic configuration, dynamic reloading baked into it. So… That should be a lot easier for the processor part of this. We're also talking about The exporter and, like, routing part of this, but that's… we're still a bit too early to, like, get there.
But that's the way.
Harrison Fritz 00:33:35 And that's the issue… that's the issue you linked, or the pull request you linked, right?
jea 00:33:40 Yeah, I can actually just… it's been merged, so I can just link you the actual, like, OTEP.
Boom, give me one sec.
Pavel, you've had your hand raised, I want to give it to you.
Pavol Loffay 00:33:55 Yeah, thank you. I think pretty much everything was mentioned. I agree that we should be smart about the scope, and kind of constrain it somehow. There is, as well, this proposal from Bene, I put it into the agenda. It's about… patching the existing collector CR, which… I think it's related as well as the capability to kind of distribute the configuration.
So, but yeah, it's… it's related, I don't think we have made any good progress on it either, but there is diff… that there is… definitely shows that there is multiple people thinking about this, and how… That there is a need for such a… Feature, but, yeah, we haven't come to a good conclusion yet.
Mikołaj Świątek 00:34:54 Yeah, the cluster observability is actually a sign that we're trying to solve the other part of the problem from our perspective. The part where we want to be very opinionated… we want to put out a very opinionated way of collecting telemetry in the coronavirus cluster. That doesn't actually… help you, I think. Like, your needs are much more… general than what this does, but if the cluster observability CR works out, then that will kind of leave the other parts of the problem to solve what you're doing, essentially, without, Without interference from, you know, pulling it both ways, trying to… trying to do two different things.
Pavol Loffay 00:35:44 Yeah, I think the patching from the cluster observability should be really patching about the collector CRM. Like, it should be more generic, not tied to the cluster of sellability.
I think those are two different use cases. One is about providing good defaults for users, like a get-started configuration that works for most users, and second one is more… How to distribute the configuration.
How to allow users to tweak it.
Harrison Fritz 00:36:22 Gotcha. Yeah, I'll take a closer look at all of those.
Thanks for, such a, like, deep, long discussion. I think, like, I have a few more, like, technical examples and things that I can… Chew on before the next… the next time we meet.
Mikołaj Świątek 00:36:40 Yeah, I think, like, the technical problem, for example, of resource isolation is quite difficult. I'm not sure you can do this in any way other than… by using some kind of proxy for it. You can't actually tell how much CPU a pipeline is using, right? But you can tell how much data is flowing through it.
So… That's a possibility, to have, like, not even, like, proper resource isolation, but just have circuit breakers for.
Harrison Fritz 00:37:12 Easy.
Mikołaj Świątek 00:37:13 appear to be… appear to be too heavy. And… and if you do go with an approach of expensive processing happens in the gateway, which is much more… much more scalable, then you can kind of deal with it, right? Somebody can still DDoS you.
Technically. Yeah. I think… Yeah.
Harrison Fritz 00:37:34 And I think other operators, like… like Fluent, FluentD, like, you can do some pretty expensive processing on… on logs, like, using, like, regex or whatever.
And I don't think they solved that problem either, but it is worse for a hotel, just because you can do so much. Like, you, so yeah. But I will… Yeah, it's…
Mikołaj Świątek 00:37:58 In FluentBit, in FluentBit, you can even write, like, you know, you have Lua available, so you can, you can technically, you can implement, like, a Bitcoin miner in there, if you're, you're very determined, most likely.
But yeah, maybe, like, maybe if this… if the fluent… Solution is not… you know, if the Fluent solution solves a lot of… a lot of problems for a lot of people, and… and it doesn't have the resource isolation, maybe we don't need to care that much about resource isolation to begin with. Maybe we can, like, either do a best effort attempt at this, or just say we're not solving it right now, maybe we'll figure it out in the future.
Right? And maybe this is not a deal-breaker. There are some things that are deal-breakers, like the config reloading, or the validation, I think, because those are just going to be too operationally problematic.
But… but maybe the resource one is not.
Harrison Fritz 00:38:59 Yeah, okay. Well, Yeah, I guess the only, like, final question I would have is, should I join… like, this seems like the right forum.
some other forums I'm thinking about joining is, like, there's a few, like, Prometheus and Fluent, like, community meetings that, like, I don't know if they would be… amenable to, like, someone coming in and being like, hey, I'm interested in learning about what you guys did, so I can, like, build an hotel version of that.
Just any other suggestions?
jea 00:39:31 It's very, like…
Harrison Fritz 00:39:32 forums I should join.
jea 00:39:34 I think that you could… read their docs. I think going to their meetings and asking that question might be a bit, might not be seen in, like, the best… you might not… They're probably just gonna complain about the, like, existing hotel stuff, rather than.
Harrison Fritz 00:39:49 Yeah, yeah.
jea 00:39:50 what they did.
Yeah.
Harrison Fritz 00:39:52 Yeah, that's fair.
jea 00:39:53 I would just messaging our, like, Operator channel, and we can do discussion there.
We're all decently active on Slack.
So… It's probably the best place.
Harrison Fritz 00:40:08 Great.
Mikołaj Świątek 00:40:10 I would say, for fluent, I have no idea, personally.
Prometheus, in general, I think, like, the collaboration between Prometheus and Otto isn't too bad, overall, but I don't know if, like, this specific thing… if you go to Prometheus Operator and ask about this, I don't know if they, like, have… This isn't the problem that they have, right? They have a very good abstraction that fits their model, and they don't care about anything else, because why would they, right?
Did that… Jacob, did that talk actually say that? Because I was there, and I recall that it was kind of ambiguous who was fast.
jea 00:41:00 No, no, there was a talk on the, there was a talk during Observability Day, like, two or three years ago, where, somebody showed that, like, the collector had 3X performance for, like, 1 third or one-fourth the memory of, like, fluid bits.
Mikołaj Świątek 00:41:15 I don't think that's even true, like, fluent bit is really efficient, right?
jea 00:41:20 No, it's really bad at.
Mikołaj Świątek 00:41:21 beautiful hand-rolled C codes in there, with a custom asynchronous, like, a custom coroutine implementation.
jea 00:41:30 That's, the Fluent D, not Fluent bit.
Mikołaj Świątek 00:41:34 Yeah, no.
jea 00:41:34 like, single-threaded Ruby.
Mikołaj Świątek 00:41:37 No, you're mixing it up. I'm mixing it up.
jea 00:41:39 Oh.
Mikołaj Świątek 00:41:40 Yes.
Harrison Fritz 00:41:41 Fluent bit's, like, the super performant one.
jea 00:41:45 Oh, okay. Yeah, FluentD is the baby one, but, that's the one that they compared it to.
Mikołaj Świątek 00:41:51 That's…
jea 00:41:52 Which makes sense.
Mikołaj Świątek 00:41:54 That's surprise… that's not… that's not… I'm not… I'm not surprised that FluentB is slow. I would be surprised, like, if FluentBit was slow, considering that, like, the whole…
jea 00:42:03 Yeah, yeah.
Mikołaj Świątek 00:42:03 The whole big, you know, unique proposition of that project is that it's really performant.
Essentially.
jea 00:42:12 Yeah. And yeah, Prometheus has gotten a lot better with their hotel support. I think that Nikolai's right, like, the answer that they would give you is probably just, like.
only use Prometheus, is that?
It's probably what the…
Mikołaj Świątek 00:42:25 You know, they would say, oh, you need to collect logs, how unfortunate for you, you know? If you're only collecting metrics, then we have a solution for you, and it's called Prometheus Operator, it's really great.
Harrison Fritz 00:42:38 Well, now that… with OTEL, like, there's no… the only reason to run Prometheus is as, like, a database. Like, because you can just do all the scraping with… with OTEL.
At least that's been my experience, so…
Mikołaj Świątek 00:42:53 It highly depends on, kind of, where… what your stack actually looks like, and… and what you're… what you do. Like, there's a certain amount of convergence going on between Autel and Prometheus in a lot of respects, like… Prometheus also has a bunch of stuff they really don't want to maintain, like, for example, they're all their custom exporters they've written over the years into Prometheus, and they're like, can we turn this into an auto collector? That's what they said during the recent QCon.
Essentially. Like, can we, can we get rid of this stuff?
And the interoperability between open metrics and the auto, protocol is complicated, but it works.
So, so these are, like… the collaboration there is alright. In the fluent world, it's… I don't know if I would say it's a rivalry necessarily, but they probably like us a bit less.
By the way, this meeting is recorded, should I be saying this stuff?
It's.
jea 00:44:00 I don't think they get posted anymore.
Mikołaj Świątek 00:44:02 But it is recorded.
jea 00:44:03 I'm gonna put…
Mikołaj Świątek 00:44:04 Who knows? Who knows?
jea 00:44:05 Thank you.
Mikołaj Świątek 00:44:05 snow.
Harrison Fritz 00:44:07 I've watched a few, yeah, I don't know, but I've had great experience with Fluent stuff, just so it's on the record.
Mikołaj Świątek 00:44:17 Alright, so I don't want to eat too much more time, because I know others waiting with.
jea 00:44:21 Yeah, we do have a couple.
Mikołaj Świątek 00:44:22 OBI RFC, which is another complicated topic. I just wanted… I don't need to… we don't need to discuss We have coverage for unit tests, an incredible advance in the year of our Lord, 2026.
You can click, you will see that the coverage is, like, 65%. That's pretty low, but the places where it's low, it's, like, the… are pretty trivial places where an LLM might easily add a bunch of stupid unit tests to make it happy.
Notably, Jacob, OpamBridge doesn't have great test coverage, did you know?
jea 00:44:58 It has some pretty good black box test coverage, but that makes sense.
Mikołaj Świątek 00:45:03 It is the case that we don't count the coverage from end-to-end tests… yet.
jea 00:45:08 Yo.
Mikołaj Świątek 00:45:09 Just the unit tests.
Sorry, Ozzy, you have the floor.
Ozzy 00:45:21 I'm muted, sorry.
Those meetings do get recorded, and there is a link to them. I've watched them on occasion, so they are out there.
Yeah, I, let's see… share my screen, I suppose.
It's sometimes the easiest thing to do.
I mainly… I updated this based on the feedback, or at least how I interpreted the feedback, kind of the… what people wanted and didn't want.
to, basically, to focus on adding it as a receiver.
The good news, actually, is that the problem with that last time, when, when it was… I brought it up in the SIG, was that, There was no, That it wasn't in the collector contrip distribution, so users, you know, you could… the operator could, like, support it, and… But they'd have to build their own image, which would be annoying. But the good news is this PR seems to have merged today, and now that this OB receiver has been It's now in the, collector contrib image.
this marched today, and presumably, I think, when they have these nightly bills that run, I can test it. I was trying to build it myself, but it was making Zoom act weird, and my laptop was getting hot, so I'll do that after the meeting, maybe. But this means that, yeah, they should… that if we add it to the operator, they should be able to, as I understand it, at least, you just use the contrip image.
And then the idea would be to not do what I had first proposed, not adding a new CRT.
On a new controller, because, Yeah, that's a little complex and not necessary, and there seems to be some opposition to that, which I also understand that. It was just… it was just one, possibility, but it's… it's more stuff to maintain and stuff.
Yeah, and that they can use it as a receiver, like this.
Do you know, where they can stay with what namespace, you know, how they want to discover the different things. And then the nice thing is.
When it's, in a collector, then they can do the same thing for, you know, rooting for how they want to actually, let's say, only Each tenant gets their… their traces and things like that.
Now… there's… yeah, basically, I mean, I also decided all the operator is going to do, as such is, similar to what we already do for other receivers, where sometimes it might… Create a service and things like that, it will configure the… the Orbach, or rather, actually, sorry, the volume mounts, mainly.
And… and set the host pit to true, and I decided also, and the same with this, mount some things like the cgroups it needs access to, the read-only file system. Now, in the proposal previously, I had this thing about that the operator would try and, You know, if they set privilege false, then it would try and work out what Linux capabilities they needed, the user needed, based on what they had configured Obi with. I would not do that for now, that's at least what I changed it to. I think that's a little complicated, and it could be added later, if it was a nice thing.
If it was something people want, but what, basically.
how I've done it now is that it runs as… it'll run as privilegeTrue by default, which is also what the, the Helm chart for Obi does, too, and that's kind of… Maybe not the… the most… security-type option, but it's… it works everywhere, it's very compatible. And then if somebody wants to not do that.
then they can just add the security context to the collector like that, and they… they figure it out themselves, which I think is probably better than we don't have to maintain that or be responsible for setting that. If you're, you know, a user that's decided that this is what you want to do, then presumably, in my mind, you have some awareness of Of which ones are needed, and it is documented for OB as well, and for which particular features require particular capabilities. Yeah, and I'll stop talking, and my main thing was that, I don't know, did anybody have any feedback, or… ideas or, things about we shouldn't do this or should. I did also join the OB SIC meeting, two weeks ago. Unfortunately, their meeting is quite long and has a lot more attendees, and, so I didn't… I only got really to ask a question or two in the last 5 minutes. I didn't really get much information or get feedback, but they did say, that to come back, next time. Maybe they could give us more time. They just had quite a busy meeting, so I could… I could also If anybody here has any… questions for them as well, I could, Yeah, I could note them down and go join the meeting or anything next year.
Mikołaj Świątek 00:50:26 Sorry, go ahead.
jea 00:50:31 I think this is, all pretty good. I mean, this looks pretty easy.
All things considered, I think as long as we have the ability to do security restrictions.
As you showed, I think that's what really matters. I don't think that there's any other… Things we would need to change, on our side, no?
Mikołaj Świątek 00:50:50 Do we not want to kind of unify it from an API perspective with the rest of the instrumentation stuff?
What I mean is not necessarily put it in the instrumentation CRD, in a way, because I am happy, I am happy that we can just use an auto collector.
jea 00:51:06 I don't know.
Mikołaj Świątek 00:51:07 What I'm wondering is whether we do actually want to have a separate CRD, whatever we call it, for this.
Which will, as part of its implementation, it will just make an auto collector the right way, the right configuration.
jea 00:51:19 Mmm.
Mikołaj Świątek 00:51:19 So, to have, like, a wrapper with… with a nicer experience, because I don't know if we necessarily want to record… well, maybe for a start this is fine, but I think it would be a nicer user experience if we didn't expose the technical details.
of this.
to users, at the end of the day, in the same way that we, like, don't expose the technical details of a lot of the instrument… auto-instrumentation, right? People don't know how we… how we inject the Python auto-instrumentation, I bet.
Right. Yeah. It just works.
jea 00:51:53 LinkedIn.
Yeah, I like that idea. I'm wondering if, you could look at what Pavel's designed for the instrumentation V2?
Looks like, and see if there's a good way to incorporate it.
in that way, because Obi uses, declarative config, no?
Mikołaj Świątek 00:52:17 Is it crazy.
Ozzy 00:52:17 I don't know, I think they plan to change Actually, this I do know. They plan to change their configuration, and presumably, like, there's a V2 version, which I guess is going to use the declarative config. I've seen that when I was doing research, digging into their repository stuff, so they're planning some structural change to the configuration. So maybe that would be maybe one reason, in my mind, not to do anything yet that maybe ties us to it too much, because I think they're planning to change it a lot. On the instrumentation thing, I think, like, some way that it might, you know, that it could integrate with existing instrumentation, or I would like to.
And some of the other ideas and things I had earlier included that. I just thought maybe that this is, like, the simplest, minimal thing, to just get something in there, and I don't think it would… Yeah, prevent adding something on later where we, yeah, like, Nicolai said, like, kind of hide it a bit, or make it nicer, I suppose.
Mikołaj Świątek 00:53:15 So what you wanna… so what you wanna do as, like, a minimum for this is essentially automate… because anybody right now can just create a collector with this config, right? After… if they put the right image in, right? Where we don't have that image, the thing that just got merged, right? But anybody can just create the collector.
this way.
and the main thing we would do first is to add some handling for this case. I don't know if this will be easy, actually, with the way we currently have things set up, because You would have to look at the configuration, and based on the fact that this receiver is there, go out and set some things in the pod.
itself?
And… We don't have a generic mechanism for this in the codebase right now. We have a way of saying.
this… this receiver exposes parts, so let's open the parts and reflect them in the service, and so on. We have a way of saying this receiver requires some air back, so let's create the air back automatically, for example. We don't have a way of saying this receiver requires you to run as privileged, or with, like, some specific Linux capability, which is not a problem in and of itself, but you'll probably have to write more code than expected to actually implement this.
And I'm wondering if this is actually valuable. I'm kind of wondering if it's, like, just this, just, like, I put the… because the thing, the reason we do it for, like, the case attributes receiver, or… the… or, like, for receivers which open parts, is that this is just reducing tedium for users. Like, this reduces the amount of boilerplate manifests they have to write for their collector to actually work. It's not some transformative feature.
And in this case, it might be better… it might be better to just start by saying, hey, you can do this.
I have a PR up right now, which reorganizes the documentation, and afterwards, it's going to be much easier to just go in… there's going to be a section in there called Reference Architectures.
And that section can just contain a tutorial to start with, to say.
you do want EVPF instrumentation, right? Then you create this, you point it here.
And then you have it, and a guide on how to configure this to get to the end.
So, basically, I'm wondering, like, what level of… what level of implementation do we want to do? Like, and what level is actually valuable? I am a little bit afraid.
Of automatically setting… setting anything for users related to privile… to, like, the privileged attributes on their collector.
Because that is dragons, right? If they said it themselves, they said it themselves, you know, they got it. It's their choice. If we set it automatically, and they don't know, and then suddenly there's a security issue with the whole thing, that is on us that we set it for them.
So that's, like, kind of the thing I am… A little bit wary of, essentially.
Ozzy 00:56:49 Aren't the, I think the documentation thing is a good idea, because even if… we did this thing, and I proposed it would still be good to document it, otherwise people don't know that… that it does… that the operator does this nice thing, so the documentation has to… has to be there either way. And you were right, also, it could just be documentation, It's only that, I suppose, even… and also, yes, what the RFC is now, it's not… it's not… yeah, I don't know about the code change, but it's not, it's not doing much.
But, I mean, even if it's only something small, where it just makes it more convenient and they don't have to figure out, like.
you know, volume mounts and things like that, I think that still may be nice. I'm actually curious about this thing that you mentioned about the, about the privileged true, the operator setting that automatically, because I also thought of that.
And I was wondering what's normal and how that's handled. My thinking was that, at first, I was like, oh, that's very bad, that we can't do that.
But… and maybe somebody, again, who knows more about this or more experience could tell me. But then I thought that maybe… that the security model is that… Well, normally, that there are other restraints in place that stop, some random namespace in your cluster just creating, privileged pods that… if the operator can… if they will start for the operator, then anybody could do it. You know, you use the pod security admissions or… or in OpenShift, there's the security context constraints on that that says, like, this namespace cannot run privileged workloads. Is that… Absolutely.
Mikołaj Świątek 00:58:21 Assuming they have the ability to create pods, which they often do not, but they might have the ability to create OpenTelemetry collectors, but not have the ability to create pods.
That is an issue. If there is, like, a pod security policy defined, it will stop it, but it will stop it in a way that is very obscure.
Because it will not stop you from creating the OpenTeometry Collector CRD.
the CRD will just not reconcile.
Or maybe it will reconcile, actually, because the PSP is configured in such a way that it would stop a user, but it does not stop the operator, which is, relatively speaking, runs with a lot of… with a high level of privilege in the cluster. So this is a complicated topic. It's quite likely that we'll soon have a feature which will restrict this as well.
by which I mean, it will restrict setting a lot of these, like.
pod attributes, which are necessary for OBI to work in a way where you'll have to, like… there will be some additional validation for it. For example, you'll have to configure the set of namespaces you allow this to happen as part of the operator configuration, because it is dangerous. It's dangerous that you can do this, and we don't… documented clearly enough right now, in my opinion, that it's like, if you create… being able to create an OpenTelemetry Collector CR is equivalent to being able to create an arbitrary pod.
Which is, again, it's dangerous if you allow anything at all to happen in there. I think it's fine, for the record. I think it's fine.
If you have a feature in the operator which requires a highly privileged daemon set, for example, to exist, that is fine, this just has to be very clearly documented, and it's easier to control this if it's a separate CRD.
it's like, it's easier to control for this situation, if it's a separate CRD, than if it's just an open telemetric collector, where we, you know, we see the receiver, we set the fields, and then we try to do some elaborate validation authorization step that the user is actually allowed to create this thing, because it's very implicit, and that's kind of scary.
For the air back as well, it should be noted that for the air back, you have to act… the airbag creation is not enabled by the pod. You have to actually enable it before it works.
So… so this is kind of… this is all possible to do, but you have to be quite careful when you just set these kinds of things without… This being explicitly Told to the user.
Like, without them knowing.
Does that make sense?
Ozzy 01:01:12 Yes, yes. What… just to summarize then, what would we like to do, then? Because I… I told maybe… from your perspective, adding it to the collector, CR was maybe… is convenient, but you would… you would see that another CRD would… would have a role, or something, or that around that? I'm just curious, like.
Mikołaj Świątek 01:01:30 kind of like this. I think it would be easier to do with a new CRD.
Ozzy 01:01:34 Yeah.
Mikołaj Świątek 01:01:35 Because, because we could then just say, this CRD is highly, highly sensitive, it creates highly privileged resources.
Yeah, and you can use the…
Ozzy 01:01:47 Oh, fuck, dude.
Mikołaj Świątek 01:01:48 Be careful with it, don't give random people the ability to, to, to…
Ozzy 01:01:52 And that CRD then would need a… would you see it having, like, a new controller and reconciler that creates a demon set, or underneath it creates a collector, or something like that?
Mikołaj Świątek 01:02:03 I would create… I would just have it create a collector version.
jea 01:02:07 I have to drop, unfortunately. But… This is a good discussion. Thank you, Ozzy, for doing this work. Appreciate it.
Ozzy 01:02:14 Thank you.
jea 01:02:16 2.
Pavol Loffay 01:02:19 Yeah, I wanted to mention that the… even if we go with a new CRD, I think we would face very similar problems. Like, there will be people that Would like to have the full control over the security and specify everything.
And then… the question will be… we would… what… what are we doing by default? Do we create something unsecure by default, with elevated privileges?
So I don't think we escaped this problem with the new CRD.
I would probably much rather… support of the… In the operator with the smallest minimal change that we can do right now.
Learn how people actually use it.
And then… Kind of think about how we can simplify the config.
And what's… And automates the use… or simplify those use cases that people… use the OB4.
Mikołaj Świątek 01:03:29 The smallest possible change in the operator to use it is nothing.
Pavol Loffay 01:03:35 Exactly.
Mikołaj Świątek 01:03:36 Create the collector by yourself.
Pavol Loffay 01:03:40 Exactly, and maybe the volumes, or… like, there's a couple of things that Aussie listed on this RFC that the operator can do on the behalf of the user. Maybe… We start with that, without touching anything related to security, and then…
Mikołaj Świątek 01:03:58 volume.
Pavol Loffay 01:03:58 are…
Mikołaj Świątek 01:03:59 Related to security, my dear Pavel, if you mount them, if you mount them, that's already… like, being able to mount host path volumes is… Is, like, a vector for various, like, escapes to the node, essentially. And that's kind of what, what I think what OBI requires to do. Sorry for interrupt.
Pavol Loffay 01:04:25 Yeah, I'm not sure what exactly it needs, but I think we can start with something that is not security-related.
And then maybe progressively add it. And maybe we could have, like, a flag in the Optel CR that has to be explicitly enabled to… automatically default Or… default security configs for all B.
Ozzy 01:04:59 I know in the proposal I have, I did say at the end that it would be behind a feature flag, or SC, so it would just be, in the beginning, at least, not enabled by… default… Sorry, Michael, I'm going to repeat a question, but just to make sure I understood it the first time. So what you were thinking would be possibly a good idea was that, like, there would be a new controller, a new CRD, and that that controller, when it reconciles that C or D, creates a collector CO, which is configured, and then that gets reconciled by the… I'm just… just double checking.
is a pattern.
Mikołaj Świątek 01:05:31 Yeah, exactly, exactly, yeah. We should reuse our existing infrastructure, and see a new reason to just… if this is just a collector, then let's just create a collector. Maybe it would do some other things as well, for example, it might, Take care of some… data massaging, for example. I don't know how compliant the OBI data is with some semantic conventions, for example, at the moment. It doesn't have all the metadata that you would expect.
from something collected from Kubernetes? I don't know. If it doesn't, then we might, you know, might add a processor in there to make it nicer until the upstream project figures it out. But, you know, these kinds of… these kinds of things I would, consider.
Ozzy 01:06:25 Okay, you know, I get… I think that's an interesting idea, and then that the base, kind of, the existing collector, reconciler doesn't have anything touching to do with escalating privileges or anything like that, it's all in the… in the… in the room for the, the new CR… CRD, okay.
Mikołaj Świątek 01:06:49 I would start with documentation.
Document end-to-end what you need to create. And we can merge that, kind of, in parallel.
with, with the, with, with the RFC, and, just see how it looks.
Okay, yeah. I wouldn't even… I wouldn't even mind, I wouldn't even mind just writing a test.
Just, just, you know, put up a pull request with a test which uses OBI, and just asserts that it shipped some data.
Example. Because that's, like, easy… should be relatively easy to do in our, like, normal end-to-end test setup on Kind.
There's no problem with privilege escalation over there.
So, do that, and show that it, you know, it works, it does something.
And the subsequent changes… subsequent changes can be like, okay, we've done this, we've documented that you can do this, you know, how do we want to make it nicer?
Does that make sense.
Ozzy 01:07:53 Okay, yes, yes, so I'll request to add some documentation on how to use it as of today.
and also to, to actually test that with the operator, that this given COR with these privileges and using this image, which should be available very soon, actually, actually works, yes?
I think that's a good suggestion, thank you.
Mikołaj Świątek 01:08:22 Cool. I will, review my documentation, PR, someday.
Pavol Loffay 01:08:28 Oh, dude.
I think you changed it from the draft scene.
Too ready, right?
Mikołaj Świątek 01:08:34 Yeah, but it doesn't actually, like… It just rearranges stuff.
If you find something in there that looks awkward and that you would like to fix immediately, I'll fix it immediately, but the idea of it is to just, like… Introduce the new structure, and then we can, like, fix things.
Independently, after that structure is in place.
Pavol Loffay 01:08:58 Yeah, I'll do. And thank you for prompt reviews on the book.
Mikołaj Świątek 01:09:05 Yeah, sometimes it's a pain that the OpenShift tests don't actually run as part of the operator CI.
Pavol Loffay 01:09:16 Yeah, I absolutely agree, and I would like… to… if possible, move some of those tests to the main codebase. I mean, some of them are really OpenShift-specific, but some of the parts of those tests could be… could be done in the… In the main test suite.
Mikołaj Świątek 01:09:44 it works for me, I don't mind. I also wouldn't mind actually just running them on OpenShift if there is a way to do it, but I'm not aware of a way to do that.
Easily.
Pavol Loffay 01:09:59 Yeah, there's no way, there's no easy way how to do it. OpenShift, it's like… It requires so much resources, there is no way how to run them.
on GitHub CI.
Anyways, I have to drop as well. Who's been talking to?
Mikołaj Świątek 01:10:19 It was good talking. See ya.
Pavol Loffay 01:10:21 Thank you.
Ozzy 01:10:21 Bye.
Harrison Fritz 01:20:17 Confirm my reservation.
F, R, I, T, Z.
No.
F, R, I, T, Z.
Do I have guaranteed availability?
Can I speak to a representative?
I want to confirm… That there is a car available.
Yes.
Yeah.
If I'm staying until Tuesday, I might as well just stay until Thursday, and then I can go… I can go back, like.
Friday morning or something.
Yeah, I… yeah. Where… how far away is the place where we'd be staying from the McLean office?
bought, can you give me, like, the neighborhood or address so I can plug it into the maps?
Okay.
Looks like it's about, like, a 40-minute drive.
Or I could just take the metro in.
I mean, could you drop me at the metro station, like, in the morning?
Yeah.
Yeah, yeah, it is.
Alright.
Yeah, that'll be… that'll be easy.
So, when was I originally gonna come down? On the 8th?
Okay.
Well, why don't I come down… do you want me to come down on the 8th or 9th?
And then I… I would go back… When would I go back?
And your Moe's is on… on Thursday.
I mean… Do you think you'll be okay? Like, do you think you'll need, like, multiple days of care after, like, most surgery?
Oh.
You'll just be tired, and then… And, like, the next day, you'll… you'll… so what if I were to come down on, like, the… the 9th, and then I can just stay through… And go back on, like, the 17th?
So the fri- on Friday?
Yeah, tickets aren't that expensive.
Yeah, I'm looking.
I could take, like, a 3 o'clock and get in by 6 o'clock.
Coming down.
And then… Oh, yeah… Then… I could leave at… Like, 1?
On the… on the 17th?
When do you think your, like, your surgery's gonna be?
Oh, gotcha. Okay.
And… And I think for that, I'll probably… I'll plan to be down there for at least a week.
Is that, like, does that sound about right?
Hmm. I wonder what… does the recovery really… I have no idea if the recovery's, like, that bad.
let me see, I'm reading about both.
Equally.
Lumpectomy is, like, I think pretty easy.
It says… People are saying, like, their recovery isn't that bad.
But… No, for… I'm reading about for, like, even for, Like, mastectomies, the recovery, like, let's see… People just say, like, it's hard to… like, you… you can't, like, lift stuff, but they… Let's see… No, it's okay.
Well, let's see what the… let's see what, like, the treatment is, and then I can… I can decide. Because if, like, let's… what if they… do you think they could schedule it for, like, July 20th, and then I, like, I could just be like, well.
Okay.
Because then I'd just be like, oh, well, why don't I just stay?
Yeah.
Yeah.
Yeah, well, we can wait and find out.
Yeah.
Let me… also see… Let me talk to Jeff on Monday before I book.
And see, maybe I can get Capital One to, like, for me to go down there.
I'm pretty sure I can.
If I wanted to.
Oh yeah, I'll send her.
Alright, I just asked my boss if… I can travel down to McLean.
No, I just said I wanted to get time with, like, the McLean folks.
And then… I could… I could get a… I could get a hotel if I wanted to.
But Awesome.
Like, there's, like… Yeah.
Cool. Well, let me, I'll let you know what my boss says, and I'll book it, but I think… Plan on that, and I'll put it in the calendar.
I think so. I would buy… I might buy, like, a flexible train ticket, just in case I need to, like, change it.
Yeah.
Cool, cool. Well, thank you.
Good. Oh, I have an interview with, Like, the recruiter got back to me from that, like, company, Temporal, so I have an interview with them lined up.
I have to skip.
Yeah.
They're all gonna be virtual.
Because it's a… it's a remote company, yeah, yeah.
Yeah.
I think, like, 3 or 4?
No feedback, like, it was just a screen. Like, he gave me some, like, like, what the interview process would look like.
Oh, yeah.
Yeah.
Great.
Mail.
I'm gonna let you go, because I'm gonna wrap up my workday and go explore the city.
Yeah, it's nice every day.
Yeah, love you too. I'll talk to you later.
