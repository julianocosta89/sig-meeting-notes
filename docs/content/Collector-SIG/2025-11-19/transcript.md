SIG: Collector SIG
Date: 2025-11-19
Duration: 16 minutes
Zoom Recording URL: https://zoom.us/rec/share/bkWeaY2jhNqAmKfJ5ma1Y2hFWHoAaOVixCJWt5hk3AB3693DT3OnA-YGxKUtJfrA.lOoqL1pVT11dPSL8
============================================================

## Zoom Recording Transcript

**Andrew Wilkins @ Elastic Observability** 01:15 Hi, Paula.
**Paulo Janotti** 01:54 Okay, I have Valjeel now, can you hear me?
**Andrew Wilkins @ Elastic Observability** 01:58 Can I hear you. Here you go.
**Paulo Janotti** 02:27 So, just the two of us…
**Andrew Wilkins @ Elastic Observability** 02:31 Yep, looks like it. I don't have anything specific for the agenda, or just one thing occurred to me.
which I've been thinking about.
find an issue for it in a minute. Do you have any opinions on…
configHTTP and configGRPC, and making them a little bit more…
consistent in the way that they use ConfigNet.
Is that… do you care about that?
**Paulo Janotti** 02:58 I heard about that, but I don't have any specific,
feedback I've been using enough. The problem is that I'm kind of so used to them.
the, I kind of…
especially config, looking to the user, I tend to kind of, I adapt too much to the things, you know? I'm not a good user in that sense. I adapt and…
Kind of.
**Andrew Wilkins @ Elastic Observability** 03:28 I know, I hear, I do the same thing. So, at the moment, I think it's config gRPC embeds ConfigNet.
Let me just find it.
Hmm… Server config.
Yeah, here we go, I'll just share my screen.
Can you see my browser?
**Paulo Janotti** 04:10 Yes, very good.
**Andrew Wilkins @ Elastic Observability** 04:11 Yeah, okay, so config gRPC server config embeds this net adder.
There's a change…
hasn't been merged yet, but there's a change that's coming to add reuse port to the GR… I think it was configure HTTP, actually, being added to the config.http server config.
But not yet to configure.
GRPC, so it's one or the other, but not both. I can't remember which one, actually.
If we then go to server config over here, it's got endpoint, so it's just an endpoint string, in…
Whereas in configGRPC, it's using configNet. In configNet… It has… Where is it?
Yeah, it's got this adder config, so there's endpoint, but there's also… you can specify the transport. So for gRPC, it means you can use…
TCP, and also Unix, domain sockets, which I think would also be sensible for HTTP, so you could use an abstract domain socket, for example, and have a named
path, rather than… rather than just a TCP address.
This would also be a sensible place to set options like SO reuse port.
Sorry, that was… I didn't complete my thought before. So there's this change going in to config.http to add SO reuse port, and I think it would make sense to add it here rather than in the config.http, server config struct.
And then it would apply to anything that embeds this. So I'm thinking that we should change the
config HTTP to embed this as well. It would be a breaking API change, but it shouldn't be a breaking user change, because the endpoint field would still be exposed, and it would default to TCP, as it does today.
Does this sound… Sensible to you?
**Paulo Janotti** 06:15 By your description, it sounds very sensible. There is no need to have that on the server config, makes sense to be out in the address, you know. So, logically, kind of, the concern seems to be the right place in the address config.
**Andrew Wilkins @ Elastic Observability** 06:34 Yep.
Okay, I'll, I did comment on an issue about it, but…
Possibly no one saw it, so I'll open a new issue explicitly about this, and specifically about this, rather.
And… probably raise it in Slack, just to make sure, everyone's aware.
But that would be a breaking change to the API, so I think it's probably better if we do it now.
**Paulo Janotti** 06:58 Rather than later. Yeah, yeah. Before.
**Andrew Wilkins @ Elastic Observability** 07:00 We'll end today.
**Paulo Janotti** 07:02 Yeah.
It's a…
But you mentioned that it's not a breaking change for the users. It's a breaking change for…
Yeah, developers, there will be a breaking change, but people just using the YAML, they can keep their configuration.
Correct. Yeah, no, that… that's… that's good. That's great.
**Andrew Wilkins @ Elastic Observability** 07:27 But the API is also… part of the, the 1.0 contract, right? Yeah.
**Paulo Janotti** 07:33 Yeah, yeah, no, it's just my tendency is… devs the compiler catch.
**Andrew Wilkins @ Elastic Observability** 07:40 Avoid turkeys.
**Paulo Janotti** 07:42 YAML people don't read the changelog.
**Andrew Wilkins @ Elastic Observability** 07:44 Yep, yep, yep.
Okay, cool, thanks for the chat.
I'll open a show about that later.
Don't have anything else… on my mind.
**Paulo Janotti** 07:54 Yeah, me neither. I kind of been involved with other things. I really want to get some stuff done for Windows, like…
I would like to run tests in Nano Server, a Docker image.
And… I was thinking, because some of requirements for deployments of some customers.
That perhaps… but this is a bigger issue.
Because right now, the installer for Windows deploys a local system.
I'm thinking that we should default to local service.
But actually, I don't know what's gonna break for that. So, probably I need also to do, kind of, a test, create a PRO in my fork, running as local
service instead of local system to see what breaks with that, you know?
Perhaps, perhaps nothing much breaks, but I need to confirm before that.
**Andrew Wilkins @ Elastic Observability** 09:03 Is that something that should… can or should be running in GitHub CI?
**Paulo Janotti** 09:09 Yeah, yeah, we… we need to adapt, perhaps I need to do some tools so we can run as local service. It's possible to do that, you know.
But that's what I'm thinking. Before running the test on Windows, I kind of always switch to local service, then I can see whatever breaks, you know?
**Andrew Wilkins @ Elastic Observability** 09:37 I don't have an opinion on it, so…
**Paulo Janotti** 09:40 Yeah, no, if you think… if you think nowadays, for a long time, there is this local service account. It's kind of… if you are familiar with Windows, it's kind of, okay, it's a powerful account, but it's not root.
**Andrew Wilkins @ Elastic Observability** 09:56 It's been a while since I did an.
**Paulo Janotti** 09:58 Yeah, so Yeah, local system is root, can do everything. Local service has some restrictions.
And if we support local service, perhaps it's easier for more people to deploy and security requirements.
**Andrew Wilkins @ Elastic Observability** 10:17 Okay, makes sense.
It's just less… less privileged.
**Paulo Janotti** 10:21 Yeah.
**Andrew Wilkins @ Elastic Observability** 10:24 Okay, sounds good. So… that's something that will come to CI at some point?
**Paulo Janotti** 10:31 Yeah, that's my idea, to run that in CI. I'm not sure, I probably would just have time to work on this on the beginning of next year. I'm also… as most people who are taking some time this time, I'm gonna take next week, then…
Two weeks in the end of the year, you know, so…
**Andrew Wilkins @ Elastic Observability** 10:54 Sounds good.
Anything else?
Or,
just… I'm not sure if you care about this, I can't even remember if we've talked about it in previous meetings, but I'm looking into…
Making scrapers… A top-level concept.
So… The idea is that scrapers should be able to be triggered Bud.
different events. So, at the moment, scrapers are just another kind of receiver, and they have a embedded
time interval. What I want to make possible is to do one-shot scrapes.
So you just, invoke the scraper once, send it through the pipeline, wait for the exporter to
Sender and acknowledge.
come back, and then exit. So it would be a new, eventually I'd like to have a new command line, subcommand, and, or potentially also support for things like webhooks, invoking scrapers, and…
I don't know what else at the moment, but basically, I just want to decouple scrapers from receivers.
So I'm planning to put together a design for that.
That is Narcity.
**Paulo Janotti** 12:19 I… I don't think I… I had a use case for that now, but it sounds interesting, but…
One thing, so… You triggered a scraper, Based on… event.
And you said that the event can only be triggered again after the export, or the export of the data. You said something along synchronizing with the exporting.
**Andrew Wilkins @ Elastic Observability** 12:49 I know, just what I mean is, it… it would… I want to make it possible to…
So my ultimate goal is to externalize the scheduling of scrapes. So, imagine that you had
Kubernetes cluster, you deploy the collector as a cron job, rather than as a deployment or a daemon set, and then you want to scrape, I don't know, the Kubernetes cluster API server metrics.
Rather than having a deployment or daemon set which is idle most of the time, and then wakes up every minute to do something, we could just have a cron job, which…
start… that creates a job every minute. And then it would run a command, so it would be something like hotel coal, scrape.
Give it the name of a pipeline and a scraper, and then it would…
It would run the scraper, send it through the pipeline, then once the pipeline is finished, it would exit.
That's all.
**Paulo Janotti** 13:54 Okay, but… but in that sense of… perhaps I should look at the issue, but,
What's coming to my mind?
okay, the collector is kind of a heavy thing to start, but in principle, you could do this with config, right?
Because you put, like, okay, I'm gonna collect that every one minute, you do one collection, and kind of have something to terminate the collector.
The collector doesn't have this nice mechanism, but you could send a signal to terminate after some time.
You know.
**Andrew Wilkins @ Elastic Observability** 14:33 That would be an option, yes.
**Paulo Janotti** 14:35 But I think what you want to have is kind of the same functionality.
Running together with the receivers that collect all the time.
**Andrew Wilkins @ Elastic Observability** 14:47 Potentially, yes. So, another use case I was describing, is you might have a webhook which receives an event, or it could be, the new Lambda receiver, hypothetically, receiving an event, and then…
doing a scrape. So, actually, the AWS Lambda receiver.
it could be rebuilt in terms of this, so it could be receiving an event from S3, and then performing an S3 scrape. So if we had just the S3 scraper… scraper as a top-level thing, it could be triggered by an event, and that event could just be whatever came from
the S3 notifications.
**Paulo Janotti** 15:28 Does that make sense?
Yeah, yeah. As I said, I don't think I have a use case for that in my mind right now, but sounds interesting. I'm not sure, as I said, I'm a bit packed for the end of the year.
If you want to share with me via Slack the links, I'll take a look. Both these and the…
The thing about the config that you mentioned before.
**Andrew Wilkins @ Elastic Observability** 15:56 Okay, yep, I'll… I'll link an agenda after, and I'll ping you on.
**Paulo Janotti** 15:59 Oh, yeah, yeah, yeah, the agenda, the agenda is fine, yeah.
**Andrew Wilkins @ Elastic Observability** 16:04 Sounds good.
**Paulo Janotti** 16:09 I don't have anything else.
No, I don't have anything else.
**Andrew Wilkins @ Elastic Observability** 16:16 Okay. I'll keep it short then.
Have a nice time off.
**Paulo Janotti** 16:20 Alright.
**Andrew Wilkins @ Elastic Observability** 16:21 Catch you later.
**Paulo Janotti** 16:22 Bye.
