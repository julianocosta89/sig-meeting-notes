SIG: Service and Deployment SemConv
Date: 2025-10-30
Duration: 35 minutes
============================================================

## Zoom Recording Transcript

**Janhvi** 01:28 Hey, hello.
Hey, can you hear me?
That still works.
**Joao G. (Dynatrace)** 02:14 Work. Should work. Bye.
**Janhvi** 02:17 No, I can, I can hear you now.
Let's give it a few more minutes for other folks to join as well.
And then we can get started.
**Joao G. (Dynatrace)** 02:37 Right, so today we are in this slot.
B, right? Meeting time, yes.
**Janhvi** 02:42 Yep.
We'll just go through what was discussed in the last meeting in the last week, and then if there's anything more to the agenda, please feel free to add. Ehartik.
**Joao G. (Dynatrace)** 02:56 Right.
**Kartik** 02:59 Hey, hey everyone.
**Joao G. (Dynatrace)** 03:01 I joined the meeting.
That we had, it was last week?
**Janhvi** 03:06 Okay.
**Joao G. (Dynatrace)** 03:08 So I can… I can also give some… Some updates, context…
**Janhvi** 03:14 Sounds good, that helps.
How can you see the calendars on your invite? I was seeing in the Slack channel, there was some confusion around the invites. I think folks didn't have this particular invite. Do you see that on the calendar?
**Joao G. (Dynatrace)** 03:29 I see that in my calendar, yes.
**Janhvi** 03:31 Okay.
**Joao G. (Dynatrace)** 03:32 I'm not sure if they fixed… fixed something. I also didn't… I also fail to check when the person mentioned there was a problem, I fail to check if my calendar was also missing.
So I… I really don't know. But now, looks correct. I have both invites.
In my calendar.
Maybe, maybe the… the… what do you call it? The GC folks fixed it, Drask fixed it, maybe.
**Janhvi** 04:01 Yeah, yeah, could be.
**Joao G. (Dynatrace)** 04:04 But we're here, so it works.
**Janhvi** 04:07 Hey, Rudin. Hey.
**Dotan Horovits** 04:10 Hello.
**Joao G. (Dynatrace)** 04:12 Okay, so do you want me to give some context before we…
**Janhvi** 04:17 Yep.
**Joao G. (Dynatrace)** 04:18 Yeah, we can just probably do a rundown of last week's meeting, and then we can take it from there. Yeah, okay, yeah, so we… we discussed, So, basically, Josh showed… showed, started the discussion on the PR that is linked in the document. So, basically, he's trying to formalize the definition of What a service is.
So there's this pull request, this draft pull request from him.
Aya, thanks for sharing. Yeah, so he, yeah.
basically, we went through the PR and had discussions about The definition of what the service is, and what the service instance is, and, you know, like, how they… how they play together, and we also talked about the nomenclature of things, like… Because we also discussed, in connection to this, how Kubernetes name things, and how the Kubernetes side of things, It's related to our side of things, like… We more or less got to the point when where we say… we could say, more or less, that a deployment in Kubernetes is… will be the equivalent of a service.
**Janhvi** 05:35 In OpenTelemetry.
**Joao G. (Dynatrace)** 05:37 And then the… Instance would be a container or something like that, that is running.
So… Yeah, we discuss stuff like this, and… Discuss the modeling, like this diagram.
that we see, but I guess those we also discussed when you guys were in the meeting, I think, at the first meeting, or something like that, so there was nothing new about the diagram, we just, yeah.
We're just more or less focused on the… Definition of… Like, what the service is, and we talked a lot about, as well, that the fact that the service… Is a logical component, so nothing exists for a service.
Right, so, like, when you call… When we have the service name.
that has, let's say, HTTP server, checkout service.
That doesn't… that doesn't exist, like, there's no actual thing deployed that is that, right? It's just a logical grouping.
And the actual thing that exists is the instance, right? Which is, like, a component that's deployed, that is running.
So that's, I think, what's written in the PR, or at least the PR tries to write something like that. Yeah, this is, like, the service is one of the logical, distinct components that make up the application.
Yeah, I think that was it, and we talked a little bit about, as well, like, how to call this, or what to name, because we see it sometimes say application, like, to, you know, as a term to group the… all the components, or also system, and then, yeah, or… There is also, distributed system that is also, seen out there, And then Josh put the PR up, and yeah, I asked all of us to, you know, go review and give our opinions on On what we think about this definition, if we think it aligns, and maybe also think about… How this, how this aligns with, Kubernetes and so on, and we also, in the end, discussed, the last thing, we discussed as well, like.
If people already use… we looked into the link about the, recommended Kubernetes, Annotations or labels.
Not sure if there is a link in the PR as well, I think maybe Josh put the link.
**Janhvi** 08:01 Yeah, I think this one.
**Joao G. (Dynatrace)** 08:02 Yeah, exactly, that one. And so we talked about these labels and how those match, right?
And what we talked about as well, like, if people have these labels already, if we should map them, you know, like, for example, there is no service name in the telemetry, but we see, like, you know, app Kubernetes slash name.
Should we, you know, take the value of that and, you know, use that as the service name to avoid people from having to, you know, redo or adding more things? You know?
So we talked a little bit about this as well, but no.
No conclusion, we're just…
**Janhvi** 08:42 Huh.
**Joao G. (Dynatrace)** 08:43 Because I mentioned… yeah, because I mentioned that there is, like, also… other… technologies like Istio, that they also have their own labels for I don't know what they call a service, right? And, some backends that I know, for example, take the value of that for the service. For example, if there's no service name, right? Because they essentially do the same thing.
**Janhvi** 09:12 Yeah, this, this helps. How? Thanks, thanks for giving the summary. Quick question. So, if I were to understand this model right, so namespace now is more like a logical grouping of different services.
And in that, the service.name is also, like, a logical construct, it's not, like, an actual service, whereas the instance, which is the third attribute, is the actual instance that's running in some environment.
**Joao G. (Dynatrace)** 09:39 Yes, that's correct, exactly.
**Janhvi** 09:41 And that environment would be the deployment attribute that we have in OpenTelemetry, a different attribute. I think deployment is also an entity in OpenTelemetry, right?
**Joao G. (Dynatrace)** 09:51 Yeah, yeah, the deployment we didn't discuss in the meeting at all, so that one is, like, completely… Due to be touched, yes, but that's… that's pretty much about it, yeah.
And I think, Josh tried, as you can see the screenshot in the meeting, right, he tried with AI to… To see what he would say about… What definition would come up for if somebody just asks it, right?
So we also looked into it a little bit to see what he would come up with.
And in API, I post my, my, interaction with it, and what it… What it came out for me.
So it was, it was pretty, it was a pretty, interesting exercise, I think.
to use AI to, to ask what he would… What he would think about it.
**Janhvi** 10:43 So, are we aligning on the, naming for, like, namespace? I mean, namespace doesn't really feel like an umbrella item for a group of services, right?
**Joao G. (Dynatrace)** 10:53 Yeah, I think the rest we are okay, but yeah, the namespace, I'm not sure as well, yeah.
**Janhvi** 11:00 Yeah.
**Kartik** 11:02 So is, is namespace… like, sort of loosely corresponding to an application, so in this… in the screen, I'm seeing… reference to an application, right? Which is, like, an entire system.
**Joao G. (Dynatrace)** 11:13 Yeah.
**Kartik** 11:14 It contains multiple components. One of the components is, like, a service.
So it's, like, are we saying namespace and application are, like, somewhat… On par with each other.
**Joao G. (Dynatrace)** 11:27 Yeah, I don't think so, yeah, that's what… that's what we… I think we are leaning towards, yeah.
**Kartik** 11:32 7.
**Joao G. (Dynatrace)** 11:32 we didn't find a good name for it, and I think Josh even considered, instead of calling namespace calling application or something like that.
Yeah, but… We're not sure, but that's that, yeah, exactly.
So it's all like a namespace in Kubernetes, where there's actual isolation of, you know, resources and stuff like this.
Yeah. Yup.
**Janhvi** 11:58 Cool.
Yeah, the Kubernetes attributes, right? In there, I… so I see a name, which says it's name of the application.
And there's no other, like, namespace or other service name kind of a thing.
So, are there, like, different attributes in Kubernetes for the same thing?
**Joao G. (Dynatrace)** 12:20 Yeah, so, if you, what do you call it?
Yeah, so…
**Janhvi** 12:25 This is the one that I'm looking at.
**Joao G. (Dynatrace)** 12:27 Yeah, so if you scroll, we had also a hard time with it, but if you… it's just not so straightforward, you have to spend some time on it, but what I think maps, To our service name is this component label.
If you scroll a little bit down, there is an example.
Yeah, so, for example, like, the… Yeah, so, like, there's the… What was the component?
Component is a database. Yeah, yeah, exactly. So, no, it was not a component, it's actually the name, so name is the service name.
**Janhvi** 13:07 I see.
**Joao G. (Dynatrace)** 13:07 It would match, and then instance is instance, right?
And then there is this, part of, and then the part of would be the namespace that we, like, our, The application. Service.namespace, yeah, that's the name of the application that, you know, like, that these things compose the application.
I'm not sure if there was another example.
Yeah, there's, like, my service.
**Janhvi** 13:38 Yeah, okay.
**Joao G. (Dynatrace)** 13:40 Yeah.
WordPress… Yeah, I think in the… .
**Janhvi** 13:51 I think it looks like part of… is… is the namespace in OpenTelements, right?
**Joao G. (Dynatrace)** 13:58 Yeah, and then, yeah, and then the component, we don't have a thing to say what it is, in hotel, we don't have, I think there was discussion at some point to have something like a role, a role attribute.
To say, like, web server, database, yeah, some stuff like this, but we don't have that.
**Janhvi** 14:20 Got it.
Okay, so I think we'll take a look at the PR as well. I haven't taken a look, but at least, I think on the high level, it's the namespace, then the service name, and finally the instance, which is the actual piece that's running, not the logical one.
**Joao G. (Dynatrace)** 14:40 Yeah, exactly, yes.
**Janhvi** 14:42 Got it, got it, okay.
And I think As part of this SIG, we also want to add new attributes to the service entity, right? For example, cost center, criticality. How do we go about that? Should we first look at how other vendors are already using it, and then figure out where they should be added in the service entity? I mean, how do we go about adding those new attributes?
**Joao G. (Dynatrace)** 15:09 Yeah, I think that that's a good idea, right? Like, just try to do some research on what you can find out there, and, you know, what's, I guess, customary to… To, to do, how they use, and then just bring that, yeah, can create an issue, and then put the results there, and then we, I guess, go from there.
If you look at the PR that Josh created, he actually…
**Janhvi** 15:35 He actually created.
**Joao G. (Dynatrace)** 15:37 He actually split the… the, service from the service instance, entity, so now there is, like, a service entity that only has the… I guess if you look at the… YAML file, the entities.yaml.
Yeah, so, like, now there is a service entity that only has the… The… name?
And the reason for that is because those attributes are already stable, and the other ones are still in development, and, yeah, and there's… there are different things, right? There are different entities, like, like.
Like we discussed, and then now there's the instance, entity, and that has the… yeah.
That has the instance attribute, and, yeah.
I think we talked about, like, criticality or something, right?
**Janhvi** 16:43 Yeah.
**Joao G. (Dynatrace)** 16:44 So I guess that would be also part of the service, probably, not part of the instance.
Boom.
Yeah. Because it applied to all the instances.
Yeah, and then there's the namespace as well.
The namespace entity.
**Janhvi** 17:01 Hmm.
**Joao G. (Dynatrace)** 17:01 So, yeah, or we have, like Josh said, that the other thing will be a different entity, the criticality, the cost center, stuff like this.
**Janhvi** 17:12 They'll be part of the service entity, right? I mean, we'll have to figure out the naming and everything, but eventually… Got it.
Yeah, I think I can probably take that AI for next time when we meet. I can look into how other vendors are using these.
**Joao G. (Dynatrace)** 17:27 Because, like, yeah, because, like, the cost center, if… If, like, we think there is… there's gonna be, like, more attributes to the cost center, Right, like… I don't know, cost center… ID, cost center name, I don't know, you know, like, just ideas. Then I guess that will be also, like, similar, as you have here, like, entity.service.cost underscore center, for example.
**Janhvi** 17:50 Yo.
**Joao G. (Dynatrace)** 17:51 But, yeah, so that will be there, and, yeah, it would have attributes.
**Janhvi** 17:58 We'll have to have that as nested attributes under the same cost umbrella.
**Joao G. (Dynatrace)** 18:04 Yeah, not sure if we need to have, but yeah, that's… that's one idea, right? So, like, if we have… if we have… if we think the cost center of a service Makes sense to be modeled like that as an entity, with, you know, multiple attributes and so on.
Or we just add them to the service entity, I'm not sure, as descriptive.
Attributes.
I'm not sure if you know, but the entity model, the attributes have roles in them, and there is, attributes that are identifying, so…
**Janhvi** 18:37 M.
**Joao G. (Dynatrace)** 18:38 There can be only one or multiple, but all of them together make up the… Make up a unique entity.
Right? And then there's the attributes that can be descriptive.
So there is just, like, metadata. Like, the version, for example, is a descriptive attribute.
Or no, I'm not sure what the version is, but… Yeah, so for example, if we had identity cost center, like, if the… I don't know, if you want to have, like, a cost center ID or something, then that would be, like, an identifying attribute of the entity, and then we have, I don't know, cost center, department or something.
As descriptive or something like that.
**Janhvi** 19:20 Is it always mandatory to have, like, one, one identifiable attribute?
**Joao G. (Dynatrace)** 19:25 Yes. Yes.
**Janhvi** 19:28 If we go ahead…
**Joao G. (Dynatrace)** 19:28 There must be one identifying attribute, yes.
**Janhvi** 19:32 Okay, so if we go ahead with, like, a nested attribute, we need one identifying attribute in that case. If we just go with, like, one common field, then… then we don't really need… it could just be a descriptive attribute in that case.
**Joao G. (Dynatrace)** 19:44 Yes, but I am almost certain that we need to have a… Not identify, because otherwise there's no way to, yeah, identify the entity.
**Janhvi** 19:55 Got it. Okay, I can… I can take that AI for next time. I'll try to figure out the usages for this and the definition, so we can discuss that next time once we meet.
**Joao G. (Dynatrace)** 20:04 Cool. Wow, sounds good.
**Janhvi** 20:08 I think there was another proposal from somebody on Slack around criticality, that the president… Oh, yeah.
I'll… I'll share it here so that everybody can take a look, because as part of the SIG, we want to stable… we want to add criticality and then eventually stabilize it.
Let me add that proposal.
**Joao G. (Dynatrace)** 20:25 In our meeting document, we have a link to the project board?
No, right?
Should add that, let me see if I can pull it up. Because I saw the issue, and then I added to the… we have a project board.
So we actually should go to the project board and do some… I don't know, triaging, I guess. Just a sec, I will…
**Janhvi** 20:52 I'll try to pull it up.
Yeah, I think this is the one.
**Joao G. (Dynatrace)** 21:06 Yeah, nice, yeah.
Yeah, I already added to the service deployment project.
**Janhvi** 21:13 Yeah, I think on a high level, it tries to add, like, a new attribute called criticality to the service entity.
And with criticality, I think they're trying to classify the services in terms of, let's say they're high criticality, medium, low, and then people can have queries based on that, give me all the metrics for all critical services and stuff like that.
**Joao G. (Dynatrace)** 21:39 Huh.
**Janhvi** 21:42 Yeah, I think maybe offline, let's go through that proposal. I know, I think back, he's going to be present in the next SIG meeting, who's the author for this proposal, and they want to So if I've sent them the invite, I think they'll be there in the next meeting that we have.
**Joao G. (Dynatrace)** 22:02 Oh, okay, so you know them already.
**Janhvi** 22:04 Yeah, yeah, they pinged me on Slack for this, so…
**Joao G. (Dynatrace)** 22:07 Cool.
**Janhvi** 22:10 Okay, cool. So I think two AIs, probably, for next time. We can go through this more in detail, and the second one would be the cost center thing.
**Joao G. (Dynatrace)** 22:18 Alright.
Yes, I will… let me add the link to the project board to the Sikh.
Document?
**Janhvi** 22:34 Let me take this note.
How would you know once, Josh's PR is submitted, what is the next step to get this stabilized? I think namespace is not stabilized right now, right?
**Joao G. (Dynatrace)** 22:54 No, no, not. I think instance also is not stabilized.
Yeah, the, the process is, yeah, we, we would… Do some prototyping, and then, you know, verify if this makes sense in reality, and… with the broader community, and then I think that that will be… That will be it, I think. For the instance, instance ID, there was a lot of, discussion and a lot of, thought put into it, into the algorithm. I think you saw, maybe you saw the lengthy text about it in the notes and so on.
So… so I think that one will go fairly, and it's already implemented, I think, in some SDKs, I think the Java SDK.
already generates service instance IDs, So I think… I think those will be fairly okay to stabilize. The namespace might be the trickiest one, yeah, because… Yeah.
**Janhvi** 23:53 like…
**Joao G. (Dynatrace)** 23:54 maybe it gets confused. My fear is that people is gonna… it's gonna create confusion with the Kubernetes namespace event.
Yeah. They might think that it's the same thing. It might be the same thing, but in some cases, it might not be the same thing, and… Maybe you can use the same value for it, maybe not, yeah.
**Kartik** 24:12 So, is there a reason we… Went with namespace as the name for this entity, like, as opposed to… Thinking of something else, like application itself, like, what's the reason for using namespace as the starting point here?
**Joao G. (Dynatrace)** 24:26 I don't… I don't think it was, intentional. I think it was just, like, yeah, let's go this way. I don't actually remember what was the reason. I don't remember, maybe this one is there for so long that, But I don't think there was, like, let's use because it's as similar as Kubernetes. I would doubt, so this is just, like, makes sense, and… Without much, much, much deep thought into it.
Well, I might be wrong.
Maybe Josh knows.
**Kartik** 24:56 Yeah, I'll check with John.
**Janhvi** 24:59 Since it's in development mode, how hard would it be if you, like.
But if we, like, propose a different name.
I think when it's stable, I know it gets very difficult to change the naming convention, but now, since we're anyways driving the standardization and stabilizing, right, is it still going to be very hard if we propose a different name at this point?
**Joao G. (Dynatrace)** 25:19 for the namespace, I think it would be acceptable. The problem that we are facing, that we always face with CENCOM, is that some things are there for so long that it's…
**Janhvi** 25:31 Hmm.
**Joao G. (Dynatrace)** 25:32 It's kind of de facto stable.
Yeah. Because so many people are using them, and, you know, they expect that this is like that. So for those, I'd say, yeah, it would be… Still possible, because, I mean, it's still marked as in development, right? But… But I think for this one, I don't… I'm not entirely sure, but I don't think many people adopt it, so it's not, like, something broad. It's also not something so old, I think.
So for the namespace, I think if we have good arguments, I'm sure people will also be unhappy, but, I mean, it's unstable, so… I think we… if we want to do it, now it's the right time, so…
**Janhvi** 26:14 Okay. To change it.
**Joao G. (Dynatrace)** 26:17 Like, for example, the service name, we wouldn't be able to change, I think. It's a stable, okay, but even if it wasn't, that one is, like, all over the place, so… Yeah.
**Janhvi** 26:30 Okay.
Sounds good.
Okay, cool. I don't have anything else on the agenda for today. Anyone else? Anything you'd want to call out, discuss?
**Joao G. (Dynatrace)** 26:43 Can you open the… and put the project board on the top of the document? Can you do… do we want to just go through it quickly to see if there's anything we should… So the last issue is the one that we talked, is service criticality.
I guess we still leave it in to-do, because nothing is… Being done with it, yeah. And let's see if the person, the author, joins, maybe we can, yeah.
**Janhvi** 27:08 Stanley, we can.
**Joao G. (Dynatrace)** 27:09 Assigned to them, yeah, assigned to them, or, yeah, see who… who's gonna… Take it, and yeah.
**Janhvi** 27:17 I think this one… should we move this to in progress?
**Joao G. (Dynatrace)** 27:23 Instance ID.
Hmm.
Down one.
But I think I'm assuming there would be different PR to stabilize this. I think as of now, we're just looking at the definitions and the naming.
Yeah, let's, let's maybe put this one in progress, yeah.
I can also try to take a look at it to see what's the… -Oh.
I see that there is a few comments, and it is quite old issue, so… I'll just revive it, I guess.
Yeah, just change it to in progress.
**Janhvi** 27:59 How do I edit this? Do I need different axes to edit this?
**Joao G. (Dynatrace)** 28:03 I think you need to… in this view, I think you don't. I'll just… via the issue, you can… you can change. I changed it now.
**Janhvi** 28:11 Okay.
**Joao G. (Dynatrace)** 28:12 I think you can have to change the board, the view board.
Yeah, and then there's, like, a Kanban, you can drag things.
**Janhvi** 28:21 Sounds, sounds good.
Okay, I think deployment, we've anyways not talked about it, so next time when we talk about deployment, we can go through this.
This is, again, deployment, service.pool.name.
**Joao G. (Dynatrace)** 28:36 Yeah, the first one is also, like, the… this one is, like, the… What it was in Kubernetes component, Label.
**Janhvi** 28:49 I see, the final host book was actually…
**Joao G. (Dynatrace)** 28:51 Yeah, like, purpose, database, application, service, web server, whatever.
**Janhvi** 28:56 Yeah, yeah, this refers to the, component thing that's there in the Kubernetes attributes.
**Joao G. (Dynatrace)** 29:03 Yeah, that seems to map, yeah.
**Janhvi** 29:07 Okay.
**Joao G. (Dynatrace)** 29:13 Yeah, I'll try to take a look at this. I commented 3 weeks ago, even.
Okay, I'll take a look at this as well.
a to-do.
Those bedboards.
Can you move it to to-do?
I lost my board now.
**Janhvi** 29:33 Let me do this.
Should I put this in in progress, or to do, to do…
**Joao G. (Dynatrace)** 29:38 Just put a to-do, so I can take a look, yeah.
**Janhvi** 29:41 I don't think I can even move it, I probably don't have the right axis.
**Joao G. (Dynatrace)** 29:45 Nope.
**Janhvi** 29:47 Yeah.
**Joao G. (Dynatrace)** 29:49 Okay, that's weird.
No worries, Dandon, I'll do it later.
It's strange.
If you click on the issue, can… You don't see the little drop-down here.
Maybe you don't have… Yeah, yeah, I think it… because you don't have right access to the results.
Okay.
Should see if we can fix that, I guess.
Let's maybe put this in the agenda, maybe.
I don't have powers to do any of that, but maybe we can ask Josh to take a look.
I can follow up with Josh offline for that.
Okay, cool, then.
Then please do.
**Janhvi** 30:42 Okay.
**Joao G. (Dynatrace)** 30:43 Yes, we have to add you to the… we have this, yeah, Github owners file.
**Janhvi** 30:52 Okay.
**Joao G. (Dynatrace)** 30:53 have to add you to the team, or something like that, to the GitHub team user.
**Janhvi** 30:59 Okay, okay, I'll check with Josh on that.
**Joao G. (Dynatrace)** 31:05 Cool.
**Janhvi** 31:06 Okay, alright, cool. Thanks, everyone.
**Joao G. (Dynatrace)** 31:10 Yeah, have a nice day.
**Janhvi** 31:11 Thank you.
Sure, huh?
