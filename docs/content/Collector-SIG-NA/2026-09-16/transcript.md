SIG: Collector SIG (NA)
Date: 2026-09-16
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Andrzej Stencel** 01:12 Hello.
**Pablo Baeyens** 01:16 Hey.
**Andrzej Stencel** 02:37 So I'm just finding out that the legal name for Grafana Labs is Rainpank Inc.
Apparently.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 02:47 Yeah.
Wow. Kinda like… kind of like, Honeycomb's name is technically Hound Technology Inc. Both are doing business as, yeah?
**Andrzej Stencel** 02:59 And that's what was showing up in the dev stats thing, yeah, that's true.
Do we want to start?
Tyler, do you want to…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 03:51 I can go first.
OTTL is looking to graduate, but just like K8 Attributes Processor just was tagged 1.0, we would like to tag OTTL 1.0.
I just put in Zoom, and it's in the meeting notes as well, the official component, graduation issue.
Part of, becoming 1.0 is end user or vendor, adoption evidence, so if you are an end user or a vendor who uses OpenTelemetry, whether that's from the transform processor, the filter processor, the routing connector, the tail sampling processor, or some custom component, or any way that you could be using OTTL, We would love to hear how you're using it, in this issue. That will really help, speed through the process of tagging OTTL 1.0.
Thank you.
**David Ashpole (Google LLC)** 05:00 Cool, I think I'm next.
So, I wanted to come and, give everyone an update. I'm not sure if… people here really have been following telemetry policies, but I wanted to briefly introduce the concept, and Yeah, offer an invitation for anyone who wants to join and help us out. So, telemetry policies… It's something that comes, I think it's inspired by, like, XDS from Envoy.
But the idea is that it's dynamic configuration. That's… Kind of sent in small pieces.
and is component agnostic. So, in theory, policies are going to start to be implemented.
In SDKs, as well as in the Collector, maybe in places like OBI. So there… there's some overlap here with things like OTTL and transformations, but generally speaking, policies are much more limited.
And they're… it's kind of like… there's some different trade-offs made as well, where we really would like to be able to support really, really large numbers of policies, at once. So that's kind of one of the design goals, is that it's efficient, when you have a large number of them.
To start out with, we're starting with a policy processor.
And a file, policy provider.
So, if you see pull requests for those, that's where those come from, and yeah, I think I'd encourage people to read the OTEP if they're interested, and ping me on Slack if you either have concerns, or if you'd like to help out.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 06:48 Question for you, David. In the implementation of the processor.
Once the policy has been read, And, like, the restrictions are… known by the processor. What's… what's doing the actual enforcement? Like, are you gonna loop through all of the… will you have to… will you loop through, like, the payload, and then… is there, like, a policy library in Go that's, like, outside the collector that knows how to interpret the policy and… translated into… something in Go that can actually enforce it?
**David Ashpole (Google LLC)** 07:26 So I think… so there are some prototypes that, Jacob has done.
Jake Barnhoff.
And those are in his own org and stuff. So there is an implementation We may end up… the policy protos may end up being slightly different from what he implemented, right? So we probably won't reuse his implementation directly.
But yeah, he has written a library, I think, that does policy enforcement, but I suspect that we would kind of rewrite most of that, or at minimum, like, contribute that and adapt it, for this processor.
Boop.
**Braydon Kains (Google LLC)** 08:17 Awesome.
**David Ashpole (Google LLC)** 08:17 I…
**Dakota** 08:24 I can go next, okay, with the next item on the agenda.
There is a PR up for the Google PubSub receiver fixing an issue.
I'm actually here for a coworker who has the PR open himself. We've been having some trouble getting in touch with the maintainer for the component.
So, looking to the community to get a review on it.
And I know we're also… we've been in touch with Google about getting one of their employees to be a maintainer on it.
So… That should be… Shouldn't be an issue moving forward, but for the time being, this PR is still in need of review, and the maintainer has not been responsive.
That's all I really have.
**Braydon Kains (Google LLC)** 09:18 I did DM the maintainer last week, or maybe it was even the week before.
And he said he would carve out time to look at this among a few other PRs that I know were in flight for the receiver, but it seems like, it seems like he hasn't gotten to it.
So… I might message him again, I would offer to review it if I knew anything about PubSub myself. Unfortunately, I really don't.
That's fair.
I can at least give it a, like, a… Collector code review, but, for PubSub-related stuff, I don't really know.
So, maybe I'll… maybe I'll try and message him again and see.
**Dakota** 10:00 Okay, I can also reach out to him, as well, for Slack.
**Braydon Kains (Google LLC)** 10:04 He did answer a Slack DM, so that might be worth a shot.
**Dakota** 10:08 Okay, cool.
Thanks, Braydon.
**Blake Rouse** 10:22 Okay, I'll go next. There's a link down here, there's a PR for the Export Helper. We've talked about this a few times.
Meetings. I'm still looking on our… Approval and review.
It is needed. It does occur.
On shutdown, when a context cancel happens on the exporter.
That can happen and result in… When you don't have retry on failure, the… Events that are in that batch to be lost.
It is… I have confirmed that is the case.
So, I'm just looking for approval so we can get this merged and fixed.
The export helper, we have some behavior tests on the Elasticsearch Exporter.
that… observe this behavior. The behavioral test actually has a check in it to accept that this is a known bug.
That I would like to get out of our behavioral tests once this is merged, but since it relies on the export helper.
I need to get this merged, so… Just trying to cause awareness to it, because it's been marked stale. I see Evan removed that, but yeah, it's… it's been open for a while now, so I'm just trying to get some eyes on it.
**Andrzej Stencel** 11:42 So it does have an approval from Josh MacDonald's right, who's an approver in Collector Core.
So I don't know if there's anything else that needs… to be done before merging? Oh, yeah, we have Josh from slapping.
**Pablo Baeyens** 11:56 I would ideally want a review from Dimitri or Bogdan, but I think it's been enough time that, yeah, we can maybe… Merge it, or give them a final call.
I can take this and ping them.
**Blake Rouse** 12:17 Okay.
Thank you. Appreciate it.
**Alex Boten** 12:31 I guess I'll go next. This is a discussion that's, come up this morning, for me, because I was looking at the release, repository and realized that we have a vanity URL that we've had for the Collector Contrib components for a long time, and we just haven't… Migrated over to it.
And I guess I wanted to ask the question here in this meeting, whether it's something that we should do at all, if we should just close this issue and say we'll never do this. I'm… I don't have… there, you know, I feel like if the door is open, it is closing now that we're stabilizing these contract components. So, Yeah, I'm… Open to suggestions, thoughts, comments.
**Andrzej Stencel** 13:29 I think we should do this, and… Eve.
Only just to, lessen the ties with GitHub, the project. I mean, the current URLs have github.com in the name, so… If GitHub goes down, or if we want to disconnect from GitHub, which I don't think would be easy, but that's another obstacle that would block us, or make it much, much harder to do this.
**Braydon Kains (Google LLC)** 13:57 When you transition Through a vanity URL, does the old GitHub one still work for a while?
**Pablo Baeyens** 14:05 I don't think so. So let me try and search for it, but… there was… at some point, some rumor or something that the .io domains would go away, so Kubernetes looked into migrating away from that domain for their Go modules, and… the… did not do it because of that, because there's no good way to transition between one and the other. There's some sort of proposal on, like, aliases of Go module names, but it's not implemented.
**Braydon Kains (Google LLC)** 14:43 Because in that case, this would be, like, super disruptive, like… OCB configs across the world would not work.
**Pablo Baeyens** 14:51 Yeah, we would need some sort of… Sir, go ahead.
**Alex Boten** 14:55 I was gonna say, there's discussion in the issue that I linked in here that talks about how we could have you know, work around inside OCB for supporting both the old module name and the new module name for Collector Contrip stuff. Like, we could implement aliasing ourselves, more or less.
For a period of time, or whatever.
**Braydon Kains (Google LLC)** 15:21 I guess there's also, like, There are still in the wilds.
distributions of the Collector that don't use OCB, and they do the import thing, like, the old-fashioned way, make a Go program, import everything at the top, make the components.go file yourself that way, and they would also be Be disrupted by this.
Yeah, the old-fashioned way of, like, 2 years ago.
**Alex Boten** 15:47 Yeah, the old-fashioned way of having manifests created By hand, or whatever.
**Braydon Kains (Google LLC)** 15:52 Yeah.
**Pablo Baeyens** 15:55 I personally don't feel like this is worth it. Like, if we have to migrate away from GitHub.
we'll have to break people then, and I'd rather break people at that point than break them now.
**Braydon Kains (Google LLC)** 16:13 Does the… the Go SDK's contribib also come from a vanity URL?
I can't remember.
Just like there might be impressions. I think so.
**Pablo Baeyens** 16:27 Yeah, I think so.
**Braydon Kains (Google LLC)** 16:32 That's too bad. It would have been nice for us to say, well, the Go SDK comes from… a vanity URL for core, and a GitHub URL for… for contribib, and we could have just… popped alongside that, but I guess not.
**Alex Boten** 16:49 Yeah, I mean, I guess we… we don't have to do the same thing.
It's fine. Dude… the only… I will say that it is nice to have a bit more consistency in the manifest, so that, you know, if you're getting something from the OpenTelemetry.io… OpenTelemetry project, you get it from hotel.io or whatever, and that's… that's kind of a nice-to-have, but it's not, you know… Not necessary, or whatever, so…
**Joshua MacDonald (Microsoft)** 17:18 There must be a feature request upstream with the Go toolchain for some kind of support here.
It seems like way too much pain for the benefit, but it also has been something I've been aware of for 5 years. Like, why are we the oddball with GitHub URLs in Contrib?
**Pablo Baeyens** 17:40 Yeah, so I posted the… the issue from… Kubernetes?
From a couple of years ago.
Which I think is the closest that exists as a feature request, but I don't feel like the goal maintainers are… in favor of this, at least not in the way that Cornet is pushed for.
**Alex Boten** 18:33 Alright, so I guess we have some people that are in favor, some people that are against it. Maybe we can put it… Any thoughts, comments in the issue, and we can make a decision there and either close it and remove the alias, the vanity URL that we have, or, do the work and deal with it, so… Thanks.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 19:37 Okay, looks like that's all the topics for today.
Thank you, everyone.
**Braydon Kains (Google LLC)** 19:41 Thanks, everyone.
**Pablo Baeyens** 19:45 Thank you.
**Kells Kearney** 22:16 Interesting.
through it, and…
