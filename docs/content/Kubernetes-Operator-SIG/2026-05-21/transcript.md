SIG: Kubernetes Operator SIG
Date: 2026-05-21
Duration: 66 minutes
============================================================

## Zoom Recording Transcript

jea 00:00:23 Yup.
I'm eating lunch right now, so I'm just gonna be off-camera for a minute.
Mikołaj Świątek 00:00:32 Oh, cool.
jea 00:00:42 Is, is your PR ready for review?
Mikołaj Świątek 00:00:46 Yeah.
jea 00:00:47 I'm gonna do that.
Mikołaj Świątek 00:00:52 I even put you in there specifically.
It's kind of a trivial change in some respects.
jea 00:01:03 Yeah, I mean, my only worry is, like.
It does break… it could break user expectation.
Mikołaj Świątek 00:01:16 Could it? I mean, if… honestly, I think the report is right. If this breaks user expectations, then they had the wrong expectations.
I'm sorry, but… Like, you shouldn't be able to do this.
jea 00:01:32 Yeah.
I think it's fair, I mean.
I guess the way that it could be solved is by the… The actual cluster operator giving the permissions to the user to create these things.
Mikołaj Świątek 00:01:47 they effectively have the permissions, like, that is the point. Like, they can run any program.
With this, like, because the collector is gonna create a service account linked with Cluster role and so on with them, they can attach that to whatever else they want.
Right?
jea 00:02:07 Yeah.
Mikołaj Świątek 00:02:08 And run a collector with a custom image, which does whatever they want.
jea 00:02:14 young.
Mikołaj Świątek 00:02:15 So, it really doesn't make that much of a difference.
jea 00:02:19 Yeah.
Mikołaj Świątek 00:02:25 So I think this is valid. Maybe somebody will come up and ask that we allow, like, an operator config option to disable this.
At which point, sure.
We're gonna call it insecure something something something.
But until somebody comes in and wants that, I don't think we should, like… proactively, proactively allow it. Like, people have come and asked that they can run the… that they can handle the target allocator, like, monitor secrets in an insecure way, and they're saying, just let us do that, we have… we're using a service mesh, we'll be okay.
And I'm like, okay.
the option is going to be named Allow insecure something something something. You know, and disable by default, and you can… you can do whatever you want with, you know, take responsibility for your own page.
jea 00:03:30 you know, I just approved it. Looks good. I mean, it's pretty easy, pretty straightforward, I should say.
Mikołaj Świątek 00:03:35 Yeah, it's like, it's a bunch of code, but it does vary, kind of.
trivial. I wouldn't say trivial, but it does very, very straightforward things.
It's basically, like… Okay, we're creating a collector, so let's see what airbag rules the components actually need. Let's check what airback rules the service account has, if there is one, and then let's… let's take the ones which the service account doesn't have, and check if the user has them. If the user doesn't have them, then say no.
I considered also doing a filtering approach, where we don't reject it, and we just scope it down.
But that's.
jea 00:04:23 Yup.
Mikołaj Świątek 00:04:23 That's challenging because there's actually not really a good way to communicate between the admission webhook and the, and the reconciliation loop.
And for this check, you need to know who the user is, but you don't know who the user is at the time that you reconcile this. And you can't rely on anything in the… collector CR itself, because the user can change it.
Pavol Loffay 00:04:57 Hey, guys.
Mikołaj Świątek 00:04:58 Yeah, that's it.
Well, you could help us out with the security issues as well.
Pavol Loffay 00:05:11 Yes!
Mikołaj Świątek 00:05:13 Come in! Just for you, I'm adding you as a reviewer to my pull request, just so you know that we're doing this, just, like, more explicitly. I put it also in the notes. You don't have to review it right now, but I want you to know that this is happening.
It is, like, a restriction on what the… On what the automatic airbag feature can do.
Like, it basically doesn't… it, like, rejects collectors if the automatic error back that would be added is something that the user that is submitting it isn't allowed to do.
Because otherwise, it's a privilege escalation.
Pavol Loffay 00:05:58 D, are you talking about… the automatic airbag features, like, when the operator has.
Mikołaj Świątek 00:06:04 Yes.
Yes, that's…
Pavol Loffay 00:06:06 back to configure something?
Mikołaj Świątek 00:06:09 It will allow Airbag to create cluster rows and cluster role bindings.
Pavol Loffay 00:06:17 So it will reject the collector CR in this case.
Mikołaj Świątek 00:06:20 If the user doesn't have the permissions that the operator would automatically grant to the collector.
Pavol Loffay 00:06:30 I see.
Mikołaj Świątek 00:06:32 Because that's a privilege escalation.
Pavol Loffay 00:06:34 Shall we say it's a braking change?
Mikołaj Świątek 00:06:37 I titled it a bug fix.
I consider it a bug fix, like, I don't really think anybody expects this behavior to work this way.
I don't think there's a lot of users of this behavior, even.
If you wanna… if you wanna insist that it should be a braking change, then I might consider it.
Pavol Loffay 00:07:04 I think, in general, we did a great job in hotel to signalize braking changes, and I think this can break, some users, so I would be maybe more precautious, and… said it's a breaking. But I need to review it in a bit more details as well.
Mikołaj Świątek 00:07:22 It only… it only affects the admission webhook, so existing stuff doesn't break.
Pavol Loffay 00:07:30 I mean, there could be CICD kind of creating something in the cluster.
Mikołaj Świątek 00:07:34 That's true.
I… I can easily see an argument that it should be breaking.
And, like, if you review it and tell me that it should be, then… then I will change it.
jea 00:07:53 I think it's probably technically breaking, even if it's, like, most users don't use this feature, I think it's worth calling out.
Mikołaj Świątek 00:08:04 That… I'm okay with that.
Honestly, I didn't think that much about this when submitting it yesterday, so… Alright, I think we can actually get started. I think this is… everyone is gonna be here. Hey, Antoine?
atoulme 00:08:23 Hey, good morning.
Good evening.
Mikołaj Świątek 00:08:26 Good morning to you two. I'm actually gonna share my screen, because Zoom… I was gonna say Zoom fixed this, but then it's… Doesn't want to work so much.
atoulme 00:08:38 Pull up the…
Mikołaj Świątek 00:08:42 Is it?
atoulme 00:08:42 See your screen yet.
Mikołaj Świątek 00:08:44 Right, because Zoom… Zoom fixed screen sharing on Linux, so… Yeah, after so many years.
atoulme 00:08:54 Awesome.
Mikołaj Świątek 00:08:55 Right. So… I got a bunch of stuff here. If you have some more stuff that you haven't put in there, feel free to.
My first one is, like, relatively straightforward.
It's about moving to Renovate. We've recently, if you haven't noticed, we've moved for Go dependencies to renovate. This is really live, it's happening.
And there's a bunch of other stuff that, that we still have in the PandaBot, but I think we can relatively easily still move to Renovate. The reason to move… to use Renovate is that it's more featureful. A bunch of other hotel projects use it. I'm pretty sure.
Collector, Core, and contribute use it exclusively.
And, it has much better support for… multi-module Go, like, monorepos in particular, which isn't relevant to us immediately at this moment, but will be very soon. Like, the stuff that we have here is, like, GitHub Actions and some Docker stuff, which is kind of trivial.
So, I think we can move relatively easily.
Is anyone against us?
atoulme 00:10:09 No, I would say, for Contrib, to your point, Renovate is used by CollectorContrib. Dependable is sometimes used specifically to patch vulnerability. For some reason, this is the way GitHub's going to go about this.
So… It doesn't matter in the grand scheme of things.
But, yeah, it depends… Renovate has a much better… Of the print, looks like.
It's much nicer.
Mikołaj Świątek 00:10:33 Yep.
atoulme 00:10:35 You can group, you can group dependencies, did you mention that? You can also make it so it's not opening a PR per change, but group all of them into one big bundle, so you have less, to review.
Mikołaj Świątek 00:10:51 Yeah, the PandaBot can also do that, but it's less nice about this.
And you can't group things… you can't group things from different modules, in particular. And I wanted to point to… just point everyone here to this pull request, which I'd like more people to approve before we merge it, because it's like… a new module, it just moves API.
to a new module, which we kind of agreed that we want to do in the past, but I don't want to merge this without more agreement about what's in there. This is just, like, an aside.
This is one of the reasons I want to use… I wanted to use Renovate for these, is that we're gonna have a module in there, and I would like to not have I would like the dependencies to be kept in sync, basically.
I'm doing the right desktop.
So that's it.
Pavol Loffay 00:11:52 Does it mean that, if you want to make an API change and… Can you use it directly, like… In the controller, we would need to split the PR into two.
Mikołaj Świątek 00:12:06 I don't know why. It's like, there's a replace in there.
Pavol Loffay 00:12:11 Add, use replace, okay.
Mikołaj Świątek 00:12:15 It is the same idea that, like, all the collector and Contrip also use, they all have internal replaces for all the modules.
And the API module is pretty simple, so it doesn't, like, involve a lot of stuff. The only potential pain point of it is that it's another module, and there's, like, some software that's not great at modules. You might have to use, like, a Go workspace.
Pile, if some stuff breaks for you.
But… Such is life.
I already mentioned this, so Pavel, I asked you to review it, and I put you in here.
This has to go in before the release, the third thing is… We already talked about this once, I think 2 or 3 meetings ago, and now I'm bringing it back. I also put a Slack message. I'd like to enable reviewer assignments, so basically what I want to do is… go to the approvers group. Right now, our review is automatically just code owners, and code owners is just, operator approvers group.
jea 00:13:31 Owners.
Mikołaj Świątek 00:13:32 go in there and make so that GitHub does the whatever round-robin strategy it does, so it always assigns to people from the group.
by name.
And the question is, do we still want to do it?
And what to do about actually merging, because to merge, you need, like, a maintainer.
To, to actually press the button.
I think the way Contrib and CAR do it is that they have some label, which then, after the label is in, this, like, maintainer gets pinged or something. Antoine, I think you would know more about that.
atoulme 00:14:13 Jay.
Mikołaj Świątek 00:14:16 Like, there's some machinery that does this. And I basically just want to make sure that when something is approved and ready, that it gets merged promptly.
atoulme 00:14:27 Okay, we need to merge these, Social thing, where we know to just… Know to review things, yeah.
Mikołaj Świątek 00:14:37 And does that… does Contrib do it in a way where it has both the approvers and the maintainers group as co-donors? So you get, like, one person from… from maintainers and two people from co-donors or something?
Is that how it works?
atoulme 00:14:54 I believe that, we have a pretty detailed code owners file that has, for all of them, starts with the approvers of contrib, then each of the code owners are, One by one, added.
When a PR is open, then all of those folks are being, asked.
So.
Mikołaj Świątek 00:15:13 Does it ask maintainers separately? Because we're in a situation where the approvers group is… the maintainers group is a subgroup of the approvers group, which I don't think is the case in Contrib.
atoulme 00:15:26 Should be.
jea 00:15:27 That's the… that's the default setup for most repos, is for the maintainers to be a subgroup of the approvers.
Mikołaj Świątek 00:15:35 So it does only approvers, and then a bunch of people mentioned by name.
Who are the co-donors?
atoulme 00:15:44 Yeah, supposedly that helps. There's a lot of, if you go to GitHub Action, there's a lot of stuff that's like, oh, manipulate things, assign to people. There's a rotation that's supposed to be happening where any PR opening is going to be assigned to… A rotating cast of approvers.
The reality of it is that the signing field is not working well.
Mikołaj Świątek 00:16:05 Hmm.
atoulme 00:16:06 It's… it's a problem. We don't know. We don't know what to do with this, we need to do better than that.
Just about the same.
Mikołaj Świątek 00:16:14 I don't know, like, I am personally okay just… Where is this thing? For now, I'm personally okay doing the following. You can see, still see my screen. Teams is, like, here, I go here, I do… operator approvers… There it is… For some reason, I don't know where the edit button is on this screen.
I guess I have to click Settings, right?
And here on settings, I get to do code review, right?
Enable auto-assignment, right?
I want to have two?
algorithm…
atoulme 00:17:01 Okay, yeah, sounds great. Let me check out my… Didn't.
Mikołaj Świątek 00:17:08 Around robin or load balance? I don't actually know what the difference is.
What, like, a round robin should load balance by default, doesn't it? What's the difference?
jea 00:17:25 Given, GitHub's traffic problems recently, I don't know if I trust their load balancing.
Mikołaj Świątek 00:17:33 Okay, so, I know, but, like, maybe they can handle that balance.
like, 10 people, like, that is not such a big number. I just don't know.
jea 00:17:41 I just thought.
Mikołaj Świątek 00:17:42 differences.
jea 00:17:43 I thought it was a good story joke.
Again.
Mikołaj Świątek 00:17:46 I guess maybe load bal… the way load balance works is that it's… if you go and review stuff that you're not assigned to, then it counts more of your reviews, or something like that.
atoulme 00:17:56 Might be.
Pavol Loffay 00:17:57 It will allocate more PRs to the ones that review more.
Mikołaj Świątek 00:18:01 Wow, Pavel, wow, that is… that doesn't sound like a good principle for distributed system design.
Alright, I'm putting it around ramen for now, or it doesn't even disagree.
atoulme 00:18:13 That's where it's set for the collector control trip.
Mikołaj Świątek 00:18:16 Alright.
atoulme 00:18:17 You get everything… Oh, there's one thing. At the top, there is only notify requested team members. You can… that is checked for contrib. I'm not sure why.
Mikołaj Świątek 00:18:28 Well, the difference is that… I think this is fine to not check. Like, we have enough PRs. We don't have that many PRs. If you can just click, see that you're not assigned, and if you don't care, then just unsubscribe yourself and be done with it. I think this is fine.
Okay, cool. There you go.
Everyone in favor? Nobody against?
jea 00:18:53 Nope, that sounds good.
Mikołaj Świątek 00:18:55 I'm clicking Save Changes, let's see if it lets me. Success, cool.
Alright.
Alright, that's everything I had. Pablo, you're next.
Pavol Loffay 00:19:12 Oh, right.
Mikołaj Świątek 00:19:15 You want the screen?
Pavol Loffay 00:19:16 E. coli.
You… you can keep the screen, and then maybe you can open the portal. Maybe one item before we discuss the instrumentation, which is related to instrumentation, I was looking at the Apache and… the NGINX instrumentations, they are hosted in C++ Contrib.
And I submitted one PR, and I was… I was not getting reviews, and then I asked on the Slack, and they say that those instrumentation libraries are not well maintained.
And they might even consider deprecating them and removing them.
I would like to ideally find someone who could help there? But if there is no one maintaining that, I'm kind of concerned about, kind of, exposing this on the operator as well.
Mikołaj Świątek 00:20:17 We are definitely not keeping up with updating them.
That is, like, absolutely correct.
And I would personally consider… like, if you told me right now that you would like to disable these by default, I would agree with that.
Pavol Loffay 00:20:36 Yeah, I think it's something we should consider, maybe have it as a feature flag to disable it.
Mikołaj Świątek 00:20:47 I mean, I would do the same thing that we have for the Go instrumentation right now, just to just disable by default.
Pavol Loffay 00:20:54 Yep.
Mikołaj Świątek 00:20:54 And… and then we can see.
Were there any…
Pavol Loffay 00:20:58 Okay.
Mikołaj Świątek 00:20:59 just…
Pavol Loffay 00:20:59 Yeah, sounds good. I'll open an issue, maybe it will alert some people.
And then we can take it from there. Alright, and then my main topic is the instrumentation V1 Beta 1. There is the RFC.
Mikołaj Świątek 00:21:22 What do you wanna, what do you wanna…
Pavol Loffay 00:21:23 Yes, I can highlight the objectives first.
So, the main objective is to expose the declarative config.
as a… typed, field in the CR. We will keep as well the existing config.
for the… that uses the environment variables. We would just scope this… under the envConfig field in the CR, so it's clear whether a user is using the declarative on the other environment variables.
And then… I want to do some cleanup, remove some deprecated fields.
And consolidate the resource attributes configuration.
jea 00:22:16 I think this all sounds good to me. I mean, I did an initial read-through, and I didn't find anything, that was controversial to me.
Are we not doing the… the thing that I was unsure of was the label selectors, which I thought we were gonna do.
with, the V1 Beta 1, given this is a break and change anyway.
Mikołaj Świątek 00:22:38 So just for the record, when you're talking about label selectors, that, like, this links to these?
issues, which are… I don't think that's what you're talking about when you say label selectors, Jacob.
Because this is, like, a feature to be able to define inside the instrumentation object which pods.
It should, apply to, not by using.
So this is, like, a different feature that is, like, not a breaking change, but I think what you're talking about is the changing the annotation into a label, right?
jea 00:23:21 Yes, that's the change that I care about.
Mikołaj Świątek 00:23:25 Yeah, so we don't have it here. I think we should, and I think I even… Yeah, I…
Pavol Loffay 00:23:32 I didn't think a lot about it, but I'm not sure… If… I think we can do the API change.
And then do Label Selector later.
Like, they don't have to come at the same time.
jea 00:23:50 I think these should come at the same time, because this is going to be a breaking change no matter what. Because we're not going to provide backwards compatibility for the previous version, people are going to have to migrate anyway. I think we talked about… How the conversion webhook was, like, very frustrating to work with.
Pavol Loffay 00:24:10 So let's discuss first the migration path.
Nikolai, as well, if you open my, PR description.
But there is a link to GIST.
I was looking at the… how multiple CRD versions are maintained.
So they are… I can do a quick overview. They are defined in the CRD. There is two config fields for it. There is… which version is served, and which version is stored in the ad CD. Only one version can be stored in the EdCD, and served can be multiple versions.
And then there is, a way to define the conversion of that book.
jea 00:25:04 If you…
Pavol Loffay 00:25:05 Scroll down a little bit.
so the conversion strategy is either none or webhook. If the conversion strategy is none, you can still store in EdCD one version and get the other.
It just… if the… CRD specs are not compatible, you will get, kind of, null for those fields.
And if you have the webhook, you control the conversion, so you can convert from incompatible fields.
Some operators, they… Chose the strategy to use the none.
And the way they did it is… in V1 Alpha 1, they… made a… Changes.
for the next version, so in our case, we would introduce the declarative config and the end config fields. We would deprecate what we want to deprecate.
And then we will define V1beta1 with only defining the new fields.
Leaving out all the deprecated fields.
Mikołaj Świątek 00:26:25 Okay.
Pavol Loffay 00:26:27 That's one strategy. I think I listed somewhere which operator.
jea 00:26:30 tools.
Pavol Loffay 00:26:31 the data approach. I think Prometheus, the scrape configs, They decided to use this strategy.
Or we can have the conversion webhook.
I was looking at the issues.
of the conversion webhook. The main issue is… Helm chart, because Helm chart allows users to install the operator in arbitrary namespace.
And the conversion webhook is defined in the CRD, and defines the service which converts the CRD versions, right?
so, what we had to do for the collector CRDs is to template them.
In the, in the, in the Helm chart depot.
However…
Mikołaj Świątek 00:27:24 It was very painful. It was very painful. One of the results of doing it that way, one of the downsides of shipping the CRD as a template, as opposed to a CRD, is that you… Helm treats CRDs in a special way, like, it submits them before anything else, and it, like, applies them. If your chart ships CRDs, you are also allowed to actually ship custom resources on that definition in your Helm chart, and Helm will do that correctly.
But if you try to do it… try to do… use… ship CRDs just as a templated resource, you don't get any of that. So it's impossible to ship both the CRD and the objects.
At the same time.
And that's, like, a distinction that has caused a lot of headache.
In the how chart.
I just want to make clear what this stuff actually means.
In practice.
Pavol Loffay 00:28:29 Could you please repeat? Do you mean, like, the Helm chart treats CRD in a special way, so that you can… Ship them directly with the objects, and they will… it will install them… First, or something like that?
Mikołaj Świątek 00:28:43 Yes, what… so Helm… Helm doesn't just apply stuff, it also validates things, so it has, like, its own schema registry.
So, when you tell it to apply, apply manifest, it will check whether these actually exist in the cluster, and whether they're correct, and so on. So, and when… if you ship CRDs inside a Helm chart, as inside the CRDs directory.
Helm will read those, it will add them to its own schema.
it will apply them to the cluster, and then it will do all these other bits. So, for example, if you have the auto operator helm chart, and the auto operator helm chart CRDs as CRDs, which it doesn't right now.
then the Helm chart can also include just OpenTelemetry Collector or Instrumentation CRs.
And it will… that will work correctly.
if you ship the CRDs as plain templates, as just resources, it will not work, because the validation step will not know what What resource that is.
Does that make sense?
Pavol Loffay 00:29:58 It does make sense. I was not aware that the Helm charts Kind of allows installing the operator in arbitrary namespace.
Mikołaj Świątek 00:30:14 No, no.
Pavol Loffay 00:30:14 I'm not sure why actually users do it.
Because the, the… the operator should be a single atom in the cluster and should watch all the namespaces, and I think this will be, as well, the hard requirement in OLMv1.
So that there won't be… A way how to actually kind of install multiple operators.
This is possible, technically, with OLMv1, to have the operator watch specific namespaces, but this is going away in the next version.
Mikołaj Świątek 00:30:58 It's, like, whether… so… like, these are kind of different constraints in my mind, whether you can install more than one, and whether you can change the namespace. Like, being able to install software in the namespace that you want is, like, very normal.
In the Kubernetes world, in general. So, I don't know if we can get away from doing that.
And it's… yeah, it's something of a problem.
If you wanna ship… CRDs with a conversion webhook.
This is kind of what it is. You can also do something like… Tell users, if you wanna… if you wanna use the conversion webhook.
here's how you can patch your CRD out of band.
To make it work.
But that's obviously painful.
So, this is… these are all reasons why I kind of don't want to rely on conversion webhooks, is because this deployment storage is just very… tedious. There's a lot of… Kind of sharp edges, no matter what you do.
Pavol Loffay 00:32:13 Yes, so let's explore what we want to do.
Mikołaj Świątek 00:32:19 like, maintaining conversion logic is not, like, any kind of change. Like, we have to have conversion logic anyway, in my view, no matter what we do.
the IT Act, yeah?
Pavol Loffay 00:32:36 So… So you want to go with the conversion strategy none?
Mikołaj Świątek 00:32:45 Ideally, I would. I hoped that you might be able to serve both versions at the same time, but apparently I'm wrong about that.
Pavol Loffay 00:32:54 You are wrong about it, yes.
Mikołaj Świątek 00:32:56 That sucks.
Pavol Loffay 00:32:58 So, we would have… a storage version is always… just one version, and served… Yeah, it's 2, but then our controller will receive only the storage version.
Right? So what happens if a user has installed V1 Alpha 1, Installs new operator.
where, when we add the V1 Beta 1, our controller will receive only the V1 Beta 1, And without a conversion webhook.
we will not see the fields that are defined in V1 Alpha 1 and not defined in V1 Beta 1.
Mikołaj Świątek 00:33:42 Wait, wait, so…
Pavol Loffay 00:33:48 So, let's take an example.
Mikołaj Świątek 00:33:50 of the…
Pavol Loffay 00:33:51 exporter endpoint, like spec.exporter.endpoint, in v1, alpha 1. In beta 1, we want to have spec.enfconfig.exporter.endpoint.
This field will be empty once user installs the new version of the operator.
We won't be able to access it in the controller.
Unless, I think, they run some, like, they do conversion themselves.
like, some CLI to read objects from the cluster.
Mikołaj Świątek 00:34:43 So, so maybe… I, I don't, I don't know about strategy 2.
Yet?
Pavol Loffay 00:34:50 Yeah, I think I mentioned it's over here. If you maybe scroll up, there is this strategy, identical schemas, yeah. See, you have it written, when strategy is none, no separate controllers are needed per version.
So that kind of outlines how it works.
Mikołaj Świątek 00:35:10 Okay, so you basically give it to the… so you have one version that is stored, which, for example, is… the new version… what is it? Is the old version or the new version in this… in this sense?
Pavol Loffay 00:35:24 I think you would want to have the new version stored.
like, it doesn't matter, it has to be one version, I think you want to have the new version.
Mikołaj Świątek 00:35:36 I mean, but… but if the strategy is to add the new fields to the older version, and then deprecate the old fields in the older version, and then in the new fields drop the deprecated ones, right?
Then you have to store the older version, because you need all the fields.
Pavol Loffay 00:35:55 The older version will be stored In the old installations.
If you've… and when you flip the switch to store the new version, once that Object is being read.
then I think at CD will be able to read it, because it has this implicit Conversion that the known fields will be converted automatically.
I think that's important. The identical fields are converted implicitly.
Mikołaj Świątek 00:36:34 Okay, but in that case, we have to make sure that in V1, Alpha 1, everything is covered, basically.
Pavol Loffay 00:36:43 Yep.
Mikołaj Świątek 00:36:45 Like, I need to make sure that it's, like, actually converted to the new fields.
the.
Pavol Loffay 00:36:50 Yes. I hope you…
Mikołaj Świątek 00:36:51 are essentially going to be dropped after we share.
Pavol Loffay 00:36:53 Yes, we would introduce all new fields in the V1 Alpha 1, we would deprecate all the fields that we don't want to have.
And then we would define V1 Beta 1, And yeah, that would be the process. And we wouldn't have any conversion backlook.
Puneet Singh 00:37:18 I have a doubt regarding the… exactly the conversion, webhook.
So, when V1 Alpha 1 exists and you have stored versions in V1 Alpha 1, the moment you create this V1, Beta 1 and the conversion webhook, and you mark the stored version false for V1 Alpha 1, what happens to the stored versions of the V1-alpha 1 type at that point?
Pavol Loffay 00:37:52 your users is still able to get them with kubectl get.
And I think if you make a change.
it will be stored as a B1 Beta 1.
So they are still accessible.
They're still accessible, you can access them via kubectl Git.
instrumentation V1-alpha 1, or V1 beta-1.
the API server will call the conversion webhook if they are stored in the old version.
If you make a change to that object, it will get automatically stored in the new API version.
Puneet Singh 00:38:34 So, as long as you don't make the change, it continues to exist in the older format, basically, V1 Alpha 1.
Pavol Loffay 00:38:42 Yep.
And it's fully functional, user doesn't see… It doesn't impact any user in any form.
Puneet Singh 00:38:56 Okay, I have a… I mean, the same question related to another issue, but I'll… I'll resume that later once we are done with this.
Mikołaj Świątek 00:39:09 I… 8 of these options.
jea 00:39:13 Yeah, none are great.
Mikołaj Świątek 00:39:18 Why aren't you able to serve both? If you could serve both, this would be so much simpler.
Pavol Loffay 00:39:24 They are served both, they are, but there is no controller for both.
Mikołaj Świątek 00:39:30 I mean, what do you mean? Like, you can easily start two programs which each have a watch on different versions?
Easy.
Pavol Loffay 00:39:41 I don't think… I don't think there is a watch per version, I think there is just a watch per type.
Mikołaj Świątek 00:39:49 I swear sometimes I feel like Winnities just did all the worst decisions when it comes to this process. It was just, like, all the natural ways of solving the problem are impossible.
I don't know. I don't… I don't, like, have a feeling. Maybe in that case, conversion webhook is the right way. I would, like, just compile… I would personally kind of… go do some kind of, like, what do the other established operators do? Like, you did this for a cert manager, and apparently…
Pavol Loffay 00:40:23 We should… we should deprecate Helm.
Mikołaj Świątek 00:40:27 I unfortunately don't… I mean, we can just ignore Helm, you know, I'm not… I don't have any function, I don't… I'm not a maintainer in the OpenTelemetry Helm charts repository, you know, I don't care.
jea 00:40:39 Yeah, it would really suck if you were the maintainer of the OpenTelemetry Elm charts.
Mikołaj Świątek 00:40:43 Yeah, exactly right.
jea 00:40:45 I'd hate to be that guy.
Mikołaj Świątek 00:40:47 It could be.
Smartest decision of my life to not agree to be maintainer in that repository, yeah.
More seriously, no, no, we have to… we have to square this. And there has to be some relatively painless way of doing it, right? There just has to be.
Even if it's just, like, some kind of… Automatic upgrade routine that runs.
Right? Because in, in, in principle.
In principle, we could do the strategy where we add all the new fields in the existing one, we deprecate the old fields, and then on startup, we have an upgrade routine that copies all the things to the new fields, and then eventually we, change the storage version to V1 Beta 1, and everything in theory works correct. And that avoids using the conversion webhook, or at least it avoids relying on the conversion webhook.
Like, I can see something like that working, but I would also just kind of… check what everyone else did before making this decision. We didn't do that the last time we were doing this upgrade for the collector, and it was really painful. At least this time, I want to know if we're missing some option that is less painful, or… and maybe… how everyone did… just orchestrated this. Maybe Prometheus operator, Maybe, maybe something else.
Pavol Loffay 00:42:18 Yeah, they have two versions as well with conversion in the Prometheus. The server manager as well uses the conversion webhook. They have as well this, Tool to migrate between versions.
But I would be curious how the third manager does Helm.
I think the main problem is the Helm chart, and it seems weird that there is no good solution for it in the Helm chart.
Mikołaj Świątek 00:42:46 And there's no good solution for it in Helm. So… I think this is not a problem for the search… I think… I would assume the search manager home chart just ships the CRDs as templates, and they don't care, because they don't ship any CRs, they don't ship any of their own stuff, right? And the operator home chart is okay that way, too.
Right? The operator home chart also doesn't ship any of its way. The problem is that if you want to use the operator home chart or the sub manager home chart as a subchart.
and you want to create things like, you know, certificates or open telemetry collectors, then you run into problems. Isn't that right, Jacob?
jea 00:43:30 Yes, it is, as we know all too well, unfortunately.
those… One of the worst, Couple of months we had in the operator helm chart.
Or the, hoopstack Helm chart and the operator helm chart. Very frustrating process.
Mikołaj Świątek 00:43:52 Where's the source? Here. Here, there's the source. It just goes to Cert Manager. Cert Manager Deploy.
Chart Search Manager.
jea 00:44:04 Oh, wait, go, go, 2 up for a second.
Mikołaj Świątek 00:44:07 What do you mean, trap?
jea 00:44:09 Go to, charts?
1up, sorry.
Deploy.
see, they have CRDs.
Separately.
Mikołaj Świątek 00:44:23 And this is a what?
This is just a directory.
jea 00:44:31 No, this is where they, oh, these are for reference. Okay, never mind, sorry.
Mikołaj Świątek 00:44:37 This by itself isn't anything. I was… I'm curious what is here.
jea 00:44:41 Yeah, yes.
Mikołaj Świątek 00:44:42 EA injector. Oh, how nice.
What is this?
Is this… do they have some funny thing where they… just, like, patch the CRDs at runtime, or something?
jea 00:44:58 What do the CRD files look like?
Mikołaj Świątek 00:45:00 ARD files are templates.
So it's the same thing.
jea 00:45:04 So they do the same thing as us.
Mikołaj Świątek 00:45:06 Yes. Yeah. They just don't care about their downstream. Same as… same as BC.
So you see, Pavel, there's no solution. They just do the same thing we do, and the thing we do is fine in the confines of the operator helm chart by its own. It is not fine in the broader ecosystem. They just don't care about the broader ecosystem.
And CubeStack right now, AutoCubeStack, just ships the CRDs and CRDs, right, Jacob?
jea 00:45:44 Yes, I think we do the, CRD as… template approach today. Let me double check.
Mikołaj Świątek 00:45:54 I mean, in KubeStack, it has to be CRD as…
jea 00:45:58 Yeah, we, no, what we do is we install them via a sub-chart, and then after that, they are up to you to manage.
So it's installation only, and then we… we delegate, we just say to the user, up to you now. Best of luck.
Mikołaj Świątek 00:46:12 Right, yeah. So, what would that… if we wanted to do the… oh, does KubeStack use instrumentation?
Does it show instrumentations?
jea 00:46:23 It does.
Mikołaj Świątek 00:46:24 Right, so if we wanted to do this migration here, how would it look?
jea 00:46:29 I think what we would do is go to Charts.
Hotel CRDs?
We would add it to the CRDs, directory?
And then on install, we… this is because we really did not want to do the conversion webhook.
So, I think what we would do is just do a hard upgrade to the new version, and I would just swap out the internals, and then… we would mark this as a breaking change for the chart, and then the user would have to wget to install the, the new V1, Beta 1 for the instrumentation.
I think it's the better… the best way to do this. I mean, it's disruptive, but I don't think that… we could do the install check and notes warning to say that, hey, you don't have the V1 Beta 1 installed, please update your CRDs, which I don't think is the end of the world.
Mikołaj Świątek 00:47:29 Yeah, I guess… I guess that's alright.
For CubeStack, which is, like, a managed thing, which ships a bunch of its own resources, I think this is fine, and it's also fine in CubeStack.
Maybe this is okay, maybe this is just okay. Maybe it's okay, like, the operator chart is kind of like an infrastructure chart, where you install it and then you create your own stuff, so it makes sense that you have the… the conversion webhook in there, and you upgrade at your own pace, whereas CubeStack is, like, a content chart, which makes… which creates a bunch of things.
And…
jea 00:48:05 Beautiful.
Mikołaj Świątek 00:48:05 It just decides, and if somebody is creating their own stuff, well, you know, you just have to deal with the break and change.
jea 00:48:14 Yeah, I mean, I think none of these options are great, for what it's worth. Like, I think that all of this results in the user needing to deal with some breaking changes. I think it's just how do we want to break users?
It's very annoying that we can't do the thing that we want to here, as Mikolai said.
That's… that's very frustrating.
Mikołaj Świątek 00:48:35 I wonder what the.
jea 00:48:36 The reason is for that.
It doesn't… I can't… I can't understand why.
They would want to do that.
Mikołaj Świątek 00:48:45 I'm gonna make a note here.
I'm gonna make a note to… See what other charts… see what other… Projects aside…
Pavol Loffay 00:48:58 Is there, like, open issue against Helm?
to support the conversion webhook in the CRDs?
I mean, if they solve it, we wouldn't have to deal with all this workarounds.
Mikołaj Świątek 00:49:12 There is an open issue in Helm to improve CRD handling, but Helm claims that the problem is that Kubernetes needs to add this.
fundamentally.
I am… I… I would… I don't… I don't know right now which version I would prefer.
the conversion webcook option has the benefit that it's the devil we know. But I would really rather not.
so, I kind of want to figure out what every… what's… with a bunch of other… projects did, and see if anybody has had, like, a clever idea. And if nobody had the clever idea, then, you know.
I just… just bite the bullet and do the conversion webhook. I don't… I don't really like the idea of the adding the fields and deprecation that feels, like, very hacky and kind of implicit.
At least the conversion webcook is explicit about what it does and how it does it.
Do you want to talk about anything else here, Pablo?
Pavol Loffay 00:50:39 I think that's all, yeah. Please take a look. There is as well this case just that explains the strategies. I used it to learn about it as well.
I would like to maybe… Make progress on this.
It's fine, maybe, if you don't agree what strategy we want to do.
Actually, we should, because it will block old progress.
Mikołaj Świątek 00:51:11 I… I definitely… like, the strategy, I think we can reasonably quickly get it. Like, let's… let's set ourselves a deadline until the end of next week to figure it out, and then we'll make a decision. Is that okay with you?
Pavol Loffay 00:51:23 Yeah, absolutely.
Mikołaj Świątek 00:51:25 I'm gonna write it down. The other thing that we need to, agree, in there Until it's… until the end of next week is the 20… is the 21st, let's say.
And we got off… May.
The other thing that we should agree there… should agree on is the label versus allocation version, because that's a braking change, and it would be easiest to do that braking change while also switching the version.
Pavol Loffay 00:52:02 So, let's reason why, because I don't understand why we have to make it at the same time.
Mikołaj Świątek 00:52:09 It's because it changes our public API, right? The public API is that you add an annotation.
Do I… odd?
And then the, mutating webhook acts on it, right?
Pavol Loffay 00:52:24 So we would say, once we support V1 Beta 1, it's not gonna work with annotation.
Mikołaj Świątek 00:52:30 D1 Beta 1 is not gonna work with annotation. The whole point of this change is to be able to scope our… To be able to scope the webhook into something smaller, to not have to process every single pod in the cluster, which we do right now, because there's no way to filter an annotation.
That's the question. And this will have to stay until we drop V1 Alpha 1 support.
So, just adding Vue and Beta 1 isn't going to help us with this, but we have to… we have to do it… we have to make this change gradually, because it's a breaking change.
Pavol Loffay 00:53:10 But, okay, let's think about it.
How we want to actually… if it's possible to implement it in this way.
So we would ship V1 Beta 1. Our controller would be using V1 Beta 1, which would be the storage version.
And… We have the mutation webhook.
That queries the instrumentation… at the event, right? But it doesn't use the version of instrumentation.
Just gets the instrumentation.
And the… And if we would… maybe we can specify the version, but anyway, if you have the conversion web book, they will give you the… The object, and you don't know what… version… What was the original version?
Mikołaj Świątek 00:54:09 Okay, that's fine. We can figure that out somehow. Either way, the webhook is going to have to work on both the annotation and the label.
Either way, because we support both of these, logically, putting aside the details of conversion webcooks, whatever, storage version, whatever. So it has to support both.
But when we get rid of V1 Alpha 1 will be able to drop support for the annotation.
That's, like, that I think is what we should aim for. And we should do some kind of… probably along the way, we should do some kind of check and some kind of… some set of warnings, which will be telling you, hey, you're using V1, Beta 1, but you're using… but you're not using the label, or something. Like, we should have a way to figure this out.
But the point is that… Right.
Pavol Loffay 00:55:01 And that's easy, because we will just recommend using label, and if we see annotation, we will just emit warning, right?
Mikołaj Świątek 00:55:09 Yep.
And it's, like, strictly speaking, you don't have to do it right now, but, like, we're already making some… some change by shipping Vue on Data 1, so… it's easier to, like, logically, like, tie one to the other, I think. Like, it's going to be easier for users to understand.
Pavol Loffay 00:55:30 From that perspective, yeah.
Mikołaj Świątek 00:55:33 Okay.
Pavol Loffay 00:55:34 Okay, so I'll, I'll update this.
In the proposal, I think my gist is useful.
Do you think…
jea 00:55:43 No, it's a super useful context. I would put that in the issue, honestly.
Pavol Loffay 00:55:49 Or I can maybe… Put it somewhere in the docs.
If you agree, alongside my PR.
jea 00:55:59 Yeah.
It's useful research, certainly useful context.
Mikołaj Świątek 00:56:05 Yeah, it can go into the… into the, if it's not already there, I haven't checked, it can go into the RFC references.
Actually, sorry.
Pavol Loffay 00:56:24 Okay, I'll include it as, like, a separate file. I will make sure it's not, like, an RFC, but, like, a supporting document.
Mikołaj Świątek 00:56:34 I'm sorry, I want to give Puneet a chance to talk, because we've eaten almost all the time, and and he has a thing that looks like… Jones.
Puneet Singh 00:56:47 In the last, next to this one.
Yep.
Mikołaj Świątek 00:56:56 Sorry, here.
So… Yeah, what would you like to know?
Puneet Singh 00:57:05 Yeah, so, thanks a lot. So, I wanted to, ask one thing. I think the change in CRD we want to do in, like.
in a very stable way, that once we do it, there should be under no chance that we have to revert that. I think that's the idea.
But in case of conversion webhook being used, and the storage version being disabled on the Alpha 1 side, as long as users don't change anything in V1 Alpha 1, those stored versions will continue to exist in V1 Alpha 1.
So, if we try to stabilize the feature gate first, which is disabling the webhook, I just wanted to understand that how does that create a kind of a stable condition for CRD change to, you know, happen.
Mikołaj Świątek 00:58:02 So… Only one version can be stored.
And right now, this is the beta version.
That's already the case. That's already the case. So that's not changing. The only thing that can change is what is served, right? Because the conversion goes both ways.
if you're using the V1 Alpha 1 API, what happens is that it starts as V1 Beta 1, and if you ask using the V1 Alpha 1 API, it gets converted back.
When you ask for it.
And if we disable the conversion webcook, that just stops working.
Like, it gives you an error if you try to do that.
So, like, no matter what, somebody trying to in any way interact with a V1-alpha-1 collector is going to get an error.
from a… from a conversion webhook. I am, like, 95% sure this is true. I would have to double check, but I think that's my understanding of this model.
Pavol Loffay 00:59:02 Again, just… I would like to add something here.
maybe what we can do, instead of implementing a feature gate, we could, flip the switch on the CRD to served false.
it will have the same effect. When a user will request the V1 Alpha 1, they will get 404.
Mikołaj Świątek 00:59:24 The difference between these is that if they want to undo this.
undoing the change in the CRD is significantly more complicated than just slipping a feature gate back. Flipping a feature gate back is, like, a single additional argument to the operator. If you're using the helm chart, it's like a single field added in your configuration.
And you can continue running and kind of solve your problem without… You know, without having to downgrade the whole operator. But, if you have to modify this…
Pavol Loffay 01:00:00 The CRD, they would just change the one flag in the CRD without restarting anything.
Mikołaj Świątek 01:00:06 You would have to add support for that in the home chart, I think, as well.
Specifically.
Pavol Loffay 01:00:12 I'm forgetting about Helm chart right now.
Mikołaj Świątek 01:00:14 You know, maybe you should be a maintainer of OpenTelem.
collect open telemetry helm charts around, so you don't forget.
Puneet Singh 01:00:28 So I think I… I was under… you know, I also want… I was also more in favor of the thing that Powell mentioned, is, making the CRD change doesn't seem like that unstable of a change, you know, that it needs to revert it, because for that, you know, for users, it means that they have to move from Alpha 1 to Beta 1 API.
And and after that, you know, the behavior can be controlled using feature get, but I think we are already close to time, so we'll continue this discussion some other time.
Mikołaj Świątek 01:01:03 I mean… I'm fine staying 10 more minutes. If anyone, you know, if you need to go, then you can go, but I'm also… you can continue.
jea 01:01:11 I do have to drop, unfortunately.
Pavol Loffay 01:01:14 What a smell.
Mikołaj Świątek 01:01:16 Alright, so we can continue this discussion under the issue. I'm not married to the feature gate approach, I just think it's, like, easier to turn back if you do an operator upgrade and suddenly find that your stuff doesn't work.
Puneet Singh 01:01:32 Right, I mean, I just feel that the feature gate… Because of the fact that if the stored version is not changed, it doesn't move to the… V1, beta 1.
I feel like there is a case that when you disable conversion webhook, some stored versions are still left in V1, Alpha 1, which haven't changed. And in that case, because the webhook is disabled, those are not accessible using the V1 Beta 1 API.
The other way for the user is they might shift towards Vue and Alpha, one API in order to access those stored versions. That is the case, which I see as possibility here.
Mikołaj Świątek 01:02:14 I mean, yeah, but if you set it to served false, it's… it also can't be, or can it be, still, Accessed via the beta one.
Puneet Singh 01:02:26 No, so, assuming that we disable feature git first, the… the access to those… versions is cut off by Beta 1, okay? So, they might consider using V1 Alpha 1 as an API, or they might consider migrating the whole thing towards… towards V1 Beta 1. That is the other possibility, but both of these possibilities exist, and after that, as soon as we make the CRD change.
That is, like, the disruptive one, you know? I mean, the webhook?
And the CRD change both combined together basically creates the disruption for the users. I feel that making the CRD change first is kind of, like.
More intuitive, rather than making the webhook change first.
Mikołaj Świątek 01:03:18 Maybe, I'll… I'll have to think about this. Maybe… maybe the right way to do it is to make the web… like, make the feature gate… flip the feature gate on.
then make the CRD change, and then after the CRD change, make the feature gate, unchangeable, and yeah, stable, and then do the other bits, because that way you're kind of… At each point, you are forced to kind of, like, I know, I want to give users as much agency as possible in, like, dealing with this, and I also wanted to… want this to be, like, a very obvious breakage, basically. Like, they install a new operator version, and they, as soon as possible, they see that they have to do something.
Because I know that I can put whatever breaking change notifications in the changelog, most of them will not read it.
So, so I want to… so I want the software itself to, to, like, force a change in behavior, as far as to record. Like, even if they just have to go and flip the feature flag back off.
That's… at that point, they know that they have to do something, and that's, like, a big… And it's very obvious, because the, like, the webhook, which is disabled, is going to give them a message telling them exactly why this is and what they need to do, versus the served part, which is just kind of, oops, my stuff doesn't work, why doesn't it work? You know.
Puneet Singh 01:04:49 Yeah, I think this sounds good also, because we are leaving the possibility of user to use feature gate to, you know, switch and try to stabilize things. So, this sounds fine to me, because initially I thought was that once we make FeatureGate stable, only then we do the CRD. So, doing the CRD change is not any less disruptive for users, and you won't be inclined to revert it, but with FeatureGate, there, users have an option to, you know, switch back and test it out, so this sounds fine to me.
Mikołaj Świątek 01:05:23 Alright, cool. Yeah, so it makes sense. So in that case, it's like… flip the feature gate on, so webhook is disabled, but it can be in a bit bug. The next release, say.
Puneet Singh 01:05:35 He already…
Mikołaj Świątek 01:05:35 served to false, the way the feature gate stays the same.
And the release after that, maybe two releases after that, are free. Pavel has to say, because he has these OpenShift people who never upgrade anything. Right. At that point, the feature gate becomes stable, it can't be switched anymore, and then the release after that, we drop the version. That's kind of… does that sound good to you?
Puneet Singh 01:05:58 Yeah, yeah, absolutely. I think, yeah, this sounds good, actually. Yep.
Mikołaj Świątek 01:06:00 Alright, thank you. Oh, that actually sounds better to me. I'll update my issue.
Puneet Singh 01:06:06 Cool. Thanks a lot.
Alright, see you then.
Mikołaj Świątek 01:06:11 See you. Have a… have a nice rest of the day.
Puneet Singh 01:06:13 Bye.
