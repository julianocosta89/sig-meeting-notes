SIG: Community Demo App SIG
Date: 2026-08-26
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:38 Hey, Matt.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 00:40 Long time, no speak, how's it going?
**Juliano Costa | Datadog** 00:43 Oh, good. Busy. How are ya?
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 00:46 Yeah.
Not too bad. Little… a little bummed about the K6 stuff, but what can you do?
**Juliano Costa | Datadog** 00:53 Yeah, that, that was a… Yeah, that was head. I… yeah.
I'm mostly frustrated with the rework, to be honest, like… Yeah. Because whenever we have that, the logion back, merged, we'll have to cut the release, and… Yeah.
it's not an easy process. And then update docs and everything, yeah, it's… It's fine.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 01:29 Happens.
**Juliano Costa | Datadog** 01:31 Yeah.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 01:32 But it's… getting per season as the visualization tool might be a better move anyway.
**Juliano Costa | Datadog** 01:39 Yeah, we… we… This is a long-time discussion that we… we have, mainly because the demo was always maintained by… by vendors.
Yeah. And when we… when we started, I think in the open source space, Grafana was the… the most used tool.
So we… we chose Grafana to… to be the UI?
Of the demo, for observability in the demo. But now we have process, and process is, part of the… CNCF, so I think it's, A good move.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 02:23 It's a good exercise for me, too, to be, impartial to vendors.
**Juliano Costa | Datadog** 02:28 Yeah, yeah, it is. Hey, Tobias.
**Tobias Oka | Datadog** 02:30 you know.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 02:32 Hey, how's it going?
**Tobias Oka | Datadog** 02:35 I'm, I'm great. How you doing?
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 02:39 Cheers.
**Juliano Costa | Datadog** 02:41 All good, all good.
Busy meeting today, yay!
Let's go, team!
Tobias, Tobias, is your, PR still open?
**Tobias Oka | Datadog** 03:08 It's still open, yes.
**Juliano Costa | Datadog** 03:09 Okay, okay, I'll just put on the meeting notes here so we can… So we can talk.
Donal, I saw your Podman thing, looks good. Let me know when it's good to go, and I'll take a look.
**Donal O'Sullivan** 03:33 Sounds good. Thanks, Juliano. Yeah, I was only checking recently, and I was like, oh, it actually doesn't work locally when you build, so, I think it should be fine. I tested the changes with Docker as well, it doesn't break anything, so I think we're okay. I might actually add that to the PR, but
**Juliano Costa | Datadog** 03:50 Cool.
Yeah, I actually learned with the RPR. I wasn't aware of the… I wasn't aware of the behavior on Doctor, and then, yeah, glad that, Oddman broke.
**Donal O'Sullivan** 04:09 Yeah, it's just a bit, like, it's stricter around building, like, builder versus build kit, but that whole exposed thing in Dockerfiles can be a bit misleading, because it's like, this is… it's only really for documentation, it's not actually… Exposing a port.
I want to hug to meet him.
**Juliano Costa | Datadog** 04:29 Before we start, let me just say hi to the… Two newcomers here, so Tobias… Tobias is, works at Datadog with me, so I know him.
And, hi. And Dave, I actually don't know you, so hi, welcome to the Demo SIG meeting.
**Dave Cervi** 04:51 Yeah, how's it going, guys? Yeah, my name is, Dave Cervi. I've launched a… a new startup in the observability space, so just, thought I'd join this call and, yeah, get a… get a sense of, you know, what you guys are working on, and get a sense of the community, and yeah, really appreciative work you guys do as well. So, yeah, happy to be here. And, Yeah, Donal, I like the accent, mate, as well.
**Donal O'Sullivan** 05:18 Hi, Dave, I was just gonna say, you're Irish, yeah?
**Dave Cervi** 05:20 Yeah, yeah, yeah, yeah, yeah, yeah. Whereabouts are you based? Are you in Dublin, or…
**Donal O'Sullivan** 05:24 I'm actually in Limerick myself, so you're Dublin anyway, I can tell her, yeah?
**Dave Cervi** 05:29 Yeah, Dublin, but I'm in… I'm currently in, Bonsai as my,
**Donal O'Sullivan** 05:33 Yeah, no, seriously.
**Dave Cervi** 05:34 Pretty, pretty cold at the moment, in the windows, so, yeah. So yeah, happy to be here, guys.
**Donal O'Sullivan** 05:41 Welcome, welcome.
**Juliano Costa | Datadog** 05:43 Awesome.
So… Cool.
So, I think I'll just start with the only item that I have in the agenda, from, Tobias. Do you wanna… Grab the mic and, present what you have, or do you want me to say something?
**Tobias Oka | Datadog** 06:07 I'm happy to talk you through what motivated me to write a PR, and happy to get everyone's input on, you know, if it actually makes any sense or not.
So, let me quickly…
**Juliano Costa | Datadog** 06:22 The stage is yours.
**Tobias Oka | Datadog** 06:23 Okay, cool. So, basically, in many of the services in the Auto Demo, the SDK is… Basically baked in, so, like, it's loaded as a dependency.
So in… in the case of the payment service.
Which is… which is a node service. Basically, it's just a dependency.
in the package JSON, right? And what this means is that when you want to use the hotel operator in Kubernetes to do auto-instrumentation, you can't really do that.
And, using the hotel operator, to instrument is something that people have requested, and I think it is something that would be quite valuable to be able to do.
And so, I was thinking about, okay, how can we make this possible, right? How… how can I make it possible that Demo still works.
When it's run, like, in a doc-compose, but it is also possible to run the… operator to inject an SDK version, or, like, basically a particular instrumentation version that the operator chooses.
And, the approach that I came up with is basically to, remove the dependency from the package JSON, depend only on the OTEL API, and then… bake the SDK into the Docker image, for Docker Compose.
But the idea is to have, basically, unless someone has a better idea, to have two images, one with the SDK inside, because for Docker Compose, you don't really have an operator.
And, and, and, and one potentially without it, where you can use, the, the operator to load it in. At the moment, there are… so the way I've structured this PR, there aren't really two images, there is just one image. It has an SDK in it, and the way that it works is that basically, I mean, as I mentioned, Node basically has the, has, like, all of the hard-coded, like, SDK dependencies removed. It only depends, on the API, and then I basically bake the SDK into the image itself.
By just, like, copying it in the same way that the operator would.
And what this means is that A it works, in Docker Compose, and B, if you actually use the operator in Kubernetes, because I've put it in the exact same location.
Where the operator would put it in. If the operator wants to put it in, it will overwrite what I have, and then you will have what the operator wants, and so it actually works in Kubernetes and in works.
In Docker Compose. So yeah, I mean, I guess I have, like.
two questions, like, A, does the… idea to have it instru… like, to have the ability to instrument with, with the operator? Like, is that something that, all of you also agree that this makes sense? And then the second question is.
like, what do you think about this approach here? Because, like, as I said, I had the idea, maybe we can have two different images. This here would actually also allow it to work with just one single image, but it's, like.
maybe a bit hecky? Yeah, open, open for you, for your feedback here.
**Juliano Costa | Datadog** 10:20 I have opinions, but I want to hear, I want to hear the others, so if anyone wants to say before, go for it.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 10:30 I think the auto-instrumentation piece is really helpful. Like, I think a lot of people do look for auto-instrumentation, and having a separate path to do that would be good.
I think two images would probably be better, so you had, like, a Kubernetes and a Docker image, that would be… I mean, I know they're both Docker images, but, like, one is made for Kubernetes auto instrumentation, one is made for… to be built for Docker locally.
Just to, like, separate them out and avoid the… the hackiness of this… this part, but that's my two cents.
**Tobias Oka | Datadog** 11:05 Yeah.
Yeah, it makes total sense. I mean, any other views?
**Shenoy Pratik** 11:12 I like the ease of transfer from here to Kubernetes.
So we have less code changes, and the changes are directly into the container, to the Docker file.
That's pretty much good.
From an instrumentation showcase-wise, it doesn't change, because we're still using auto-instrumentation.
So, that works Yeah, I don't have hard opinions right now, so it's pretty good.
**Tobias Oka | Datadog** 11:39 I mean, so, like…
**Juliano Costa | Datadog** 11:41 Go ahead.
**Tobias Oka | Datadog** 11:41 So the idea here, right? I mean, I'm basically just showcasing this approach here with one single service. My idea was, if you think… if we can agree that this is, in general, like.
a good approach, then we could basically apply this to other services that can be instrumented with the operator. I mean, there will be some that anyway can't, right? Where we can't do stuff at runtime, like, I don't know, Elixir or something.
But we could at least use this pattern on other services as well.
And sorry, there was a… Dave, I think you had a comment.
Or who was it? I didn't quite catch it.
**Juliano Costa | Datadog** 12:24 I think, I think you… Okay. Well, if you have anything to say, feel free to… we are an open mic, meeting, so everyone is welcome.
So… Regarding the two images thing, I would be against it, to be honest, just because it would be another thing that we need to maintain.
But Now that you are telling me that this… the operator… simply overrides it. I think that's actually good.
And I think we could, we could maybe think one, one step further, and instead of passing the node options and… the… What is the…
**Tobias Oka | Datadog** 13:22 I mean, there's two parts, right? There's the note options variable, and then there's the copying of the auto-instrumentation.
**Juliano Costa | Datadog** 13:29 So, the… if I just copy the agent, but I do not require it, it wouldn't instrument, right?
**Tobias Oka | Datadog** 13:40 Sorry, I didn't… I didn't follow that. If I did watch.
**Juliano Costa | Datadog** 13:44 So, if we still copy the Autel, auto-instrumentation, OJS to the code, but if we do not dash dash require it.
**Tobias Oka | Datadog** 13:54 Yep.
**Juliano Costa | Datadog** 13:55 What does the instrument.
**Tobias Oka | Datadog** 13:56 No, it's just random code lying somewhere in the Docker image for no reason, yeah.
**Juliano Costa | Datadog** 14:00 I think what we could do, then, is having… The node options as an argument.
On the… on… on the… On the container itself.
Then we could… use different approaches. For instance, I know that, Elastic has, distributions Of the SDK.
Right, Donal.
So, they could pass the E dot, or not E dot, but, like, the… the JavaScript SDK, or the Node SDK, whatever, in the node options, so then whenever this service starts, it gets instrumented with their SDK. And I think the same would apply for us at Datadog.
we could simply override the… the dash dash require with our own SDK, and the service would… and if the user, let's say that If the user do not change anything, then the… the… the current one, the auto instrumentation from OTEL, gets in.
I think that's, That would be, like, super configurable, and would drop the requirement of having two different images.
We would like on container size, because it would have this extra thing inside that we are not using, but it's a demo, it's a trade-off that I would be willing to… to have…
**Tobias Oka | Datadog** 15:43 So how, how, like, how, how, are we?
like, I mean, there are basically two ways, like, two places where we can put those node options, right? We can either put them in the Dockerfile itself, in which case they're part of the image.
And… If we do it like that, then basically… if… The operator comes in.
and sets the node options again, they will just overwrite that, because this variable can only exist once, right?
if… we added… on the… in the Docker Compose?
is there actually some kind of mechanism that makes sure that the same environment variables are set in the document… Docker Compose and in the Kubernetes YAML? Because if not, we could just specify two different values. We could, for example, for Kubernetes, say.
don't do it, just let the operator do its thing, and for DocuPompose, we could set it.
**Juliano Costa | Datadog** 16:52 Yeah, the mechanism is we opening up PR and taking care of that.
There's no automation in there, so the Helm charts is just us,
**Tobias Oka | Datadog** 17:10 Right, I mean, I think it's a judgment call, right? Like, it's, like, if you have it in here, it will work for both. If you put it in the Docker Compose, it's a bit more explicit, but the Docker Compose and the Kubernetes YAML just look slightly differently.
Hmm.
**Juliano Costa | Datadog** 17:31 But, I think if we… so what we do, because the Helm charts, they just change whenever we have a release.
So what we do whenever we have a release, we go through all the new environment variables, every value that changed and everything, and then update on the Helm chart. So the node options would be present in both. The only thing is that This would be easier to… to override, because whenever deploying to Kubernetes, you can define… like, So, for instance, I have… I have on my values.yaml here, service, and then I have a tag called env overrides, and then I just pass the tag and the new value, and that's it.
So, the user would just come and say, node options.
And then the new value is XYZ, my vendor SDK.
**Donal O'Sullivan** 18:36 Yeah, just another issue with this approach, so if you follow this way, like, we won't be able to use this Dockerfile at Elastic, we'd have to create our own Dockerfile, because we won't be using those node options if we had it baked in that way, so it'd be easier to, like, just inject it in.
**Juliano Costa | Datadog** 18:57 I, I, I didn't get, actually, sorry.
**Donal O'Sullivan** 19:00 No, sorry, so the… I thought we were talking about the node options environment variable there, is it?
**Juliano Costa | Datadog** 19:06 Yep. Yeah.
**Donal O'Sullivan** 19:07 Yeah, like, I wouldn't be baking that into the Docker image like that. Like, we won't be able to use that, so I think that would just cause problems for other vendors, like, I would just inject that in.
Wouldn't be hard-coding that.
**Juliano Costa | Datadog** 19:20 what I… Hmm.
**Tobias Oka | Datadog** 19:22 I mean, the problem if you don't hard code it in is that, by default, you have an image that doesn't emit any telemetry.
That's… that's… that's the… that's the… that's the problem if you don't hard code it in.
**Donal O'Sullivan** 19:35 But you can pass it in as an argument, so then…
**Tobias Oka | Datadog** 19:38 I'm so sorry.
**Donal O'Sullivan** 19:39 Then when the image is built, it will have telemetry, so it's… it's just… instead of making it, like.
Baked in here.
where you have to edit, so what I would be doing at Elastic is I'd be creating another Dockerfile to… and changing that value, but then I'd, like, at build time, if you just provide the actual value.
Just makes it a bit more dynamic, a bit more… Fork-friendly, if that makes sense.
That'd be my only argument here.
**Juliano Costa | Datadog** 20:07 Yeah, I… I mean, what if… just thinking here, what if you had an indiff container that fetches the… the SDK, and then… You have a shared volume between the two.
Thoughts, and then you just point that.
**Tobias Oka | Datadog** 20:27 I mean, that is actually what the op… that is what the OpenTelemetry operator does, actually. That's how it instruments it.
**Juliano Costa | Datadog** 20:33 Exactly.
**Tobias Oka | Datadog** 20:37 And that is why… why this actually is compatible with what the op… what the operator does. The operator will literally just go in.
And, basically, override that path, and it will override the node options, and then, like, both of those things that are in the image are just Like, not doing anything anymore.
How, how, how… does that… how does, Elastic and how do others actually use the… the demo gear, like, do you instrument… like, in what way do you… do you put your instrumentation in?
If you change it at all.
**Donal O'Sullivan** 21:23 We have our own SDKs, so we'd have to, like, modify stuff, so we have, like, our own… we have a couple of our own Docker files for… We're, like, using our SDKs, and then some… and then in… in… in the, in the manual instrumentation and the code, we've had to make updates there as well, if that makes sense. It makes it a bit annoying when you have to, like, sync with upstream, but, Yeah, we try to have separate files, like, something elastic, so, like, at least if it's a merge upstream, it doesn't, like… Cause huge headaches, if that makes sense.
**Tobias Oka | Datadog** 21:57 Yeah.
I don't have a hard opinion on, like, leaving it in here other than… if somebody just puts this service into their own compose, or whatever, and just does nothing.
If we leave this out, then that… service doesn't produce any telemetry, which… I don't really know if that is a problem, like, I don't know if people actually rely on that, or if we should just say, hey, this is not part of our default Docker Compose, so we don't care.
like, in our default token Compose, and in our default hand chart, we can make sure that this is set. And so, you know.
Like, everyone who has kind of hand-rolled their own They will just have to look at the patch notes and see, okay, well, you have to change it.
Like, how… is there any sort of precedent here, like, how to handle this?
Like, are we expecting people to just be able to pull a newer… Version of the images, and it just kind of… Behaves the same.
Like, produces the.
**Juliano Costa | Datadog** 23:07 telemetry.
**Tobias Oka | Datadog** 23:08 tree, or…
**Juliano Costa | Datadog** 23:11 So, the expectation is that, If they… if a new user comes in and runs Make Start.
He will get telemetry out of everything.
**Tobias Oka | Datadog** 23:24 But that we can satisfy either way, yeah.
**Juliano Costa | Datadog** 23:26 Yeah, yeah, yeah.
**Tobias Oka | Datadog** 23:27 Because we control that.
**Juliano Costa | Datadog** 23:30 And that… but, my… my… my suggestion on moving the node options to environment variable instead of, environment variable within the Docker file, is that I believe, in that way.
the operator… well, the operator does that, basically, but I think vendors will Would easily inject their own thing without having to create a new container.
But Donal is saying otherwise for Elastic, so… maybe I'm wrong here.
Because if that doesn't save them the time, so then what is the point of, like, trying to abstract it more?
**Tobias Oka | Datadog** 24:20 Like, how exactly would you be… like, I mean, if you want to put in your own instrumentation at runtime, you anyway have to use node options, or am I wrong?
Like, at least for Node.
**Juliano Costa | Datadog** 24:37 I… I don't know.
**Tobias Oka | Datadog** 24:43 Because I think that's the… that's the question, because if I anyway have to set the node options.
then I might as well just, you know, give it kind of a default value here, and when I set it to something else, like, whatever I set here is anyway gone.
And then there's no harm in it.
And the added benefit is that if you do nothing else, if you set nothing else, the telemetry will still get produced.
**Juliano Costa | Datadog** 25:25 Yeah.
**Shenoy Pratik** 25:26 From a consumer point of view, long-term, do we see any drift that can happen here? I'm just… Thinking from maintenance-wise.
Or is it that we just keep on updating the auto-instrumentation image inside, like, OpenTelemetry Operator, and things keep on working?
like, I'm just thinking from Dependabot point of view, like, another perspective, not looking at from folks. So, for example, Dependabot today has, what to say, 10 lines of, package updates that it needs to take care of. We have the core, we have the exporter metric, OTLP, GRPC.
For all these node packages. And now… We just need to take care of the OpenTelementary operator.
As maintainers, is that… Better for us to maintain, in long term.
**Tobias Oka | Datadog** 26:19 Thus, it at, like… If we look at the before state, like, does it actually update all of those node dependencies right now?
**Shenoy Pratik** 26:29 Yeah, yeah, yeah. Like, if there is an update coming in, dependable outcomes and creates a PR.
sometimes.
**Tobias Oka | Datadog** 26:36 a couple of.
**Shenoy Pratik** 26:36 some of the NPM packages, sometimes it's, like, one got updated, the second was not, so we'll have multiple PRs in. So I'm just thinking, will it reduce the number of PRs that we get from DependAbot? First of all, I think Dependabot might… I'm not sure, does it change the container images as well?
Sort of…
**Juliano Costa | Datadog** 26:55 Yes.
**Donal O'Sullivan** 26:55 It's a setting, isn't it? You can specify where the Pendlebot looks, I think, isn't it?
**Shenoy Pratik** 27:01 Got it, yeah. So in that Yeah, this would reduce the number of dependable peers for us.
**Tobias Oka | Datadog** 27:08 I mean, it depends on two things, right? So, there are… if we compare it, there are now less dependencies than before, because, like, this is way more packages, and now it's basically just one single line.
**Shenoy Pratik** 27:19 Nope.
**Tobias Oka | Datadog** 27:20 And… and so, perceivably, it would be much less. It depends also on how often do we actually… how often, does the operator actually release new images? Probably not that often. I mean, I… maybe I can… if I just go here, will I actually… Will I actually see the version history? No, I don't. Okay, I don't know. Like, can we easily see how often this releases something new?
**Juliano Costa | Datadog** 27:46 I think this… this one, is more…
**Tobias Oka | Datadog** 27:49 Oops, it's the… it's the one… oops, sorry, it's actually this one, I'm… it's actually this one, you're right.
